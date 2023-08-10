#!/bin/python3

from argparse import ArgumentParser
from dataclasses import dataclass
from pathlib import Path
from typing import List, Optional
import os

@dataclass
class Credential:
    moduleSubstring: str
    user: str
    password: str

@dataclass
class Submodule:
    header: str
    path: str
    url: str

@dataclass
class SubmoduleConfig:
    credentials: List[Credential]
    repo_root_path: str = "." 
    max_depth = -1
    restore=True

    def set_credential(self, url, credential: Credential):
        return url

    def format_url(self, url):
        return url

class SshSubmoduleConfig(SubmoduleConfig):
    def set_credential(self, url, credential: Credential):
        # TODO
        NotImplemented
        return url
    
    def format_url(self, url):
        ''' Format URL for SSH connection '''
        return url.replace( "https://", "git@").replace(".com/", ".com:")

class HttpSubmoduleConfig(SubmoduleConfig):
    def set_credential(self, url, credential: Credential):
        # TODO - make sure this is right.
        return url.replace("https://", f"https://{credential.user}:{credential.password}:")

    def format_url(self, url):
        ''' Format URL for HTTP connection '''
        return url.replace("git@", "https://").replace(".com:", ".com/")



class SubmoduleUpdate:
    def __init__(self, submodule_config: SubmoduleConfig):
        self.config = submodule_config

        self.verbose = False
        self.restore = False
        self.to_ignore = []
        self.found_submodule_files: List[Path] = []

    def __make_modified_gitmodules_file(self, submodules: List[Submodule])->str:
        ''' Takes a list of the parsed git modules, injects the credentials into them and then returns the new gitmodules file string.'''
        # TODO: atm only modules which has a credential supplied are kept, others are discarded here.
        new_gitmodules_file = ""
        for submodule in submodules:
            section = ""
            formatted_url = self.config.format_url(submodule.url)
            for credential in self.config.credentials:
                if credential.moduleSubstring in formatted_url:
                    url_w_cred = self.config.set_credential(formatted_url, credential)

                    section = f"{submodule.header}\npath = {submodule.path}\nurl = {url_w_cred}\n"
                    print("DEBUG:", section)


            new_gitmodules_file += section
        if self.verbose:
            print(f"Writing new gitmodules file:\n {new_gitmodules_file}")
        return new_gitmodules_file
       

    def __parse_gitmodules(self, contents)-> List[Submodule]:
        ''' Logic for how the gitmodules file is deserialized '''
        submodules = []
        name, path, url = "", "", ""
        for i, line in enumerate(contents):
            if line.startswith('['):
                for key in contents[i:]:
                    key = key.strip()
                    if key.startswith('[submodule'):
                        name = key
                    elif key.startswith('path'):
                        path = key.split('=')[1].strip()
                    elif key.startswith('url'):
                        url = key
                    if path and url:
                        submodules.append(Submodule(name, path, url))
                        name, path, url = "", "", ""
                        break
        return submodules

    def __update_submodule(self, module_path: Path, submodule: Submodule):
        ''' How we update each module '''
        if self.verbose:
            print(f"Updating {submodule.path}")

        project_root = os.curdir
        os.chdir(module_path)
        os.system(f"git submodule update --init {submodule.path}")
        os.chdir(project_root)

    def __reset(self):
        ''' Reset the submodules to their previous state using git diff'''
        for file in self.found_submodule_files:
            os.system(f"git restore {file}")

    def __recursive_check(self, current_path: Path = Path("")) -> List[Submodule]:
        ''' Recursively find and update git submodules '''
        submodules = []
        
        if current_path == Path(""):
            current_path = Path( self.config.repo_root_path )

        gitmodule_path =  current_path / '.gitmodules'
        has_gitmodules = gitmodule_path.is_file()

        if has_gitmodules:
            self.found_submodule_files.append(gitmodule_path) 
            with gitmodule_path.open('r+') as file:
                contents = file.readlines()
                submodules: List[Submodule] = self.__parse_gitmodules(contents)
                file.seek(0) # Move pointer back to beginning of file.
                file.truncate() # remove all file content
                file.write(self.__make_modified_gitmodules_file(submodules)) # overwrite with the modified content

            _s = []
            for submodule in submodules:
                check = True
                for ignore in self.to_ignore:
                    if ignore in submodule.url:
                        if self.verbose:
                            print(f"Ignoring {submodule.path}. . .")
                        check = False

                if check:
                    self.__update_submodule(current_path, submodule)
                    new_path = current_path / submodule.path
                    _s += self.__recursive_check(new_path)
            submodules += _s

        else:
            ''' Logic for no .gitmodules file can go here.'''
            if self.verbose:
                print(f"No .gitmodules file found in {current_path}")

        return submodules

    def set_verbose(self):
        self.verbose = True
        return self

    def set_restore(self):
        ''' Should the submodules be reset to their previous state using git diff '''
        if self.verbose:
            print("The .gitmodules file will be restored after update.")
        self.restore = True
        return self

    def set_ignore(self, ignore_list: List[str]):
        ''' Names of submodules to ignore based substring of the url, i.e. dont try to clone '''
        if self.verbose:
            print(f"Modules with the following urls will be ignored: {ignore_list}")
        os.chdir(self.config.repo_root_path)
        self.to_ignore = ignore_list
        return self

    def recursive_update(self):
        modules = self.__recursive_check()
        if self.restore:
            self.__reset()
        return modules

if __name__ == '__main__':

    parser = ArgumentParser()
    parser.add_argument("-v", "--verbose", action="store_true", help="Enable verbose mode.")
    parser.add_argument("-r", "--restore", action="store_true", help="Restore the gitmodules file to previous state after clone.")
    parser.add_argument("-i", "--ignore", action="append", nargs='+', help="Sring to ignore if found in module url.")

    parser.add_argument("-p", "--repo_root_path", default=".",type=str, help="Path to root of the repository you want to clone modules in.  Default is current path.")

    parser.add_argument("-c", "--credential", required=True, action="append", nargs='+', type=str, help="Pass a list of credentials to use.  Credentials can be associated with a string in the gitsubmodule and that credential will be used to selectively git clone. I.e.:  StringInUrl USER:PASS")
    parser.add_argument("-t", "--type", required=True, type=str, help="Type of connection to be made.  http or ssh.")

    args = parser.parse_args()

    credentials: List[Credential] = []
    if args.credential:
        for cred in args.credential:
            user, passw = cred[1].split(':')
            credentials.append(Credential(cred[0], user, passw))


    # TODO: remove the debug text
    config = SubmoduleConfig(credentials, repo_root_path=args.repo_root_path)
    if args.type.lower() == "ssh":
        config = SshSubmoduleConfig(credentials, repo_root_path=args.repo_root_path)
    elif args.type.lower() == "http":
        config = HttpSubmoduleConfig(credentials, repo_root_path=args.repo_root_path)
    else:
        print(f"Unsupported type: {args.type}.  Choose from 'ssh' or 'http'.")
        exit()

    git_submodule = SubmoduleUpdate(config)
    if args.verbose:
        print("Verbose mode on")
        git_submodule.set_verbose()
    if args.restore:
        git_submodule.set_restore()
    if args.ignore:
        to_ignore = [i for ignore in args.ignore for i in ignore]
        git_submodule.set_ignore(to_ignore)
    submodules = git_submodule.recursive_update()

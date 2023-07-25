


user_permissions(){
  # DZDO, sudo but doesn't use sudo config file, it uses AD
  dzdo ${some command}

  # read(4)
  # write (2)
  # execute (1)
  # I.e. read + write + execute = 7
  # owner:group:others
  chmod 744 ${filename}

  #Give the [u]ser who owns a file the right to e[x]ecute it:
  chmod u+x {{path/to/file}}

  # Give the [u]ser rights to [r]ead and [w]rite to a file/directory:
  chmod u+rw {{path/to/file_or_directory}}

  #Remove e[x]ecutable rights from the [g]roup:
  chmod g-x {{path/to/file}}

  # Give [a]ll users rights to [r]ead and e[x]ecute:
  chmod a+rx {{path/to/file}}

  # Give [o]thers (not in the file owner's group) the same rights as the [g]roup:
  chmod o=g {{path/to/file}}

  # Remove all rights from [o]thers:
  chmod o= {{path/to/file}}

  # Change permissions recursively giving [g]roup and [o]thers the ability to [w]rite:
  chmod -R g+w,o+w {{path/to/directory}}

  # Recursively give [a]ll users [r]ead permissions to files and e[X]ecute permissions to sub-directories within a directory:
  chmod -R a+rX {{path/to/directory}}


  extra_modes(){
    # setuid setgid sticky-bit
    
    # setuid - when set on a executable file, the process spawned from the file will inheirt the owners userID instead of the users.
    # setgid - like setuid, process spawned will inherit the groupID of the file owner.
    # stickybit - set on directory, only owner of a file within the dir or root user can delete or rename the file.
    #   - User, commonly set on publicly writeable directories like /tmp to prevent users from deleting/altering each others files.
  }

}

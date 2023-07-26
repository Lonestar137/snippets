import xml.etree.ElementTree as ET
from abc import abstractmethod

class ConfigReader:
    @abstractmethod
    def read(self, key): pass


class GenericConfigReader(ConfigReader):
    """
    This can be used to read ini and cfg files. (Note: Does not support multiline values)
    @param config_str: Is the ini or cfg file to parse in string format.
    """

    def __init__(self, config_str):
        self.config_str = config_str

    def read(self, key: str):
        '''@param key: example key -> header.section_key'''
        header, section_key = key.split('.')
        for line_num, line in enumerate(self.config_str.split('\n')):
            if '['+header+']' in line:
                for key in self.config_str.split('\n')[line_num+1:]:
                    if key.startswith(section_key):
                        return key.split('=')[1].strip()


class XmlConfigReader(ConfigReader):
    def __init__(self, config_str):
        self.config_str = config_str

    def _split_path_with_namespace(self, input_string):
        '''
        Function for formatting keys with namespace prefix.
        @param input_string: example {http://example.com/header}section_key.subsection_key
        '''
        result = []
        start_idx = 0
        inside_brackets = False

        for i, char in enumerate(input_string):
            if char == '{':
                inside_brackets = True
            elif char == '}':
                inside_brackets = False

            if char == '.' and not inside_brackets:
                result.append(input_string[start_idx:i])
                start_idx = i + 1

        result.append(input_string[start_idx:])

        return result


    def _format_keys(self, path):
        keys = []
        if '}' in path:
            keys = self._split_path_with_namespace(path)
        else:
            keys = path.split('.')

        return keys

    def _element_to_dict(self, element)->dict:
        '''
        Converts xml.etree.ElementTree.Element to dict.
        @param element: xml.etree.ElementTree.Element
        '''
        result = {}
        if element.text and element.text.strip():
            return element.text.strip()

        for child in element:
            if child.tag in result:
                if not isinstance(result[child.tag], list):
                    result[child.tag] = [result[child.tag]]
                result[child.tag].append(self._element_to_dict(child))
            else:
                result[child.tag] = self._element_to_dict(child)

        return result

    def read(self, path):
        '''
        # @param: Path is a path to a nested value in the XML.
        '''
        root = ET.fromstring(self.config_str)
        path_keys: list = self._format_keys(path)
        node_dict = self._element_to_dict(root)

        # Traverse the dictionary using the keys in the path_keys list
        value = node_dict
        for key in path_keys:
            if isinstance(value, dict) and key in value:
                value = value[key]
            elif isinstance(value, list) and key.isdigit():
                # Convert the key to an integer and use it as an index for the list
                index = int(key)
                if 0 <= index < len(value):
                    value = value[index]
                else:
                    # Invalid index, return None
                    return None
            else:
                # Key not found or value is not a dictionary or list
                return None
        return value


class ReadConfig:
    def __init__(self, config_file: ConfigReader):
        self.config_file = config_file

    def get_value(self, key):
        return self.config_file.read(key)


exampleCfg = """
; This is a comment in the INI file

[Database]
host = localhost
port = 5432
username = user123
password = mysecretpassword

[Application]
language = en_US
theme = dark
"""

theme = ReadConfig(GenericConfigReader(exampleCfg)).get_value('Application.theme')
assert(theme == 'dark')

host = ReadConfig(GenericConfigReader(exampleCfg)).get_value('Database.host')
assert(host == 'localhost')

exampleIni = """
; This is a comment in the INI file

[Database]
host = localhost
port = 5432
username = user123
password = mysecretpassword

[Application]
language = en_US
theme = dark

[Empty Section]

[Section with Spaces]
 key with spaces = value with spaces

[Section with Quotes]
quoted_key = "quoted value"

[Section with Special Characters]
escaped_value = This contains a \\ backslash, a \n newline,
\t tab, and a # hash character.

[Section with Multiline Value]
multiline_value = This is a multiline value.
  It continues on the next line and \
  can have backslashes at the end of the line.

[Section with Empty Lines]

[Section with Duplication]
key1 = value1
key1 = value2

[Section with Duplicated Keys]
dup_key = value1
dup_key = value2
dup_key = value3
dup_key = value4
"""
test = ReadConfig(GenericConfigReader(exampleIni)).get_value('Section with Duplication.key1')
assert(test == 'value1')

test1 = ReadConfig(GenericConfigReader(exampleIni)).get_value('Section with Duplicated Keys.dup_key')
assert(test1 == 'value1')


exampleXml = """
<library>
  <book>
    <title>1984</title>
    <author>George Orwell</author>
    <genre>Dystopian</genre>
    <publication_year>1949</publication_year>
    <isbn>978-0451524935</isbn>
  </book>
  
  <book>
    <title>To Kill a Mockingbird</title>
    <author>Harper Lee</author>
    <genre>Novel</genre>
    <publication_year>1960</publication_year>
    <isbn>978-0061120084</isbn>
  </book>
  
  <book>
    <title>The Great Gatsby</title>
    <author>F. Scott Fitzgerald</author>
    <genre>Tragedy</genre>
    <publication_year>1925</publication_year>
    <isbn>978-0743273565</isbn>
  </book>
</library>
"""

# Example XML string
xml_string = '''
<library xmlns="http://example.com/library">
  <book tag="Book1">
    <title>1984</title>
    <author>George Orwell</author>
  </book>

  <book tag="Book2">
    <title>To Kill a Mockingbird</title>
    <author>Harper Lee</author>
  </book>
</library>

'''

# Usage example
namespace = '{http://example.com/library}'
result = ReadConfig(XmlConfigReader(xml_string)).get_value(f'{namespace}book.0.{namespace}title')
assert(result == '1984')

result = ReadConfig(XmlConfigReader(xml_string)).get_value(f'{namespace}book.0.{namespace}author')
assert(result == 'George Orwell')

result = ReadConfig(XmlConfigReader(xml_string)).get_value(f'{namespace}book.1.{namespace}author')
assert(result == 'Harper Lee')

result = ReadConfig(XmlConfigReader(exampleXml)).get_value('book.0.isbn')
assert(result == '978-0451524935')

result = ReadConfig(XmlConfigReader(exampleXml)).get_value('book.2.author')
assert(result == 'F. Scott Fitzgerald')

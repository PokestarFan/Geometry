import inspect
import types
import Geometry
from typing import List, Union


def scan_module(mod: types.ModuleType) -> List[types.FunctionType]:
    """
    Scans the module provided using the inspect.getmembers function. It returns a list of functions.

    :param mod: The module to scan
    :type mod: types.ModuleType
    :return: The list of functions
    :rtype: list
    """

    funcs = []
    for item in inspect.getmembers(mod):
        if callable(item[1]):
            funcs.append(item[1])
    return funcs


def generate_directory(mod_dir):
    dictionary = {}
    for item in inspect.getmembers(mod_dir):
        if isinstance(item[1], types.ModuleType):
            dictionary[item[0]] = scan_module(item[1])
    return dictionary


def generate_string(dict_or_list: Union[dict, list], gen_str: str = None) -> str:
    formatted_string = ''
    if isinstance(dict_or_list, list):
        count = 0
        for entry in dict_or_list:
            count += 1
            formatted_string += '%d. `%s`\n' % (count, entry.__name__)
            print('Found function %s' % entry.__name__)
    elif isinstance(dict_or_list, dict):
        for name, flist in dict_or_list.items():
            formatted_string += gen_str % (name, generate_string(flist))
            print('Found module %s' % name)
    return formatted_string.strip()

if __name__ == '__main__':
    geo = generate_directory(Geometry)

    MODULE_FORMAT = """# %s

## Functions:

%s

    """.strip()
    with open('DIRECTORY.md', 'w') as file:
        file.write(generate_string(geo, gen_str=MODULE_FORMAT))
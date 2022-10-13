import glob
import os
import re
from types import ModuleType
from typing import Any, Type, TypeVar

from colorama import Fore, init

T = TypeVar('T', bound=Any)
init()
COLORS = Fore.__dict__

class Reason(Exception):
    
    def __init__(self, message: str) -> None:
        super().__init__(message)
        self.message = message


class Importer():

    def import_from(self, path: str, superclass: Type[T] = Any, blacklist: list[type] = [Any], init_components: bool = True, exclude: list[type] = [Any], verboose : bool = False) -> dict[str, T]:
        """
        `@params`
        path - the path of the classes to import
        superclass - only include classes childrens of the superclass
        blacklist - exclude the class/es
        init_components - initialize the classes or not
        exclude - exclude classes childrens 
        verboose - activate the logging session
        """
        files:dict[str, Any] = dict()
        for file in list(filter(lambda x: '__init__' not in x,[script for script in glob.glob(f'{path}/*.py')])):
            reason = ""
            with open(f'{file}','r') as f:
                txt = f.read()
                f.close()
                filename = re.search(r"(\w{1,})\.py", file)
                name = re.search(r"(?:class)\s(\w{1,})+(?:\((.{1,})\))?:", txt)
                try:
                    if name and filename:
                        filename = filename.group(1)
                        super_class = name.group(2)
                        name = name.group(1)
                        if verboose:
                            print(f"{COLORS['BLUE']} [>] Collecting {filename}.py ... {COLORS['RESET']}")
                        if superclass != Any:
                            if (super_class != superclass.__name__):
                                reason = f"{name} is not superclass of {superclass.__name__}"
                                raise Reason(reason)
                        if blacklist != [Any]:
                            if name in [b.__name__ for b in blacklist]:
                                reason = f"{name} excluded"
                                raise Reason(reason)
                        if super_class != None and "ABC" in super_class:
                            reason = f"{name} is an Abstract Base Class"
                            raise Reason(reason)
                        if super_class != None and super_class in [b.__name__ for b in exclude]:
                            reason = f"{name} excluded by derivated class ({super_class})"
                            raise Reason(reason)
                        fixed_path = os.path.join(path[2:], filename).replace('/','.').replace('\\','.')
                        imported = __import__(f'{fixed_path}')
                        imported = self.__recursive_import(imported, fixed_path, fixed_path)
                        if init_components:
                            if verboose:
                                print(f"{COLORS['GREEN']} [>] Initializating {name} ... {COLORS['RESET']}")
                            files.update({name: getattr(imported, name)()})
                        else:
                            if verboose:
                                print(f"{COLORS['GREEN']} [>] Saving {name} ... {COLORS['RESET']}")
                            files.update({name: getattr(imported, name)})
                    else:
                        print(f"{COLORS['YELLOW']} [>] Passing {filename.group(1)}.py ... {COLORS['RESET']}") #type: ignore
                except Reason as err:
                    if verboose:
                        print(f"{COLORS['YELLOW']} [>] Passing {filename}.py ... {COLORS['RESET']}\n\t * Reason: {reason}")
                except Exception as err:
                    print(f"{COLORS['RED']} [>] Showing Error:{COLORS['RESET']}\n\t * {err} ")
        return files


    def __recursive_import(self, actual_path: ModuleType, spec: str, _spec: str) -> ModuleType:
        if actual_path.__name__ == _spec: return actual_path
        return self.__recursive_import(getattr(actual_path,  spec.split('.')[_spec.find(actual_path.__name__)+1]), '.'.join(spec.split('.')[1:]), _spec)
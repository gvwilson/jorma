# Variable Role Analysis: test

## callable.py

Warning: no variables found.
### Static analysis

True True

## ex_loop_globals_2.py

### Static analysis

| Scope  | Variable | Role    | Location |
| :------| :--------| :-------| :--------|
| module | name     | stepper | line 1   |
__name__
__doc__
__package__
__loader__
__spec__
__file__
__cached__
__builtins__
name

## find_test_funcs.py

### Static analysis

| Scope             | Variable | Role        | Location |
| :-----------------| :--------| :-----------| :--------|
| module.find_tests | prefix   | fixed value | line 20  |
| module.find_tests | func     | stepper     | line 21  |
| module.find_tests | name     | stepper     | line 21  |
| module.sign       | value    | fixed value | line 1   |
test_sign_negative <function test_sign_negative at 0x1049f32e0>
test_sign_positive <function test_sign_positive at 0x1049f3240>
test_sign_zero <function test_sign_zero at 0x104abc720>
test_sign_error <function test_sign_error at 0x104abc7c0>

## func_list.py

### Static analysis

| Scope  | Variable   | Role        | Location |
| :------| :----------| :-----------| :--------|
| module | everything | fixed value | line 10  |
| module | func       | stepper     | line 11  |
First
Second
Third

## globals.py

Warning: no variables found.
### Static analysis

{'__builtins__': {'ArithmeticError': <class 'ArithmeticError'>,
                  'AssertionError': <class 'AssertionError'>,
                  'AttributeError': <class 'AttributeError'>,
                  'BaseException': <class 'BaseException'>,
                  'BaseExceptionGroup': <class 'BaseExceptionGroup'>,
                  'BlockingIOError': <class 'BlockingIOError'>,
                  'BrokenPipeError': <class 'BrokenPipeError'>,
                  'BufferError': <class 'BufferError'>,
                  'BytesWarning': <class 'BytesWarning'>,
                  'ChildProcessError': <class 'ChildProcessError'>,
                  'ConnectionAbortedError': <class 'ConnectionAbortedError'>,
                  'ConnectionError': <class 'ConnectionError'>,
                  'ConnectionRefusedError': <class 'ConnectionRefusedError'>,
                  'ConnectionResetError': <class 'ConnectionResetError'>,
                  'DeprecationWarning': <class 'DeprecationWarning'>,
                  'EOFError': <class 'EOFError'>,
                  'Ellipsis': Ellipsis,
                  'EncodingWarning': <class 'EncodingWarning'>,
                  'EnvironmentError': <class 'OSError'>,
                  'Exception': <class 'Exception'>,
                  'ExceptionGroup': <class 'ExceptionGroup'>,
                  'False': False,
                  'FileExistsError': <class 'FileExistsError'>,
                  'FileNotFoundError': <class 'FileNotFoundError'>,
                  'FloatingPointError': <class 'FloatingPointError'>,
                  'FutureWarning': <class 'FutureWarning'>,
                  'GeneratorExit': <class 'GeneratorExit'>,
                  'IOError': <class 'OSError'>,
                  'ImportError': <class 'ImportError'>,
                  'ImportWarning': <class 'ImportWarning'>,
                  'IndentationError': <class 'IndentationError'>,
                  'IndexError': <class 'IndexError'>,
                  'InterruptedError': <class 'InterruptedError'>,
                  'IsADirectoryError': <class 'IsADirectoryError'>,
                  'KeyError': <class 'KeyError'>,
                  'KeyboardInterrupt': <class 'KeyboardInterrupt'>,
                  'LookupError': <class 'LookupError'>,
                  'MemoryError': <class 'MemoryError'>,
                  'ModuleNotFoundError': <class 'ModuleNotFoundError'>,
                  'NameError': <class 'NameError'>,
                  'None': None,
                  'NotADirectoryError': <class 'NotADirectoryError'>,
                  'NotImplemented': NotImplemented,
                  'NotImplementedError': <class 'NotImplementedError'>,
                  'OSError': <class 'OSError'>,
                  'OverflowError': <class 'OverflowError'>,
                  'PendingDeprecationWarning': <class 'PendingDeprecationWarning'>,
                  'PermissionError': <class 'PermissionError'>,
                  'ProcessLookupError': <class 'ProcessLookupError'>,
                  'PythonFinalizationError': <class 'PythonFinalizationError'>,
                  'RecursionError': <class 'RecursionError'>,
                  'ReferenceError': <class 'ReferenceError'>,
                  'ResourceWarning': <class 'ResourceWarning'>,
                  'RuntimeError': <class 'RuntimeError'>,
                  'RuntimeWarning': <class 'RuntimeWarning'>,
                  'StopAsyncIteration': <class 'StopAsyncIteration'>,
                  'StopIteration': <class 'StopIteration'>,
                  'SyntaxError': <class 'SyntaxError'>,
                  'SyntaxWarning': <class 'SyntaxWarning'>,
                  'SystemError': <class 'SystemError'>,
                  'SystemExit': <class 'SystemExit'>,
                  'TabError': <class 'TabError'>,
                  'TimeoutError': <class 'TimeoutError'>,
                  'True': True,
                  'TypeError': <class 'TypeError'>,
                  'UnboundLocalError': <class 'UnboundLocalError'>,
                  'UnicodeDecodeError': <class 'UnicodeDecodeError'>,
                  'UnicodeEncodeError': <class 'UnicodeEncodeError'>,
                  'UnicodeError': <class 'UnicodeError'>,
                  'UnicodeTranslateError': <class 'UnicodeTranslateError'>,
                  'UnicodeWarning': <class 'UnicodeWarning'>,
                  'UserWarning': <class 'UserWarning'>,
                  'ValueError': <class 'ValueError'>,
                  'Warning': <class 'Warning'>,
                  'ZeroDivisionError': <class 'ZeroDivisionError'>,
                  '_IncompleteInputError': <class '_IncompleteInputError'>,
                  '__build_class__': <built-in function __build_class__>,
                  '__debug__': True,
                  '__doc__': 'Built-in functions, types, exceptions, and other '
                             'objects.\n'
                             '\n'
                             'This module provides direct access to all '
                             "'built-in'\n"
                             'identifiers of Python; for example, builtins.len '
                             'is\n'
                             'the full name for the built-in function len().\n'
                             '\n'
                             'This module is not normally accessed explicitly '
                             'by most\n'
                             'applications, but can be useful in modules that '
                             'provide\n'
                             'objects with the same name as a built-in value, '
                             'but in\n'
                             'which the built-in of that name is also needed.',
                  '__import__': <built-in function __import__>,
                  '__loader__': <class '_frozen_importlib.BuiltinImporter'>,
                  '__name__': 'builtins',
                  '__package__': '',
                  '__spec__': ModuleSpec(name='builtins', loader=<class '_frozen_importlib.BuiltinImporter'>, origin='built-in'),
                  'abs': <built-in function abs>,
                  'aiter': <built-in function aiter>,
                  'all': <built-in function all>,
                  'anext': <built-in function anext>,
                  'any': <built-in function any>,
                  'ascii': <built-in function ascii>,
                  'bin': <built-in function bin>,
                  'bool': <class 'bool'>,
                  'breakpoint': <built-in function breakpoint>,
                  'bytearray': <class 'bytearray'>,
                  'bytes': <class 'bytes'>,
                  'callable': <built-in function callable>,
                  'chr': <built-in function chr>,
                  'classmethod': <class 'classmethod'>,
                  'compile': <built-in function compile>,
                  'complex': <class 'complex'>,
                  'copyright': Copyright (c) 2001-2024 Python Software Foundation.
All Rights Reserved.

Copyright (c) 2000 BeOpen.com.
All Rights Reserved.

Copyright (c) 1995-2001 Corporation for National Research Initiatives.
All Rights Reserved.

Copyright (c) 1991-1995 Stichting Mathematisch Centrum, Amsterdam.
All Rights Reserved.,
                  'credits':     Thanks to CWI, CNRI, BeOpen, Zope Corporation, the Python Software
    Foundation, and a cast of thousands for supporting Python
    development.  See www.python.org for more information.,
                  'delattr': <built-in function delattr>,
                  'dict': <class 'dict'>,
                  'dir': <built-in function dir>,
                  'divmod': <built-in function divmod>,
                  'enumerate': <class 'enumerate'>,
                  'eval': <built-in function eval>,
                  'exec': <built-in function exec>,
                  'exit': Use exit() or Ctrl-D (i.e. EOF) to exit,
                  'filter': <class 'filter'>,
                  'float': <class 'float'>,
                  'format': <built-in function format>,
                  'frozenset': <class 'frozenset'>,
                  'getattr': <built-in function getattr>,
                  'globals': <built-in function globals>,
                  'hasattr': <built-in function hasattr>,
                  'hash': <built-in function hash>,
                  'help': Type help() for interactive help, or help(object) for help about object.,
                  'hex': <built-in function hex>,
                  'id': <built-in function id>,
                  'input': <built-in function input>,
                  'int': <class 'int'>,
                  'isinstance': <built-in function isinstance>,
                  'issubclass': <built-in function issubclass>,
                  'iter': <built-in function iter>,
                  'len': <built-in function len>,
                  'license': Type license() to see the full license text,
                  'list': <class 'list'>,
                  'locals': <built-in function locals>,
                  'map': <class 'map'>,
                  'max': <built-in function max>,
                  'memoryview': <class 'memoryview'>,
                  'min': <built-in function min>,
                  'next': <built-in function next>,
                  'object': <class 'object'>,
                  'oct': <built-in function oct>,
                  'open': <built-in function open>,
                  'ord': <built-in function ord>,
                  'pow': <built-in function pow>,
                  'print': <built-in function print>,
                  'property': <class 'property'>,
                  'quit': Use quit() or Ctrl-D (i.e. EOF) to exit,
                  'range': <class 'range'>,
                  'repr': <built-in function repr>,
                  'reversed': <class 'reversed'>,
                  'round': <built-in function round>,
                  'set': <class 'set'>,
                  'setattr': <built-in function setattr>,
                  'slice': <class 'slice'>,
                  'sorted': <built-in function sorted>,
                  'staticmethod': <class 'staticmethod'>,
                  'str': <class 'str'>,
                  'sum': <built-in function sum>,
                  'super': <class 'super'>,
                  'tuple': <class 'tuple'>,
                  'type': <class 'type'>,
                  'vars': <built-in function vars>,
                  'zip': <class 'zip'>},
 '__cached__': '/Users/gvwilson/jorma/sdxpy/test/__pycache__/globals.cpython-313.pyc',
 '__doc__': None,
 '__file__': '/Users/gvwilson/jorma/sdxpy/test/globals.py',
 '__loader__': <_frozen_importlib_external.SourceFileLoader object at 0x1050b0110>,
 '__name__': '__main__',
 '__package__': '',
 '__spec__': ModuleSpec(name='__main__', loader=<_frozen_importlib_external.SourceFileLoader object at 0x1050b0110>, origin='/Users/gvwilson/jorma/sdxpy/test/globals.py'),
 'pprint': <module 'pprint' from '/Users/gvwilson/.local/share/uv/python/cpython-3.13.9-macos-aarch64-none/lib/python3.13/pprint.py'>}

### Dynamic analysis

| Variable  | Scope                                                                                                                                                                                   | Role     |
| :---------| :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------| :--------|
| allowance | module.pprint.pprint._format._pprint_dict._format_dict_items._format._pprint_dict._format_dict_items._format                                                                            | phase    |
| char      | module.pprint.pprint._format._pprint_dict._format_dict_items._format._pprint_dict._format_dict_items._format._pprint_str.findall._compile.compile.parse._parse_sub._parse.get.__next    | phase    |
| char      | module.pprint.pprint._format._pprint_dict._format_dict_items._format._pprint_dict._format_dict_items._format._pprint_str.findall._compile.compile.parse._parse_sub._parse.match         | phase    |
| data      | module.pprint.pprint._format._repr.format._safe_repr.format._safe_repr.format._safe_repr.__repr__.__setup                                                                               | phase    |
| flag      | module.pprint.pprint._format._pprint_dict._format_dict_items._format._pprint_dict._format_dict_items._format._pprint_str.findall._compile.__and__._get_value                            | phase    |
| hi        | module.pprint.pprint._format._pprint_dict._format_dict_items._format._pprint_dict._format_dict_items._format._pprint_str.findall._compile.compile._code._compile_info.getwidth.getwidth | follower |
| indent    | module.pprint.pprint._format._pprint_dict._format_dict_items._format                                                                                                                    | phase    |
| index     | module.pprint.pprint._format._pprint_dict._format_dict_items._format._pprint_dict._format_dict_items._format._pprint_str.findall._compile.compile._code._compile._compile.__getitem__   | phase    |
| level     | module.pprint.pprint._format._pprint_dict._format_dict_items._format._repr.format._safe_repr                                                                                            | phase    |
| level     | module.pprint.pprint._format._repr.format._safe_repr.format._safe_repr                                                                                                                  | phase    |
| lo        | module.pprint.pprint._format._pprint_dict._format_dict_items._format._pprint_dict._format_dict_items._format._pprint_str.findall._compile.compile._code._compile_info.getwidth.getwidth | phase    |
| max_width | module.pprint.pprint._format._pprint_dict._format_dict_items._format                                                                                                                    | phase    |
| suffix    | module._find_and_load._find_and_load_unlocked._find_spec.find_spec._get_spec.find_spec                                                                                                  | phase    |
| this      | module.pprint.pprint._format._pprint_dict._format_dict_items._format._pprint_dict._format_dict_items._format._pprint_str.findall._compile.compile.parse._parse_sub._parse               | phase    |
| this      | module.pprint.pprint._format._pprint_dict._format_dict_items._format._pprint_dict._format_dict_items._format._pprint_str.findall._compile.compile.parse._parse_sub._parse.get           | phase    |

## globals_plus.py

### Static analysis

| Scope  | Variable    | Role        | Location |
| :------| :-----------| :-----------| :--------|
| module | my_variable | fixed value | line 2   |
{'__builtins__': {'ArithmeticError': <class 'ArithmeticError'>,
                  'AssertionError': <class 'AssertionError'>,
                  'AttributeError': <class 'AttributeError'>,
                  'BaseException': <class 'BaseException'>,
                  'BaseExceptionGroup': <class 'BaseExceptionGroup'>,
                  'BlockingIOError': <class 'BlockingIOError'>,
                  'BrokenPipeError': <class 'BrokenPipeError'>,
                  'BufferError': <class 'BufferError'>,
                  'BytesWarning': <class 'BytesWarning'>,
                  'ChildProcessError': <class 'ChildProcessError'>,
                  'ConnectionAbortedError': <class 'ConnectionAbortedError'>,
                  'ConnectionError': <class 'ConnectionError'>,
                  'ConnectionRefusedError': <class 'ConnectionRefusedError'>,
                  'ConnectionResetError': <class 'ConnectionResetError'>,
                  'DeprecationWarning': <class 'DeprecationWarning'>,
                  'EOFError': <class 'EOFError'>,
                  'Ellipsis': Ellipsis,
                  'EncodingWarning': <class 'EncodingWarning'>,
                  'EnvironmentError': <class 'OSError'>,
                  'Exception': <class 'Exception'>,
                  'ExceptionGroup': <class 'ExceptionGroup'>,
                  'False': False,
                  'FileExistsError': <class 'FileExistsError'>,
                  'FileNotFoundError': <class 'FileNotFoundError'>,
                  'FloatingPointError': <class 'FloatingPointError'>,
                  'FutureWarning': <class 'FutureWarning'>,
                  'GeneratorExit': <class 'GeneratorExit'>,
                  'IOError': <class 'OSError'>,
                  'ImportError': <class 'ImportError'>,
                  'ImportWarning': <class 'ImportWarning'>,
                  'IndentationError': <class 'IndentationError'>,
                  'IndexError': <class 'IndexError'>,
                  'InterruptedError': <class 'InterruptedError'>,
                  'IsADirectoryError': <class 'IsADirectoryError'>,
                  'KeyError': <class 'KeyError'>,
                  'KeyboardInterrupt': <class 'KeyboardInterrupt'>,
                  'LookupError': <class 'LookupError'>,
                  'MemoryError': <class 'MemoryError'>,
                  'ModuleNotFoundError': <class 'ModuleNotFoundError'>,
                  'NameError': <class 'NameError'>,
                  'None': None,
                  'NotADirectoryError': <class 'NotADirectoryError'>,
                  'NotImplemented': NotImplemented,
                  'NotImplementedError': <class 'NotImplementedError'>,
                  'OSError': <class 'OSError'>,
                  'OverflowError': <class 'OverflowError'>,
                  'PendingDeprecationWarning': <class 'PendingDeprecationWarning'>,
                  'PermissionError': <class 'PermissionError'>,
                  'ProcessLookupError': <class 'ProcessLookupError'>,
                  'PythonFinalizationError': <class 'PythonFinalizationError'>,
                  'RecursionError': <class 'RecursionError'>,
                  'ReferenceError': <class 'ReferenceError'>,
                  'ResourceWarning': <class 'ResourceWarning'>,
                  'RuntimeError': <class 'RuntimeError'>,
                  'RuntimeWarning': <class 'RuntimeWarning'>,
                  'StopAsyncIteration': <class 'StopAsyncIteration'>,
                  'StopIteration': <class 'StopIteration'>,
                  'SyntaxError': <class 'SyntaxError'>,
                  'SyntaxWarning': <class 'SyntaxWarning'>,
                  'SystemError': <class 'SystemError'>,
                  'SystemExit': <class 'SystemExit'>,
                  'TabError': <class 'TabError'>,
                  'TimeoutError': <class 'TimeoutError'>,
                  'True': True,
                  'TypeError': <class 'TypeError'>,
                  'UnboundLocalError': <class 'UnboundLocalError'>,
                  'UnicodeDecodeError': <class 'UnicodeDecodeError'>,
                  'UnicodeEncodeError': <class 'UnicodeEncodeError'>,
                  'UnicodeError': <class 'UnicodeError'>,
                  'UnicodeTranslateError': <class 'UnicodeTranslateError'>,
                  'UnicodeWarning': <class 'UnicodeWarning'>,
                  'UserWarning': <class 'UserWarning'>,
                  'ValueError': <class 'ValueError'>,
                  'Warning': <class 'Warning'>,
                  'ZeroDivisionError': <class 'ZeroDivisionError'>,
                  '_IncompleteInputError': <class '_IncompleteInputError'>,
                  '__build_class__': <built-in function __build_class__>,
                  '__debug__': True,
                  '__doc__': 'Built-in functions, types, exceptions, and other '
                             'objects.\n'
                             '\n'
                             'This module provides direct access to all '
                             "'built-in'\n"
                             'identifiers of Python; for example, builtins.len '
                             'is\n'
                             'the full name for the built-in function len().\n'
                             '\n'
                             'This module is not normally accessed explicitly '
                             'by most\n'
                             'applications, but can be useful in modules that '
                             'provide\n'
                             'objects with the same name as a built-in value, '
                             'but in\n'
                             'which the built-in of that name is also needed.',
                  '__import__': <built-in function __import__>,
                  '__loader__': <class '_frozen_importlib.BuiltinImporter'>,
                  '__name__': 'builtins',
                  '__package__': '',
                  '__spec__': ModuleSpec(name='builtins', loader=<class '_frozen_importlib.BuiltinImporter'>, origin='built-in'),
                  'abs': <built-in function abs>,
                  'aiter': <built-in function aiter>,
                  'all': <built-in function all>,
                  'anext': <built-in function anext>,
                  'any': <built-in function any>,
                  'ascii': <built-in function ascii>,
                  'bin': <built-in function bin>,
                  'bool': <class 'bool'>,
                  'breakpoint': <built-in function breakpoint>,
                  'bytearray': <class 'bytearray'>,
                  'bytes': <class 'bytes'>,
                  'callable': <built-in function callable>,
                  'chr': <built-in function chr>,
                  'classmethod': <class 'classmethod'>,
                  'compile': <built-in function compile>,
                  'complex': <class 'complex'>,
                  'copyright': Copyright (c) 2001-2024 Python Software Foundation.
All Rights Reserved.

Copyright (c) 2000 BeOpen.com.
All Rights Reserved.

Copyright (c) 1995-2001 Corporation for National Research Initiatives.
All Rights Reserved.

Copyright (c) 1991-1995 Stichting Mathematisch Centrum, Amsterdam.
All Rights Reserved.,
                  'credits':     Thanks to CWI, CNRI, BeOpen, Zope Corporation, the Python Software
    Foundation, and a cast of thousands for supporting Python
    development.  See www.python.org for more information.,
                  'delattr': <built-in function delattr>,
                  'dict': <class 'dict'>,
                  'dir': <built-in function dir>,
                  'divmod': <built-in function divmod>,
                  'enumerate': <class 'enumerate'>,
                  'eval': <built-in function eval>,
                  'exec': <built-in function exec>,
                  'exit': Use exit() or Ctrl-D (i.e. EOF) to exit,
                  'filter': <class 'filter'>,
                  'float': <class 'float'>,
                  'format': <built-in function format>,
                  'frozenset': <class 'frozenset'>,
                  'getattr': <built-in function getattr>,
                  'globals': <built-in function globals>,
                  'hasattr': <built-in function hasattr>,
                  'hash': <built-in function hash>,
                  'help': Type help() for interactive help, or help(object) for help about object.,
                  'hex': <built-in function hex>,
                  'id': <built-in function id>,
                  'input': <built-in function input>,
                  'int': <class 'int'>,
                  'isinstance': <built-in function isinstance>,
                  'issubclass': <built-in function issubclass>,
                  'iter': <built-in function iter>,
                  'len': <built-in function len>,
                  'license': Type license() to see the full license text,
                  'list': <class 'list'>,
                  'locals': <built-in function locals>,
                  'map': <class 'map'>,
                  'max': <built-in function max>,
                  'memoryview': <class 'memoryview'>,
                  'min': <built-in function min>,
                  'next': <built-in function next>,
                  'object': <class 'object'>,
                  'oct': <built-in function oct>,
                  'open': <built-in function open>,
                  'ord': <built-in function ord>,
                  'pow': <built-in function pow>,
                  'print': <built-in function print>,
                  'property': <class 'property'>,
                  'quit': Use quit() or Ctrl-D (i.e. EOF) to exit,
                  'range': <class 'range'>,
                  'repr': <built-in function repr>,
                  'reversed': <class 'reversed'>,
                  'round': <built-in function round>,
                  'set': <class 'set'>,
                  'setattr': <built-in function setattr>,
                  'slice': <class 'slice'>,
                  'sorted': <built-in function sorted>,
                  'staticmethod': <class 'staticmethod'>,
                  'str': <class 'str'>,
                  'sum': <built-in function sum>,
                  'super': <class 'super'>,
                  'tuple': <class 'tuple'>,
                  'type': <class 'type'>,
                  'vars': <built-in function vars>,
                  'zip': <class 'zip'>},
 '__cached__': '/Users/gvwilson/jorma/sdxpy/test/__pycache__/globals_plus.cpython-313.pyc',
 '__doc__': None,
 '__file__': '/Users/gvwilson/jorma/sdxpy/test/globals_plus.py',
 '__loader__': <_frozen_importlib_external.SourceFileLoader object at 0x104a98110>,
 '__name__': '__main__',
 '__package__': '',
 '__spec__': ModuleSpec(name='__main__', loader=<_frozen_importlib_external.SourceFileLoader object at 0x104a98110>, origin='/Users/gvwilson/jorma/sdxpy/test/globals_plus.py'),
 'my_variable': 123,
 'pprint': <module 'pprint' from '/Users/gvwilson/.local/share/uv/python/cpython-3.13.9-macos-aarch64-none/lib/python3.13/pprint.py'>}

### Dynamic analysis

| Variable  | Scope                                                                                                                                                                                   | Role     |
| :---------| :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------| :--------|
| allowance | module.pprint.pprint._format._pprint_dict._format_dict_items._format._pprint_dict._format_dict_items._format                                                                            | phase    |
| char      | module.pprint.pprint._format._pprint_dict._format_dict_items._format._pprint_dict._format_dict_items._format._pprint_str.findall._compile.compile.parse._parse_sub._parse.get.__next    | phase    |
| char      | module.pprint.pprint._format._pprint_dict._format_dict_items._format._pprint_dict._format_dict_items._format._pprint_str.findall._compile.compile.parse._parse_sub._parse.match         | phase    |
| data      | module.pprint.pprint._format._repr.format._safe_repr.format._safe_repr.format._safe_repr.__repr__.__setup                                                                               | phase    |
| flag      | module.pprint.pprint._format._pprint_dict._format_dict_items._format._pprint_dict._format_dict_items._format._pprint_str.findall._compile.__and__._get_value                            | phase    |
| hi        | module.pprint.pprint._format._pprint_dict._format_dict_items._format._pprint_dict._format_dict_items._format._pprint_str.findall._compile.compile._code._compile_info.getwidth.getwidth | follower |
| indent    | module.pprint.pprint._format._pprint_dict._format_dict_items._format                                                                                                                    | phase    |
| index     | module.pprint.pprint._format._pprint_dict._format_dict_items._format._pprint_dict._format_dict_items._format._pprint_str.findall._compile.compile._code._compile._compile.__getitem__   | phase    |
| level     | module.pprint.pprint._format._pprint_dict._format_dict_items._format._repr.format._safe_repr                                                                                            | phase    |
| level     | module.pprint.pprint._format._repr.format._safe_repr.format._safe_repr                                                                                                                  | phase    |
| lo        | module.pprint.pprint._format._pprint_dict._format_dict_items._format._pprint_dict._format_dict_items._format._pprint_str.findall._compile.compile._code._compile_info.getwidth.getwidth | phase    |
| max_width | module.pprint.pprint._format._pprint_dict._format_dict_items._format                                                                                                                    | phase    |
| suffix    | module._find_and_load._find_and_load_unlocked._find_spec.find_spec._get_spec.find_spec                                                                                                  | phase    |
| this      | module.pprint.pprint._format._pprint_dict._format_dict_items._format._pprint_dict._format_dict_items._format._pprint_str.findall._compile.compile.parse._parse_sub._parse               | phase    |
| this      | module.pprint.pprint._format._pprint_dict._format_dict_items._format._pprint_dict._format_dict_items._format._pprint_str.findall._compile.compile.parse._parse_sub._parse.get           | phase    |

## locals.py

### Static analysis

| Scope              | Variable | Role        | Location |
| :------------------| :--------| :-----------| :--------|
| module.show_locals | high     | fixed value | line 1   |
| module.show_locals | low      | fixed value | line 1   |
| module.show_locals | i        | stepper     | line 3   |
start: {'low': 1, 'high': 3}
loop 1: {'low': 1, 'high': 3, 'i': 1}
loop 2: {'low': 1, 'high': 3, 'i': 2}
end: {'low': 1, 'high': 3, 'i': 2}

## manual.py

### Static analysis

| Scope            | Variable  | Role        | Location |
| :----------------| :---------| :-----------| :--------|
| module           | TESTS     | fixed value | line 40  |
| module.run_tests | all_tests | fixed value | line 24  |
| module.run_tests | results   | fixed value | line 25  |
| module.run_tests | test      | stepper     | line 26  |
| module.sign      | value     | fixed value | line 2   |
pass 2
fail 1
error 1

## runner.py

### Static analysis

| Scope            | Variable | Role        | Location |
| :----------------| :--------| :-----------| :--------|
| module.run_tests | results  | fixed value | line 21  |
| module.run_tests | name     | stepper     | line 22  |
| module.run_tests | test     | stepper     | line 22  |
| module.sign      | value    | fixed value | line 1   |
pass 2
fail 1
error 1

## signature.py

Error during dynamic analysis (TypeError): one() missing 1 required positional argument: 'value'
### Static analysis

| Scope      | Variable | Role        | Location |
| :----------| :--------| :-----------| :--------|
| module     | func     | stepper     | line 7   |
| module.one | value    | fixed value | line 4   |
zero

## type_func.py

Warning: no variables found.
### Static analysis

<class 'function'>

## type_int.py

Warning: no variables found.
### Static analysis

<class 'int'>

## type_len.py

Warning: no variables found.
### Static analysis

<class 'builtin_function_or_method'>


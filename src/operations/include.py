#
# include.py
#
# The Pashmak Project
# Copyright 2020 parsa shahmaleki <parsampsh@gmail.com>
#
# This file is part of Pashmak.
#
# Pashmak is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Pashmak is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Pashmak.  If not, see <https://www.gnu.org/licenses/>.
#########################################################################

''' Includes another script file to program '''

import os
from syntax import parser
from core import modules

def run(self, op: dict):
    ''' Includes another script file to program '''

    self.require_one_argument(op, 'include operation requires argument')
    arg = op['args'][0]
    self.arg_should_be_variable_or_mem(arg, op)

    content = ''

    if arg == '^':
        paths = self.get_mem()
    else:
        self.variable_required(arg[1:], op)
        paths = self.get_var(arg[1:])

    if not paths:
        return

    if type(paths) == str:
        paths = [paths]
    elif type(paths) != list and type(paths) != tuple:
        self.raise_error('ArgumentError', 'invalid argument type passed to include operation', op['index'])

    for path in paths:
        code_location = path
        if path[0] == '@':
            code_location = path
            module_name = path[1:]
            try:
                namespaces_prefix = ''
                for part in self.namespaces_tree:
                    namespaces_prefix += part + '.'
                namespaces_prefix += '@'
                if not namespaces_prefix + module_name in self.included_modules:
                    content = modules.modules[module_name]
                    # add this module to imported modules
                    self.included_modules.append(namespaces_prefix + module_name)
                else:
                    return
            except KeyError:
                self.raise_error('ModuleError', 'undefined module "' + module_name + '"', op)
        else:
            if path[0] != '/':
                path = os.path.dirname(os.path.abspath(self.main_filename)) + '/' + path
            try:
                content = open(path, 'r').read()
                content = '$__file__ = "' + path.replace('\\', '\\\\') + '";\n$__dir__ = "' + os.path.dirname(path).replace('\\', '\\\\') + '"\n' + content
                content += '\n$__file__ = "' + self.get_var('__file__').replace('\\', '\\\\') + '"'
                content += '\n$__dir__ = "' + self.get_var('__dir__').replace('\\', '\\\\') + '"'
                code_location = path
            except FileNotFoundError as ex:
                self.raise_error('FileError', str(ex), op)
            except PermissionError as ex:
                self.raise_error('FileError', str(ex), op)
    
        operations = parser.parse(content, filepath=code_location)
        self.exec_func(operations, False)

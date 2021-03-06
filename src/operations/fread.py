#
# fread.py
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

''' Reads file content '''

def run(self, op: dict):
    ''' Reads file content '''
    self.require_one_argument(op, 'fread operation requires argument')
    arg = op['args'][0]
    self.arg_should_be_variable_or_mem(arg, op)

    if arg == '^':
        path = self.get_mem()
    else:
        self.variable_required(arg[1:])
        path = self.get_var[arg[1:]]

    try:
        f = open(path, 'r')
        self.mem = f.read()
        f.close()
    except FileNotFoundError as ex:
        self.raise_error('FileError', str(ex), op)
    except PermissionError as ex:
        self.raise_error('FileError', str(ex), op)

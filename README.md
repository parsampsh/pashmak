
##### NOTE: this file is auto generated from `doc` folder. do not change it directly. If you want to edit documentation, edit `doc/` folder files. your changes will built from that folder into this file.

# Pashmak Programming Language
Hi there. this is Pashmak programming language. Pashmak is an interpreter written in Python.
Pashmak scripts have cool and pashmaki syntax.

### hello world!
this is a simple hello world script in pashmak:

```bash
println 'hello world'
```

## Online interpreter
if you want to test pashmak without installing and need to run it online, go to [Pashmak online interpreter](https://pashmio-parsampsh.fandogh.cloud/)

## Authors
pashmak is written by [parsampsh](https://github.com/parsampsh) and [contributors](https://github.com/pashmaklang/pashmak/graphs/contributors)

## Contributing
if you want to contribute to this project, read [Contributing Guide](CONTRIBUTING.md)

## Changelog
to see pashmak versions changelog, read [Changelog](CHANGELOG.md)

## Security Policy
if you detected an bug or vulnearability, read [Pashmak Security Policy](/SECURITY.md).

# Documentation
read the following Documentation to learn pashmak.

### Table of contents
- [Installation](#installation)
- [Basics](#basics)
- [Variables](#variables)
- [Constants](#Constants)
- [Read Input From User](#read-input-from-user)
- [Sections](#sections)
- [If statements](#if-elif-else-statement)
- [Functions](#functions)
- [Arrays](#arrays)
- [Try-Endtry statement](#try-and-endtry-statement)
- [OS Commands](#os-commands)
- [Importing scripts](#include-scripts)
- [Namespaces](#namespaces)
- [Classes](#Classes)
- [Eval](#eval)
- [Modules](#internal-modules)



## Installation

### GNU/Linux/Unix
this installation guide is for GNU/Linux/UNIX systems. also compile process needs `pyinstaller`.
if you don't have pyinstaller, type `pip3 install pyinstaller` in terminal

compile & install:

```bash
# checkout to latest release
git branch installation $(git describe --abbrev=0)
git checkout installation

# compile and install
make all
make
sudo make install

# back to master branch and delete installation branch
git checkout master
git branch -D installation
```

run above commands in terminal to install pashmak interpreter on your GNU/Linux/UNIX system.

also if you want install latest version (in development), do not run above git commands and just run it:

```bash
make all
make
sudo make install
```

above commands install latest (development) state of the program

now you can run interpreter in terminal:

```bash
pashmak --info # shows info about pashmak
pashmak -v # --version, shows version of pashmak
pashmak app.pashm
pashmak /path/to/script.pashm # runs file
pashmak - # gets code from stdin and run that
pashmak -r "<you code...>" # run code from cli arguments with `-r` option
pashmak -m # or --modules. shows list of available pashmak modules on the system
```

IF YOU DON'T WANT TO INSTALL IT, you can run this with python3 in terminal:

```bash
cd /path/to/project/folder
python3 src/pashmak.py
# or
./src/pashmak.py
```

#### uninstallation
to uninstall pashmak, run this make command in terminal:

```bash
sudo make uninstall
```

pashmak will be remove from your system.

### Windows
in windows, you can run program with python interpreter without compiling:

```bash
cd \path\to\project
python src\pashmak.py
```

but also you can compile it with `pyinstaller`. if you don't have pyinstaller, enter `pip install pyinstaller` in command line

compile:

```bash
# install pyinstaller with pip
pip install pyinstaller

# configure & compile
.\win-configure.bat
python -m PyInstaller src\pashmak.py --onefile
```

now executable file is created in `dist\pashmak.exe`:

```bash
dist\pashmak.exe -v
```



## Basics

a simple printing in pashmak on screen:

```bash
mem 'something to print\n'; print ^
```

or

```bash
print 'something to print\n';
```

#### how it works?

first, we go through pashmak syntax structure.
the base structure of pashmak syntax is this:

```bash
<operation> [arguments];
<operation> [arguments];
<operation> [arguments]; <operation> [arguments];
```

in this example, we have two operations:

```bash
mem 'something to print\n'; # first operation
out ^; # second operation
```

##### NOTE: the `;` in the end of lines is not required. you can write your code without `;` IF you don't want to write two or more operations in one line

here, mem is an operation and `'something to print\n'` is the argument of that, and
out is an operation and `^` is the argument of that.

but what is the function of this code?

when you run the script in terminal:

```bash
pashmak myscript.pashm # or any filename you saved code in that
```

##### NOTE: the `.pashm` extension for pashmak scripts is not required. you can run any file with any name as pashmak script

you will get this output:

```
something to print
```

this code, prints `'some thing to print'` on the stdout.
but how?

first, `mem` command brings the string `'some thing to print'` in memory, and next `out` command prints the memory value on screen.

### what is `mem`?
mem is a temp place to make values.

```bash
mem 'hello world'
print ^ # the ^ is pointer of mem
```

the ^ is pointer of mem

you can also write the code like this to have shorter code (we have to use `;` to seprate them):

```bash
mem 'hello world\n'; print ^
```

###### NOTE: remember to put \n when you want to go to the next line

#### mem is temp

look at this example:

```bash
mem 'some thing\n'

print ^ # output: some thing

print ^ # output: None
```

why in the first time when mem value was read, the value correctly was printed on screen, but in the second time, the `None` was printed?

because memory is temporary. when you read the memory, that will be empty after read automaticly.

look at this example:

```bash
mem 'first value\n'
print ^

mem 'second value\n'
print ^
```

output of this code:

```
first value
second value
```

###### NOTE: the # character is comment operation. you can put comment in your code after # character

### more about mem
you can calculate every thing in mem

for undrestanding, look at the following examples:

```bash
mem 'hi there'; print ^ # output: hi there

# you can paste strings
mem 'first string ' + 'last string'; print ^ # output: first string last string

# run math operations
mem 2*7; print ^ # output: 14

mem 3*(2+1); print ^ # output: 9

mem str(7*7) + ' is sum'; print ^ # output: 49 is sum
# the `str` function gets a value and convert it to string.
# in here you can not paste number to string. first need to convert num to str with str()
```

the `mem` command is absolutely important and you need to use it everywhere

#### print `;` and `#`
for printing `;` and `#` special characters, put a `\` before them:

```bash
mem 'this is \; semicolon\n'; print ^
mem 'this is \# sharp\n'; print ^
```

output:

```
this is ; semicolon
this is # sharp
```

### printing without using mem
this is a easier syntax for printing:

```bash
mem 'hello world\n'; print ^

# this is easier
print 'hello world\n'

print str(2*2)

print 'hello ' + 'parsa\n'

print 'num is ' + str(100+7)
```

you can use all of features of `mem` in the argument of commands like above example.

after this, we never use `mem <something>; print ^;` pattern for printing, and we just use `print` command.

### println

if you want to print something and go next line, you have to put `\n` after your string.

but with `println` command, you don't need to use `\n` and that will put automaticaly:

```bash
println 'hello world'
```

output:

```
hello world<nextline>
```

also there is a alias for `println`, this is `printl`:

```bash
#println "hello world"
printl "hello world"
```



## Variables

variables are like a pot where you can save data in it

we work with three commands: `set`, `copy`, `free`, to set and handle variables in pashmak

```bash
$myvar = 'this is data'

println $myvar # output: this is data
```

###### NOTE: always put $ before name of variable everywhere

also you can set more than one variable with `set` command:

```bash
set $var1
# or
$var1
$var2; $var3 # default value is null
```

### use variables in mem

look at this example:

```bash
$name = 'parsa' # set name variable

println 'hello ' + $name # output: hello parsa

$num = 12
println $num * 5 # output: 60

$num2 = 4 # alias of `copy ^ $num2`

println $num * $num2 + 1 # output: 49
```

#### copy variables in other variables

look at this example:

```bash
$var1 = 'hi'
$var2 = 'bye'

println $var1 # output: hi
println $var2 # output: bye

$var2 = $var1

out $var1 # output: hi
out $var2 # output: hi

```

#### NOTE: allowed characters for variable name are `A-Z`, `a-z`, `&._` characters.

### put `mem` value to variable

we can set value of mem to variables with this code:

```bash
mem 'something'
$myvar = ^
```

if you put `^` (mem symbol) as value, memory value will put in the variable

also you can use that mem alongside another values.

for example:

```bash
mem 'parsa'
$message = 'my name is ' + ^
println $message # output: my name is parsa

mem 10
println (^ + 5) * 2 # output: 30
```

### free(delete) variables
when you set a variable, that var is in memory. you can delete that var with `free` command:

```bash
$somevar = 'some value'
println $somevar # output: some value

free $somevar

println $somevar # you will get VariableError: undefined variable $somevar (because it was deleted by free command)
```

also you can make free more than one variable with `free` command:

```bash
free $var1 $var2 $var3 # ...
```

### checking a variable isset
you can check a variable existens with `isset` command

look at this example:

```bash
$somevar; $v # set `somevar` and `v` variables

isset $somevar; println ^ # output: True
isset $this_var_not_found; println ^ # output: False
isset $somevar $sassadffgdty; println ^ # output: False
isset $somevar $v; println ^ # output: True
```

#### how it works?

the isset command gets one or more variable names and if all of that vars exist, it will put `True` in  memory and if all or one/more of them are not exists, it will put `False` in memory

### typeof command

you can get the data type of a variable with `typeof` function.

look at this example:

```bash
$mystr = 'hi'
$myint = 20
$myfloat = 15.32
$mybool = False

typeof $mystr; println ^ # output: <class 'str'>
typeof $myint; println ^ # output: <class 'int'>
typeof($myfloat); println ^ # output: <class 'float'>
typeof($mybool); println ^ # output: <class 'bool'>
# NOTE: the `()` is not required
```

this command puts the typeof variable in mem

### required command

the required command requiring an variable existens.

look at this example:

```bash
$name

required $name
```

when we run this code, program will run successful.

but now we comment the first line:

```bash
#$name
required $name
```

now $name variable is not set, and you will get this error:

```
VariableError:
    undefined variable $name
```

the `required` command checks a variable is exists, if no, raising RequireError

### python datatype methods
datatype of the pashmak variables, is handled by python. this means you can use all python methods on them.

for example:

```bash
$mystring = '  hello world          '
println $mystring->strip() # output: `hello world`
```

#### NOTE: in python, for calling function or access to property of a object, we use `.` character, but in pashmak we use `->` symbol(like php)

## Constants
constants (consts) are even like variables, but one thing is different in constants, **Constants values cannot be changed**.

for example:

```bash
# declare the const
$&name = 'the value'

println $&name
```

output:

```
the value
```

to declare consts, you only need to put a `&` in the name of variable(location of that is not important).

```bash
$&const1 = 123
$&const2 = 'fsgdf'
# ...
```

when we try to change value of the const, we will get error:

```bash
$&name = 'the name'

$&name = 'new value'
```

output:

```
ConstError: "$&name" is const and cannot be changed...
```

also you can **declare** a constant, but set value of that later.

for example:

```bash
$&name # only declare constant, default value is `None`

# set value
$&name = 'parsa'

println $&name
```

output:

```
parsa
```



## Read Input From User

you can read input from user in stdin

look at this example:

```bash
$name # set the name variable
print 'what is your name? '
read $name # read a input and copy that in $name variable
println 'hello ' + $name # say hello to $name :)
```

when we run this code, output is this:

```
what is your name? <input>parsa
hello parsa
```

after print `what is your name? ` program waits for input, and when you type something and press enter, program prints `hello <your-input>`

for example here I entered `parsa` as input and program printed `hello parsa`

we can get input from user like above example

also look at this example:

```bash
$num1; $num2

print 'enter first number: '
read $num1

print 'enter second number: '
read $num2

# now, $num1 and $num2 are string. we convert string to int:
$num1 = int($num1)
$num2 = int($num2)

# now we want to plus them
$sum = $num1 + $num2

println str($sum)
```

program output:

```bash
enter first number: <input>12
enter second number: <input>2
14
```

this example gets two numbers from user and shows sum of them

also you can read value directly:

```bash
print 'enter your name: '
$name = ^ read ^
println 'hello ' + $name
```

the `^ read ^` reads value and puts that in the variable.

### read command line arguments
to access command line arguments, you can use `$argv` variable.

look at this example:

```bash
println $argv[1]
```

we run above code:

```bash
pashmak mycode.pashm hello
```

output:

```
hello
```

actualy, `$argv` is an array contains command line arguments.



# Sections
section is a system to make pointer to a part of code. this is useful to create loop, if and...

look at this example:
```bash
section my_loop
    println 'hello world'
goto my_loop
```

this code prints `hello world` non-stop

actually when my code starts, prints hello world and then `goto` commands directs program step to the `my_loop` section and it will repeat again and again.

###### NOTE: that TAB before `println 'hello world'...` line is not required. this is writen only to have beautiful code

look at this example:

```bash
$i = 1

section loop
    println $i # print $i
    $i = $i + 1 # add 1 to $i
mem $i < 10; gotoif loop # check the condition in `mem` and use gotoif command
```

the output of this code is
```
1
2
3
4
5
6
7
8
9
```

we have 3 operations about section system:
- section
- goto
- gotoif

### section
this command gets name of section as parameter like above examples. this is for declare the section

### goto
goto gets a name as section name and goto to that section.

### gotoif
gotoif checks `mem` and if mem is True, will go to wanted section. if not, do nothing and continue

look at this example:

```bash
# read age from user
print 'enter your age: '
$age; read $age
$age = int($age)

mem $age > 18; gotoif age_is_more_than_18 # if age is more than 18, goto age_is_more_than_18 section

# if not, this line will run and program goes to age_is_less_than_18
goto age_is_less_than_18

section age_is_more_than_18

    println 'you are more than 18'
    goto after_if

section age_is_less_than_18

    println 'you are less than 18'

section after_if

println 'program ends'
```

we run the program:

```bash
enter your age: <input>22
you are more than 18
program ends
```

run again:
```bash
enter your age: <input>14
you are less than 18
program ends
```



# If elif else statement
in the previous part, you learned how to use **sections** for creating **Conditions** and **Loops**.
but there is a easy way to create **Conditions**, that is **If..elif..else** statement. this system is very easy for creating conditions and handling program flow.

example:

```bash
if 2 == 2
    println 'yes, 2 is 2'
endif
```

or:

```bash
if 3 == 7
    println '3 is 7'
else
    println '3 is NOT 7'
endif
```

in this part, we learn how to use this system.

The if syntax is this:

```bash
if <condition>
    # code
endif
```

for example:

```bash
$age = 30

if $age > 18
    println 'Welcome!'
endif
```

output:

```
Welcome!
```

```bash
$age = 12

if $age > 18
    println 'Welcome!'
endif

# above code haven't output
```

also you can use `else`:

```bash
$age = 12

if $age > 18
    println 'Welcome!'
else
    println 'you cannot access'
endif
```

if condition of `if` is not true, `else` block will be runed.

also there is other keyword `elif`:

```bash
$num = 17

if $num == 5
    println 'num is 5'
elif $num == 6
    println 'num is 6'
elif $num == 17
    println 'num is 17'
else
    println 'nothing'
endif
```

output:

```
num is 17
```

actually, `elif` block will be checked one by one. `elif` means `else if`.

### If in If
you can write ifs in ifs.

look at this example:

```bash
$num = 15
$test = True

if $num == 18
    pass
elif $num == 15
    println 'num is 15'

    # another if in the parent if
    if $test
        println 'this is a test'
    else
        println 'this is not test'
    endif
endif
```

output:

```
num is 15
this is a test
```



# Functions
function is a system to make alias for some codes (function).

look at this example:
```bash
func say_hello
    println 'hello world'
endfunc

say_hello
# or
say_hello()
```

output:

```
hello world
```

```bash
func say_hello
    println 'hello world'
endfunc

say_hello
say_hello()
```

output:

```
hello world
hello world
```


you can declare a function and call it from everywhere. when you call a function, all of codes inside that function will run

for declare a function you have to write `func <name-of-function>;`. and write codes. then for close function write `endfunc;` after codes

look at this smarter function:
```bash
mem 'program started\n'; out ^

func say_hello
    $name = ^ # copy mem to $name
    println 'hello ' + $name
endfunc

mem 'parsa'; say_hello
```

program output:

```
program started
hello parsa
```

##### NOTE: name of functions should not have `.` character. for example, name `foo.bar` for function is invalid and you will get error `FunctionNameContainsDotError`

### passing argument to Functions
for pass argument to the Functions, you can put value after name of function:

```bash
func myfunc
    out ^
endfunc

myfunc "hello"
# or
myfunc("hello")
```

output:

```
hello
```

##### NOTE: using `()` in end of function is optional. for example:

```bash
myfunc
myfunc()
# above codes are not different
```

or with arguments:

```bash
myfunc "arg1", "arg2"
myfunc("arg1", "arg2")
```

##### how it works?
you can put a value after name of function. this value will put in mem and you can access this argument from mem.

look at this example:

```bash
func say_hello
    $name = ^ # copy mem(the passed argument to function) to $name
    println 'hello ' + $name
endfunc

say_hello 'parsa'
```

output:

```
hello parsa
```

also you can pass more than 1 argument to functions:

```bash
func say_hello
    $args = ^ # copy mem to $args
    $first_name = $args[0]
    $last_name = $args[1]
    println 'hello ' + $first_name + ' ' + $last_name
endfunc

say_hello 'parsa', 'shahmaleki'
```

arguments should be split with `,` and this will make a array in mem and function can access that array and use arguments.

we to copy function argument (in mem) to a variable, using this syntax:

```bash
func say_hello
    $name = ^
    println 'hello ' + $name
endfunc

say_hello 'parsa'
```

but also we can use this syntax to copy function argument to variable with better syntax:

```bash
func say_hello ($name)
    println 'hello ' + $name
endfunc

say_hello 'parsa'
```

we can put `($varname)` after name of function (with a space between them) and mem will copy automatic in that variable.
also you can don't use `()` and you can write above code like this:

```bash
func say_hello $name # without ()
    println 'hello ' + $name
endfunc

say_hello 'parsa'
```

also we can use mem symbol in argument of function.

for example:

```bash
func say_hello $name # without ()
    println 'hello ' + $name
endfunc

mem 'parsa'

say_hello ^
```

or:

```bash
func say_hello $name # without ()
    println 'hello ' + $name
endfunc

mem 'parsa'

say_hello ^ + ' shahmaleki'
```

#### how two handle multiple arguments?
in the above examples, all of created functions only have ONE argument. some times our functions recives more than one arguments. how we can handle this?

to handle this, you can use something like this:

```bash
func say_hi ($args)
    $first_name = $args[0]
    $last_name = $args[1]
    println 'hello ' + $first_name + ' ' + $last_name
endfunc

say_hi 'parsa', 'shahmaleki'
```

in above example, all of our arguments are in `$args`. that variable is a python tuple/list. we can handle multiple arguments like this example.

### local variables & global variables

look at this example:

```bash
func myfunc
    $name = 'new name'
    println $name
endfunc

$name = 'parsa'
println $name

myfunc

println $name
```

output:

```
parsa
new name
parsa
```

there is a note. why when we changed `$name` variable in `myfunc` function, this was the old value after function?

the `$name` where was set in `myfunc`, is local. means that do not points to global `$name` in out program.

the seted variables in Functions, are local. also Functions cannot change global variables

the variable environment in Functions are isolated.

so, how to change a global variable from a function?

the answer is in `gset`:

```bash
func myfunc
    $name = 'new name'
    gset 'name', $name
    println $name
endfunc

$name = 'parsa'
println $name

myfunc

println $name
```

output:

```
parsa
new name
new name
```

here, `gset` command gets two parameters: first, global variable name and second, new value for that

this command sets value of that variable globaly.

##### NOTE: after running gset, new value will set for global variable but it will not set also localy. so, after use gset, also use copy to update value localy (if you want)

### handle functions output

when you calling a function, that function may return a output. this value as output should be save in mem

look at this example:

```bash
func add_two_nums ($nums)
    $sum = $nums[0] + $nums[1] # add two numbers
    mem $sum # put result to mem
endfunc

# now we call this function
add_two_nums 10, 5
$result = ^ # function output is in mem and we copy mem to variable $result
println $result
```

output:

```
15
```

now, above syntax is ugly. we can write this code like this:

```bash
func add_two_nums ($nums)
    $sum = $nums[0] + $nums[1] # add two numbers
    mem $sum # put result to mem
endfunc

# now we call this function
$result = ^ add_two_nums 10, 5
println $result
```

we write two operations in one operation to have better syntax. calling function and assigning mem (function output) to `$result`.
we just have to write variable name and an `=`, and next write `^` and them write our code after this.

like it:

```bash
$variable = ^ my_command_or_function 'my', 'arguments'
```

and them this code will run and mem value will put into the variable



# Arrays
arrays are a list from variables

look at this example:

```bash
$names = ['parsa', 'pashmak', 'jack']

println $names # output: ['parsa', 'pashmak', 'jack']
println $names[0] # output: parsa
println $names[1] # output: pashmak
println $names[2] # output: jack
```

this is a example about array and loop:

```bash
$names = ['parsa', 'pashmak', 'jack']

$i = 0

section loop
    println $names[$i]
    $i = $i + 1
mem $i < len($names); gotoif loop
```

output:

```
parsa
pashmak
jack
```

the above code prints names one by one

### arraypush
you can add new item to a array:

```bash
$myarray = ['red', 'green', 'blue']
println $myarray # output: ['red', 'green', 'blue']

mem 'yellow'; arraypush $myarray ^ # add mem (^) to the $myarray
println $myarray # output: ['red', 'green', 'blue', 'yellow']
```

`arraypush` operation gets two argument: array and new item you want to add to the array

also you can use python methods:

```bash
$myarray = ['first', 'second']
mem $myarray->append('new item')
```

### arraypop
you can delete a item from array:

```bash
$myarray = ['red', 'green', 'blue']
println $myarray # output: ['red', 'green', 'blue']

mem 1; arraypop $myarray ^ # remove index mem (^) from $myarray
println $myarray # output: ['red', 'blue']
```

`arraypop` operation gets two argument: array and index of that item you want to be remove from array

also you can use python methods:

```bash
$myarray = ['first', 'second']
mem $myarray->pop(0)
```



# Try and Endtry statement

we may recive some errors in our program. for example:

```bash
println $this_var_not_found
```

output:

```
VariableError:
    undefined variable $this_var_not_found
```

or:

```bash
# undefined operation
printlgdfgfd ^
```

output:

```
SyntaxError:
        undefined operation "outttt"
```

they are errors

##### but how to handle errors?

we can handle errors with `try-endtry` statement.

look at this example:

```bash
try handle_error
    println $somevar
endtry

goto after_error

section handle_error

mem 'some errors raised\n'; out ^

section after_error
```

when you write code between `try <section-name> ... endtry`, errors will not raised in them and if an error is raised, that section where passed to try operation will run.

this is helpful.

#### how to access raised error data?

when error is raised in try statement, error data will put in mem (^):

```bash
try handle_error
    println $somevar
endtry

goto after_error

section handle_error

$ex = ^ # copy mem (^) to $ex variable (this includes information about raised error)
println $ex # output: {"type": "VariableError", "message": "undefined variable $somevar"}...

section after_error
```

#### raising errors
```bash
println 'program started'

raise 'MyError', 'this is my error'
# or
raise('MyError', 'this is my error')

println 'this will not print'
```

output:

```
progrma started
MyError: this is my error
```

the `raise` function can raise errors in program

first argument `'TheError'` is error type and second error `'this is my error'` is error message.



# OS Commands

here is some commands about OS

### chdir
change directory. with this command you can change program working directory:

```bash
chdir '/tmp'
```

### cwd
get current working directory.

```bash
cwd
println ^
```

output:

```
/tmp
```

or:

```bash
cwd # or `cwd()`
$cwd = ^
println $cwd
```

or:

```bash
$cwd = ^ cwd
println $cwd
```

this command puts current working directory path in mem

### system
you can run shell commands by this command:

```bash
system 'ls /tmp'
```

also after run `system` function, exit code will put in `mem`:

```bash
system 'ls /'
println ^ # output: 0
```

### exit
this command exits program

look at this example:

```bash
println 'first print\n'

exit

println 'last print\n' # this will not print
```

output:

```
first print
```

###### exit with exit code:

```bash
println 'hello world\n'
exit 1
```

exit code of program will be `1`

or you can use `exit` command:

```bash
exit # with 0 default exit code
exit 10 # with 10
```

### `$__file__` and `$__dir__` variables
`$__file__` and `$__dir__` variables are two variables contains self script filepath and dirpath.

for example, if you run an script in `/home/parsa/myscript.pashm` with this content:

```bash
println $__file__
println $__dir__
```

output is:

```
/home/parsa/myscript.pashm
/home/parsa
```

The `$__file__` variable contains filepath of current running script.

The `$__dir__` variable contains dirpath of current running script.



# Include scripts
you can distribute your code in more than 1 files.

for example, we have 2 files: `app.pashm`, `fib.pashm`.
`app.pashm` is main file. `fib.pashm` contains a function to show fibonaccy algo.

###### fib.pashm:
```bash
func fib
    $a = 1
    $b = 1

    section loop;
        println $a

        $tmp_a = $a
        $tmp_b = $b

        $a = $tmp_b

        $b = $tmp_a + $tmp_b
    mem $a < 10000; gotoif loop
endfunc
```

###### app.pashm:
```bash
import 'fib.pashm'

fib
```

when we run `import` function and pass a file path to that, content of that file will be included in our code and will run. for example, here we used a function from the `fib.pashm` file.

also you can import more than 1 scripts in one line:

```bash
# seprate them with `,`
import 'a.pashm', '/path/to/b.pashm', 'dir/c.pashm'
# or with () is not different
import('a.pashm', '/path/to/b.pashm', 'dir/c.pashm')
```



# Namespaces

name space is a very useful system to split sections of program.

look at this example:

```bash
namespace App
    func say_hello
        println 'hello world'
    endfunc

    say_hello
endnamespace

App.say_hello
```

output:

```
hello world
hello world
```

actualy, everything where is declared between `namespace <something>;` and `endnamespace;` will be under this.

in above example, we declared a namespace named `App`. and we declared `say_hello` function in that.

next, we called `say_hello` inside the namespace, and one time we called `say_hello` outside the namespace.

when we are calling a member of namespace from outside of that namespace, we have to put name of namespace with a `.` before name of that function

for example here, our namespace name is `App` and out function name is `say_hello`. we can write only `say_hello` inside the namespace but for call it from outside of namespace, we have to write `App.say_hello`.

also look at this example:

```bash
namespace First
    func dosomething
        println 'i am from First'
    endfunc
endnamespace

namespace Last
    func dosomething
        println 'i am from Last'
    endfunc
endnamespace

First.dosomething
Last.dosomething
```

output:

```
i am from First
i am from Last
```

also you can use `endns` keyword insted of `endnamespace`:

```bash
namespace App
    func say_hello
        println 'hello world'
    endfunc

    say_hello
endns

App.say_hello
```

also namespace system is sync with variables:

```bash
namespace App
    $name = 'parsa'
    println $name # output: parsa
    println $App.name # output: parsa
endns

println $App.name # output: parsa

# but this has error:
println $name # VariableError: undefined variable $name, because it is in App namespace and is accessible with `$App.name`
```

##### NOTE: name of namespace should not have `.` character. if you want to do this, use [subnamespace](#namespace-in-namespace-subnamespace).

this system is very useful.

### use operation
the `use` operation is a command to use content of a namespace.

look at this example:

```bash
namespace App
    func dosomething
        println 'hello world'
    endfunc

    $name = 'parsa'
endns

App.dosomething
println $App.name
```

output:

```
hello world
parsa
```

we have to put `App.` before `dosomething` to run this function.
but i want to don't use namespace prefix and just type name of function to call this. what i have to do?

look at this example:

```bash
namespace App
    func dosomething
        println 'hello world'
    endfunc

    $name = 'parsa\n'
endns

use App

App.dosomething
dosomething

println $App.name
println $name
```

output:

```
hello world
hello world
parsa
parsa
```

when i use `use` operation and give a namespace as argument to that, i can call all of that namespace members without namespace prefix.

for example if there is a namespace named `App` and have a function named `dosomething`, for call that function i have to write `App.dosomething`. but if i run `use App`, after that i can call this function just by typing `dosomething;`

### namespace in namespace (subnamespace)
you can declare a namespace in a namespace

look at this example:

```bash
namespace App
    func hello
        println 'hello world'
    endfunc

    # declare namespace `Core` under `App`
    namespace Core
        func run
            println 'the core'
        endfunc
    endns
endns

# now we use it
App.hello

App.Core.run
```

output:

```
hello world
the core
```

### importing inside namespaces
you can import an script inside an namespace.

for example, we have `foo.pashm` and `bar.pashm` scripts.

##### `foo.pashm`:

```bash
namespace foo
    func hello
        println 'hello world'
    endfunc
endns

func bye
    println 'good bye'
endfunc
```

##### `bar.pashm`:

```bash
import 'foo.pashm';

namespace App;
    import 'foo.pashm';
endns;

foo.hello # output: hello world
bye # output: good bye

App.foo.hello # output: hello world
App.bye # output: good bye
```

in above example, we imported `foo.pashm` inside an namespace and content of `foo.pashm` is loaded under that namespace. for example, `foo.hello` function is loaded under `App` namespace, so finally will be set as `App.foo.hello`.



# Classes
class is a system to declare a structure of data. actually, class is a model with some fields.

for example, we want to declare a model from **Car**. we can declare a class:

```bash
class Car
    $name
    $color
endclass
```

in above example, we declared a class named `Car` with `name` and `color` properties.

let's use this:

```bash
class Car
    $name
    $color
endclass

$my_car = ^ new Car

println $my_car
```

output:

```
[PashmakClass name="Car"]
```

now, we want to set the properties:

```bash
class Car
    $name
    $color
endclass

$my_car = ^ new Car
$my_car->name = 'BMW'
$my_car->color = 'white'

println $my_car->name ' ' + $my_car->color
```

output:

```
BMW white
```

so, let's review the classes. for declaring the classes, we have to use `class` and `endclass` commands:

```bash
class TheClassName
    # declare the properties
endclass
```

between them, you have to declare properties like normal variables:

```bash
class TheClassName
    # declare the properties
    $prop1
    $prop2
    $prop3; $prop4
endclass
```

default value for that properties is `None`.

also you can set the default value:

```bash
class TheClassName
    # declare the properties
    $prop1 = 'the default value'
    $prop2 = 12
    $prop3; $prop4
endclass
```

now, we declared our class, how to create a instance from that? actually, we can create infinitivly object from that. for example we have a thing named `Car`, this is a class and we have much many objects with `Car` class.

```bash
class TheClassName
    # declare the properties
    $prop1 = 'the default value'
    $prop2 = 12
    $prop3; $prop4
endclass

$my_object = ^ new TheClassName
```

the `new` command gets name of class and creates an instance from that and puts that in the mem temp value.
means, if i want to put created object in a variables, i need to write `$var = ^ new ClassName`.

also we can create that with another syntax:

```bash
$my_object # declare the variable
new ClassName # create the object
copy $my_object # copy created object to variable

# finally
$my_object; new ClassName; copy $my_object
```

now, we can create object from a class. how to access to the properties? look at this example:

```bash
class Car
    $name = 'default name'
    $color
endclass

$my_car = ^ new Car

println $my_car->name # output: default name
```

we can access to the object properties by writing `$varname->property_name`

the `->` symbol is important.

also you can set the value with this syntax:

```bash
class Car
    $name = 'default name'
    $color
endclass

$my_car = ^ new Car

println $my_car->name # output: default name

# setting the new value
$my_car->name = 'new name'
println $my_car->name # output: new name
```

### classes in namespaces
you can declare classes inside the namespaces like variables and functions.

for example:

```bash
namespace Models
    class Car
        $name
        $color
    endclass
endns

$my_car = ^ new Models.Car
```

all of laws for **classes in namespaces** is like `functions` and `variables`.

### Advance property usage
you can use more features of the properties. actually, you can create any structure in your properties.

look at this example:

```bash
class Brand
    $title = 'the brand name'
endclass

class Car
    $name
    $color

    # the brand property is a object from Brand class
    $brand = ^ new Brand
endclass

$my_car = ^ new Car
$my_car->name = 'my car'
$my_car->brand->title = 'BMW'

println $my_car->name
println $my_car->brand->title
```

output:

```
my car
BMW
```

actually, your property value can be a object from other property and this process can be continued recursivly.

you can access to properties by `->` symbol:

```bash
# access to `prop3` of `prop2` of `prop1` of $obj
$obj->prop1->prop2->prop3
```

also you can set new properties on a object:


```bash
class Car
    $name
    $color
endclass

$my_car = ^ new Car
$my_car->name = 'my car'
$my_car->color = 'red'

$my_car->the_new_prop = 'the value'

println $my_car->the_new_prop
```

output:

```
the value
```

in the above example, property `the_new_prop` is not declared in class by default, but you can add props without any problem in objects.

also you can use **Consts** in classes.

for example:

```bash
class Person
    $name = 'parsa'
    $_age = 100 # age is const
endclass

$p = ^ new Person

$p->_age = 50
```

output:

```
ClassConstError:...
```

if you want to set a peoperty as constant, you have to put a `_` in the start of that name.

### inheritance
the inheritance in classes means classes can be child of another classes. this means the child class has all of he's/she's parent properties.

look at this example:

```bash
class Thing
    $name
endclass

class Animal < Thing
    $title
    $size
    $color
    $gender
endclass

class Cat<Animal
    $mioo
endclass

class Human<Animal
    $height
endclass
```

in the above example, we used `<` symbol to make a class child of another class:

```bash
class Parent

endclass

# the `Child < Parent` sets this class as child of the `Parent`
class Child < Parent

endclass
```

the child class, has all of properties of the parent.

for example:

```bash
class Father
    $name = 'hello world'
endclass

class Child < Father
    $age = 100
endclass

$child = ^ new Child

println $child->name # output: hello world
println $child->age # output: 100
```

actually, the parent class has not properties of he's childs, but childs has all of parent's props.

#### All of classes extends `Object` class
all of classes by default extedns from a class named `Object`. this class is a internal pashmak class.
all of classes are child of this class.

### Classes general attributes
classes has some general properties:

- `__name__`: name of the class
- `__parent__`: name of parent of class

for example:

```bash
class Person

endclass

$person = ^ new Person

println $person->__name__ # output: Person
```

### Class methods
you can declare function inside classes. the class's function is named **Method**.

look at this example:

```bash
class Cat
    $name

    func mio
        println 'miooo...'
    endfunc
endclass

# create a object from Cat
$my_cat = ^ new Cat

$my_cat@mio
```

output:

```
miooo...
```

actually, you can call functions of a class.

another example:

```bash
class Cat
    $name

    func mio
        println 'miooo... my name is ' + $this->name
    endfunc
endclass

# create a object from Cat
$my_cat = ^ new Cat
$my_cat->name = 'gerdoo'
$my_cat@mio
```

output:

```
miooo... my name is gerdoo
```

in above example, we used a variable named `$this`. this variable is a pointer to self of object.

another example:

```bash
class Person
    $name

    func set_name $name
        $this->name = $name
    endfunc

    func say_hi
        println 'hello. my name is ' + $this->name
    endfunc
endclass

$p = ^ new Person

$p@set_name 'parsa'

$p@say_hi
```

output:

```
hello. my name is parsa
```

**You can set object self properties by using $this variable like above examples**

total syntax:

```bash
$object_name@method_name 'arguments...'
```

also all of classes extends parent methods.

for example:

```bash
class Father
    func hi
        println 'hello world'
    endfunc
endclass

class Child < Father; endclass

$obj = ^ new Child

$obj@hi
```

output:

```
hello world
```



# Eval

you can run pashmak code from string.

look at this example:

```bash
mem 'println "hello world from string"'; eval ^
```

output:

```
hello world from string
```

this code is runed from a string

look at this example:

```bash
$code
print 'enter some code: '
read $code

eval $code
```

output:

```
enter some code: <input>mem 'hi\n'; out ^;
hi
```

the above code gets a string from user and runs that as pashmak code.

also you can use `std_eval` function to have easier syntax:

```bash
# you can pass value directly
std_eval '<some-code>'
```

## run python code
you can run python code like `eval` with `python` command:

```bash
$code = 'print("hello world from python")'
python $code
```

output:

```
hello world from python
```




# Internal Modules
pashmak has some internal libraries to use. that modules are helpful for you.

## how to import module
you can import modules with `include` operation.

look at this example:

```bash
mem '@hash'; include ^
# or using import to have easier syntax
import '@hash'
import "@module_name"
import "@module1", '@module2'

# also you can import modules without quotes
import @sys
import @hash, @mymodule

# also you can import modules like scripts under the namespaces
namespace Foo
    import '@hash'
endns

# ...
```

you have to give name of module with a `@` before that to the include operation.

### hash module
with hash module, you can calculate hash sum of values:

```bash
import '@hash'

hash.sha256 "hello" # also you can use hash.md5 and...
out ^ # output: 2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824
```

##### how it works?
first, we call `hash.sha256` and pass `hello` string as argument (or put it in mem) to calculate sha256 hash. then, this function calculates hash sum of mem value and puts that into the mem. now you can access sum of that from mem.

#### another hash algos
- hash.blake2b (string)
- hash.blake2s (string)
- hash.md5 (string)
- hash.sha1 (string)
- hash.sha224 (string)
- hash.sha256 (string)
- hash.sha384 (string)
- hash.sha3_224 (string)
- hash.sha3_256 (string)
- hash.sha3_384 (string)
- hash.sha3_512 (string)
- hash.sha512 (string)
- hash.shake_128 (string, length)
- hash.shake_256 (string, length)


### time module
with this module, you can work with time.

##### time.time
this function gives you current UNIX timestamp:

```bash
import '@time'

time.time
out ^ # output is some thing like this: `1600416438.687201`
```

when you call this function, this function puts the unix timestamp into mem and you can access and use that.

##### time.sleep
this function sleeps for secounds:

```bash
import '@time'

time.sleep 2 # sleeps for 2 secounds
# mem 2.4; time.sleep; # sleepss for 2.4 secounds
```

when you run this script, program waits for 2 secounds and then will continued

with this function, you can wait for secounds.

you have to put a int or float into mem or pass as argument and next call `time.sleep` function, then program will sleep for value of `mem` as secounds

#### Another time functions
- time.ctime
- time.gmtime
- time.localtime

### random module
this module makes random numbers

##### random.randint
```bash
import '@random'

random.randint 1, 10 # generates a random int between 1 and 10

out ^ # and puts generated random number in mem and you can access that
```

##### random.random
```bash
import '@random'

random.random # generates a random float less that 1

out ^ # and puts generated random number in mem and you can access that
```

### file module
with this module, you can work with files smarter.

##### file.open
with this function, you can open a file:

```bash
import '@file'

file.open '/path/to/file.txt', 'r' # first argument is file path, and second argument is open type. here is `r` means `read`

# now, opened file is in the mem. we can copy it in a variable

$f = ^

# or

$f = ^ file.open '/path/to/file.txt', 'r'
```

##### file.read
wtih this function, you can read opened file:

```bash
import '@file'

$f = ^ file.open '/path/to/file.txt', 'r'

file.read $f # now, content of file is in the mem
out ^ # output is content of file
```

##### file.write
with this function, you can write on opened file:

```bash
import '@file'

$f = ^ file.open '/path/to/file.txt', 'w' # open type is `w` (write)

file.write $f, 'new content' # first arg is opened file and second arg is content.
```

now file is changed

##### file.close
with this function you can close file after your work:

```bash
import '@file'

$f = ^ file.open '/path/to/file.txt', 'r'

# work with file

file.close $f # close file after work
```

##### example:

```bash
import '@file'

$file = ^ file.open '/path/to/file.txt', 'r'

$content = ^ file.read $file

print 'content of file is: ' + $content
```

### test module
the `test` module has some assertion functions to testing.

##### default `assert` function
this function is a function in the pashmak. this function gets a value and asserts that is true:

```bash
# NOTE: you don't need to import anything for use this function
assert 2 == 2 # ok
assert 4 > 1 # ok
assert True # ok
assert 'foo' == 'bar' # error: AssertError
```

##### test.assertTrue
asserts true:

```bash
import '@test'

test.assertTrue True
test.assertTrue 5 == 5
test.assertTrue 10 > 5
```

above code will be run without error.

this code will get `AssertError`:

```bash
test.assertTrue False
test.assertTrue 3 == 2
```

##### test.assertFalse
this function is reverse of `test.assertTrue`.

```bash
test.assertFalse False # run be run without error
test.assertFalse 3 == 2 # run be run without error
test.assertFalse 2 == 2 # AssertionError
```

##### test.assertEquals
this function asserts two values equals.

```bash
# two arguments should be passed:
test.assertEquals 'hello', 'hello' # successful
test.assertEquals 2, 2 # successful
test.assertEquals 'foo', 'bar' # AssertionError
```

##### test.assertNotEquals
this function is reverse of `test.assertEquals`.

```bash
test.assertNotEquals 'foo', 'bar' # successful
test.assertNotEquals 2, 7 # successful
test.assertNotEquals 2, 2 # AssertionError
```

##### test.assertEmpty
asserts the value is empty.

```bash
test.assertEmpty None
test.assertEmpty 'hello' # error
```

##### test.assertNotEmpty
asserts value is not empty

```bash
test.assertNotEmpty 'hello'
test.assertNotEmpty None # error
```

### sys module
this module has some functions to manage pashmak internal envrinonment.

#### sys.path module
this module is for manage module paths. you can add new module paths and load modules from everywhere at runtime with this module.

to know about this module, go to next section [Module path system](#module-path-system).

#### `$sys.pashmakinfo`, access to pashmakinfo

if you want to access to pashmak interpreter info, `sys` module has a variable named `pashmakinfo`:

```bash
import @sys

println $sys.pashmakinfo
```

output is something like this:

```
{'version': 'vx.y.z', 'pythoninfo': 'x.y.z (default, Jul x y, a:b:c) [GCC x.y.x]'}
```

this variable is a dictonary.
for example, to access pashmak version:

```bash
import @sys

println $sys.pashmakinfo['version']
```

output:

```
v1.x.y
```

and `$sys.pashmakinfo['pythoninfo']` shows info of python.

## Python standard modules
you can use this python standard modules in pashmak directly in your code:

- `os`
- `time`
- `hashlib`
- `random`

for example:

```bash
println os.getuid()
println random.random()
println 'hash is ' + hashlib.sha256('hello'.encode()).hexdigest()
$cwd = os.getcwd()
$time = time.time() - 100
# ...
```

this is very useful!

## Module path system
module path is a system to add pashmak scripts as modules to pashmak. for example, you have an directory named `/var/lib/pashmak_modules` and there is an file named `/var/lib/pashmak_modules/mymodule.pashm`. this file is a pashmak script. now, how to add that pashmak script to pashmak as module?

for example, we want to import that module:

```bash
import '@mymodule'
```

to do this, you have to add directory `/var/lib/pashmak_modules` to pashmak path:

```bash
PASHMAKPATH=/var/lib/pashmak_modules pashmak my_program.pashm
```

to add an directory to pashmak path, you have to set that directory to environment variable `PASHMAKPATH`:

```
PASHMAKPATH=/path/to/first/dir:/path/to/another/dir:/another/dir2...
```

you can seprate paths with `:`.

next, pashmak interpreter loads modules from that directories. how? pashmak loads pashmak files with `.pashm` extension as module. for example, if name of file is `my_module.pashm`, you can import that with `import "@my_module"`.

also you can import an directory as module. for example, `/usr/lib/pashmak_modules` is in the module path. and there is a directory in `/usr/lib/pashmak_modules/mymodule/`. if you import `import "@mymodule"`, pashmak uses `/usr/lib/pashmak_modules/mymodule/__init__.pashm` file in that directory as module main file. you can load another scripts of your module in this file.

for example:

##### __init__.pashm:

```bash
import $__dir__ + '/core.pashm'
import $__dir__ + '/another-file.pashm'
# ...
# or whatever you want to do
```

### Default paths
the default module paths in pashmak are:

- `<home-directory>/.local/lib/pashmak_modules`
- `/usr/lib/pashmak_modules` (only in UNIX systems)

### Show list of available modules
to see list of available modules, run this command:

```bash
pashmak -m
# or
pashmak --modules
```

### Adding module paths at runtime (sys.path module)
there is an namespace named `sys.path` in the `sys` module, this module is for adding new module paths at the runtime.
with this feature, you can add another directories to your path and load modules from them in your program.

for example:

```bash
import '@sys'

sys.path.add '/home/parsa/my-directory';
```

in above code, directory `/home/parsa/my-directory` will be added to the module path. after this action, you can import modules of that directory.

for example, we have `/home/parsa/my-directory/mylib.pashm` module and we can import that:

```bash
import '@sys'

sys.path.add '/home/parsa/my-directory';

import '@mylib'

# do whatever you want
```

this system is very helpful, specialy when you want to add your local modules from an directory in your project.

for example, i have an project and there is an directory named `pashmak_modules` contains local library. i can add this directory to module path in my code start point:

```bash
import $__dir__ + '/pashmak_modules/'

# now i can import libraries from pashmak_modules directory
```

also you can get list of module paths:

```bash
import '@sys'

$module_paths = ^ sys.path.list
# OR
$module_paths; sys.path.list; copy $module_paths

println $module_paths
```

output:

```
['/path1', '/path2', '...']
```

### Another useful libraries written by others

- The [polor-pashm](https://github.com/sami2020pro/polor-pashm) library by [sami2020pro](https://github.com/sami2020pro)





##### NOTE: this file is auto generated from `doc` folder. do not change it directly. If you want to edit documentation, edit `doc/` folder files. your changes will built from that folder into this file.

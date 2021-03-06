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

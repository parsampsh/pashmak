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

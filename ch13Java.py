# cracking the coding interview
# chapter 13 java

# interview questions

# 13.1 private constructor
# in terms of inheritance what is the purpose of keeping a constructor private?
"""
making a constructor private means you can only access the constructor if you can also access it's private methods
the only things that can access these private methods are the class itself, the inner classes of this class, and the other
inner classes of this classes parent class
meaning if A and B are inner classes of Q and C is an inner class of A then ABC can access the private constructor

This demonstrate inheritance because a subclass calls its parent's constructor. Meaning the A class can be inherited by its own
subclasses or by its parent's other subclasses
"""

# 13.2 return from finally
# in java does the finally block get executed if we insert a return statement inside the try block of a try-catch-finally?
"""
yes
the finally block gets executed when the try block exits regardless of return, continue, break, etc
the finally block only doesn't execute if the virtual machine exits before the finally block begins executing
or if the thread that is running the try catch block gets killed
"""

# 13.3 final, etc
# what is the difference between final, finally, and finalize?
"""
genrally
final - controls whether a method, variable, or class is changeable
finally - is used in a try/catch block to make sure a piece of code always runs
finalize - is a method called by the garbage collector once it determines no more references exist

specifics
final
    when applied to primitive var, value can not change
    when applied to var reference, the reference cannot change to point to another obj on the heap
    when applied to a method, the method cannot be overridden
    when applied to a class, the class cannot be subclassed
finally
    this block executes even if an exeption is thrown
    its usually used to clean up code
finalize
    this is called just before the automatic garbage collector actually destroys an obj
    this method can be overridden if someone wishes to define custom behavior for garbage collection
"""

# 13.4 generics vs templates
# Explain the difference between templates in c++ and generics in java
"""
java generics are used because of type erasure
meaning it eliminates parameterized types when source code is translated to the JVM byte code
doesn't really change anything is just makes it a bit prettier
syntactic sugar

c++ templates are glorified macro set, with the complier creating a new copy of the template code for each type
MyClass<Bar> where the type here is bar will not share static variables with MyClass<Foo> where the type is Foo
but two instances of MyClass<Foo> will share static variables

in java static variables are shared across the class regardless of the different type parameters

some other differences
    c++ uses primatives like int while java uses Integer
    in java you can restrict the template's type parameters
    in c++ the type parameter can be instantiated but you can't do this in java
    in java, the type parameter cannot be used for static methods because the types maybe different between instances of the class
        c++ does have this problem because two different type parameters use two different static methods
    in java all instances of a template class are of the same type regardless of the type parameters and the type parameters are
        erased at runtime
    in c++ instances with different type parameters are different types
"""

# 13.5 treemap, hashmap, linkedhashmap
# explain the differences between treemap, hashmap, and linkedhashmap. provide an example of each
"""
hashmap - O(1) lookup and insertion, implemented by an array of linked lists
treemap - O(logN) lookup and insertion, keys are ordered, implemented by redBlackTree, can implement comparable interface
linkedhashmap - O(1) look up and insertion, hashmap where items have a previous and next pointer, allows you to order items in
    the hashmap

the differences are the ordering and big O
linkedhashmap gives you the order of insertion
treemap gives you sorted order
hashmap gives you random order
"""

# 13.6 object reflection
# explain what object reflection is in java and why it is useful
"""
Object reflection provides a way to get reflective information about java classes and objects and perform operations like
    get info about methods and fields present inside the class at runtime
    create new instances of a class
    getting and setting object fields directly by getting field reference regardless of what the access modifier is

why use this?
    it can help you observe or manipulate the runtime behavior of applications
    helps when debugging and testing programs by giving you direct access to methods, constructors, and fields
    you can call methods by name without knowing the method in advance (ex. you let the user create the method name)
"""

# 13.7 lambda expressions
# there is a class country with methods getContinent and getPopulation. write a function int getPopulation(
# List<Country> countries, String continent) that computes the total population of a given continent given a list
# all the countries and teh name of a continent
"""
int getPopulation(List<Country> countries, String continent) {
    # filter countries
    Stream<Country> sublist = countries.stream().filter(
        country -> {return country.getContinent().equals(continent);}
    );

    # convert to list of populations
    Stream<Integer> populations = sublist.map(
        c -> c.getPopulation()
    );

    # sum the list
    int population = populations.reduce(0, (a, b) -> a + b);
}
"""

# 13.8 lambda random
# using lambda expressions, write a function List<Integer> getRandomSubset(List<Integer> list) that returns a
# random subset of arbitrary size. All subsets (including the empty set) should be equally likely
"""
Random random = new Random();
Predicate<Object> flipCoin = o -> {
    return random.nextBoolean();
}

List<Integer> getRandomSubset(List<Integer> list) {
    List<Integer> subset = list.stream().filter(flipCoin).
        collect(Collectors.toList());
    return subset;
}
"""
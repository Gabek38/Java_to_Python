# Reflection: Reverse Engineering Java to Python

## What Was Easiest to Translate

The overall class structure was the easiest part to translate. Java's `extends` 
keyword became simply putting the parent class name in parentheses in Python, 
and `super()` worked almost identically in both languages. The logic inside each 
method transferred directly since the underlying object-oriented concepts are 
the same in both languages.

## What Required the Most Thought

The trickiest part was handling private attributes. In Java, the `private` keyword 
is strictly enforced by the compiler. In Python, true privacy does not exist the 
same way, so I used double-underscore name mangling such as `self.__title` to 
approximate the same behavior. This was a new concept that required careful thought 
about how Python handles encapsulation differently than Java.

## What I Learned About the Differences

**Constructors:** Java uses the class name as the constructor. Python always uses 
`__init__()` with `self` as the first parameter, which has to be passed into every 
method.

**Private Attributes:** Java enforces privacy at the compiler level. Python uses 
naming conventions like double underscores to signal that an attribute should not 
be accessed directly from outside the class.

**Inheritance:** Both languages use `super()` but Python does not require you to 
pass the class name or `this` into it like older Java versions did.

**toString() vs __str__():** Java uses `toString()` which gets called automatically 
when an object is printed. Python uses `__str__()` which works the same way. The 
concept is identical, just different syntax.

**Naming Conventions:** Java uses camelCase for methods like `checkOut()` and 
`returnItem()`. Python convention is snake_case so those became `check_out()` and 
`return_item()`.

## Overall Takeaway

This assignment showed me that object-oriented design ideas transfer across 
languages even when the syntax looks different. Understanding the design of the 
original Java program made it much easier to rebuild it in Python with confidence.
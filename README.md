# Java_to_Python: Library Demo

## Overview
This project is a reverse engineered Python version of a Java Library application. The orgiinal Java was built using Object-oriented design with a base class and subclass. This Python version preserves the same design and behavior.

## Classes
- `LibraryItem` - base class with title, item ID, and checkout state
- `Book` - subclass that adds author
- `DVD` - subclass that adds duration

## How to Run
```bash
python library_demo.py
```

## Concepts Demonstrated
- Inheritance and super()
- Private attributes with name mangling (__var)
-__str__() vs Java's toString()
- Snake_case naming conventions
- Main driver using if __name__ == "__main__"
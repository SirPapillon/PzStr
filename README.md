# PzStr - Python String Extension


`PzStr` is a Python string extension that adds additional functionality and methods to the built-in `str` class. It aims to provide a more convenient way to work with strings by offering various methods for manipulation and transformation.

## Features

- Extends the built-in `str` class with additional methods.
- Methods for reversing, removing, and modifying strings.
- Functional-style methods for filtering, mapping, and iterating over characters.
- Access to length, first, and last properties.
- Seamless integration with existing strings.

## Installation

Simply copy the `PzStr` class into your Python project to start using it:

## Usage

Create a PzStr object
```python
my_string = PzStr("Hello, world!")
```

Reverse the string
```python
reversed_string = my_string.reverse()
print("Reversed:", reversed_string)  # Output: Reversed: !dlrow ,olleH
```

Remove a substring
```python
new_string = my_string.remove("o")
print("Without 'o':", new_string)  # Output: Without 'o': Hell, wrld!
```

Get a substring
```python
substring = my_string.substring(7, 12)
print("Substring:", substring)  # Output: Substring: world!
```

Check if the string is empty or not
```python
is_empty = my_string.isEmpty()
print("Is Empty?", is_empty)  # Output: Is Empty? False
```

Convert the string to a list of characters
```python
char_list = my_string.asList()
print("Character List:", char_list)  # Output: Character List: ['H', 'e', 'l', 'l', ',', ' ', 'w', 'o', 'r', 'l', 'd', '!']
```

Remove characters that meet a condition
```python
my_string.removeWhere(lambda char: char == "l")
print("After Removing 'l':", my_string)  # Output: After Removing 'l': Heo, word!
```

Iterate over characters and print them
```python
my_string.forEach(lambda char: print(char))
# Output:
# H
# e
# o
# ,
#  
# w
# r
# d
# !
```

Map characters to uppercase
```python
my_string.where(lambda char: char != " ", lambda char: char.upper())
print("Uppercased:", my_string)  # Output: Uppercased: HEO, WRD!
```

Insert "Awesome" at index 2
```python
my_string.insert("Awesome", 2)
print(my_string)  # Output: HeAwesomello, world!
```

Insert "X" wherever the character is 'o'
```python
my_string.insertWhere("X", lambda item: item == 'o')
print(my_string)  # Output: HeAwesoXmelloX, woXrld!
```

Access the length of the string
```python
string_length = my_string.length
print("Length:", string_length)  # Output: Length: 10
```

Access the first and last characters
```python
first_char = my_string.first
last_char = my_string.last
print("First Char:", first_char)  # Output: First Char: H
print("Last Char:", last_char)    # Output: Last Char: D
```

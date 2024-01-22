"""
int(x [,base]): Converts x to an integer. The base parameter is optional and represents the base of the number system. If not specified, the default is base 10.

python
Copy code
x = int("123")
float(x): Converts x to a floating-point number.

python
Copy code
x = float("3.14")
str(x): Converts x to a string.

python
Copy code
x = str(42)
list(iterable): Converts an iterable (like a tuple or string) to a list.

python
Copy code
x = list((1, 2, 3))
tuple(iterable): Converts an iterable to a tuple.

python
Copy code
x = tuple([4, 5, 6])
set(iterable): Converts an iterable to a set.

python
Copy code
x = set([1, 2, 2, 3, 3, 3])
dict(): Creates a dictionary from an iterable of key-value pairs.

python
Copy code
x = dict([(1, 'one'), (2, 'two'), (3, 'three')])
bool(x): Converts x to a Boolean. Returns False if x is false or omitted, True otherwise.

python
Copy code
x = bool(42)
chr(x): Converts an integer to a character (Unicode).

python
Copy code
x = chr(65)  # Returns 'A'
ord(x): Converts a character (Unicode) to its integer value.

python
Copy code
x = ord('A')  # Returns 65
These functions are essential for handling different data types and performing conversions as needed in Python programs.
"""
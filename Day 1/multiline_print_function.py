# we need these lines to get printed in output.
# Day 1 - Python Print Function
# The function is declared like this:
# print('what to print')

'''f
Single quotes: 'string'
Triple double quotes: """multiline string"""
Double quotes: "string"
f-string, format() to print strings along with the variables
\n means new line
If you want to use more than one type of string in a single print function, you can concatenate or use multiple print statements. Here's an example:

code:
# Using concatenation
print('This is a ' + """multiline string""" + " and this is a 'string'.")

# Using multiple print statements
print('This is a ', """multiline string""", ' and this is a \'string\'.')
...

 Remember to escape single quotes within single-quoted strings using \' to avoid prematurely ending the string.
'''

print("""Day 1 - Python Print Function
The function is declared like this:
print("what to print")""")


# ----

# also there are ways to format the string using f-string, format() method.

'''
f-string :-
code:
name = "Alice"
age = 25
print(f"My name is {name} and I am {age} years old.")
...

String Formatting with format() method:
code:
name = "Bob"
age = 30
print("My name is {} and I am {} years old.".format(name, age))

...
'''
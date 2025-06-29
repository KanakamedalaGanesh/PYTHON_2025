'''String formatting in Python: String formatting is the process of inserting values into a string.
# It allows you to create dynamic strings by replacing placeholders with actual values.
# There are several ways to format strings in Python, including:
# 1. f-strings (formatted string literals): Introduced in Python 3.6, f-strings allow you to embed expressions inside string literals using curly braces {}.
# 2. str.format() method: This method allows you to format strings by using placeholders {} and passing values as arguments.
# 3. %-formatting: This is an older method that uses the % operator to format strings, similar to printf in C.
# 4. Template strings: The string.Template class provides a way to create strings with placeholders that can be substituted with values.
# 5. String concatenation: You can concatenate strings using the + operator, but this is not considered a formatting method.'''
# Here are some examples of string formatting in Python:

# 1. f-strings
name = "Alice"
age = 30
formatted_string = f"My name is {name} and I am {age} years old."
print(formatted_string)  # Output: My name is Alice and I am 30 years old.


# 2. str.format() method
name = "Bob"
age = 25
formatted_string = "My name is {} and I am {} years old.".format(name, age)
print(formatted_string)  # Output: My name is Bob and I am 25 years old.

# 3. %-formatting
name = "Charlie"
age = 20
formatted_string = "My name is %s and I am %d years old." % (name, age)
print(formatted_string)  # Output: My name is Charlie and I am 20 years old.

# 4. Template strings
from string import Template
name = "David"
age = 35
template = Template("My name is $name and I am $age years old.")
formatted_string = template.substitute(name=name, age=age)
print(formatted_string)  # Output: My name is David and I am 35 years old.


# 5. String concatenation
first_name = "Eve"
last_name = "Smith"
formatted_string = "My name is " + first_name + " " + last_name + "."
print(formatted_string)  # Output: My name is Eve Smith.


# 6. Using format specifiers
pi = 3.14159
formatted_string = "The value of pi is {:.2f}.".format(pi)
print(formatted_string)  # Output: The value of pi is 3.14.


# 7. Padding and alignment
number = 42
formatted_string = "The number is {:>5}.".format(number)  # Right-aligned with width 5
print(formatted_string)  # Output: The number is  42.



# 8. Using named placeholders   
formatted_string = "My name is {name} and I am {age} years old.".format(name="Frank", age=28)
print(formatted_string)  # Output: My name is Frank and I am 28 years old.


# 9. Using positional and named placeholders together
formatted_string = "My name is {0} and I am {age} years old.".format("Grace", age=22)
print(formatted_string)  # Output: My name is Grace and I am 22 years old.


# 10. Using f-strings with expressions
x = 10
y = 5
formatted_string = f"The sum of {x} and {y} is {x + y}."
print(formatted_string)  # Output: The sum of 10 and 5 is 15.


# 11. Using f-strings with method calls
def greet(name):
    return f"Hello, {name}!"
formatted_string = f"{greet('Hannah')}"
print(formatted_string)  # Output: Hello, Hannah!


# 12. Using f-strings with dictionaries
person = {"name": "Ian", "age": 40}
formatted_string = f"My name is {person['name']} and I am {person['age']} years old."
print(formatted_string)  # Output: My name is Ian and I am 40 years old.






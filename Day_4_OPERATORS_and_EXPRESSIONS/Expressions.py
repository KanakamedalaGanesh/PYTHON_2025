'''Expression: An expression is any combination of variables,values,operators and function calls that can be evaluated to produce a result.
Expressions always return a value.
Examples:
# 5+3           (gives 8)
# len('hello')  (gives 5)
'''
# math is a module for mathematical functions like sqrt,power,factorial,pi and fabs(absolute value-returns float).
import math

# area of triangle
# base=int(input("Enter base:"))
# height=int(input("Enter height:"))
# areaoftriangle=(base*height)/2
# print(areaoftriangle)

# # area of square
# side=int(input("Enter side:"))
# areaofsquare=side**2
# print(areaofsquare)

# # area of rectangle
# l=int(input("Enter len:"))
# b=int(input("Enter breadth:"))
# areaofrectangle=l*b
# print(areaofrectangle)

# area of circle
radius=int(input("Enter radius:"))
area=(math.pi*(radius**2))
print(area)

# Quadratic equation
# b=1
# a=1
# c=1
# q=(-b+math.sqrt(b**2-(4*a*c)))/2*a
# print(q)


# Identifier : An identifier is a name given to a variable, function, class, module etc. in a program. It is used to access the variable, function, class, module etc. in a program. 
# Identifiers can be of any length but they cannot start with a digit. They can contain letters , digits, and underscores. They are case sensitive. For example, a and A are two different identifiers. 
# Example: x,y,z,my_variable,my_function,my_class,my_module etc. 

# Keywords : Keywords are the reserved words in a programming language. They have a special meaning in the language and cannot be used as identifiers. They are used to define the syntax of the language. 
# Example: if,else,for,while,def,class,import,pass etc.


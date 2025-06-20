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

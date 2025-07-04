'''Operators: Operators are used to perform operations on variables and values.
Types of operators in python:
1.Arthmetic operators: +,-,*,/,%,//,**
2.Assignment operators: +=,-=,*=,/=,%=,**=,&=,|=,^=,<<=,>>=
3.comparison operators: <,>,=,==,!=,<=,>=
4.Logical operators: and,or,not
5.Identity operators: is,is not
6.Membership operators: in, not in
7.Bitwise operators: &,|,~,^,<<,>>'''

# 1.Arthmetic
# Add
x=10
y=20
print(x+y)

# Sub
print(x-y)

# Mul
print(x*y)

# Div
print(x/y)

# FloorDiv
print(x//y)

# Exponent
print(x**y)


# 2.Assignment
x=10
x+=2
print(x)

# 3.Comparison: returns True or False
x=10
y=30
print(x>y)
print(x<y)
print(x==y)
print(x>=y)
print(x<=y)
print(x!=y)

# 4.Logical:
x=10
y=20
print(x<y and y>x)
print(x<y or y>x)
print(not(x<y and y>x))

# 5.Identity:
x=5
y=x
z=5
print(x is y)
print(x is z)
print(x is not y)

# 6.Membership:
x=[1,2,3,4]
y=[2,3,45,5]
print(3 in y) 
print(24 not in y)


'''Operator precedence order: If same precedence it evaluates from left to right.
()
**
+x -x ~x
* / // %
+ -
<< >>
&
^
|
> < <= >= != == is is not in not in
not 
and 
or
=,+=,-=,*=,/=,%=,//=,**=,&=,|=,^=,<<=,>>=
'''
# Examples on precedence
# 1.
print(3+4*2)

# parenthesis overrides the rule
print((3+4)*2)                            




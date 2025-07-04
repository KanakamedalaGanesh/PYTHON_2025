'''String: String is a sequential datatype,it is enclosed in single or double quotes,it accepts duplicate values,and indexing
and slicing is possible.String is mutable.
'''
# Creation of string
# 1.
str1 = "Hello, World!"
print(str1)

# 2.
str2="Ganesh","Bali","Teja"
print(str2)

# 3.
str3 = 'Hello, World!',1,54,True,9+3j,"Ganesh"
print(str3)


# Accessing string elements 
print(str2[0])
print(str2[1])
print(str2[2]) 


# Slicing string
print(str2[0:3])  
print(str2[1:4])
print(str2[:4])  
print(str2[1:])
print(str2[:])
print(str2[1:4:2])    # 2 is the step size
print(str2[1:4:1])    # 1 is the step size
print(str2[1:4:-1])   # -1 is the step size
print(str2[1:4:-2])   # -2 is the step size
print(str2[:-1])
print(str2[::-1])     # -1 is the index of the last character in the string


# Concatenation of string
str4 = "Hello, "
str5 = "World!"
print(str4 + str5)

# Repetition of string
print(str4*3)

# string traversing 
for i in str4:
    print(i)

for i in range(len(str4)):
    print(str4[i])

i=0
while i<len(str4):
    print(str4[i])
    i+=1

# String methods
# 1.upper() : converts small letters into capital letters.
s1="Ganesh"
print(s1.upper())

# 2.lower() : converts capital letters into small letters.
s2="GANESH"
print(s2.lower())

# 3.Casefold() : converts capital letters into small letters.
print(s2.casefold())

# 4.Capitalize : Gives first letter capital. Rest all small.
print(s2.capitalize())

# 5.ljust() : adds spaces to the right of the string.
s3="Hello world"
print(s3.ljust(30,'#'))

# 6.rjust() : adds spaces to the left of the string.
print(s3.rjust(30,'$'))

# 7.find() : searches the index value of given element in first occurence.
print(s3.find('o'))

# 8.rfind() : searches the index value of given element from last  occurence.(i.e from right to left).
print(s3.rfind('o'))

# 9.center() : adds spaces to both sides of the string.
print(s3.center(40,'0'))

# 10.Index() : returns the index value of the first occurrence of the specified value.  
print(s3.index('o'))

# 11.count() : it gives count of an element,like how many times it is repeated.
print(s3.count('w'))

# 12.zfill : it defaultly fills zeroes to the left of string upto given length.
print(s3.zfill(30))

# 13.strip(): it removes white spaces in a string both left and right.
s4="   Welcome to python   "
print(len(s4))
print(len(s4.strip()))

# 14.lstrip() : it removes white spaces from left side of a string.
print(len(s4.lstrip()))
print(len(s4))

# 15.rstrip () : it removes white spaces from right side of a string.
print(len(s4.rstrip()))
print(s4)

# 16.replace() : it replaces the given element with another element.
s5= 'a,b,c,d'
print(s5.replace(',','-'))

# 17.join() : it is used to join two strings.
s6="Ganesh"
s7="I am from Tenali, Guntur."
out=(s6.join(s7))
print(out)

# 18.startswith() : it checks whether the string starts with the given element or not.
print(s4.startswith('W'))

# 19.endswith() : it checks whether the string ends with the given element or not.
print(s4.endswith(' '))

# 20.isalpha() : it checks whether the string contains only alphabets or not.
print(s6.isalpha())

# 21.isdigit():it works for only string. it checks whether the string contains only digits or not.
s8='100'
print(s8.isdigit())

# 22.isalnum() : returns true if the string is both alphabets and numbers.
s9='Ganesh4224'
print(s9.isalnum())

# 23.removeprefix() : it removes the prefix from the string.
print(s7.removeprefix('I'))

# 24.removesuffix() : it removes the suffix from the string.
print(s7.removesuffix('Tenali'))

# 25.partition(): divides the string into 3 parts,gives in tuple format.
print(s7.partition('from'))

# 26.Title(): convers every character in string in capital letter.
print(s7.title())

# 27.swapcase() : swaps small letters into capital letters and capital letters into small letters.
s10=' aChIeVeRs It'
print(s10.swapcase())

# 28.isspace(): returns true if all characters in string is white spaces.
s11='    '
print(s11.isspace())

# 29.isinstance(): checks if the object belongs to specific class or not.
s12=(1,2,3,4,5)
print(isinstance(s12,tuple))

# 30.split(): returns the string in list.
print(s10.split(''))

# identity operators: even though 2 strings has same content their ids are different, returns true if 2 strings content is same otherwise false.
S1="Ganesh"
S2="Ganesh1"
print(id(s1))
print(id(s2))
print( S1 is not S2)



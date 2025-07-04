'''Base Conversion : Base coversion in python is used to convert numbers between different bases.
Decimal to other bases:
1.Decimal to binary : bin()
2.Decimal to octal : oct() 
3.Decimal to hexadecimal : hex()


a.Decimal : Decimal number is a number that has a base of 10. It is the base we use in our daily life . 
  It is the base that we use to count, measure, and express quantities. It is the base that we use to represent numbers in our everyday life.Numbers in decimal system are represented using 10 digits: 0, 1, 2, 3, 4, 5, 6, 7, 8, and 9.

b.Binary : Binary number is a number that has a base of 2. It is the base that we us in computers. It is the base that we use to represent numbers in computers. 
  Numbers in binary are represented using 0s and 1s.

c.Octal : Octal number is a number that has a base of 8. It is the base that we use in some computer programming languages. 
  It is the base that we use to represent numbers in some computer programming languages.Numbers in octal are represented using digits 0-7.

d. Hexadecimal : Hexadecimal number is a number that has a base of 16. It is the base that we use in some computer programming languages. 
   Numbers in hexadecimal are represented by 0-9 and A-F.
'''

# decimal to binary : bin()
print(bin(10))  # Output: 0b1010
print(bin(20))  # Output: 0b10100
print(bin(30))  # Output: 0b11110


# decimal to octal : oct()
print(oct(10))  # Output: 0o12
print(oct(20))  # Output: 0o123
print(oct(30))  # Output: 0o37


# decimal to hexadecimal : hex()
print(hex(10))  # Output: 0xa
print(hex(20))  # Output: 0x14
print(hex(30))  # Output: 0x1e


# binary to decimal : int()
print(int('1010', 2))  # Output: 10
print(int('10100', 2))  # Output: 20
print(int('11110', 2))  # Output: 30


# binary to octal : oct()
print(oct(int('1010', 2)))  # Output: 0o12
print(oct(int('10100', 2)))  # Output: 0o123
print(oct(int('11110', 2)))  # Output: 0o37


# binary to hexadecimal : hex()
print(hex(int('1010', 2)))  # Output: 0xa
print(hex(int('10100', 2)))  # Output: 0x14
print(hex(int('11110', 2)))  # Output: 0x1e


# octal to decimal  : int()
print(int('12', 8))  # Output: 10
print(int('123', 8))  # Output: 83
print(int('37', 8))  # Output: 29


# octal to binary : bin()
print(bin(int('12', 8)))  # Output: 0b1010
print(bin(int('123', 8)))  # Output: 0b1111011
print(bin(int('37', 8)))  # Output: 0b100101


# octal to hexadecimal : hex()
print(hex(int('12', 8)))  # Output: 0xc
print(hex(int('123', 8)))  # Output: 0x53
print(hex(int('37', 8)))  # Output: 0x25


# hexadecimal to decimal : int()
print(int('a', 16))  # Output: 10
print(int('14', 16))  # Output: 20
print(int('1e', 16))  # Output: 30


# hexadecimal to binary : bin()
print(bin(int('a', 16)))  # Output: 0b1010
print(bin(int('14', 16)))  # Output: 0b11110
print(bin(int('1e', 16)))  # Output: 0b11110


# hexadecimal to octal : oct()
print(oct(int('a', 16)))  # Output: 0o12
print(oct(int('14', 16)))  # Output: 0o23
print(oct(int('1e', 16)))  # Output: 0o34





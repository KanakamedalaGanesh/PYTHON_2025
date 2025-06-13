# form input types
import re as Regex

# email
email=input("Enter your email:")
print(Regex.fullmatch('[a-z0-9]*@{1}gmail.com',email))

# password
password=input("Enter your password:")
print(Regex.fullmatch('[A-Za-z0-9@$&]{8,16}',password))

# text
name=input("Enter your name:")
print(Regex.fullmatch('[A-Za-z]{3,20}' ,name))

#mobile number
mobile=input("Enter your mobile number:")
print(Regex.fullmatch('[0-9]{10}',mobile))


# DOB
DOB=input("Enter your date of birth:")
print(Regex.fullmatch('[0-9]{1,2}/[0-9]{1,2}/[0-9]{1,4}',DOB))

# Address
Address=input("Enter your address:")
print(Regex.fullmatch('[A-Za-z0-9\-\/\s,\.]{3,100}',Address))

# match
email=input("Enter your email:")
print(Regex.match('[a-z0-9]*@{1}gmail.com',email))

password=input("Enter your password:")
print(Regex.match('[A-Za-z0-9]{8,16}',password))

# findall
email=input("Enter your email:")
print(Regex.findall('[a-z0-9]*@{1}gmail.com',email))



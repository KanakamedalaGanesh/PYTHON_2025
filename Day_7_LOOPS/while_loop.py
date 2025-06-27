'''while loop: With the while loop, you can execute a block of code/set of statements repeatedly as long as a certain condition is met.
The while loop is used when you don't know in advance how many times you want to loop through the code.
# 1. Initialize a variable
# 2. Check a condition
# 3. If the condition is true, execute the code inside the loop
# 4. Increment the variable
# 5. Repeat steps 2-4 until the condition is false
# 6. If the condition is false, exit the loop
# 7. Print the final value of the variable
syntax:
while condition:
code to be executed
'''
# # Example 1: Print numbers from 1 to 5
# i=1
# while i<=5:
#     print(i)
#     i+=1

# # Example 2: Print numbers from 5 to 1
# i=5
# while i>0:
#     print(i)
#     i-=1

# # Example 3: Print numbers from 1 to 10 with a step of 2
# i=1
# while i<= 10:
#     print(i)
#     i+=2

# # Example 4: Print numbers from 10 to 1 with a step of 2
# i=10
# while i>=1 :
#     print(i)
#     i-=2

# # Example 5: counter
# n=0
# while n<5:
#     n=n+1
#     print(n)

# Example 6: summation
# s=int(input("Enter the number:"))
# i=0
# sum=0
# while i<s:
#     i=i+1
#     sum=sum+i
# print(sum)

# Example 7: print each digit of a number
# num=int(input("Enter the number:"))
# while num>0:
#     digit=num%10
#     print(digit)
#     num=num//10

# Example 8 : summation of digits of a number
# num=int(input("Enter the number:"))
# sum=0
# while num>0:
#     digit=num%10
#     print(digit)
#     sum=sum+digit
#     num=num//10  
# print(sum)

# Example 9: print each character of a string
# s= input("Enter the string:")
# i=0
# while i<len(s):
#     print(s[i])
#     i=i+1

# Example 10: print each character of a string in reverse order
# s= input("Enter the string:")
# i=len(s)-1
# while i>= 0:
#     print(s[i])
#     i=i-1

# Example 11 : Factorial of a number
# num=int(input("Enter a number:"))
# fact=1
# while num>0:
#     fact=fact*num
#     num-=1
# print(fact)

# Example 12: print 1 to N
# n=int(input("enter a number:"))
# i=0
# while i<n:
#     i=i+1
#     print(i)

# Example 13: print N to 1
# n=int(input("Enter a number:"))
# i=n
# while i>=1:
#     print(i)
#     i=i-1

# Example 14: print even numbers from 1 to N
# n=int(input("Enter a number:"))
# i=0
# while i<=n:
#     if i%2==0:
#         print(i)
#     i=i+1

# Example 15: print odd numbers from 1 to N
# n=int(input("Enter a number:"))
# i=1
# while i<=n:
#     if i%2==1:
#         print(i)
#     i=i+1


# Example 16: palindrome number
# n=int(input("Enter a number:"))
# original=n
# rev=0
# while n>0:
#     rev=rev*10+n%10
#     n=n//10

# if (original==rev) :
#     print("palindrome")
# else:
#     print("not a palindrome")


# Example 17: prime numbers
# n=int(input("Enter a number:"))
# i=1
# count=0
# while i<=n:
#     if n%i==0:
#         count+=1
#     i+=1
# if count==2:
#     print("prime")
# else:
#     print("not prime")






       




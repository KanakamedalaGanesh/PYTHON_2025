'''For loop: For loop is used to iterate over a sequence[list,tuple,string,set or dict], this is used when we know how many times to loop a code.
Syntax: for var in sequence: code to be executed
Example:
for i in range(5):
print(i)

'''
# For loop examples

# Example 1: Iterating over a list
# fruits = ['apple', 'banana', 'cherry']
# for i in fruits:
#     print(i)


# # Example 2: Iterating over a range
# for i in range(5):
#     print(i)


# # Example 3: Iterating over a string
# for i in "Ganesh":
#     print(i,end=" ")


# # Example 4: print numbers from 1 to 10
# for i in range(1,11):
#     print(i)


# Example 5: print even numbers from 2 to 20
# for i in range(2,21,2):
#     print(i)


# Example 6: print odd numbers from 1 to 20
# for i in range(1,20,2):
#     print(i)


# Example 7: sum of numbers from 1 to N
# n=int(input("Enter a number:"))
# sum=0
# for i in range(1,n+1):
#     sum+=i
# print(sum)


# Example 8: print numbers from N to 1
# n=int(input("Enter a number:"))
# for i in range(n,0,-1):
#     print(i)



# Example 9: print numbers from 1 to N
# n=int(input("Enter a number:"))
# for i in range(1,n+1):
#     print(i)


# Example 10: Factorial of a number
# n=int(input("Enter a number:"))
# fact=1
# for i in range(1,n+1):
#     fact*=i
# print(fact)



# Example 11:check if a number is prime or not
# n=int(input("Enter a number:"))
# count=0
# for i in range(1,n+1):
#     if n%i==0:
#         count+=1
# if count==2:
#     print("prime number")
# else:
#     print("not a prime number")


# E`xample 12: print the prime numbers from 1 to N
# n=int(input("Enter a number:"))
# for i in range(1,n+1):
#    count=0
#    for j in range(1,i+1):
#       if i%j==0:
#          count+=1

#    if count==2:
#       print(i,end=" ")

# Example 13: print the Fibonacci series up to N
n = int(input("Enter a number: "))
a, b = 0, 1
print("Fibonacci series up to", n, ":")
while a <= n:
    print(a, end=" ")
    a, b = b, a + b


# Example 14: print the multiplication table of a number
# n = int(input("Enter a number: "))
# for i in range(1, 11):
#     print(f"{n} x {i} = {n * i}")




# star patterns:

# Example 1: Left aligned triangle
# for i in range(1,6):
#     print("* "*i)


# Example 2: Right aligned triangle
# rows=5
# for i in range(1,rows+1):
#     print(" "*(rows-i)+"*"*i)


# Example 3: Inverted left aligned triangle
# for i in range(5,0,-1):
#     print("* "*i)


# # Example 4: Inverted right aligned triangle
# for i in range(5,0,-1):
#     print(" "*(5-i)+"*"*i)


# # Example 5: Diamond pattern
# n = 5
# for i in range(1, n + 1): 
#     print(" " * (n - i) + "* " * i)
# for i in range(n - 1, 0, -1):
#     print(" " * (n - i) + "* " * i)



# # Example 6: Hollow square pattern
# n = 5
# for i in range(n):
#     for j in range(n):
#         if i==0 or i==n-1 or j==0 or j==n:
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     print()



# # Example 7: Hollow  right aligned triangle pattern
# n = 5
# for i in range(n):
#     for j in range(n):
#         if j == 0 or i == n - 1 or i == j:
#             print("*", end=" ")
#         else: 
#             print(" ", end=" ")
#     print()



# # Example 8: Hollow diamond pattern
# n = 5
# for i in range(n):
#     for j in range(n):
#         if i == 0 or i == n - 1 or j == 0 or j == n - 1 or i == j or i + j == n - 1:
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     print()



# # Example 9: Hollow rectangle pattern
# n = 5
# m = 10
# for i in range(n):
#     for j in range(m):
#         if i == 0 or i == n - 1 or j == 0 or j == m - 1:
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     print()



# # Example 10: Hollow pyramid pattern
# n = 5
# for i in range(n):
#     for j in range(n):
#         if j == n - i - 1 or j == n + i - 1 or i == n - 1:
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     print()


# # Example 11: Hollow inverted pyramid pattern
# n = 5
# for i in range(n):
#     for j in range(n):
#         if j == i or j == n - i - 1 or i == 0:
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     print()


# # Example 12: Hollow hourglass pattern
# n = 5
# for i in range(n):
#     for j in range(n):
#         if i == 0 or i == n - 1 or j == 0 or j == n - 1 or i + j == n - 1 or i - j == 0:
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     print()

    
# Example 13: Triangle
# rows=5
# for i in range(1,rows+1):
#     print(" "*(rows-i)+"* "*i)


# Example 14: Inverted Triangle
# rows=5
# for i in range(5,0,-1):
#     print(" "*(rows-i)+"* "*i)


# Example 15: Right aligned number triangle
for i in range(1,6):
    print(" "*(5-i)+str(i)*i)


# Example 16: Left aligned number Triangle
for i in range(1,6):
    print(str(i)*i)

# Example 17 : Left aligned increasing number triangle
for i in range(1,6):
    for j in range(1,i+1):
        print(j,end=" ")
    print()

'''Conditional statements: conditional statements are used to perform different actions based on different conditions. 
The conditional statements are as follows:-
1. if statement
2. if-else statement
3. if-elif-else statement
4. match-case statement
5. nested if statement
6. switch-case statement (simulated using dictionary)
'''
# Examples
# If statement
marks = int(input("Enter your marks: "))
if marks > 91:
    print("First Class")

# If-else statement
marks = int(input("Enter your marks: "))
if marks > 91:
    print("First Class")
else:
    print("Fail")



# If-elif-else ladder
Billamount = int(input("Enter your Bill amount: "))
if 1000 < Billamount < 5000:
    Discount = 0.1
    print("The Final price is", Billamount - Discount * Billamount)
elif 5000 < Billamount < 10000:
    Discount = 0.25
    print("The Final price is", Billamount - Discount * Billamount) 
elif Billamount > 10000:
    Discount = 0.5
    print("The Final price is", Billamount - Discount * Billamount) 
else:
    print("No Discount")


# Match-case statement
monthno = int(input("Enter a number between 1-12: "))   
match monthno:
    case 1:
        print("Jan")
    case 2:
        print("Feb")
    case 3:
        print("Mar")
    case 4:
        print("Apr")
    case 5:
        print("May")
    case 6:
        print("Jun")
    case 7:
        print("Jul")        
    case 8:
        print("Aug")
    case 9:
        print("Sep")
    case 10:
        print("Oct")
    case 11:
        print("Nov")
    case 12:
        print("Dec")
    case _:
        print("Enter a number between 1-12")


# Nested if statement
num = int(input("Enter a number: "))
if num > 0:
    if num % 2 == 0:
        print("Positive Even Number")
    else:
        print("Positive Odd Number")
else:
    if num % 2 == 0:
        print("Negative Even Number")
    else:
        print("Negative Odd Number")

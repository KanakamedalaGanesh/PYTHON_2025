#simple if
marks=int(input("Enter your marks:"))
if (marks>91) :
    print("First Class")

#If-else
marks=int(input("Enter your marks:"))
if(marks>91):
    print("First Class")
else:
    print("Fail")

#else-if ladder
Billamount=int(input("Enter your Billamount:"))

if(Billamount>1000 and Billamount<5000):
    Discount=0.1
    print("The Final price is ",Billamount-Discount)
elif(Billamount>5000 and Billamount<10000):
    Discount=0.25
    print("The Final price is ",Billamount-Discount)
elif(Billamount>10000):
    Discount=0.5
    print("The Final price is ",Billamount-Discount)
else:
    print("No Discount")

#Match Case
monthno=int(input("Enter between 1-12:"))
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
    case 12:
        print("Nov")
    case 12:
        print("Dec")
    case _ :
        print("Enter a number between 1-12")


# Nested if
num = int(input("Enter a number: "))
if num > 0:
    print("Positive number")
    if num % 2 == 0:
        print("Even number")
    else:
        print("Odd number")
else:
    print("Negative number")
    if num % 2 == 0:
        print("Even number")
    else:
        print("Odd number")



#Switch case# Python does not have a built-in switch-case statement, but we can use a dictionary to simulate it.
def switch_case(monthno):
    switcher = {
        '1': 'Jan',
        '2': 'Feb',
        '3': 'Mar',
        '4': 'Apr',
        '5': 'May',
        '6': 'Jun',
        '7': 'Jul',
        '8': 'Aug',
        '9': 'Sep',
        '10': 'Oct',
        '11': 'Nov',
        '12': 'Dec'
    }
    return switcher.get(str(monthno), "Enter a number between 1-12")
monthno = int(input("Enter between 1-12: "))
print(switch_case(monthno))
   



   
    
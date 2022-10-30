# CONDITIONAL STATEMENTS #
'''
- Conditional statements are also called decision-making statements.
- We use those statements while we want to execute a block of code when the given condition is TRUE or FALSE.
- We have a 5 types of conditional statement execution method.
    1. Simple IF
    2. IF - ELSE
    3. IF - ELIF - ELSE
    4. IF - ELIF - ELSE ladder
    5. Nested IF - ELSE
'''

# ○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○

# 1. SIMPLE IF:
'''
- If we have only one condition then we can use 'SIMPLE IF'
- Here, the program evaluates the 'test expression' and will execute 'IF body or statement' only if the test expression is TRUE.
- If the test expression is FALSE, the 'if body or statement' is not executed.
- In Python, the body of the if statement is indicated by the indentation (1 tab or 4 space by default). The body starts 
  with an indentation and the first unindented line marks the end.
- Python interprets non-zero values as TRUE and 0 & None interpreted as FALSE.
'''

# Syntax:-
'''
IF <test expression>:
    (IF body or statement)
'''

# EXAMPLE: 1
'''
num = int(input("Enter the number: "))

if num > 0:
    print(num, "is a positive number.")
'''

# ○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○

# 2. IF - ELSE:
'''
- When we want to execute a code only if a certain condition is satisfied. Contradictory condition - True and False.
- The 'IF-ELSE' statement evaluates test expression and will execute the body of IF only when the test condition is TRUE.
- If the condition is FALSE, the body of ELSE is executed.
- Indentation is used to separate the block.
'''

# Syntax:-
'''
IF <test expression>:
    (body of if)
ELSE:
    (body of else)
'''

# EXAMPLE: 1
'''
num = int(input("Enter the number: "))

if num > 0:
    print("You have entered a Positive Number")
else:
    print("You have entered a Negative Number")
'''

# ○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○

# 3. IF - ELIF - ELSE:
'''
- It allows us to check for multiple expressions.
- The elif is short for else if
- If the condition for IF is FALSE, it checks the condition of the next ELIF block.
- If all the conditions are FALSE, the body of ELSE is executed.
- Only one block among the several 'IF...ELIF...ELSE' blocks is executed according to the condition.
- The IF block can have only one ELSE block. But it can have multiple ELIF blocks.
'''

# Syntax:-
'''
IF <test expression.:
    (body of if)
ELIF <test expression>:
    (body of elif)
ELSE:
    (body of else)
'''

# EXAMPLE: 1

'''
num = float(input("Enter the number: "))

if num > 0:
    print("You have entered a Positive number")
elif num == 0:
    print("You have entered Zero")
else:
    print("You have entered a Negative number")
'''

# ○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○

# 4. IF-ELIF-ELSE ladder:
'''
- User can decide among multiple options.
- User can add any no. of statement by using ELIF no. of times.
- The IF statements are executed from the top down.
- As soon as one of the conditions controlling the IF is TRUE, the statement associated with that IF is executed, and 
  the rest of the ladder is bypassed/skipped.
- If none of the conditions is TRUE, then the final ELSE statement will be executed.
'''

# Syntax:-
'''
if test expression1:
    (body of if)
elif test expression2:
    (body of elif)
elif test expression3:
    (body of elif)
.
.
.
else:
    (body of else)
'''

# EXAMPLE: 1
'''
num = float(input("Enter the number: "))

if (num == 0):
    print("Please enter greater no.")
elif (num > 1):
    print("Please enter lesser no.")
elif (num == 1):
    print("You have entered a Exact no.")
else:
    print("Try again")
'''

# ○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○

# 5. NESTED IF-ELSE:
'''
- We can have a 'if...elif...else' statement inside another 'if...elif...else' statement. This is called nesting in 
  computer programming.
- Any number of these statements can be nested inside one another.
- Indentation is the only way to figure out the level of nesting.
'''

# Syntax:-
'''
if <test expression1>:
        if <test expression2>:
            (body of if2)
        else:
            (body of else)
else:
    (body of else)
'''

# EXAMPLE: 1
'''
num = float(input("Enter a number: "))

if num >= 0:
    if num == 0:
        print("Zero")
    else:
        print("Positive number")
else:
    print("Negative number")
'''

# ☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻

'''
Date = int(input("Enter Birth Date: "))
Month = int(input("Enter Birth Month: "))
Year = int(input("Enter Birth Year: "))

Age = 2022 - Year

if Date != 0 and Date <= 31 and Month != 0 and Month <= 12 and Year != 0:
    if Age <= 23 and Age != 0:
        print("Wishing You a Happy Birthday Neha :) ")
    elif Age <= 27 and Age > 23:
        print("Happy Birthday Dear Neha. Wish You many many Happy returns of the Day. "
              "God Bless You. May your wishes come True. :) :) :) :) :)")
    else:
        if Age > 27 and Age <= 30:
            print("Happy Birthday Dear Neha. :)")
        else:
            print("Then and then Happy Birthday Neha :) ")
else:
    print("Nitin Patil wishing you a Very Happy Birthday in a different style.")
'''




























# PRACTICE

# SIMPLE IF

# 1
'''For greater no.'''
# Var1 = int(input("Enter the number: "))
#
# if Var1 > 25:
#     print("You entered a greater number")
# print("Thanks for using program")

# 2
'''For positive no.'''
# Var2 = float(input("Enter the number: "))
#
# if Var2 > 0:
#     print("You entered a positive number")
# print("Be positive")

# 3
'''For negative no.'''
# Var3 = float(input("Enter the number: "))
#
# if Var3 > 0:
#     print("You entered a negative number")
# print("Still be positive")

# 4
'''To detect float no.'''
# Var4 = float(input("Enter any float number: "))
#
# if Var4 == float():
#     print("You entered a float number")
# print("You detected float number.")

# 5
'''To detect int no.'''
# Var4 = int(input("Enter any float number: "))
#
# if Var4 == int():
#     print("You entered a int number")
# print("You detected int number.")

# 6
# Var5 = 5
# if Var5 < 10:
#     print("Var5 is less than 10")

# 7
# num = int(input("Enter any number: "))
# print("Last digit of number is ", num % 10)

# 8
# mail_address = "nitinpatilnp260923.np@gmail.com"
# if '@' in mail_address:
#     print("Valid mail address")
# print("Thanks for using our service")

# 9
# if 'Python' in ['Python', 'Java', 'HTML']:
#     print("Yes, Python is present in given list")

# 10
# mail_Id = "nitinpatilp29@gmail.com"
# if mail_Id.endswith('.com'):
#     print("Valid mail id")
# print("Thanks for using our service")





# IF ELSE

# 1

'''Write a program to check whether a number is divisible by 7 or not.'''
# NumB = int(input("Enter your no: "))
# if NumB % 7 == 0:
#     print("Yes its divisible by 7")
# else:
#     print("Its not divisible by 7")










# i = int(input("Enter the number: "))
# def evens(i):
#     if i%2 == 0:
#         print(True)
#     else:
#         print(False)
# evens(i)







# 2

'''Write a program for a number you enterd is Even or Odd'''
# Num = int(input("Enter your no: "))
#
# if Num % 2 == 0:
#     print("You entered a even no.")
# else:
#     print("You entered a odd no.")

# 3

'''License verification'''
# my_age = int(input("Enter your age: "))
#
# if my_age <= 18:
#     print("You can not drive")
# else:
#     print("You can drive")

# 4

'''Age verification'''
# age = int(input("Enter your age: "))
#
# if age <= 20:
#     print("You are not that much mature to get married")
# else:
#     print("You are ready to destroy your own life")

# 5

# variable6 = ['Elephant', 'Dog', 'Cat', 'Tiger']
#
# if 'Dog' in variable6:
#     print("Dog is in the list/variable6")
# else:
#     print("Dog is in Dogvan")

# 6

'''Check for valid mail address'''
# Mail_Id = str(input("Enter your mail id here: "))
# if Mail_Id.endswith('.com'):
#     print("It is a valid mail")
# else:
#     print("It is invalid mail")

# 7

'''Verification of mail'''
# mail = str(input("Enter your mail here: "))
# if mail.split('@')[1].endswith('.com'):
#     print("Valid mail")
# else:
#     print("Invalid mail")

# 8

# string = "NITIN PATIL"
# if string.isupper():
#     print("Yes")
# else:
#     print("No")

# 9

# string1 = str(input("Enter sting here: "))
# if string1.startswith('M'):
#     print("Yup")
# else:
#     print("No")

# 10

# Email = str(input("Enter your Email here: "))
# if Email.split('@'):
#     print(Email.split('@')[1])
# else:
#     print("Nothing")

# 11

'''Write a program to check whether the last digit of a number( entered by user ) is divisible by 3 or not.'''

# numbE = int(input("Enter the number: "))
# numbE1 = (numbE % 10)
# if (numbE1 % 3 == 0):
#     print("Hiii")
# else:
#     print("bye")

# 12

# from datetime import date
# DayDate = date.today()
# if DayDate.year % 4 == 0:
#     print("Its a leap year")
# else:
#     print("Its not a leap year")

    # or

# year = int(input("Enter year: "))
# if year % 4 == 0:
#     print("Its a leap year")
# else:
#     print("Its not a leap year")

# 13

'''Write a program to whether a number (accepted from user) is divisible by 2 and 3 both.'''

# both = int(input("Enter the number: "))
# if both % 2 == 0 or both %3 ==0:
#     print("Yes")
# else:
#     print("No")

# 14

'''Write a program to check whether a number entered is three digit number or not.'''

# digit = (input("Enter a number: "))
# if len(digit) == 3:
#     print("Yes its a 3 digit no.")
# else:
#     print("No its not a 3 digit no.")

# 15

'''Write a program to check a character is vowel or not.'''

# character = input("Enter any character or alphabet: ")
# Vowels = 'aeiouAEIOU'

# if character in Vowels:
#     print("Its a vowel")
# else:
#     print("Its not vowel")

# 16

'''Accept the following from the user and calculate the percentage of class attended:

a.     Total number of working days

b.     Total number of days for absent

    After calculating percentage show that, If the percentage is less than 75, than student will not be able to sit in exam.'''

# Working_days = int(input("Enter no. of working days: "))
# absent = int(input("Total no. of days for absent: "))
# percentage = absent*100/Working_days
#
# if percentage < 75:
#     print("Student will not be able to sit in exam")
#     print("Because percentage of class attended is", percentage, "less than 75%")
# else:
#     print("Student can sit in exam")
#     print("Because percentage of class attended is", percentage, "greater than 75%")


# IF-ELIF-ELSE

# 1

# price = float(input("Enter price amount: "))
#
# if price > 100:
#     print("Price is greater than 100")
# elif price == 100:
#     print("Price is 100")
# elif price < 100 and price != 0:
#     print("Price is less than 100")
# else:
#     print("Free of cost")

# 2

# percentage = float(input("Enter your percentage here: "))
#
# if percentage > 75:
#     print("First class with distinction")
# elif 60 < percentage and percentage < 75:
#     print("First class")
# else:
#     print("Please study")

# 3
'''
Write a program to calculate the electricity bill (accept number of unit from user) according to the following criteria :
     Unit                                                       Price
First 100 units                                               no charge
Next 100 units                                              Rs 5 per unit
After 200 units                                             Rs 10 per unit
'''

# Meter_Unit = float(input("Enter meter reading: "))
#
# if Meter_Unit <= 100:
#     print("For first 100 units No extra charge.")
# elif Meter_Unit > 100 and Meter_Unit <= 200:
#     print("Rs 5 per unit is extra above 100 units and your electricity bill is: ", Meter_Unit*5)
# else:
#     print("Rs 10 per unit is extra after 200 units and your electricity bill is: ", Meter_Unit*10)

# 4

# filename = input("Enter file name with extension: ")
#
# if filename.endswith('.pdf'):
#     print("It is a PDF file")
# elif filename.endswith('.py'):
#     print("It is a Python file")
# else:
#     print("Different format")

# 5

# from datetime import date
# todays_date = date.today()
# if todays_date == '2022-04-05':
#     print("Tuesday")
# elif todays_date == '2022-04-04':
#     print("Monday")
# else:
#     print(todays_date)

# 6

# from datetime import datetime
# todays_datetime = str(datetime.now())
# if todays_datetime.endswith('45'):
#     print("Something is wrong")
# elif todays_datetime.endswith('18'):
#     print("Again wrong")
# else:
#     print(todays_datetime)

# 7

# variable7 = int(input("Enter number: "))
# variable8 = float(input("Enter no you want to add: "))
#
# addition = variable7 + variable8
#
# if addition > 100:
#     print("Good morning")
# elif addition < 100 and addition != 0:
#     print("Good afternoon")
# else:
#     print("Good night")

# 8
'''
Write a program to accept the cost price of a bike and display the road tax to be paid according to the following criteria :

         Cost price (in Rs)                                        Tax
        > 100000                                                  15 %
        > 50000 and <= 100000                                     10 %
        <= 50000                                                   5 %
'''

# CP_of_Bike = int(input("Enter your bike's cost price: "))
#
# if CP_of_Bike > 100000:
#     print("You have to pay road tax 15 %, which is equal to: ", 0.15*CP_of_Bike)
# elif CP_of_Bike > 50000 and CP_of_Bike <= 100000:
#     print("You have to pay road tax 10 %, which is equal to: ", 0.10*CP_of_Bike)
# else:
#     print("You have to pay road tax 5 %, which is equal to: ", 0.05*CP_of_Bike)


    # or


# tax = 0
# pr = int(input("Enter the price of bike"))
# if pr > 100000:
#      tax = 0.15*pr
# elif pr >50000 and pr <=100000:
#      tax = 0.10/100*pr
# else:
#      tax = 0.05/100*pr
# print("Tax to be paid ", tax)

# 9

'''Write a program to accept a number from 1 to 7 and 
display the name of the day like 1 for Sunday , 2 for Monday and so on.'''

# Day_No = int(input("Enter number no. between 1 to 7: "))
# if Day_No == 1:
#     print("Sunday")
# elif Day_No == 2:
#     print("Monday")
# elif Day_No == 3:
#     print("Tuesday")
# elif Day_No == 4:
#     print("Wednesday")
# elif Day_No == 5:
#     print("Thursday")
# elif Day_No == 6:
#     print("Friday")
# elif Day_No == 7:
#     print("Saturday")
# else:
#     print("Please enter proper no.")

# 10

'''Write a program to accept a number from 1 to 12 and display name of the month and days in that month 
like 1 for January and number of days 31 and so on.'''

# Month = int(input("Enter a number between 1 to 12: "))
# Days_in_Month = 30
# if Month == 1:
#     print("January")
#     print("Days in January", Days_in_Month + 1)
# elif Month == 2:
#     print("February")
#     print("Days in February", Days_in_Month - 2)
# elif Month == 3:
#     print("March")
#     print("Days in March", Days_in_Month - 1)
# elif Month == 4:
#     print("April")
#     print("Days in April", Days_in_Month - 0)
# elif Month == 5:
#     print("May")
#     print("Days in May", Days_in_Month - 1)
# elif Month == 6:
#     print("June")
#     print("Days in June", Days_in_Month - 0)
# elif Month == 7:
#     print("July")
#     print("Days in July", Days_in_Month - 1)
# elif Month == 8:
#     print("August")
#     print("Days in August", Days_in_Month - 1)
# elif Month == 9:
#     print("September")
#     print("Days in September", Days_in_Month - 0)
# elif Month == 10:
#     print("October")
#     print("Days in October", Days_in_Month - 1)
# elif Month == 11:
#     print("November")
#     print("Days in November", Days_in_Month - 0)
# elif Month == 12:
#     print("December")
#     print("Days in December", Days_in_Month - 1)
# else:
#     print("Please enter correct no.")

# 11

'''
A company decided to give bonus to employee according to following criteria:

    Time period of Service                Bonus

    More than 10 years                    10%

    >=6 and <=10                           8%

    Less than 6 years                      5%

Ask user for their salary and years of service and print the net bonus amount.
'''

# service = int(input("Time period of service: "))
# salary = int(input("What is your current salary: "))
#
# if service > 10:
#     print("You will get bonus 10% & your bonus amount is", 0.10*salary)
# elif service >= 6 and service <= 10:
#     print("You will get bonus 8% & your bonus amount is", 0.08*salary)
# elif service < 6 and service != 0:
#     print("You will get bonus 5% & your bonus amount is", 0.05*salary)
# else:
#     if service == 0 or salary == 0:
#         print("You have entered a wrong data")

# 12

'''
Accept the marked price from the user and  calculate the Net amount as (Marked Price – Discount) to 
pay according to following criteria:

Marked Price	   Discount
>10000               20%
>7000 and <=10000	 15%
<=7000	             10%

'''

# marked_price = int(input("Please enter marked price of product: "))
#
# if marked_price > 10000:
#     Discount = 20 * marked_price / 100
#     print("You will get 20% Discount and the net payable amount is: ", marked_price - Discount)
# elif marked_price > 7000 and marked_price <= 10000:
#     Discount = 15 * marked_price / 100
#     print("You will get 15% Discount and the net payable amount is: ", marked_price - Discount)
# elif marked_price <= 7000 and marked_price != 0:
#     Discount = 10 * marked_price / 100
#     print("You will get 10% Discount and the net payable amount is: ", marked_price - Discount)
# else:
#     print("You have entered a wrong data")

# 13



# 14

'''
Write a program to accept two numbers and mathematical operators and perform operation accordingly.

Like:

Enter First Number: 7

Enter Second Number : 9

Enter operator : +

Your Answer is : 16
'''

# Num1 = float(input("Please enter first no: "))
# Num2 = float(input("Please enter second no: "))
# operator = input("Please select operator from +, -, *, /, %, //, ** : ")
#
# if operator == '+':
#     print("Addition is: ", Num1 + Num2)
# elif operator == '-':
#     print("Substraction is: ", Num1 - Num2)
# elif operator == '*':
#     print("Multiplication is: ", Num1 * Num2)
# elif operator == '/':
#     print("Division is: ", Num1 / Num2)
# elif operator == '%':
#     print("Remainder is: ", Num1 % Num2)
# elif operator == '//':
#     print("Floor division is: ", Num1 // Num2)
# elif operator == '**':
#     print("Power is: ", Num1 ** Num2)
# else:
#     print("Select correct operator")

# 15

'''
Accept the age, sex (‘M’, ‘F’), number of days and display the wages accordingly

Age	            Sex	        Wage/day
>=18 and <30	 M	          700
                 F	          750
>=30 and <=40	 M	          800
                 F	          850

If age does not fall in any range then display the following message: “Enter appropriate age”
'''
# Age = int(input("Enter your age here: "))
# Sex = input("Please select 'M' or 'F' or 'm' or 'f': ")
# Days = int(input("Enter no. of days: "))
#
# if Age >= 18 and Age < 30 and Sex.upper() == 'M':
#     Amount = Days * 700
#     print("Total amount of wage is: ", Amount)
# elif Age >= 18 and Age < 30 and Sex.upper() == 'F':
#     Amount = Days * 750
#     print("Total amount of wage is: ", Amount)
# elif Age >= 30 and Age <= 40 and Sex.upper() == 'M':
#     Amount = Days * 800
#     print("Total amount of wage is: ", Amount)
# elif Age >= 30 and Age <= 40 and Sex.upper() == 'F':
#     Amount = Days * 850
#     print("Total amount of wage is: ", Amount)
# else:
#     print("Enter appropriate age")

# 16

'''
Accept the kilometers covered and calculate the bill according to the following criteria:

First 10 Km              Rs11/km

Next 90Km               Rs 10/km

After that               Rs9/km
'''

# kilometers = int(input("Enter how much kilometer you covered: "))
#
# if kilometers <= 10 and kilometers != 0:
#     Total_charge = kilometers * 11
#     print("The charge per km is Rs.11 and your bill is Rs:", Total_charge)
# elif kilometers > 10 and kilometers <= 100:
#     Total_charge = kilometers * 10
#     print("The charge per km is Rs.10 and your bill is Rs:", Total_charge)
# elif kilometers > 100:
#     Total_charge = kilometers * 10
#     print("The charge per km is Rs.9 and your bill is Rs:", Total_charge)
# else:
#     print("You are eligible for free traveling")

# 17

'''
Accept the marks of English, Math and Science, Social Studies Subject and display the stream allotted according to following

All Subjects more than 80 marks —       Science Stream
 
English >80 and Math, Science above 50 –Commerce Stream
 
English > 80 and Social studies > 80    —   Humanities
'''

# English = int(input("Enter the marks obtained in English: "))
# Maths = int(input("Enter the marks obtained in Maths: "))
# Science = int(input("Enter the marks obtained in Science: "))
# Social_Syudies = int(input("Enter the marks obtained in Social_Syudies: "))
#
# if English == Maths == Science == Social_Syudies > 80:
#     print("Go for Science Stream")
# elif English > 80 and Maths == Science > 50:
#     print("Go for Commerse Stream")
# elif English > 80 and Social_Syudies > 80:
#     print("Go for Humanities Stream")
# else:
#     print("You are not eligible for any stream")




# NESTED IF ELSE

# 1

# Num = int(input("Enter the number: "))
#
# if Num > 0:
#     if Num > 100:
#         print("Welcome to nested if else statement")
#     else:
#         print("Welcome Dear")
# else:
#     print("Thanks for using Nested if")

# 2

'''
Accept three sides of triangle and check whether the triangle is possible or not.
'''

# Side1 = int(input("Please enter side1 dimension: "))
# Side2 = int(input("Please enter side2 dimension: "))
# Side3 = int(input("Please enter sode3 dimension: "))
#
# if Side1 != 0 and Side2 != 0 and Side3 != 0:
#     if Side1 + Side2 > Side3 and (Side2 + Side3) > Side1 and (Side1 + Side3) > Side2:
#         print("Triangle possible")
#     else:
#         print("Try again")

# 3

'''
Accept three sides of a triangle and check whether it is an equilateral, isosceles or scalene triangle.

Note :

An equilateral triangle is a triangle in which all three sides are equal.

A scalene triangle is a triangle that has three unequal sides.

An isosceles triangle is a triangle with (at least) two equal sides.
'''

# Side1 = int(input("Enter 1st side dimension here: "))
# Side2 = int(input("Enter 2nd side dimension here: "))
# Side3 = int(input("Enter 3rd side dimension here: "))
#
# if Side1 != 0 and Side2 != 0 and Side3 != 0:
#     if Side1 == Side2 == Side3 != 0:
#         print("It is a Equilateral triangle")
#     elif Side1 != Side2 != Side3:
#         print("It is a Scalene triangle")
#     elif Side1 == Side2 != Side3 or Side1 == Side3 != Side2 or Side2 == Side3 != Side1:
#         print("It is a Isosceles triangle")
# else:
#     print("Please enter valid dimensions")







'''
# P = [10, 20, 30, 40, 50, 33, 35, 37]

# from functools import reduce
#
# print(reduce(lambda x, y: x + y, P))

# even = [x for x in P if x % 2 ==0]
# print(even)

# #Comprehension
# list
# tuple
# dict

# e = ['nitinpatilp29@gmail.com', 'nitin@yahoo.com', 'priyankakamblep29@redifmail.com']
# d = ['abcd', 'abdc', 'abcx']
#
# e1 = [x for x in e if x.endswith('@gmail.com')]
# print(e1)
#
# e2 = [y for y in d if y.startswith('abc')]
# print(e2)

# d1 = {i:i for i in range(10)}
# print(d1)

# for i in range(10):
#     print({i:i})

# P = [[1, 2, 3], ['python', 'java', 'html']]
# d2 = [i for x in P for i in x]
# print(d2)

# for x in P:
#     for i in x:
#         print(i)


# P = [[1, 2, 3], ['python', 'java', 'html']]
# # Dictionary = {x:j for x in P[0] for i in P for j in P[0]}
# # print(Dictionary)
#
# for x in P[0]:
#     for i in P[1]:
#         print(f"{x}:{i}")
'''


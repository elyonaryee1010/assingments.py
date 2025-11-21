#Taking Inputs

a = input("Type Value of A")
b = input("Type Value of B")
c = input("Type Value of c")

#swap

temp = a
a = b
b = temp


#Display results

print(Value of A after the swap", a)
print(Value of B after the swap", b)
print(Value of C after the swap", c)

#Odd or Even

number = int(input("Enter a numer :"))
print("number is :", number)
    if number%2==0:
        print("Even Number detected")
        else:
            print("Odd Number detected")

            #BMI
weight = int(input("Enter your weight in kilograms :"))
height = int(input("Enter your weight in cm"))
BMI = eight/(height/100)**2
print("Your BMI is :", BMI)

if BMI<18.5:
     print("Your are underweight")
elif BMI>=18.5 and BMI<24.9:
    print("You are normal")
elif BMI>=25 and BMI<29.9:
    print("You are overweight")
else:
    print("You're obese")

    #Double Check

number = int(input("Enter your number here"))
print("You're number is:", number)
if number>=50:
    if num%2==0
    print("Great")
else:
    print("Less")

    else:
        print("nothing_)"


    #Time &date
import datetime
current_time = datetie.datime.new()
print("current time here is:", current_time)



#Assignment

print("Welcome to Age-Verfications for your JASSCO 2025 Application. Please note that you are to be 18 years before you proceed")

age = int(input("Age:"))
print("You're age:", age)
if age >= 18:
    print("You are eligble. Please proceeed with you're JASSSCO Apllication.")
else:
    print("Sorry, You're too underaged to take your JASSCO Exam. Try again when you're older.")

    
#15/11/2025

num = 200
num_str = str(num)
n = len(num_str)
total_sum = 0
for digit_char in num_str:
    digit = int(digit_char)
    total_sum += digit**n
    
if total_sum == num:
    print(f"{num} This is an ARMstrong number")
else:
    print(f"{num} This isnt armstrong")

#Fabonacci
int(input("Enter Number"))
def fibonacci_recursive(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)
    print("This is a correct Fibonacci")


print(f"Fibonacci number: {fibonacci_recursive(10)}")

    

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

#Assignment

print("Welcome to Age-Verfications for your JASSCO 2025 Application. Please note that you are to be 18 years before you proceed")

age = int(input("Age:"))
print("You're age:", age)
if age >= 18:
    print("You are eligble. Please proceeed with you're JASSSCO Apllication.")
else:
    print("Sorry, You're too underaged to take your JASSCO Exam. Try again when you're older.")

    

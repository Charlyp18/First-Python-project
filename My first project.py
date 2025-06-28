print(" My Simple Calculator")
name =input( " What is your name? ")
print("Hello "+name)

print("Today,you have the chance to use my simple calculator".upper())
num1 = float(input("Enter first number: "))
operation = input("Enter operator (+, -, *, /): ")
num2 = float(input("Enter second number: "))

if operation == '+':
    print(num1 + num2)
elif operation == '-':
    print(num1 - num2)
elif operation == '*':
    print(num1 * num2)
elif operation == '/':
    print(num1 / num2)
else:
    print("Invalid operator".upper())
   
print("Thank you and have a nice day".upper())
    
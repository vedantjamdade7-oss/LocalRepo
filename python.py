# Simple Calculator


num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

sum = input("Choose an operation +, *, -, / : ")

if sum == "+":
    print("Result:", num1 + num2)

elif sum == "*":
    print("Result:", num1 * num2)

elif sum == "-":
    print("Result:", num1 - num2)

elif sum == "/":
    if num2 != 0:
        print("Result:", num1 / num2)
    else:
        print("Error: Cannot divide by zero")

else:
    print("Invalid choice")




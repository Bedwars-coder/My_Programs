print("Welcome to calculator.")
num1 = input("Enter a number:")
choice = input("Enter a operand(add, sub, mul, div):")
num2 = input("Enter the seconmd number:")
if choice=='add':
    print("The sum of the two numbers is", float(num1)+float(num2))
elif choice=='sub':
    print("The difference between the two numbers is", float(num1)-float(num2)))
elif choice=='mul':
    print("The product of the two numbers is", float(num1)*float(num2))
elif choice=='div':
    print("The quotient of the two numbers when they are divided is", float(num1)/float(num2))
else:
    print("What are you thinking man? Enter a valid option please.")
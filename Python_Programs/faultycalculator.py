try:
    def rerun():
        # 45 * 3 = 555, 56 + 9 = 77, 56/6 = 4
        num1 = float(input("Enter a number:"))
        operator = input("Enter a operator(add, sub, mul, div )")
        num2 = float(input("Enter another number:"))
        if operator=='add' and num1==56 and num2==9:
            print("The sum is 77")
        elif operator=='add':
            print("The sum is ",num1+num2)
        elif operator=='sub' :
            print("The difference is ",num1-num2)
        elif operator=='mul' and num1==45 and num2==3:
            print("The product is 55")
        elif operator=='mul':
            print("The product is ",num1*num2)
        elif operator=='div' and num1==56 and num2 ==6:
            print("The Quotient is 4")
        elif operator=='div':
            print("The Quotient is ",num1/num2)
        else:
            print("Enter a valid input MAN!")

    choice = input("Do  you want to calculate?")
    list = ['yes', 'yea', 'yep', 'y']
    if choice in list:
        print("Ok")
        rerun()
    else:
        exit("Exited successfully!")
except Exception as error1:
    print("Hmmm, Something went wrong. Please consider trying again!")
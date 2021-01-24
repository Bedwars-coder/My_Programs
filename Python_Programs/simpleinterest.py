try:
    def reruncode():
        print("Welcome\n")
        p = float(input("Enter the principal:\n"))
        t = float(input("Enter the time in years:\n"))
        r = float(input("Enter the rate of interest:\n"))
        si = (p*t*r)/100

        choice1 = input("What do you want? 'si' for Simple Interest or 'a' for Amount:\n")
        if choice1 == 'si':
            print("The Simple Interest is",si)
        elif choice1 == 'a':
            print("The amount that you will get is",si+p)


        choice1 = input("Do you want to play again?('y' or 'n')?\n")
        if choice1 == 'y':
            print("Thanks, for playing game again!")
            reruncode()
        elif choice1 == 'n':
            exit("Thanks!")
        else:
            print("Invalid input!! You dumb!!")
        




    reruncode()
except Exception as error1:
    print("Invalid input!! You dumb!!")
import datetime
def reruncode():
    try:
        def time():
            return datetime.datetime.now()
        timer = str(time())
        def log(felog):
            if felog == 1:
                value = input("Enter what you ate today: ")
                with open("dibya_food.txt", "a") as op:
                    op.write(timer+ ": " +value+"\n")
                print("Successfully logged!")
            elif felog == 2:
                value = input("Enter what exercises you did today: ")
                with open("dibya_exer.txt", "a") as op:
                    op.write(timer+": " +value+"\n")
                print("Successsfully logged!")
            else:
                print("Kindly enter a valid input!")

        def ret(feret):
            if feret == 1:
                with open("dibya_food.txt") as op:
                    for lines in op:
                        print(lines)
            elif feret == 2:
                with open("dibya_exer.txt") as op:
                    for lines in op:
                        print(lines)
            else:
                print("Kindly enter a valid input!")

        def clear():
            clr = int(input("What would you like to clear? 1 for food and 2 for exercise!"))
            if clr == 1:
                with open("dibya_food.txt", "w") as op:
                    op.write("")
            elif clr == 2:
                with open("dibya_exer.txt", "w") as op:
                    op.write("")
            else:
                print("Invalid Input!")
            print("Cleared!")

        print("Welcome to health management software!")
        print("You can press 3 to clear your records!")
        choice = int(input("What would you,like to do? Press 1 for Log and 2 for Retrieve: "))
        if choice == 1:
            felog = int(input("What would you like to log? Press 1 for Food and 2 for Exercise"))
            log(felog)
        elif choice == 2:
            feret = int(input("What would you like to retrieve? Press 1 for Food and 2 for Exercise"))
            ret(feret)
        elif choice == 3:
            clear()
        else:
            print("Kindly enter a valid input!")


        choice1 = input("Wanna run again? y or n")
        if choice1 == 'y':
            reruncode()
        elif choice1 == 'n':
            exit()
        else:
            print("Kindly enter a valid input!")

    except Exception as error1:
        print("You have entered an invalid input!")

reruncode()
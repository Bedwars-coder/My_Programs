# using for loops
def reruncode():
    try:
        rows = int(input("How many rows do you want?\n"))
        true_false = bool(int(input("Enter 0 or 1\n")))
        if true_false == True:
            for i in range(1, rows + 1 ):
                for j in range(1, i + 1):
                    print('*',end='')
                print()
        elif true_false == False:
            for i in range(rows, 0, -1):
                for j in range(1, i + 1):
                    print('*',end='')
                print()
        else:
            print("Invalid input\n")
    except Exception as error1:
        print("Invalid input!! You dumb!!")



    choice = input("Do you want to play again?('y' or 'n')?\n")
    if choice == 'y':
        print("Thanks, for playing game again!")
        reruncode()
    elif choice == 'n':
        exit("Thanks!")
    else:
        print("Invalid input!! You dumb!!")
reruncode()

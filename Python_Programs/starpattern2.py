# using while loops
def reruncode():
    try:
        rows = int(input("Enter the number of rows you want:\n"))
        truefalse = bool(int(input("Enter '0' or '1':\n")))


        def star(rows, truefalse):
            if truefalse == True:
                c = 1
                while c <= rows:
                    print(c * "*")
                    c = c + 1
            elif truefalse == False:
                while rows > 0:
                    print(rows * "*")
                    rows = rows - 1


        star(rows, truefalse)
    except Exception as error1:
        print("That's not a valid input u dumb!!")


    choice = input("Do you want to run the code again?('y' or 'n')")
    if choice == 'y':
        print("Thanks for playing again!")
        reruncode()
    elif choice == 'n':
        exit("Exited Successfully!")
    else:
        print("That's not a valid input u dumb!!")
reruncode()

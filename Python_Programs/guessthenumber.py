def replay():
    try:

        print("Welcome to the number guessing game.")
        print("You have 5 attemps to guess the correct number.")
        n = 18
        attempts = 1
        while attempts <= 5:
            num = int(input("Enter the correct number:\n"))
            if num < n:
                print("You entered a smaller number. Try again!")
            elif num > n:
                print("You entered a greater number. Try again!")
            else:
                print("You won with",5-attempts, "attempts left and using",attempts, "attempts!")
                break
            attempts = attempts + 1


        if attempts > 5:
            print("You lost!")


        rerun = input("Do you want to play again?('y' or 'n')")
        if rerun == 'y':
            print("Thanks for playing again!")
            replay()
        elif rerun == 'n':
            print("Exited Successfully!")
            exit()
        else:
            print("Something went wrong!")

    except Exception as error1:
        print("Something went wrong!")
replay()


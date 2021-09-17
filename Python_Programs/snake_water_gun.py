def reruncode():
    import random
    import time

    localtime = time.asctime(time.localtime(time.time()))

    print("Welcome to Snake Water Gun game!")
    comp_Choice = ['Snake', 'Water', 'Gun']
    user_Choice = ['snake', 'water', 'gun']
    attempts = 0
    user_points = 0
    comp_points = 0
    user_chpice = input("Press 'p' for playing and 's' for statistics!")
    name = input("Enter your name: ")
    
    if user_chpice == 'p':
        while attempts <= 10:
            user_input = input("Enter 'snake', 'water' or 'gun'!").lower()
            while user_input not in user_Choice:
                print("You need to enter a valid input!")
                attempts -= 1
                break
            if user_input in user_Choice:
                ran = random.choice(comp_Choice).lower()
                if user_input == ran:
                    print(f"It was a tie!\nYour choice: {user_input}\nComputer's choice: {ran}")

                elif user_input == 'snake' and ran == 'gun':
                    print(f"Ohhh No! Your snake was killed by Computer's gun")
                    comp_points += 1

                elif user_input == 'gun' and ran == 'snake':
                    print("Woohooo! Your gun killed computer's snake!")
                    user_points += 1


                elif user_input == 'water' and ran == 'snake':
                    print("Oh no! Your whole water was poisoned by computer's snake.")
                    comp_points += 1

                elif user_input == 'gun' and ran == 'water':
                    print("Computer threw water on your gun!")
                    comp_points += 1

                elif user_input == 'snake' and ran == 'water':
                    print("Bravo! Your snake poisoned the water of computer")
                    user_points += 1


                elif user_input == 'water' and ran == 'gun':
                    print("Wew! You threw water on computer's gun. Now gunpowder is wet!")
                    user_points += 1

            attempts += 1
            print(f"Attempt number. {attempts}!")
            print(f"Your points: {user_points}")
            print(f"Computer's point: {comp_points}")


        if user_points < comp_points:
            print("You lost! Wish you a better luck next time!")
            with open(name+".txt", "a") as op:
                op.write(localtime+": Lose\n")

        elif user_points > comp_points:
            print("You won! Winner Winner Chicken Dinner!")
            with open(name+".txt", "a") as op:
                op.write(localtime+": Win\n")

        elif user_points == comp_points:
            print("It was a tie! I wish you better luck next time!")
            with open(name+".txt", "a") as op:
                op.write(localtime+": Tie\n")

        else:
            print("Invalid input!")

    elif user_chpice == 's':
        del_or_show = input("What do you want? 'd' for deleting statistics amd 's' for showing the statistics")
        try:
            if del_or_show == 's':
                with open(name+".txt") as op1:
                    for lines in op1:
                        print(lines)

            elif del_or_show == 'd':
                with open(name+".txt", "w") as op2:
                    op2.write("")
                print("Successfully cleared!")

        except FileNotFoundError:
            print("An error occurred.\nBut still you can fix it and I will help you.")
            print("Try these methods:-\n1)Enter the name that you had entered when you started playing.\n")
    rerun_or_stop = input("Wanna run again? 'y' or 'n'!")
    if rerun_or_stop == 'y':
        reruncode()

    elif rerun_or_stop == 'n':
        exit()

    else:
        print("You made something go wrong!")
reruncode()

import random
print("Welcome to Snake Water Gun game!")
comp_Choice = ['Snake', 'Water', 'Gun']
user_Choice = ['snake', 'water', 'gun']
ran = random.choice(comp_Choice).lower()
attempts = 0
user_points = 0
comp_points = 0

while attempts <= 10:
    user_input = input("Enter 'snake', 'water' or 'gun'!").lower()
    while user_input not in user_Choice:
        print("You need to enter a valid input!")
        attempts -= 1
        break
    if user_input in user_Choice:
        points = 0
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

elif user_points > comp_points:
    print("You won! Winner Winner Chicken Dinner!")

elif user_points == comp_points:
    print("It was a tie! I wish you better luck next time!")

else:
    print("Invalid input!")
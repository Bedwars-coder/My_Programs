try:
    def reruncode():
        choice = input("Enter 'simple' or 'advanced'\n").lower()
        if choice=='simple':
            d1 = {'Harry':'Coder', 'Dibya':'Learner'}
            Key1 = input("Enter 'Harry' or 'Dibya' \n")
            print(d1[Key1])
        elif choice=='advanced':
            d2 = {'Harry':{'Youtube':'Codewitharry', 'Website':'codewithharry.com'}, 'Dibya':'Learner'}
            d3 = {'Youtube':'Codewitharry', 'Website':'codewithharry.com'}
            Key2 = input("Enter 'Harry' or 'Dibya'")
            if Key2=='Harry':
                print(d2[Key2])
                choice2 = input("Enter 'Youtube' or 'Website'")
                if choice2=='Youtube':
                    print(d3[choice2])
                elif choice2=='Website':
                    print(d3[choice2])
                else:
                    print("Enter a valid input please.")
            elif Key2=='Dibya':
                print(d2[Key2])
        else:
            print("Enter a valid input man.")

        choice3 = input("Do you want to run the code again?('y' or 'n')")
        if choice3 == 'y':
            print("Thanks for playing again!")
            reruncode()
        elif choice3 == 'n':
            exit("Exited Successfully!")
        else:
            print("That's not a valid input u dumb!!")


    reruncode()
except Exception as error1:
    print("That's not a valid input u dumb!!")
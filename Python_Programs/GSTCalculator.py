def codererun():
    try:
        print("Welcome to the GST Calculator developed by Dibya")
        selling_price = int(input("Enter your selling price: \n"))
        gst_percent = int(input("Enter the GST%(Don't include '%'): \n"))
        output_type = int(input("What type of answer do you want? '1' for only GST and '2' for amount+GST: \n"))

        gst = (gst_percent/100) * selling_price

        if output_type == 1:
            print(gst)

        elif output_type == 2:
            print(gst + selling_price)

        else:
            print("I need a valid input!!!")

        rerun = input("Wanna run again? 'y' or 'n'")

        if rerun == 'y':
            codererun()

        elif rerun == 'n':
            exit("Exited successfully")

        else:
            print("I need a valid input!!!")

    except Exception as error1:
        print("Gimme a valid input!!!")
codererun()
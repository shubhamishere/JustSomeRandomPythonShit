def menu():
    choice = True
    while choice:

        user_input = raw_input("Do you want to update status [Y/N]")
        if user_input == "Y":
            print "Your status has been updated"
        elif user_input == "N":
            print "Thank you."
            choice = False
        else:
            print "Invalid input, please enter again"
menu()
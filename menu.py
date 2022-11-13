"""
This bloc is used to  display the menu
"""
import functions as fn

def adminMenu():
    """This function show the admin menu"""

    print()
    print("ADMIN MENU LIST")
    print("1 - Display Statistics")
    print("2 - Add a Job")
    print("3 - Display All Jobs")
    print("4 - Change Jobs Priority")
    print("5 - Remove Job")
    print("6 - Run Printer")
    print("7 - Exit")
    print()

    choice = input("Enter your choice:")

    if choice=="1":
        fn.displayStat()
        adminMenu()
    elif choice=="2":
        fn.addJob()
        adminMenu()
    elif choice=="3":
        fn.displayJobs()
        adminMenu()
    elif choice=="4":
        fn.changeJobsPriority()
        adminMenu()
    elif choice=="5":
        fn.removeJob()
        adminMenu()
    elif choice=="6":
        fn.runPrinter()
        adminMenu()
    elif choice=="7":
        fn.exit()
    else:
        print("Wrong input")
        adminMenu()

#####################################################################

"""
This bloc is used to  display the menu
"""

def userMenu(username):
    """This function show the user menu"""
    
    print()
    print("USER MENU LIST")
    print("1 - Add a new Job")
    print("2 - Exit")
    print()

    choice = input("Enter your choice:")
    
    if choice=="1":
        fn.addNewJob(username)
        userMenu(username)
    elif choice=="2":
        fn.exit2()
    else:
        print("Wrong input")
        userMenu(username)
    
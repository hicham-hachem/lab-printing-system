"""
This is the main page
"""
import menu
import read_data as rd

admin_username = "admin"
admin_password = "admin123123"

print("Welcome to our Lab Printing System")
print()

def login():
    """This function is used to login"""
    
    # Giving 5 chances to enter a correct username and password
    i=0
    while i<5: # O(1)
        username = input("Enter your username:")
        password = input("Enter your password:")
        # 
        # if the username and password are correct
        if (username!="" and password!="") or (username==admin_username and password==""):
            if username==admin_username and password==admin_password:
                print("This is an Admin account")
                menu.adminMenu()
            else:
                i+=1
                continue
        elif username!="" and username!=admin_username and password=="":
            print("This is a User account")
            menu.userMenu(username)
        else:
            print("Wrong input")
            login()

login()
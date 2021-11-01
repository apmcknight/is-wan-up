# 
# Developed by Adam McKnight (@apmcknight) on gh.
# Software is Open Source, all I ask is that
# you make a back-link to my github if you 
# deploy it to production use.
# 
# If you find an issue, please open a Ticket
# PR's will be rejected if .gitignore is removed
# See the CONTRIBUTING.md for more info.
#

import socket

# Defines the Main Function
def main():
    print("\n\n¯\_(ツ)_/¯")
    print("  IS WAN  UP")
    print("Developed by Adam P. McKnight")
    print("Support the project on GitHub: www.github.com/apmcknight/is-wan-up")

    print("\n\nTo begin please make a selection...\n\n")

    options = ["Check for WAN uplink: Type 1 or enter uplink", "Ping an Address: Type 2 or enter pingaddr", "Ping Default Gateway: Type 3 or enter pinggw", "To Stop, type 'stop' or enter 0"]

    for o in options:
        print(o)

    menu_selection = input("\nEnter an Option: ")
    print("\n\n")
    menu(menu_selection)


def menu(menu_selection):
    if(menu_selection == 0 or menu_selection == "Exit" or menu_selection == "exit" or menu_selection == "stop"):
        exit()
    if(menu_selection == 1):
        test_func()


    
# Test Function, for development - will be removed for production use
def test_func():
    print("\n\nThis is a test function\n\n")




# Defines a Function that will ping the gateway to see if there is a WAN uplink
check_duration = 80

def connection_established():
    print("Checks Starting...")
    print("Checking your connection to 1.1.1.1")

    try:
        socket.create_connection(("1.1.1.1", check_duration))
        return True
    except OSError:
        return False


# Calls the main function
if __name__ == "__main__":
    main()

    
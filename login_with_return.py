def user(username):
    if username == "koolk1d":
        return True
    else:
        return False

def pss(password):
    if password == "12345678":
        return True
    else:
        return False

            
def welcome():
    while True:
        username = input("Username: ")
        password = input("Password: ")
        if user(username) and pss(password):
            print("Welcome!")
            break
        else:
            print("Wrong Login")
            continue
welcome()
        
        

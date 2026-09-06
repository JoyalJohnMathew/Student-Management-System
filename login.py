# Login Module

def login(username, password):
    if username == "admin" and password == "1234":
    print("Welcome, Admin!")"

def logout():
    print("Logged out successfully")
if __name__ == "__main__":
    username = input("Enter username: ")
    password = input("Enter password: ")

    print(login(username, password))
# Login Module

def login(username, password):
    if username == "admin" and password == "1234":
        return "Login successful"
    return "Invalid username or password"


if __name__ == "__main__":
    username = input("Enter username: ")
    password = input("Enter password: ")

    print(login(username, password))
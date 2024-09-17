# login.py
def login(username, password):
    rpa.navigate_to("https://example.com/login")
    rpa.type("Username", username)
    rpa.type("Password", password)
    rpa.click("Submit")

# Use-Case
# import login

# def main():
    # ...
    # login("your_username", "your_password")
    # ...

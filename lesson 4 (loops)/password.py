"""
Create a username and password. Make the user input both, and if they fail at either make them restart.
"""

username = "andre-gordon"
password = "supersecure"

while(input("Username: ") != username or input("Password: ") != password):
    print("Incorrect password/username!")

print("Good job logging in!")
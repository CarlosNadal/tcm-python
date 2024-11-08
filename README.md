# Here are the proyects for the python 101 for cybersecurity course from TCM-SEC Academy

### "Remember, the difference between script kiddies and professional hackers is that the former uses other people’s tools." - Charlie Miller

 
1. shh-brute force: A brute-force script that attempts to log in to an SSH server using a list of passwords.
  ﻿﻿﻿A running SSH service you are authorised to test (such as on your localhost) is required to test this script.

  Note that the default Kali SSH configuration will block authentication attempts after 10 attempts (MaxStartups 10:30:10). If you want     to test 100 connections + the valid password using a wordlist, you will need to edit your sshd_config (for example, by setting    MaxStartups 101) and restarting the service. Alternatively to test, use a wordlist with less than 10 invalid passwords.

2. sha256sum cracker: The script is a basic password-cracking tool that uses a dictionary-based approach, comparing each password in a wordlist to the target SHA-256 hash. It utilizes pwn's progress bar and logging system to provide feedback on the cracking process

3. web-login-brute-forcing: A basic scritp for web login brute forcing using a username list, a password list and a  "needle" to check the target response. An authorised web page is required to test this script.

# PasswordEncryption

This repository contains basic password hashing/encryption code that served as the basis of my Flask server that incorporated password encryption.

## Getting started: 
Run hash_password.py in a command line window. You will get a prompt to enter a password. Once you have typed in your desired password, hit enter.

Note: You must have Hashlib installed for this to work. It comes pre-installed with Python, but can also be downloaded using pip.

You will see thata this has created a file called pwdhash.txt. If it has not, the program did not work successfully.

Once you have entered a password and have hit enter, close the Python file. Open pwdhash.txt, and you should see a long string of letters and numbers. If you have done this, your password has been successfully entered.

Close pwdhash.txt, and run check_password.py in a terminal window. You will be prompted to enter a password.

Enter the password you have previously entered in hash_password.py. If you receive a message saying 'Welcome!', you have successfully entered your password. If you have made a spelling mistake, it will inform you that your password is incorrect.

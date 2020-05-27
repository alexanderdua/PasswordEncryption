# PasswordEncryption

This repository contains basic password hashing/encryption code that served as the basis of my Flask server that incorporated password encryption.

To run this program, first open pwdhash.txt in the text editor of your choice. Confirm that the document is blank. If there is anything on the document, please delete it and save the file. Most likely, there will be a single space (' ') at the beginnig of the file which should be deleted.

Once this is done, ensure that the two Python files are in the same directory as the text file.

Once all the files are in the same directory and there is nothing on the pwdhash.txt file, run hash_password.py in a command line window. You will get a prompt to enter a password. Once you have typed in your desired password, hit enter.

Note: You must have Hashlib installed for this to work. It comes pre-installed with Python, but can also be downloaded using pip.

Once you have entered a password and have hit enter, close the Python file. Return to pwdhash.txt, and you should see a long string of letters and numbers. If you have done this, your password has been successfully entered.

Once again, close pwdhash.txt, and run check_password.py in a terminal window. You will be prompted to enter a password.

Enter the password you have previously entered in hash_password.py. If you receive a message saying 'Welcome!', you have successfully entered your password. If you have made a spelling mistake, it will inform you that your password is incorrect.

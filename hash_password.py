import hashlib


def main():
    # Get the password from the command line.
    password = input("Enter a password: ")

    # Calculate the SHA-256 hash of the password
    password_bin = password.encode()
    password_hash = hashlib.sha256(password_bin).hexdigest()

    # Write the password hash to a file
    with open("pwdhash.txt", "w") as outfile:
        outfile.write(password_hash)


if __name__ == "__main__":
    main()

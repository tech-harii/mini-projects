import csv

FILE_NAME = "_passwords_.csv"
KEY = 3  # encryption shift value || PLANNING TO CHANGE IT SO THAT THE USER CAN HAVE A 'CUSTOM-KEY' IN THE FUTURE :) 

# ENCRYPTION FUNCTION
def encrypt(text):
    encrypted = ""
    for char in text:
        encrypted += chr(ord(char) + KEY)
    return encrypted

def decrypt(text):
    decrypted = ""
    for char in text:
        decrypted += chr(ord(char) - KEY)
    return decrypted

#  ADD PASSWORD FUNCTIOn
def add_password():
    platform = input("Enter platform/account name: ")
    password = input("Enter password: ")

    encrypted_password = encrypt(password)

    with open(FILE_NAME, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([platform, encrypted_password])

    print("Password stored successfully!")

# PASSWORD VIEW FUNCTION
def view_passwords():
    try:
        with open(FILE_NAME, "r") as file:
            reader = csv.reader(file)
            print("\nStored Passwords:")
            for row in reader:
                platform, encrypted_password = row
                print(platform, "-->", decrypt(encrypted_password))
    except FileNotFoundError:
        print("No passwords saved yet.")

# PASSWORD UPDATE FUNCTION
def update_password():
    try:
        updated_data = []
        found = False

        with open(FILE_NAME, "r") as file:
            reader = csv.reader(file)
            for row in reader:
                platform, encrypted_password = row
                if platform == input_platform:
                    new_password = input("Enter new password: ")
                    encrypted_password = encrypt(new_password)
                    found = True
                updated_data.append([platform, encrypted_password])

        if found:
            with open(FILE_NAME, "w", newline="") as file:
                writer = csv.writer(file)
                writer.writerows(updated_data)
            print("Password updated successfully!")
        else:
            print("Platform not found.")

    except FileNotFoundError:
        print("No passwords to update.")

# MAIN MENU 
def main():
    while True:
        print("\n--- Simple Password Manager ---")
        print("1. Add Password")
        print("2. View Passwords")
        print("3. Update Password")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_password()
        elif choice == "2":
            view_passwords()
        elif choice == "3":
            global input_platform
            input_platform = input("Enter platform name to update: ")
            update_password()
        elif choice == "4":
            print("Program Quit")
            break
        else:
            print("Invalid choice!")

main()

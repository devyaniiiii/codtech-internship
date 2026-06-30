passwords = {}

while True:
    print("\nPassword Manager")
    print("1. Add Password")
    print("2. View Passwords")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        account = input("Enter account name: ")
        password = input("Enter password: ")
        passwords[account] = password
        print("Password saved!")

    elif choice == "2":
        if passwords:
            for account, password in passwords.items():
                print(f"{account}: {password}")
        else:
            print("No passwords stored.")

    elif choice == "3":
        print("Exiting...")
        break

    else:
        print("Invalid choice!")

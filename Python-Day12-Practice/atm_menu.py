balance = 5000 

while True:
    print("\n===== ATM Menu =====")
    print("1. check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        print("Your balance is:, balance")

    elif choice == "2":
        amount = int(input("Enter withdrawl amount: "))

        if amount <= balance:
            balance = balance - amount
            print("Amount withdraw successfully")
            print("New balance:", balance)
        else:
            print("Insufficient balance")

    elif choice == "4":
        print("Thank you for using ATM")
        break

    else:
        print("Invalid choice")
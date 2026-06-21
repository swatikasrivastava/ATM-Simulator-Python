balance = 10000
pin = "1234"
entered_pin = input("Enter your pin:")
if entered_pin == pin:
    while True:
        print("\n===== ATM Menu =====")
        print("1. Check Balance")
        print("2. Withdraw Money")
        print("3. Deposit Money")
        print("4. Exit")
        choice = input("Enter your choice:")
        if choice == "1":
            print("Your balance is:",balance)
        elif choice == "2":
                amount = float(input("enter amount to deposit:"))
                balance += amount
                print("Amount deposited successfully!")
                print("updated balance:",balance)
        elif choice == "3":
            amount = float(input("enter amount to withdraw:"))
            if amount <= balance:
                balance -= amount
                print("please collect your cash.")
                print("Remaining Balance:",balance)
            else:            
                print("insufficient balance!")
        elif choice == "4":
            print("Thank you for using the ATM.")
            break
        else:
            print("Invalid choice! Please try again.")
    else:
        print("Incorrect pin! Access denied.")



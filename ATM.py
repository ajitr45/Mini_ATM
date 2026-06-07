def check_balance(balance):
    print(f"\nCurrent Balance: ₹{balance}")

def deposit(balance):
    amount = float(input("Enter amount to deposit: ₹"))
    balance += amount
    print(f"₹{amount} deposited successfully.")
    return balance

def withdraw(balance):
    amount = float(input("Enter amount to withdraw: ₹"))

    if amount > balance:
        print("Insufficient Balance!")
    else:
        balance -= amount
        print(f"₹{amount} withdrawn successfully.")

    return balance


# Initial Data
correct_pin = "1234"
balance = 5000

# Login
pin = input("Enter ATM PIN: ")

if pin == correct_pin:
    print("\nLogin Successful!")

    while True:
        print("\n===== ATM MENU =====")
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            check_balance(balance)

        elif choice == "2":
            balance = deposit(balance)

        elif choice == "3":
            balance = withdraw(balance)

        elif choice == "4":
            print("Thank you for using ATM!, Visit again..")
            break

        else:
            print("Invalid Choice!")

else:
    print("Incorrect PIN!")
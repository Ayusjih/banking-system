
import os

# Configuration: File to store the balance
BALANCE_FILE = "account.txt"

def load_balance():
    """
    Loads the balance from the file.
    If the file does not exist, it initializes it with 0.0.
    """
    if not os.path.exists(BALANCE_FILE):
        return 0.0
    
    try:
        with open(BALANCE_FILE, "r") as file:
            data = file.read().strip()
            # Handle empty file case
            if not data:
                return 0.0
            return float(data)
    except ValueError:
        print("Error: Corrupted balance file. Resetting to 0.0")
        return 0.0

def save_balance(balance):
    """
    Saves the current balance to the file.
    This ensures data persists after the program closes.
    """
    try:
        with open(BALANCE_FILE, "w") as file:
            file.write(str(balance))
    except IOError:
        print("Error: Could not save data to file.")

def deposit(current_balance):
    """
    Handles the deposit logic.
    Validates that the amount is positive.
    """
    try:
        amount = float(input("Enter amount to deposit: "))
        if amount <= 0:
            print("❌ Amount must be positive!")
            return current_balance
        
        new_balance = current_balance + amount
        save_balance(new_balance)
        print(f"✅ Successfully deposited ${amount:.2f}")
        return new_balance
    except ValueError:
        print("❌ Invalid input! Please enter a number.")
        return current_balance

def withdraw(current_balance):
    """
    Handles the withdrawal logic.
    Checks for sufficient funds and positive amounts.
    """
    try:
        amount = float(input("Enter amount to withdraw: "))
        if amount <= 0:
            print("❌ Amount must be positive!")
            return current_balance
        
        if amount > current_balance:
            print("❌ Insufficient funds! Transaction cancelled.")
            return current_balance
        
        new_balance = current_balance - amount
        save_balance(new_balance)
        print(f"✅ Successfully withdrew ${amount:.2f}")
        return new_balance
    except ValueError:
        print("❌ Invalid input! Please enter a number.")
        return current_balance

def check_balance(current_balance):
    """
    Displays the current available balance.
    """
    print(f"\n💰 Current Balance: ${current_balance:.2f}")

def main():
    """
    Main program loop matching the Flowchart logic.
    """
    print("--- 🏦 Welcome to the Banking System ---")
    balance = load_balance()
    
    while True:
        print("\nChoose an option:")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Check Balance")
        print("4. Exit")
        
        choice = input("Enter your choice (1-4): ")
        
        if choice == '1':
            balance = deposit(balance)
        elif choice == '2':
            balance = withdraw(balance)
        elif choice == '3':
            check_balance(balance)
        elif choice == '4':
            print("👋 Thank you for banking with us. Goodbye!")
            break
        else:
            print("❌ Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

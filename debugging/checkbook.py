#!/usr/bin/python3
class Checkbook:
    def __init__(self):
        self.balance = 0.0
    
    def validate_amount(self, amount):
        """Validate that the amount is a positive number."""
        if not isinstance(amount, (int, float)):
            raise ValueError("Amount must be a number")
        if amount <= 0:
            raise ValueError("Amount must be positive")
        return float(amount)
    
    def deposit(self, amount):
        try:
            validated_amount = self.validate_amount(amount)
            self.balance += validated_amount
            print("Deposited ${:.2f}".format(validated_amount))
            print("Current Balance: ${:.2f}".format(self.balance))
        except ValueError as e:
            print(f"Error: {e}")
    
    def withdraw(self, amount):
        try:
            validated_amount = self.validate_amount(amount)
            if validated_amount > self.balance:
                print("Insufficient funds to complete the withdrawal.")
            else:
                self.balance -= validated_amount
                print("Withdrew ${:.2f}".format(validated_amount))
                print("Current Balance: ${:.2f}".format(self.balance))
        except ValueError as e:
            print(f"Error: {e}")
    
    def get_balance(self):
        print("Current Balance: ${:.2f}".format(self.balance))

def get_float_input(prompt):
    """Helper function to get and validate float input."""
    while True:
        try:
            value = input(prompt)
            return float(value)
        except ValueError:
            print("Error: Please enter a valid number")

def main():
    cb = Checkbook()
    while True:
        try:
            action = input("What would you like to do? (deposit, withdraw, balance, exit): ").lower().strip()
            
            if action == 'exit':
                print("Thank you for using Checkbook. Goodbye!")
                break
            elif action == 'deposit':
                amount = get_float_input("Enter the amount to deposit: $")
                cb.deposit(amount)
            elif action == 'withdraw':
                amount = get_float_input("Enter the amount to withdraw: $")
                cb.withdraw(amount)
            elif action == 'balance':
                cb.get_balance()
            else:
                print("Invalid command. Please try again.")
        except KeyboardInterrupt:
            print("\nProgram terminated by user.")
            break
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            print("Please try again.")

if __name__ == "__main__":
    main()

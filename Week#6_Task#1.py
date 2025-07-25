import time

def measure_time(func):
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter()
        print(f"⏱️ {func.__name__} executed in {end - start:.6f} seconds")
        return result
    return wrapper

class Bank:
    def __init__(self, account_number, balance, owner_name):
        self.account_number = account_number
        self.balance = balance
        self.owner_name = owner_name

    @measure_time
    def withdraw(self, amount):
        if amount > self.balance:
            print(f"Cannot withdraw {amount}Rs. Insufficient balance. Current balance: {self.balance}Rs") 
        else:
            self.balance -= amount
            print(f"Withdrew {amount}Rs. New balance: {self.balance}Rs")
            
    @measure_time
    def deposit(self, amount):
        if amount < 0:
            print(f"Cannot deposit negative amount. Current balance: {self.balance}Rs") 
        else:
            self.balance += amount
            print(f"Deposited {amount}Rs. New balance: {self.balance}Rs")
            
    @measure_time
    def transfer(self, target_account, amount):
        if amount > self.balance:
            print(f"Transfer failed. Insufficient balance. Current: {self.balance}Rs")
        elif amount < 0:
            print("Cannot transfer negative amount")
        else:
            self.balance -= amount
            target_account.balance += amount
            print(f"Transferred {amount}Rs to {target_account.owner_name}'s account")
            print(f"Your new balance: {self.balance}Rs")
    
    @measure_time
    def display_balance(self):
        print(f"Account {self.account_number} ({self.owner_name}) balance: {self.balance}Rs")


def main():
    # Create accounts
    ahmed_account = Bank("123ABF23", 5000, "Salaman Ahmed")
    khan_account = Bank("ACC789012", 2500, "Umer Khan")
    
    # Display initial balances
    ahmed_account.display_balance()
    khan_account.display_balance()
    
    print("\nTransactions:")
    
    print("\nSalaman Ahmed deposits 1500Rs:")
    ahmed_account.deposit(1500)
    
    print("\nUmer Khan withdraws 800Rs:")
    khan_account.withdraw(800)
    
    print("\nSalaman Ahmed transfers 2000Rs to Umer Khan:")
    ahmed_account.transfer(khan_account, 2000)
    
    # Invalid transactions
    print("\nAttempt invalid transactions:")
    ahmed_account.withdraw(10000)  # Should fail
    khan_account.deposit(-500)     # Should fail
    ahmed_account.transfer(khan_account, -100)  # Should fail
    
    # Final balances
    print("\n--- Final Balances ---")
    ahmed_account.display_balance()
    khan_account.display_balance()


if __name__ == "__main__":
    main()
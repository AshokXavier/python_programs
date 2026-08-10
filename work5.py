
accounts = {}
transactions = []
bank_balance = 0


def create_account(name, acc_no, balance, acc_type="Savings"):
    """Create a new bank account."""
    global bank_balance
    accounts[acc_no] = {"name": name, "type": acc_type, "balance": balance}
    bank_balance += balance
    return "Account created successfully"


def deposit(balance, amount):
    """Add amount to balance."""
    global bank_balance
    bank_balance += amount
    return balance + amount


def withdraw(balance, amount):
    """Withdraw amount if balance is sufficient."""
    global bank_balance
    if amount <= balance:
        bank_balance -= amount
        return balance - amount, "Withdrawal successful"
    return balance, "Insufficient balance"


def check_balance(balance):
    """Return current balance."""
    return balance


def transaction_history(*items):
    """Display transaction history using *args."""
    for item in items:
        print(item)
    return items


def customer_details(**data):
    """Display customer details using **kwargs."""
    for key, value in data.items():
        print(key, ":", value)


def loan_eligibility(balance, income=25000):
    """Check loan eligibility."""
    if balance >= 10000 and income >= 20000:
        return "Eligible for Loan"
    return "Not Eligible for Loan"


def print_balance(balance):
    print("Balance:", balance)


def return_balance(balance):
    return balance


def display_message():
    print("Welcome to Online Banking")
    

def scope_demo():
    x = "Local"

    def inner():
        nonlocal x
        x = "Enclosing"
        print("Enclosing:", x)

    inner()


def legb_demo():
    x = "Global"

    def test():
        x = "Local"
        print("LEGB Local:", x)

    test()


interest = lambda amount: amount * 0.05
gst = lambda amount: amount * 0.18


def functional_demo():
    balances = [10000, 15000, 20000, 25000]
    names = ["Sneha", "Anu", "Rahul"]

    print("\nInterest:", list(map(interest, balances)))
    print("Balance > 10000:", list(filter(lambda x: x > 10000, balances)))
    print("Sorted Names:", sorted(names))

    print("GST on 5000:", gst(5000))
    print("Total:", sum(balances))
    print("Maximum:", max(balances))
    print("Minimum:", min(balances))
    print("Number:", len(balances))
    print("Average:", round(sum(balances) / len(balances), 2))


def compound_interest(amount, rate, years):
    if years == 0:
        return amount
    return compound_interest(amount * (1 + rate), rate, years - 1)


def pin_verify(pin, attempt=1):
    print("PIN Verification Attempt:", attempt)
    if attempt == 3:
        print("Maximum Attempts Reached")
        return
    return pin_verify(pin, attempt + 1)


def main():

    while True:
        print("\n------ ONLINE BANKING SYSTEM ------")
        print("1. Create Account")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Check Balance")
        print("5. Transaction History")
        print("6. Loan Eligibility")
        print("7. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            name = input("Enter Name: ")
            acc_no = input("Enter Account Number: ")
            balance = float(input("Enter Initial Balance: "))
            acc_type = input("Account Type (Enter for Savings): ")

            if acc_type:
                print(create_account(name, acc_no, balance, acc_type))
            else:
                print(create_account(name, acc_no, balance))

            customer_details(name=name, account_no=acc_no,
                             account_type=accounts[acc_no]["type"])

        elif choice == 2:
            acc_no = input("Enter Account Number: ")

            if acc_no in accounts:
                amount = float(input("Enter Deposit Amount: "))
                old = accounts[acc_no]["balance"]

                new = deposit(old, amount)
                accounts[acc_no]["balance"] = new
                transactions.append(f"Deposited: {amount}")

                print("Amount Deposited Successfully")
                print("Updated Balance:", new)
                print("Interest:", interest(new))

            else:
                print("Account not found")

        elif choice == 3:
            acc_no = input("Enter Account Number: ")

            if acc_no in accounts:
                amount = float(input("Enter Withdrawal Amount: "))
                old = accounts[acc_no]["balance"]

                new, status = withdraw(old, amount)
                accounts[acc_no]["balance"] = new

                if status == "Withdrawal successful":
                    transactions.append(f"Withdrawn: {amount}")

                print(status)
                print("Updated Balance:", new)

            else:
                print("Account not found")

        elif choice == 4:
            acc_no = input("Enter Account Number: ")

            if acc_no in accounts:
                print("Balance:",
                      check_balance(accounts[acc_no]["balance"]))
            else:
                print("Account not found")

        elif choice == 5:
            transaction_history(*transactions)

        elif choice == 6:
            acc_no = input("Enter Account Number: ")

            if acc_no in accounts:
                income = float(input("Enter Monthly Income: "))
                balance = accounts[acc_no]["balance"]

                print(loan_eligibility(balance, income))
            else:
                print("Account not found")

        elif choice == 7:
            print("\n--- Function Demonstrations ---")

            functional_demo()

            print("\nPrint vs Return:")
            print_balance(5000)
            result = return_balance(5000)
            print("Returned:", result)

            print("\nNone Return:")
            result = display_message()
            print("Return value:", result)

            scope_demo()
            legb_demo()

            print("\nCompound Interest:",
                  round(compound_interest(10000, 0.05, 3), 2))

            print("\nRecursive PIN:")
            pin_verify(1234)

            print("\nThank you!")
            break

        else:
            print("Invalid choice")


main()
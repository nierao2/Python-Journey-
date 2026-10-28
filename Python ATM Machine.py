print("----------Welcome to Python ATM Machine---------")
balance = 1000
pin = 9852
transaction_history = []

for pinattempts in range(3):
    enter_pin = int(input("enter your 4 digit atm pin: "))
    if enter_pin == pin:
        print("Login Successful")
        break
    else:
        print("invalid pin")
else:
    print("Too many wrong attempts, account locked")
    exit()


def balance_check():
    print(f"your current balance is: {balance}")


def deposit():
    global balance
    deposit_amount = int(input("enter your amount: "))
    balance += deposit_amount
    transaction_history.append(f"{deposit_amount} is succefully deposited")
    print(f"Your Updated Balance is: {balance}")


def withdrawl():
    global balance
    withdrawl_amount = int(input("enter withdrawl amount: "))
    if withdrawl_amount <= balance:
        balance -= withdrawl_amount
        transaction_history.append(f"{withdrawl_amount} is succefully withdrawn")
        print(f"Your Updated Balance is: {balance}")
    else:
        print("Insufficient funds")


def transactions():
    if not transaction_history:
        print("No transactions made yet")
    else:
        print(transaction_history)


while True:
    print("--------Select your choice-------")
    print("--------Select 1 for balance_enquiry------")
    print("--------Select 2 for deposit------")
    print("--------Select 3 for withdrawl------")
    print("--------Select 4 for transaction_history------")
    print("--------Select 5 for exit------")

    enter_your_choice = int(input("enter your choice:"))
    if enter_your_choice == 1:
        balance_check()
    elif enter_your_choice == 2:
        deposit()
    elif enter_your_choice == 3:
        withdrawl()
    elif enter_your_choice == 4:
        transactions()
    elif enter_your_choice == 5:
        print("Thank you for using Python ATM Machine")
        break
    else:
        print("Invalid option, try again")
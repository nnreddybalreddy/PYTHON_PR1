class InsufficientFundError(Exception):
    pass 

def withdraw(balance,amount):
    if amount > balance:
        raise InsufficientFundError("Not enough funds")

    return balance-amount 


balance=5000
amount=int(input("Enter amount:::"))

try:
    balance=withdraw(balance,amount)
    print("Withdraw successfull;;;")
    print("Remain balance",balance)
except InsufficientFundError as e:
    print(e)    
amount=eval(input("Enter the amount: "))

if amount < 1000:
    total = amount - (amount * 0.1)
elif amount >=1000 and amount < 5000:
    total = amount - (amount * 0.15)
elif amount >= 5000 and amount < 10000:
    total = amount - (amount * 0.2)
else:
    total = amount - (amount * 0.25)

print("Total amount after discount is:", total)

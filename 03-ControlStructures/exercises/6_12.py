nb = int(input("Number of products purchased: "))
price = int(input("Product price: "))
amount = 0
if nb > 2:
    amount = (2*price)+((nb-2)*(price*0.75))
else:
    amount = price * nb
print(f'Amount to pay: {amount}')
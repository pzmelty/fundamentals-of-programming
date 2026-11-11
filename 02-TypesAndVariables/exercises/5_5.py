price = float(input("Wpisz kwotę:"))
discount = int(input("Wpisz procent zniżki:")) /100
f_price = price - (price * discount)
reduction = (price * discount)
print(f"Price with discount: {f_price:.2f}")
print(f"Reduction: {reduction:.2f}")

amount = int(input('Enter the amount in PLN: '))

coins_5 = amount // 5 #dzielenie z zaokrągleniem
amount = amount % 5 #reszta z dzielenia

coins_2 = amount // 2
amount = amount % 2

coins_1 = amount // 1

print(f'The amount of PLN in coins:')
print(f'5 PLN coins: {coins_5}')
print(f'2 PLN coins: {coins_2}')
print(f'1 PLN coins: {coins_1}')

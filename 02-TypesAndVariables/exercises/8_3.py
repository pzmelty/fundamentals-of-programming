###
# A program that reads temperature in degrees Celsius from the keyboard.
# Use comments to briefly describe the program's algorithm.

#Zczytaj temperaturę w stopniach Celsjusza z klawiatury
temp = float(input('Podaj temperaturę w stopniach Celsjusza: '))
temp_k = temp + 273.15
temp_f = (temp * 9/5) + 32
print(f'Temperatura w stopniach Kelvina: {temp_k}')
print(f'Temperatura w stopniach Fahrenheita: {temp_f}')
h = int(input("Number of hours: "))
if h > 0 and h < 3:
    print ("Pay 5 PLN")
elif h >= 3 and h < 7:
    print ("Pay 15 PLN")
else:
    print("Pay 20 PLN")
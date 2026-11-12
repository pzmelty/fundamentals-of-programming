pin = '0805'

for i in range(1,4):
    t = input('Enter the Pin code: ')
    if t != pin:
        q= False
        print("Incorrect...")
    else:
        q = True
        print("PIN correct")
        break
if q == False:
    print("Sorry, your payment card has been blocked.")
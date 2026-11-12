ean = input("Enter EAN-13 article number: ")
if len(ean) == 13:
    print('Artice number is correct')
    if ean[0:3] == "590":
        print('Article manufactured in Poland')
    else:
        print("Article wasn't manufactured in Poland")
else:
    print('Article number is incorrect.')
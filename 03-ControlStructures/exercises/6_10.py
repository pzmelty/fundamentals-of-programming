age = int(input("Enter dog age in human years: "))
dog_age = 0
if age < 3 and age >= 0:
    dog_age = age * 10.5
    print(f"The dog's age in dog years is: {dog_age}")
elif age >= 3:
    dog_age = 21 + (age - 2) * 4
    print(f"The dog's age in dog years is: {dog_age}")
else:
    print("Invalid age entered.")
#for i in range(6,-1,-3):    #pętla zmniejsza się o 3
 #   for j in range(1,4):    #przyjmuje wartości 1, 2, 3
  #      print(f'{i+j}',end=' ') #dodaje wartości obu zmiennych
   # print()

i = 6
while i >= 0:
    j = 1
    while j < 4:
        print(f'{i+j}', end= ' ')
        j += 1
    i-=3
    print()
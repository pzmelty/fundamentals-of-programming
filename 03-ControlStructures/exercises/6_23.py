nb = int(input('Enter number: '))
sm = 0
for i in range(1,11):
    sm = nb * i
    print(f'{nb} x {i} = {sm}')
    i += 1
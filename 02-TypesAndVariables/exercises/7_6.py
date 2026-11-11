speed = int(input('Enter speed in km/h: '))
is_over_limit = speed >= 40 and speed <= 140
print(f'speed is over limit: {is_over_limit}')
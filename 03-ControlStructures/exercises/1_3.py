###
# Checking whether a car exceeded the speed limit
#
speed_limit = 140
car_speed = int( input('Enter car speed (km/h): ') )

if car_speed <=140:
    print(f'Your speed is {car_speed} km/h, good job!')
else:
    print(f'Warning: Your speed is {car_speed} km/h, speed limit exceeded!!')
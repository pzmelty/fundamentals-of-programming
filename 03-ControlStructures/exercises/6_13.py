car_speed = int(input("Enter car speed: "))
speed_limit_max = 140
speed_limit_min = 40
if car_speed > 140 or car_speed < 40:
    print("Invalid car spped.")
else:
    print("All good.")
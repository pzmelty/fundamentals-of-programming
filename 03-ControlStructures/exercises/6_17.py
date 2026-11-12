time = input('Enter time (24-hour format): ')
hour = time[0:2]
if hour == '13':
    hour = '1'
elif hour == '14':
    hour = '2'
elif hour == '15':
    hour = '3'
elif hour == '16':
    hour = '4'
elif hour == '17':
    hour = '5'
elif hour == '18':
    hour = '6'
elif hour == '19':
    hour = '7'
elif hour == '20':
    hour = '8'
elif hour == '21':
    hour = '9'
elif hour == '22':
    hour = '10'
elif hour == '23':
    hour = '11'
elif hour == '00':
    hour = '12'

if int(time[0:2]) < 12:
    period = 'am'
else:
    period = 'pm'

print(f'Time in 12-hour format: {hour + time[2:]} {period}') #hour - godzina, time[2:] - minuty
    
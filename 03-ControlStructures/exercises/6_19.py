computer_science = input('Are you interested in computer science? (y/n): ')
computer_games = input('Do you like playing computer games? (y/n): ')
instagram = input('Do you have an Instagram account? (y/n): ')

computer_science = computer_science == 'y'
computer_games = computer_games == 'y'
instagram = instagram == 'y'

print('\nSURVEY RESULTS')
print(f'Interested in computer science: {"Yes" if computer_science else "No"}')
print(f'Playing computer games: {"Yes" if computer_games else "No"}')
print(f'Has an Instagram account: {"Yes" if instagram else "No"}')
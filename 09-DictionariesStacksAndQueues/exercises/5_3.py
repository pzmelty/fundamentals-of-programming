translations = {
    'computer': 'komputer',
    'mouse': 'myszka',
    'keyboard': 'klawiatura',
    'printer': 'drukarka'
}

word = input("Enter a word in English: ")

if word in translations:
    print("Translation:", translations[word])
else:
    print("Translation is not available.")
import MyText

text = "An apple a day keeps the doctor away"

print("Text:", text)

print("Number of words:", MyText.word_count(text))

longest = MyText.longest_words(text)
print("Words from the longest:", ",".join(longest))

alphabetical = MyText.alphabetical_words(text)
print("Words ordered alphabetically:", ",".join(alphabetical))
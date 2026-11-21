# Returns the number of words in text
def word_count(text):
    words = text.split()
    return len(words)


# Returns words ordered from longest to shortest
def longest_words(text):
    words = text.split()
    return sorted(words, key=len, reverse=True)


# Returns words ordered alphabetically
def alphabetical_words(text):
    words = text.split()
    return sorted(words, key=str.lower)
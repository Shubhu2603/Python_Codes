#Highlight given word in a sentence
def highlight_word(sentence, word):
    if word in sentence:
        wordn=word.upper()
    return sentence.replace(word,wordn)
print(highlight_word("Have a nice day", "nice"))
print(highlight_word("Shhh, don't be so loud!", "loud"))
print(highlight_word("Automating with Python is fun", "fun"))
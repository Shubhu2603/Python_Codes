#Convert String to pig latin
def pig_latin(text):
    lis=[]
    say = " "
    # Separate the text into words
    words = text.split()
    for word in words:
        # Create the pig latin word and add it to the list
        w=word[0]
        pqr = word.replace(w, "")
        abc=pqr+w+"ay"

        lis.append(abc)
        # Turn the list back into a phrase
    return say.join(lis)


print(pig_latin("hello how are you"))  # Should be "ellohay owhay reaay ouyay"
print(pig_latin("programming in python is fun"))  # Should be "rogrammingpay niay ythonpay siay unfay"
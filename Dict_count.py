#Print number of times a word appears in a string
str="Hello Hello Hi Hi"
arr=str.split()
dict={}
for word in arr:
    if word.isalpha():
        if word not in dict:
            dict[word]=1
        else:
            dict[word]+=1


print(dict)
#Open a file and count the number of occurrences of each word in a file and store it in a dictionary
dict1={}
with open('D:\Coursera\pg37924.txt','r') as file:
    for line in file:
        for word in line.split():
            if word in dict1:
                dict1[word]=1
            else:
                dict1[word]+=1

print(dict1)
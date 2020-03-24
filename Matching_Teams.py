#Implementation of for loop for pairing teams against each other in a tournament
teams =['a','b','c','d']
for home in teams:
    for away in teams:
        if home!=away:
            print(home+" vs " + away)
    print()
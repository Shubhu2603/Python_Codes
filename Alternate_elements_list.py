#Print alternate elements of list
def skip_elements(elements):
	lis=[]
	for i in range(len(elements)):
		if i%2==0:
			lis.append(elements[i])
	return lis

print(skip_elements(["a", "b", "c", "d", "e", "f", "g"])) # Should be ['a', 'c', 'e', 'g']
print(skip_elements(['Orange', 'Pineapple', 'Strawberry', 'Kiwi', 'Peach'])) # Should be ['Orange', 'Strawberry', 'Peach']
print(skip_elements([])) # Should be []
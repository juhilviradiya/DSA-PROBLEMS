#Find All Occurrences

numbers = [10, 20, 30, 20, 40, 20]
target = 20
found = False
for ind in range(len(numbers)):
    if target == numbers[ind]:
        print(ind)
        found = True
        
if found == False:
    print(-1)

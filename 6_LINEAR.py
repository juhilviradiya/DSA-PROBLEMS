# to find the first negative occurance in list 

numbers = [15, 21, 33, 42, 56, 18, 70]
for ind in range(len(numbers)):
    if numbers<numbers[ind]:
        print(ind)
        break
else:
    print(-1)

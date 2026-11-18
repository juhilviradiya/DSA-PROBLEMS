# to find first even occurance 
numbers = [15, 21, 33, 42, 56, 18, 70]
for ind in range(len(numbers)):
    if numbers[ind] % 2 == 0:
        print(ind)
        break
else:
    print(-1)

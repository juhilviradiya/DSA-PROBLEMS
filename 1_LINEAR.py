number = [10,20,30,40,50]
target = 30
for ind in range(len(number)):
    if target == number[ind]:
        print(ind)
        break
else:
    print(-1)

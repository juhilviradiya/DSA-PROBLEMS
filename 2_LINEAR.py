#Search for 60 in the given list. If the element is not present, print "Element Not Found".

number = [10,20,30,40,50]
target = 60
for ind in range(len(number)):
    if target == number[ind]:
        print(ind)
        break
else:
    print('Element Not Found')
        


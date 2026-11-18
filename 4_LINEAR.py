# find the target occurance first index and last index.
numbers = [10, 20, 30, 20, 40, 20]
target = 20

first = -1
last = -1
for ind in range(len(numbers)):
      if target == numbers[ind]:
         if first == -1:
             first = ind

         last = ind
print("First Position:", first)
print("Last Position:", last)

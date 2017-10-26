#using slice() with comprehension list and looping
numbers = [number+1 for number in range(1,11)]
print(numbers[2:5])

###############################################

#looping slice
numbers = [number+1 for number in range(1,11)]

#here are the numbers I will pick
for number in numbers[0:4]:
    print(number)


#statistics of million numbers
millions = []
for number in range(1,1000000):
    millions.append(number)

print(min(millions))
print(max(millions))
print(sum(millions))

############################

#three argument range() to make list of odd numbers
for number in range(1,10,2):
    print(number)

############################

#comprehension list to write cubes from 1-10
cubes = [number**3 for number in range(1,11)]
print(cubes)

############################

#statistics on comprehension list
aliens = [number*2 for number in range(1,11)]
print("Max: "+str(max(aliens)))
print("Min: "+str(min(aliens)))
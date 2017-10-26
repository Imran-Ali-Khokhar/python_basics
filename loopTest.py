#prinitng seasons using loop
seasons = ['winter', 'summer', 'autumn', 'spring']
for season in seasons:
    print("Welcome season "+season)
    print("bye season "+season)

print("Bye All")

############################

#square of numbers 1-10
for number in range(1,11):
    print(number**2)

############################

#alternate way to make number's array - shortcut way
numbers = [number**2 for number in range(1,11)]
print(numbers)

############################


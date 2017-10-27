#Simple if condition
cars = ['audi', 'bmw', 'toyota', 'suzuki']

for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())


#checking existance of item using 'in'
vehicle = 'bmw'
if vehicle in cars:
    print(vehicle+" is available")
else:
    print(vehicle+" is not available")

#checking unavailability in list by using 'not in'
vehicle = 'mercedez'
if vehicle not in cars:
    print(vehicle+" is not available")
else:
    print("availble "+vehicle)

#using if and loops  with lists
current_users = ['admin', 'imran', 'kashif']
new_users = ['sabih', 'salman', 'kashif', 'aslam']

for new_user in new_users:
    if new_user in current_users:
        print(new_user+" is already in list")
    else:
        print(new_user+" is a new user")

names = ['Kashif', 'Sabih', 'Salman', 'Imran']
print(names)

#modifying last index
names[3] = 'Abid'
print(names)

#adding value in last
names.append('Imran')
print(names)

#insertion in list
names.insert(0, 'Jalil')
print(names)

#deletion in list using del command
del names[0]
print(names)

#deletion in list using pop() method. it removes given item from list and retained that removed item in variable for future use.
popped_names = names.pop(0)
print(names)
print(popped_names)
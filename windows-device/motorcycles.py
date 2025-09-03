motorcycles =['honda', 'yamaha','suzuki']
print(motorcycles)

# modifying the element of list
motorcycles[2] = 'ducati'
print(motorcycles)

# adding a new element to out list
motorcycles.append('suzuki')
print(motorcycles)

# adding new elements dynamically using append
motorcycles =[]
motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')

# adding an element at any position using insert
motorcycles =['honda', 'yamaha','suzuki']
motorcycles.insert(0,'ducati')

# removing elements from list
motorcycles = ['honda', 'yamaha', 'suzuki']
del motorcycles[0]
print(motorcycles)

# without deleting data when can pop it out as below example
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

popped_motorcycles = motorcycles.pop() # poped the last element from the list (last element of the list)
print(motorcycles)
print(popped_motorcycles)

# poping any element from the list using index
motorcycles = ['honda', 'yamaha', 'suzuki']
print('The first motorcyles i owned was a '+motorcycles.pop(0)+".")
print(motorcycles)

# poping any elements from the list using value
motorcycles = ['honda', 'ducati', 'yamaha', 'suzuki']
print(motorcycles)
motorcycles.remove('ducati')
print(motorcycles)
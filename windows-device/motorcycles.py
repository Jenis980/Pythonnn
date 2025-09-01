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
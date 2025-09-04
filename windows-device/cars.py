cars = ['bmw', 'audi', 'toyota', 'tesla']
cars.sort() # sorts the list permanently in alphabetical order. PERMANENTLY means that the original list is changed and cannot be reverted back to its original order.
print(cars)
cars.sort(reverse=True) # sorts the list permanently in reverse alphabetical order.
print(cars)

# to sort a list temporarily without changing the original order, use the sorted() function
cars = ['Tesla', 'Bmw', 'Audi', 'Toyota']
print("Here is the original list: ")
print(cars)
print("\nHere is the sorted list: ")
print(sorted(cars)) # sorts the list temporarily in alphabetical order.
print("\nHere is the original list again: ")
print(cars)

# to sort the list in reverse order without changing the list alphabetically.
cars = ['Tesla', 'Bmw', 'Audi', 'Toyota']
print('here is the original list')
print(cars)
print('\nhere is the reversed list')
print(cars.reverse()) # prints the output 'None' because the reverse() method does not return any value. It only changes the order of the list permanently.
print(cars) # prints the reversed list permanently.
print(len(cars))
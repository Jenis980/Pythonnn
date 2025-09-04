places = ['venice', 'athens', 'jerusalem', 'equador', 'bali']

print("Original list:")
print(places)

# printing the list in alphabetical order without changing the original list
# places.sorted() # not working this way
print("\nHere is the sorted list:")
print(sorted(places))
print(places)

# to sum up, sorted(places) is built-in function
# whereas places.sort() is a list method

reverse_sorted = sorted(places, reverse=True) # the other way is places.sort(reverse=True)
print(reverse_sorted)

places.reverse()
print(places)

places.sort()
print(places)
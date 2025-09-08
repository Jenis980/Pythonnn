for num in range(1,21):
  print(num)

nmbers = list(range(1,1000001))
print(min(nmbers))
print(max(nmbers))
print(sum(nmbers))

for odd_number in range(1,21,2):
  print(odd_number)

  # multiples of 3
for multiple_of_3 in range(3,31,3):
  print(multiple_of_3)

  # cubing number 
for first_10_cube in range(1,10):
  print(first_10_cube**3)

  # cube compression list
cubes = [first_10_cube**3 for first_10_cube in range(1,11)]
print(cubes)
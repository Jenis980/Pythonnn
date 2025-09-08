ordial_numbers = list(range(1,10))
print(ordial_numbers)

for number in ordial_numbers:
  if number == 1:
    print(str(number) + "st")
  elif number == 2:
    print(str(number) + "nd")
  elif number == 3:
    print(str(number) + "rd")
  elif number > 3:
    print(str(number) + "th")
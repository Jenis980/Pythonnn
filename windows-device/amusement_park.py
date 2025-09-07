age = 12

if age < 4:
  print("Your admission cost is Rs.0")
elif age < 18:
  print("Your admission cost is Rs.5")
else:
  print("Your admission cost is Rs.10")

# program can be written in simpler way
age = 80

if age < 4:
  price = 0
elif age < 18:
  price = 5
else:
  price = 10
print("Your admission cost is Rs."+str(price)+".")
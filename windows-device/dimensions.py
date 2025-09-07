# tuple is immutable / uchanged list with parenthesis() instead of square bracket[]
dimensions = (200,50)
print(dimensions[0])
print(dimensions[1])

# what happens when we try to change immutable
# dimensions[0] = 88 . TypeError error occurs

for value in dimensions:
  print(value)  

  # can change or modify the tuple but can be override. just check this out
print("modified tuple")
dimensions = (800,10)
print(dimensions[0])
print(dimensions[1])


# tuple exercise
food_item = ('rice', 'curd', 'salad', 'ice cream', 'apple cider')
for food in food_item:
  print(food)

food_item = ('rice', 'curd',' salad', 'pepsi', 'pineapple')
print("\nrevised food items in buffet")
for food in food_item:
  print(food)
  print("again",food)
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]

print(friend_foods)

# lets add new food item to my_foods and friend_food
my_foods.append('cannoli')
friend_foods.append('ice cream')

print(my_foods)
print(friend_foods)

# exercise 4.12 of printing foods
print("\nMy friend's favorite foods are: \n")
for food in friend_foods:
  print(food)
print("\nThis are the food he like!")
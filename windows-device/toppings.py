requested_toppings = 'mushrooms'

if requested_toppings != 'anchovies':
  print('Hold the anchovies')

# to check if there exits the value already or not
requested_toppings = ['mushrooms', 'onions', 'pineapple']
'mushorooms' in requested_toppings
print(bool(requested_toppings))

# When the name of a list is used in an if statement, Python returns True if the list contains at least one item; an empty list evaluates to False. 
requested_toppings = []
if requested_toppings: # it checks if variable is non-empty. if true execute FOR, if not execute ELSE  
  for requested_topping in requested_toppings:
    print("adding" + requested_toppings + ".")
  print("\n Finished making pizza!")
else:
  print("Are you sure you want a plain pizza?")
# passing arbitrary number( random /when number of argument is not fixed ) of argruments
def make_pizza(*toppings):
  print("\nmaking a pizza with the following toppings:")
  for topping in toppings:
    print("- " + topping)

make_pizza('pepperoni')
make_pizza('mushrooms','green peppers', 'extra cheese')
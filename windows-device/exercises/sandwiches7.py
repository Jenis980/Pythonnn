sandwich_orders = ['reuben', 'cheesesteak', 'italian', 'tuna melt', 'chicken parmesan']
finished_sandwiches = []

for sandwich_order in sandwich_orders:
  print("I made your " + sandwich_order.title() + " sandwich.")
  
  finished_sandwiches.append(sandwich_order)

print("\nPrepared sandwiches are:")
for item in finished_sandwiches:
  print(item.title() + " ")
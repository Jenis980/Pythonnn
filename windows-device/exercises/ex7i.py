print("The deli has run out of pastrami")
sandwich_orders = ['reuben', 'pastrami', 'cheesesteak', 'pastrami', 'italian', 'tuna melt', 'chicken parmesan','pastrami']
finished_sandwiches = []

# print(sandwich_orders)
while 'pastrami' in sandwich_orders:
  sandwich_orders.remove('pastrami')
finished_sandwiches = sorted(sandwich_orders)
print(finished_sandwiches)
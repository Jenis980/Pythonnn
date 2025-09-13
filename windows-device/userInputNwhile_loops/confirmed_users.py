unconfirmed_users = ['alice', 'brian', 'candace']
confirmed_users = []

while unconfirmed_users: # it can be understand as ' while unconfirmed_users list is not empty, execute this loop'
  current_user = unconfirmed_users.pop()
  print("Verifiying users: " + current_user.title())
  confirmed_users.append(current_user)

print("\n the following users have been confirmed: ")
for confirmed_user in confirmed_users:
  print(confirmed_user.title())
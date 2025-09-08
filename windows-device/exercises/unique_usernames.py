current_users = ['ram', 'hari', 'sam', 'john', 'admin']
new_users = ['ramesh', 'hari', 'suresh', 'gita', 'John']

for new_user in new_users:
  if new_user.lower() in current_users:
    print("Please enter new username.")
  else:
    print("Username is available.")
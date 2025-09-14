def greet_users(names):
  """Print a simple greetings to each user in the list."""
  for name in names:
    msg = "Hello, " + name.title() + "!"
    print(msg)

usernames = ['hannah', 'ry', 'margot']
greet_users(usernames)
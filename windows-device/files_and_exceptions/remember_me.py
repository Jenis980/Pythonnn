import json

# load the username, if it has been stored previously.
# otherwise, prompt for the username and store it.

filename = "username.json"
try: # in case of file exist, read(read mode) username from it to print.
  with open(filename) as f_obj:
    username = json.load(f_obj)
except FileNotFoundError: # in case of if file was not created, create (write mode)file and prompt the user for name and store to that file
  username = input("What is your name?")
  with open(filename, 'w') as f_obj:
    json.dump(username, f_obj)
    print("We'll remeber you when you come back, " + username + "!")
else: # in case of file exist, just print the username which was read in try block.
  print("Welcome back, " + username + "!")
banned_users = ['andrew', 'carolina', 'david']
user = 'marie'

if user not in banned_users:
  print(user.title()+", you an post a response if you wish.")

# check if the person is aged to vote
age = 18  
if age >= 18:
  print("Your are eligible to vote.")
  print("Have you registered to vote yet?")
else:
  print("Sorry, you are too young to vote.")
  print("Please register to vote as soon as you turn 18.")
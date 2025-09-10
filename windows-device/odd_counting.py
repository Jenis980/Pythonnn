current_number = 0 
while current_number < 10:
  current_number += 1
  if current_number % 2 == 0:
    continue
  
  print(current_number)

  # another program that uses while loop
prompt = "\nPlease enter the name of city you have visited:"
prompt += "\n(Enter 'quit' when you are finished.)"

while True:
  city = input(prompt)
  if city == 'quit':
    break
  else:
    print("I'd love to go to " + city.title() + "!")
filename = 'pi_digits.txt'

with open(filename) as file_object:
  lines = file_object.readlines() # readlines() takes each line from the file and stores it in a LIST.

  pi_string = ''

  for line in lines:
    pi_string += line.strip()

birthday = input("Enter your birthday, in the form mmddyy: ")
if birthday in pi_string:
  print("Your bithday appears in the first million digits of pi!")
else:
  print("Your bithday does not appear in the first million digits of pi.")    

print(pi_string)    
print(len(pi_string))
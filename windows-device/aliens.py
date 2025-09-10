alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 4}
alien_2 = {'color': 'blue', 'points': 10} # creating three dictionaries
aliens = [alien_0, alien_1, alien_2] # creating a list of dictionaries
for alien in aliens:
  print(alien)

  # another way of doing it ; nesting the dictionaries
# first, lets make an empty list
aliens = []
# second, lets make a loop from range of 30 aliens
for aline in range(30):
  new_alien = {'color': 'green', 'points': 5, 'speed':'slow'} # at its heart, it is dictionary
  aliens.append(new_alien)

# now that we have created the aliens, lets see if it had been created or not.
for alien in aliens:
  print(alien)  
print(".....")

# lets count the number of aliens on console. ahaha just joking.
print("Total number of alies created are: " + str(len(aliens)))
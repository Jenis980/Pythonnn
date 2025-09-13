# dictinaries on python. it connects the pieces of related information. its a key-value pairs
alien_0 = {'color': 'green', 'points': 5}

print(alien_0['color'])
print(alien_0['points'])
print(alien_0)

# adding new key-value
alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)

# modifying the values in dictionary
alien_0['color'] = 'blue'
print("Now the color of initial dictionary is changed to " + alien_0['color'] + ".")

# program snippet
alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print("Original x-position: " + str(alien_0['x_position']))

# move the alien to the rightf
# determine how far to move the alien based on its current speed
if alien_0['speed'] == 'slow':
  x_increment = 1
elif alien_0['speed'] == 'medium':
  x_increment = 2
else:
  x_increment = 3

# the new position is the old position plus the increment
alien_0['x_position'] = alien_0['x_position'] + x_increment

print("New x-position: " + str(alien_0['x_position']))

# removing the key-value pairs
print(alien_0)
alien_0['color'] = 'red'
print(alien_0)
del alien_0['y_position'] 
print(alien_0) # deleted the key-value permanently


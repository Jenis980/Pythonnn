# inviting people to dinner
guest_names = ['Jacob', 'Simson', 'Jenish']
print('Welcome to dinner '+guest_names[0]+".")
print('Welcome to dinner '+guest_names[1]+".")
print('Welcome to dinner '+guest_names[2]+".")

# one of the guest can't attend the dinner
busy_guest = 'Jenish'
guest_names.remove(busy_guest)
print(guest_names)
print(busy_guest + " can't attend the dinner.")

# adding new guest to list
guest_names.append('Sugam')
print(guest_names)
print("\n I found a bigger table for dinner. So, why not add more guest names on list!")

# adding new guest names
guest_names.insert(0,'Paul')
guest_names.insert(3,'Kailesh')
guest_names.insert(-1,"Hari")
print("We list the names of guest as follow ",guest_names)

# ohh i found new table won't make it here on time. I can only call 2 guest
print("ohh i found new table won't make it here on time. I can only call 2 guest ")
print(guest_names)
cancel_guest = guest_names.pop()
print(cancel_guest+", sorry for cancelling the dinner.")
cancel_guest1 = guest_names.pop()
print(cancel_guest+", sorry for cancelling the dinner.")
cancel_guest = guest_names.pop()
print(cancel_guest+", sorry for cancelling the dinner.")
cancel_guest1 = guest_names.pop()
print(cancel_guest+", sorry for cancelling the dinner.")
print(guest_names)
print(" The names on this list is still invited:",guest_names)

# empty the list
del guest_names[1]
del guest_names[0]
print(guest_names)

# at last, short thing i noticed: the 'del' is a STATEMENT not a  METHOD
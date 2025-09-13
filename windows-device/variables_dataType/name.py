name = " ada lovelace"
print(name.title())
name = "Ada Lovelace"
print(name.upper())
print(name.lower())

first_name = "ada"
last_name = "lovelace"
full_name = first_name + " " + last_name
print(full_name)

message = "Hello, "+full_name.title() + "!"
print(message) # string combine or concatation


# add whitespaces on string with Tabs or Newlines
print("Python")
print("\n")
print("\tPython")
# add new line
print("Languages:\nPython\nC\nJavaScript")

# remove whitespaces
favorite_language = "python "
print(favorite_language)
print(favorite_language.rstrip()) # remove right space 
print(favorite_language) # removes temporarily

# to permanently remove whitespace, store stripped value to a variable
favorite_language = favorite_language.rstrip()
print(favorite_language)
name = input("What's your name? ")
age = int(input("How old are you? "))
color = input("What's your favorite color? ")

print(f"{name}, you are {age} years old and your favorite color is {color}.")
if age < 18:
    print("You are not eligible to vote.")
else:
    print("You are eligible to vote.")

print("Thank you for sharing your informations")
print("Goodbye!")
print("ok?")
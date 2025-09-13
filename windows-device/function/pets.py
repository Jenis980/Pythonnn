def describe_pet(animal_type='dog', pet_name='willie'):
  '''Display information about a pet.'''
  print("\nI have a " + animal_type + ".")
  print("My " + animal_type + "'s name is " + pet_name.title() + ".")
  # positional arguments which means each argument should be on same order as def function parameters
describe_pet('hamster', 'harry')
describe_pet('dog', 'willie')
  # keyword arguments which means each argument should be as name-value pair. it does not concern with order.
describe_pet(pet_name='harry', animal_type='hamster')
describe_pet('willie')
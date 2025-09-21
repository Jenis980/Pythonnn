from collections import OrderedDict

  # using the list and dictionary style
favorite_languages = OrderedDict()

favorite_languages['jen'] = 'python'
favorite_languages['sarah'] = 'c'
favorite_languages['edward'] = 'ruby'
favorite_languages['phil'] = 'python'
friends = ['phil', 'sarah']

for name in favorite_languages.keys():
  print(name.title())

  if name in friends:
    print("Hi " + name.title() + ", I see your favorite language is " + favorite_languages[name].title() + "!")
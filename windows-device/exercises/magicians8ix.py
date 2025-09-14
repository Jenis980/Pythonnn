magician_names = ['mahesh', 'bibek', 'suresh', 'mukesh', 'rajesh']

def show_magicians(magician_names):
  for names in magician_names:
    print(names.title())

def make_great(magician_names):
  great_magicians = []
  for name in magician_names:
    great_magicians.append('the great ' + name)
    
  show_magicians(great_magicians)    

make_great(magician_names[:])    
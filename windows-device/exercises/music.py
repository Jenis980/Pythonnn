def make_album(artist_name, album_title, number_of_album=''):
  album = {'singer': artist_name, 'song': album_title}
  if number_of_album:
    album['number_of_album'] = number_of_album
  return album

singer1 = make_album('Adele','Hello')
print(singer1)
singer2 = make_album('Mohit','Tum Ho',3)
print(singer2)
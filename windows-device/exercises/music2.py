def make_album(artist_name, album_title, number_of_tracks=''): # this method makes the album but does not print it
  album = {'singer': artist_name, 'song': album_title}
  if number_of_tracks:
    album['number_of_album'] = number_of_tracks
  return album

# lets use while loop to print user's information and exit the loop if user presses 'q' at any time
while True:
  print("Enter the details : ")
  print("(press 'q' to quit)\n")

  artist_name = input("enter the name of singer: ")
  if artist_name == 'q':
    break
  album_title = input("Enter the name of album of the artist: ")
  if album_title == 'q':
    break
  number_of_tracks = input("Enter the number of track(optional):")
  if number_of_tracks == 'q':
    break
  album_info = make_album(artist_name,album_title,number_of_tracks)
  print("Your information(s):\n")
  print(album_info)


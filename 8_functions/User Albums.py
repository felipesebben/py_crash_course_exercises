def make_album(artist, title, tracks=None):
    """Return a dictionary of information about an album."""
    album_dict = {
        'artist': artist.title(),
        'title': title.title(),
        }
    if tracks:
        album_dict['tracks'] = tracks
    return album_dict

while True:
    print("\nPlease enter the album's artist and title names:")
    print("(enter 'q' at any time to quit)")
    
    a_name = input("Artist name: ")
    if a_name == 'q':
        break
    
    t_name = input("Title: ")
    if t_name == 'q':
        break
    
    formatted_album = make_album(a_name, t_name)
    print(f"\nArtist: {a_name.title()}" +
          f"\nTitle: {t_name.title()}")

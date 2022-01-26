def make_album(artist, title, tracks=None):
    """Return a dictionary of information about an album."""
    album_dict = {
        'artist': artist.title(),
        'title': title.title(),
        }
    if tracks:
        album_dict['tracks'] = tracks
    return album_dict

album_info = make_album('led zeppelin', 'the song remains the same')
print(album_info)

album_info = make_album('jimi hendrix', 'electric ladyland', tracks= 12)
print(album_info)
album_info = make_album('jorge ben', 'tabua de esmeralda')
print(album_info)


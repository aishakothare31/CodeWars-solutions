def song_decoder(song):
    #replace 'WUB' with 1 space and remove any heading or trailing extra spaces
    return ' '.join(song.replace('WUB', ' ').split())
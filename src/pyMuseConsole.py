#!/usr/bin/env python3
import os
import sys

from genrePlaylist import Playlist


if len(sys.argv) == 1:
    print("Usage: List each genre as argument seperated by spaces")
    sys.exit()

playlist = Playlist()

musicDir = input("Scan different directory? (Hit return for cwd)\n")
print("working...")
if len(musicDir) > 0:
    for genre in sys.argv:
        playlist.getByGenre(genre, musicDir)
else:
    for genre in sys.argv:
        playlist.getByGenre(genre, os.getcwd())


for track in playlist.playlist:
    print (track)

if input("Remove an artist? (y/n)") == "y":
    playlist.filterArtist(input("Artist to remove?"))

name = input("Playlist name?\n")
if len(name) > 0:
    playlist.generatePlaylist(os.getcwd(), name)
else:
    playlist.generatePlaylist(os.getcwd())

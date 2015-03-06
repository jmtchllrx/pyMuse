#!/usr/bin/env python3
import os
import sys

from genrePlaylist import Playlist


if len(sys.argv) == 1:
    print("Usage: List each genre as argument seperated by spaces")
    sys.exit()

playlist = Playlist()

musicDir = input("Scan different directory? (Hit return for cwd) ")
print("working...")
if len(musicDir) > 0:
    for genre in sys.argv:
        playlist.getByGenre(genre, musicDir)
else:
    for genre in sys.argv:
        playlist.getByGenre(genre, os.getcwd())


print("playlist.m3u")
for track in playlist.playlist:
    print (track)

if input("Change artists, albums, or playlist name?(y/n) ") == "y":
    if input("Remove an artist? (y/n) ") == "y":
        artist = " "    
        while artist != "":
            artist = input("Artist to remove? (enter to finish)")
            playlist.filterArtist(artist)


    if input("Remove an album? (y/n) ") == "y":
        album = " "    
        while album != "":
            album = input("Album to remove? (enter to finish)")
            playlist.filterAlbum(album)


    name = input("Playlist name? ")
    if len(name) > 0:
        playlist.generatePlaylist(os.getcwd(), name)
    else:
        playlist.generatePlaylist(os.getcwd())
else:
    playlist.generatePlaylist(os.getcwd())

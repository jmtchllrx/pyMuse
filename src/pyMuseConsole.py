#!/usr/bin/env python3
import os

from genrePlaylist import Playlist


playlist = Playlist()

genre = input("Genre?\n")
musicDir = input("Different directory? (Hit return for cwd)\n")

print("working...")
if len(musicDir) > 0:
    playlist.getByGenre(genre, musicDir)
else:
    playlist.getByGenre(genre, os.getcwd())


for track in playlist.playlist:
    print (track)

if input("Remove an artist? (y/n)") == "y":
    playlist.filterArtist(input("Artist to remove?"))


if input("Edit output directory or name? (y/n)") == "y":
    outputDir = input("Enter directory: ")
    name = input("Enter playlist name: ")
    playlist.generatePlaylist(playlist, outputDir, name)
else:
    playlist.generatePlaylist(playlist, os.getcwd())

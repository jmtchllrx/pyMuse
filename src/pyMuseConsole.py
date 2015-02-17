#!/usr/bin/env python3
import os

import genrePlaylist

genre = input("Genre?\n")
musicDir = input("Different directory? (Hit return for cwd)\n")

playlist = Playlist

#TODO
# 1. Just makes this better

print("working...")
if len(musicDir) > 0:
    playlist.getByGenre(genre, musicDir)
else:
    playlist.getByGenre(genre, os.getcwd())

if input("Edit output directory or name? (y/n)") == "y":
    outputDir = input("Enter directory: ")
    name = input("Enter playlist name: ")
    playlist.generatePlaylist(playlist, outputDir, name)
else:
    playlist.generatePlaylist(playlist, os.getcwd())

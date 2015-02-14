#!/usr/bin/env python3
import os

import genrePlaylist

genre = input("Genre?\n")
musicDir = input("Different directory? (Hit return for cwd)\n")

#TODO
# 1. Just makes this better

print("working...")
if len(musicDir) > 0:
    playlist = genrePlaylist.getByGenre(genre, musicDir)
else:
    playlist = genrePlaylist.getByGenre(genre, os.getcwd())

if input("Edit output directory or name? (y/n)") == "y":
    outputDir = input("Enter directory: ")
    name = input("Enter playlist name: ")
    genrePlaylist.generatePlaylist(playlist, outputDir, name)
else:
    genrePlaylist.generatePlaylist(playlist, os.getcwd())

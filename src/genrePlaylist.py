#!/usr/bin/env python3

import random
import os
import sys
from os.path import join

from hsaudiotag import auto

class Playlist():


    FORMATS = ('.mp3', '.wma', 'flac', '.ogg', '.aif', 'aiff')
    playlist = []


    def getByGenre(self, genre, directory):
        """Searches cwd and subdirectories for music files with matching
        genre ID3 tags and returns a list of them
        """

        # TODO 
        # turn into list comprehension

        for root, dirs, files in os.walk(directory):
            for item in files:
                if item[len(item)-4:len(item)] in self.FORMATS:
                    if auto.File(join(root, item)).genre == genre:
                        self.playlist.append(join(root, item))


    def filterArtist(self, artist):
        self.playlist = [track for track in self.playlist if auto.File(track).artist != artist]


    def generatePlaylist(self, directory, name="playlist", randomize=True):
        """Generates m3u file to parameter specification, no return value"""
        if randomize:
            random.shuffle(self.playlist)

        playlistFile = open(join(directory, name + ".m3u"), "w")
        playlistFile.write("#EXTM3U\n")
        for song in self.playlist:
            playlistFile.write(song + "\n")

        playlistFile.flush()
        playlistFile.close()


# Run this file from directory to search
# with genres as arguments
if __name__ == "__main__":
    playlist = Playlist()
    for genre in sys.argv:
        playlist.getByGenre(genre, os.getcwd())

    playlist.generatePlaylist(os.getcwd())

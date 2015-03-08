#!/usr/bin/env python3

import random
import os
import sys
from os.path import join

from hsaudiotag import auto

class Playlist():


    FORMATS = ('.mp3', '.wma', 'flac', '.ogg', '.aif', 'aiff', '.m4a')
    playlist = []


    def getByGenre(self, genre, directory):
        """Searches cwd and subdirectories for music files with matching
        genre ID3 tags
        """

        for root, dirs, files in os.walk(directory.encode('utf-8')):
            for item in files:
                if item[len(item)-4:len(item)].decode('utf-8') in self.FORMATS:

                    # Basically, the hsaudiotag library does not handle text
                    # correctly. This bytes-file opening weirdness is the only way I can get
                    # it to handle non-ascii characters
                    # (The only good library is GPL, so I'm sticking with hsaudiotag)
                    path = root + b'/' + item
                    currentFile = open(path, 'rb')
                    if auto.File(currentFile).genre == genre:
                        self.playlist.append(path)
                    currentFile.close()


    def filterArtist(self, artist):
        self.playlist = [track for track in self.playlist if auto.File(track).artist != artist]

    def filterAlbum(self, album):
        self.playlist = [track for track in self.playlist if auto.File(track).album != album]

    def generatePlaylist(self, directory, name="playlist", randomize=True):
        """Generates m3u file to parameter specification, no return value"""
        if randomize:
            random.shuffle(self.playlist)

        # See comment in getByGenre. I'm not even entirely sure why all this bytes stuff works
        playlistFile = open(join(directory, name + ".m3u"), "wb")
        playlistFile.write(b"#EXTM3U\n")
        for song in self.playlist:
            playlistFile.write(song + b"\n")

        playlistFile.flush()
        playlistFile.close()


# Run this file from directory to search
# with genres as arguments
if __name__ == "__main__":
    if len(sys.argv) == 1:
        print("Usage: List each genre as argument seperated by spaces")
        sys.exit()

    playlist = Playlist()
    for genre in sys.argv:
        playlist.getByGenre(genre, os.getcwd())

    playlist.generatePlaylist(os.getcwd())

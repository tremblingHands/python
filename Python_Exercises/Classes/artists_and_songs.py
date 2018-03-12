#!/usr/bin/env python

class MusicFile(object):
    def get_artist(self, path):
        artist = dict()
        with open(path, 'r') as f:
            for line in f.readlines():
                line = line.replace('\n', '')
                info = line.split(' - ', 1)
                if not artist.get(info[0]):
                    artist[info[0]] = []
                artist[info[0]].append(info[1])
        return artist


    def __init__(self, path = './music.txt'):
        self.path = path
        self.artist = self.get_artist(self.path)
    
    

def main():
    music = MusicFile('./music.txt')
    print(music.artist['Joy Division'])

if __name__ == '__main__':
    main()

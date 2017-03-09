__author__ = 'developer'


class Game:
    id = 0
    name = "Game"
    fileUrl = "http://google.com"
    gameUrl = "https://duckduckgo.com/"
    files = []
    summary = ""
    covertUrl = ""
    screenUrl = ""
    pokesUrl = ""


class File:
    fileName=""
    url=""

class searchResult:
    id=0
    title=""


class configuration:
    fuseCommand = "fuse-sdl"
    inputPath="/dev/input/js0"
    model="48"
    bios="48.zip"
    download=True



class reg(object):
    def __init__(self, cursor, row):
        for (attr, val) in zip((d[0] for d in cursor.description), row) :
            setattr(self, attr, val)
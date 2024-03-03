from os import path, getcwd
from zipfile import ZipFile
import json

class ZipReader:
    
    def __init__(self, filename):    
        self.root     = self.getFullFilename(filename)

    def getFullFilename(self, filename):
        fullfilename = path.join(getcwd(), filename)
        if not path.exists(fullfilename):
            raise ValueError('Specified filename does not exists.')
        return fullfilename

    
    def __fetchFile(self, filename):
        result = None
        with ZipFile(self.root, 'r') as zip:
            fetchedFile = [name for name in zip.namelist() if name.endswith(filename)]
            if fetchedFile:
                with zip.open(fetchedFile[0]) as file:
                    data = file.read()
                    result = json.loads(data)

        return result

    def getFollowers(self):
        return self.__fetchFile("followers_1.json")

    def getFollowing(self):
        return self.__fetchFile("following.json")
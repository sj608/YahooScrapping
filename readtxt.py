import math
import string

class readtxt:
    
    def __init__(self, target):
        self.filename = target
    

    def read_file(self):
        url = []
        shares = []
        f = open(self.filename, 'r')
        for txt in f:
            line = txt.split(",")
            url.append(line[0])
            shares.append(int(line[1]))
        f.close()
        return url, shares
'''
IRC data processing
'''

import fileinput

class data(object):
    '''We require a filename and username'''
    def __init__(self, filename, user):
        self.filename = filename
        self.user = user
        self.build()

    def build(self):
        '''Uses fileinput to reduce memory use'''
        self.text = []
        for l in fileinput.input(self.filename):
            i = self.validate(l)
            if i != None:
                self.text.append(i)

    def validate(self, string):
        '''Will confirm if the line in the log matches what we want'''
        string = string.lower().split()
        o = None
        if len(string) >= 3:
            if self.user in string[1]:
                o = ' '.join(string[2:])
        return o
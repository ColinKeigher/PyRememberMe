'''
Module for building a MarkovChain
'''

from pymarkovchain import MarkovChain

class markovbuild(object):
    '''Builds a markov chain DB and outputs data'''
    def __init__(self, data, lines=5):
        self.database = '/tmp/markov.db'
        self.lines = lines
        self.data = '\n'.join(data)
        self.mchain = MarkovChain(self.database)

    def build(self):
        '''Builds a markov chain'''
        self.mchain.generateDatabase(self.data)

    def output(self):
        '''Outputs markov chain data'''
        self.build()
        return [ self.mchain.generateString() for x in xrange(0, self.lines) ]
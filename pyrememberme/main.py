'''
Main module for building the markov chain data
'''

from reddit import data as reddit_data
from irc import data as irc_data

from markov import markovbuild

class builddata(object):
    '''Building and processing is automatic'''
    def __init__(self, target, reddit=None, irc=None, markov_limit=None):
        self.target = target
        self.markov_limit = markov_limit
        self.reddit = { 'user': reddit, 'text': [] }
        self.irc = { 'user': irc['user'], 'file': irc['log'], 'text': [] }
        self.build()
        self.process()

    def output(self, string):
        '''Fancy text output'''
        print '*** %s' % string

    def pull_irc(self):
        '''Retrieves IRC data from the IRC module'''
        if None not in [ self.irc['user'], self.irc['file'] ]:
            msg = 'Building data from IRC log using nickname matching "%s"'
            self.output(string=msg % self.irc['user'])
            i = irc_data(filename=self.irc['file'], 
                user=self.irc['user'])
            self.irc['text'] = i.text
            if len(self.irc['text']) == 0:
                msg = 'No lines to add from IRC.'
            else:
                msg = 'Added all lines found from the provided log file.'
            self.output(msg)

    def pull_reddit(self):
        '''Retrives Reddit data from Reddit module'''
        if self.reddit['user'] != None:
            u = self.reddit['user']
            msg = 'Building data from Reddit using account "%s".' % u
            self.output(string=msg)
            r = reddit_data(user=u)
            self.reddit['text'] = r.text
            if len(self.reddit['text']) == 0:
                msg = 'No lines to build from Reddit.'
            else:
                msg = 'Added all comments from Reddit.'
            self.output(msg)

    def build(self):
        '''Runs through each module to see if items are needed done.'''
        self.pull_reddit()
        self.pull_irc()

    def markov_build(self):
        '''Returns markov chain-generated text'''
        mbuild = markovbuild(data=self.text, 
            lines=self.markov_limit,
            target=self.target)
        return mbuild.output()

    def process(self):
        '''Processes all text retrieved from each module.'''
        self.text = []
        for x in [ self.reddit, self.irc ]:
            self.text += x['text']

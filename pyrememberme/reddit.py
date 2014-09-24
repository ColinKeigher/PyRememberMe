'''
Reddit data import module
'''

import requests

class reddit_data(object):
    '''We just require a target user'''
    def __init__(self, target_user):
        self.target_user = target_user
        self.url = 'http://reddit.com/user/%s.json' % target_user
        self.data = None
        self.user_agent = 'PyRememberMe Chainer'

    def retrieve(self):
        '''User agent has to be changed in order to not get blocked'''
        head = { 'User-Agent': self.user_agent }
        r = requests.get(self.url, headers=head)
        if r.status_code == 200:
            self.data = r.json()

class data(object):
    def __init__(self, user):
        '''Just a friendly interface'''
        self.user = user
        rd = reddit_data(target_user=user)
        rd.retrieve()
        self.data = rd.data
        self.text = []
        self.retrieve_text()

    def retrieve_text(self):
        '''If there is data to process, add them to the text list'''
        if self.data != None:
            self.text = [ x['data']['body'].encode('utf-8', 'ignore') 
                for x in self.data['data']['children'] if 'body' in x['data'].keys() ]

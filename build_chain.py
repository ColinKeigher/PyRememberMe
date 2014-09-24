#!/usr/bin/env python
'''
PyRememberMe - A Markov Bot Builder
Created by Colin Keigher <colin@keigher.ca>

See LICENCE.txt for licensing details.
'''

import argparse

from pyrememberme.main import builddata

def main():
    '''Parses the args and then runs it through the module'''
    opts = args()
    build = builddata(reddit=opts['reddit'], 
        irc={ 'user': opts['irc_nick'], 'log': opts['irc_log'] },
        markov_limit=opts['markov_limit'],
        target=opts['identity'])
    display(identity=opts['identity'], 
        lines=build.markov_build())

def display(identity, lines):
    '''Outputs results in an IRC-esque fashion'''
    out = '<%s> %s'
    print
    for line in lines:
        print out % (identity, line)
    print

def welcome():
    '''Simple welcome banner'''
    print
    print 'PyRememberMe - A Markov Bot Builder'
    print '-------------------------------------'
    print

def args():
    '''Not much to explain here'''
    parser = argparse.ArgumentParser(
        description='''Builds a markov chain based on content 
        from various local and network resources.''')
    parser.add_argument('--identity',
        help='Identifies the target you wish to create (required).',
        required=True)
    parser.add_argument('--reddit', 
        help='Retrieves comments from a Reddit account.', 
        required=False)
    parser.add_argument('--irc_nick', 
        help='Specifies the IRC nickname to be used (not case sensitive).', 
        required=False)
    parser.add_argument('--irc_log', 
        help='Retrieves data from specified IRC log (must be irssi format).', 
        required=False)
    parser.add_argument('--markov-limit',
        help='Sets a limit of lines created by the markov chain (default: 5).',
        default=5,
        type=int,
        required=False)
    return vars(parser.parse_args())

if __name__ == '__main__':
    welcome()
    main()
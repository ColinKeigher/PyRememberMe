PyRememberMe
============

Introduction
------------
*PyRememberMe* is a tool that aggregates data from various sources in order to create a [markov chain](http://en.wikipedia.org/wiki/Markov_chain) 
of conversations made by a specific person.

At this time, it can source data from the following:

+ Reddit
+ IRC logs (irssi format)

Requirements
-------------

+ Python 2.7 or higher
+ [Requests](http://docs.python-requests.org/en/latest/)
+ [PyMarkovChain](https://pypi.python.org/pypi/PyMarkovChain/)

Usage
-----

    usage: build_chain.py [-h] --identity IDENTITY [--reddit REDDIT]
                          [--irc_nick IRC_NICK] [--irc_log IRC_LOG]
                          [--markov-limit MARKOV_LIMIT]

    Builds a markov chain based on content from various local and network
    resources.

    optional arguments:
      -h, --help            show this help message and exit
      --identity IDENTITY   Identifies the target you wish to create (required).
      --reddit REDDIT       Retrieves comments from a Reddit account.
      --irc_nick IRC_NICK   Specifies the IRC nickname to be used (not case
                            sensitive).
      --irc_log IRC_LOG     Retrieves data from specified IRC log (must be irssi
                            format).
      --markov-limit MARKOV_LIMIT
                            Sets a limit of lines created by the markov chain
                            (default: 5).


Future
-------

+ Integration into an IRC or Twitter bot
+ Retrieval of data via Twitter
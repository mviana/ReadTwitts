#!/usr/bin/python
#-*-encoding:utf8-*-

import twitter as tw
from datetime import datetime as dt
import sys

'''
This simple class uses python-twitter v1.15 to get a list of tweets in someones timeline in the current day. Enjoy.
'''

class ReadTwitts :
	def __init__(self, keys, day, month, year, n_twitts=0):
	'''
		Inputs:
			keys: list for OAuth in order [ACCESS_TOKEN_KEY, ACCESS_TOKEN_SECRET, CONSUMER_KEY, CONSUMER_SECRET]
			day: only get tweets of this day
			month: only get tweets of this month
			year: only get tweets of this year
			n_tweets: will get a maximum of n_twits
	'''
		account = tw.Twitter(auth=tw.OAuth(keys[0],keys[1],keys[2],keys[3]))
		self.dt_look = dt(year,month,day).date()
		list = account.statuses.home_timeline(count=n_twitts)
		self.twitts = []
		for t in list:
			#Since Twitter does not use timezone and sime versions of datetime has errors with timezone, it's readed as +0000
			dt_twitt = dt.strptime(t['created_at'],'%a %b %d %H:%M:%S +0000 %Y')
			if (dt_twitt.date() == self.dt_look):
				self.twitts.append([t['created_at'],t['user'] ['screen_name'], t['texto']])

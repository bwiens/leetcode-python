#!/usr/bin/python
import datetime
key = 1
value = "Facebook"
pdict, timedict = {}, {}

def buildhashmap(key, value):
	now = datetime.datetime.now()
	now_plus_10 = now + datetime.timedelta(minutes = 10)
	pdict[key] = value
	timedict[key] = now_plus_10	
	print(pdict,timedict)

def getvalue(key):
	print(pdict.get(key))
 
buildhashmap(key,value)
getvalue(key)

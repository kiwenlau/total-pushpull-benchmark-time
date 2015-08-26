#!/usr/bin/python

import os


def getRealTime (filepath):
	str=""
	files = os.listdir(filepath)
	for file in files :
		cmd="cat | grep real"
		cmd=cmd[:4]+filepath+"/"+file+cmd[4:]
		str = str+os.popen(cmd).read()
	return str

def totalBenchmarkTime():
	f2=open("realtime.txt", "r")
	str=f2.read()
	print str
	f2.close()

str=getRealTime("output5/output2") 
print str
#totalBenchmarkTime()
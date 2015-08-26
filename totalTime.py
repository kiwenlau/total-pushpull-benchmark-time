#!/usr/bin/python

import os


def getRealTime (filepath):
	f1=open("realtime.txt", "w")
	files = os.listdir(filepath)
	for file in files :
		cmd="cat | grep real"
		cmd=cmd[:4]+filepath+"/"+file+cmd[4:]
		str = os.popen(cmd).read()
		f1.write(str)
	f1.close()

def totalBenchmarkTime():
	f2=open("realtime.txt", "r")
	str=f2.read()
	print str
	f2.close()

getRealTime("output5/output2") 
totalBenchmarkTime()
#!/usr/bin/python

import os


def getRealTime (filepath):
	realTime=""
	files = os.listdir(filepath)
	for file in files :
		cmd="cat | grep real"
		cmd=cmd[:4]+filepath+"/"+file+cmd[4:]
		realTime = realTime+os.popen(cmd).read()
	return realTime

def totalBenchmarkTime(realTime):
	totalTime=0.0
	str=realTime.split("\n")
	for s in str :
		if(s==""): # fliter the empty string
			break
		totalTime=totalTime + float(s[6:])
	return totalTime



realTime=getRealTime("output5/output2") 
totalTime=totalBenchmarkTime(realTime)
print totalTime
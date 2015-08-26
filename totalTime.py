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
	strings=realTime.split("\n")
	for s in strings :
		if(s==""): # fliter the empty string
			break
		totalTime=totalTime + float(s[6:])
	return totalTime

def allBenchmark(outputPath):
	for i in range(1, 13):
		filepath=outputPath+"output"+str(i)
		realTime=getRealTime(filepath)
		totalTime=totalBenchmarkTime(realTime)
		print totalTime/3600
	print "\n\n"

allBenchmark("output5/")
allBenchmark("output7/")
allBenchmark("output8/")

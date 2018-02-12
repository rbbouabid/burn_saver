import sys

def zscore(data, sd):
	print "i use z score"
	print data 

def abs_threshold(current, cutoff):
	threshold = cutoff
	if(current > threshold):
		return 1
	else: return 0


test_data = []

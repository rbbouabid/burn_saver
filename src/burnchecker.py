import sys


def burncheck(timestamps):
	print "i check minbias data"
	#print timestamps
	clean_timestamps = cleaner(timestamps)
	for timestamp in timestamps:
		time2run(timestamp)	
	return 1

def time2run(timestamp):
	print timestamp

def cleaner(timestamps):
	#print timestamps
	return timestamps

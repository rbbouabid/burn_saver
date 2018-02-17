import sys
import os
import subprocess


def burncheck(timestamps):
	print "~~~~~~~~~~~~~~~~~~~~"
	print "i check minbias data"
	print "~~~~~~~~~~~~~~~~~~~~"
	clean_timestamps = cleaner(timestamps)
	for timestamp in timestamps:
		if timestamp != clean_timestamps: continue
		run = time2run(timestamp)	
		MBLookup(run)
	return 1


def cleaner(timestamps):
	#print timestamps
	return timestamps[0]



def time2run(timestamp):
	time_string = timestamp.strftime('%d.%m.%Y_%H:%M:%S')
	cmd = "AtlRunQuery.py 'f t {0}-{1} / sh r'".format(time_string, time_string)
	os.system(cmd)
	
	run_string = ""
	try:
		with open("data/QueryResult.txt", "r") as results:
			for line in results:
				if "Run:" in line:
					run_line_values = line.split()
					run_string = run_line_values[1]
					
	except IOError:
		print "Whoa there! QueryResults.txt isn't there??? AtlRunQuery might not have found anything??"  
	
	return run_string

def MBLookup(runnumber):
	print "Look up min bias root file for run number: ", runnumber	


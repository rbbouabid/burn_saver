import sys
import os
import random

#def burncheck(timestamps):
def burncheck(module, peaklist):
	print peaklist
	for peak in peaklist:
		run = time2run(peak)	
		print "MBLookup(",module,", ",run,")"
		return MBLookup(module, run)



def time2run(timestamp):
	time_string = timestamp.strftime('%d.%m.%Y_%H:%M:%S')
	cmd = "AtlRunQuery.py 'f t {0}-{1} / sh r'".format(time_string, time_string)
	os.system(cmd + "&> /dev/null")
	
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

def MBLookup(module, runnumber):
	is_signal = random.randint(0,1)
	print "\tModule#: ", module, " run#: ", runnumber
	if is_signal: 
		print "\t\tThere was a burnout here!"
		return 1 
	else: 
		print "\t\tThere was not a burnout here.."
		return 0 

#end

import sys
import os
import random

#def burncheck(timestamps):
def burncheck(module, peaklist, partition):
	#print "\t\t\t",peaklist
	checked = []
	for peak in peaklist:
		run = time2run(peak)	
		if not run:	
			#print "\t\t\t\tdidn't find a runnumber, return 0"
			#return 0
			checked.append([0,0,0])
		else:		
			#print "\t\t\t\tfound a run#: ", run
			#print "MBLookup(",module,", ",run,")"
			#return MBLookup(module, run)
			checked.append([1,0,0])
	return checked



def time2run(timestamp):
	# cleaning previous atl run query
	if os.path.isdir("data"):
		os.system("rm -r data")
	# trying to grab a run 
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
		# there was no run given this timestamp. return nada
		#print "Whoa there! QueryResults.txt isn't there??? AtlRunQuery might not have found anything??"  
		pass
	
	return run_string

def MBLookup(module, runnumber, partition):
	return 1
	#is_signal = random.randint(0,1)
	##print "\tModule#: ", module, " run#: ", runnumber
	#if is_signal: 
	#	return 1 
	#else: 
	#	return 0 

#end

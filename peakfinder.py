import sys
import numpy as np
from datetime import datetime
from datetime import timedelta
print "i find peaks"

container_size = 3 
I_container = np.zeros(container_size)
window = timedelta(1)
sd = 3


def get_datetime(string1, string2):
	strip_character = ":"
	time = strip_character.join(string2.split(strip_character)[:3])
	time_string = string1 + " " + time
	return datetime.strptime(time_string, '%d-%m-%Y %H:%M:%S')
	

def threshold_alg(currents, threshold):
	print "gonna calculate some thresholds >:(" 


def finder(partition, module):
	file_string = "data/" + partition + "_LVPS_" + module + "_5VMB_OUTPUT_I.txt"
	try:
		#with open("data/EBA_LVPS_42_5VMB_OUTPUT_I.txt") as f:
		with open(file_string) as f:
			fdata = [line.rstrip() for line in f]
			for i,l in enumerate(fdata):
				if(i < 100):
					continue
	
				# grabbing the datetime obj
				values = l.split()
				pt_time = get_datetime(values[1], values[2])
	
				## grabbing the current in amps
				pt_amps = float(values[0].strip("0"))
	
				# some variables to loop backward from this pt
				n = 1
				delta_t = timedelta(0) 
				prev_amps = []
	
				while delta_t < window:
					# grabbing (i-n)th line
					prev_line = fdata[i-n]
					prev_values = prev_line.split()
					# (i-n)th time
					prev_time = get_datetime(prev_values[1], prev_values[2])
					delta_t = pt_time - prev_time
					# pushing to container of previous I(amps)
					prev_amps.append(float(prev_values[0].strip("0")))
	
					# incrementing to next line
					n += 1
					
				print "previous days worth of currents: ", prev_amps
				threshold_alg(prev_amps, sd)
				print "\n"
						
	
	except IOError:
		print "Whoa there! You're trying to open a file you do not have..\n"

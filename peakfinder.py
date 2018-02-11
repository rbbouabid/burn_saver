import sys
import numpy as np
from datetime import datetime
print "i find peaks"

container_size = 3 
I_container = np.zeros(container_size)

try:
	with open("data/EBA_LVPS_42_5VMB_OUTPUT_I.txt") as f:
		fdata = [line.rstrip() for line in f]
		for i,l in enumerate(fdata):
			if(i < 3):
				continue
			a = l.split()
			b = fdata[i-1].split()
			c = fdata[i-2].split()
			
			I_container[0] = float(c[0].strip("0")) 
			I_container[1] = float(b[0].strip("0")) 
			I_container[2] = float(a[0].strip("0"))
			
			print c 
			print b
			print a
			print I_container
			print np.average(I_container)
			print "\n"
		#	vals = line.split()
		#	#print fdata[i]
		#	if len(values) < 4:
		#		continue
		#	strip_character = ":"
		#	time = strip_character.join(values[2].split(strip_character)[:3])
		#	time_string = values[1] + " " + time
		#	utc_time = datetime.strptime(time_string, '%d-%m-%Y %H:%M:%S')
		#	print utc_time, " : ", values[0]
		#	print I_container
		#	print "\n"

		#	val_minus1 
except IOError:
	print "Whoa there! You're trying to open a file you do not have..\n"

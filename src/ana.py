import sys
from peakfinder import finder
from burnchecker import burncheck

print "This is the top level analysis macro"

#absolute_threshold_list = [9.8, 9.9, 10, 10.1, 10.2]
#for index,eventLoop in enumerate(absolute_threshold_list):
#	print index, " ", eventLoop
#sys.exit()


partition_list = ["EBA", "EBC", "LBA", "LBC"]
module_list = range(65)
module = "42"

config = [	[1, 10],  		# (absolute thresholding, 10amps)
			[2, 3.5]	] 	# (zscore, standard deviation)


# Configuration print out


# Current Loop print out
print "\tLooping over the currents..."

# peaks returned from the various algs/cuts
total_peaks_to_check = []

for i in range(len(partition_list)):
	if partition_list[i] != "EBA": continue
	for j in range(len(module_list)):
		if module_list[j] == 16: continue
		print "\t\tLooping over module: ", j, "..."
		peaks_to_check = finder(partition_list[i], 		# which partition
								str(module_list[j]), 	# which module
								config[0][0],			# which method
								config[0][1])			# which cuts
		print "\t\t\tThis peak module has ", len(peaks_to_check), "peaks to check"
		if(peaks_to_check): total_peaks_to_check.append([j,peaks_to_check])
		#total_peaks_to_check.append(peaks_to_check)

# total list of peaks!
# organized as follows: [module#, [list of datetimes w/peaks]
total = 0
for peaks in total_peaks_to_check:
	total += len(peaks[1])
print "Total number of peaks to check: ", total

is_signal = [0]*total
signal = 0
for i,peaks in enumerate(total_peaks_to_check):
	#print burncheck(peaks[0], peaks[1])
	is_signal[i] = burncheck(peaks[0], peaks[1])
	if burncheck(peaks[0], peaks[1]): signal += 1

# Plotting!
print "\n\n\n\nPlotting stuff goes here!!"
purity = 1.*signal / total
print signal 
print purity

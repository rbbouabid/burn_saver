import sys
from peakfinder import finder
from burnchecker import burncheck

def Loop(partition_list, module_list, method, cut):
	# peaks returned from the various algs/cuts
	total_peaks_to_check = []
	
	for i in range(len(partition_list)):
		#if partition_list[i] != "EBA": continue
		for j in range(len(module_list)):
			if module_list[j] == 16: continue
			#print "\t\tLooping over module: ", j, "..."
			peaks_to_check = finder(partition_list[i], 		# which partition
									str(module_list[j]), 	# which module
									1,						# which method
									cut)					# which cuts
			#print "\t\t\tThis peak module has ", len(peaks_to_check), "peaks to check"
			if(peaks_to_check): total_peaks_to_check.append([j,peaks_to_check,i])
			#total_peaks_to_check.append(peaks_to_check)
	
	# total list of peaks!
	# organized as follows: [module#, [list of datetimes w/peaks]
	total = 0
	for peaks in total_peaks_to_check:
		total += len(peaks[1])
	print "Total number of peaks to check: ", total
	
	found_run = 0
	was_burnt = 0
	saveables = 0
	for i,peaks in enumerate(total_peaks_to_check):
		if peaks[2] == 0:
			print "\tPowercycle EBC: ", peaks[0]+1 
		if peaks[2] == 1:
			print "\tPowercycle EBA: ", peaks[0]+1 
		checked = burncheck(peaks[0], peaks[1], peaks[2])
		for j,signal_array in enumerate(checked):
			if signal_array[0] == 1: 
				#print "\t\t..found a MB run!"
				found_run += 1
			if signal_array[1] == 1:
				#print "\t\t..was burnt!!"
				was_burnt += 1
			if signal_array[2] == 1:
				#print "\t\t..could have been saved!!!"
				saveables += 1
	
	return [found_run, was_burnt, saveables, total]


# End

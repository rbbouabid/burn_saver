import sys
from peakfinder import finder
from burnchecker import burncheck

print "this is the top level analysis macro"
print "i call the peakfinder and feed the info to the burnchecker"

partition_list = ["EBA", "EBC", "LBA", "LBC"]
module_list = range(65)
module = "42"

method = 1 # absolute threshold

# peaks returned from the various algs/cuts
peaks_to_check = []


for i in range(len(partition_list)):
	if partition_list[i] != "EBA": continue
	for j in range(len(module_list)):
		if module_list[j] != 42: continue
		peaks_to_check = finder(partition_list[i], str(module_list[j]), method)

print peaks_to_check
burncheck()


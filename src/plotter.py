import sys
import matplotlib.pyplot as plt
from eventLoop import Loop


print "can you ever have too many different files"

# Parameters
Partitions = ["EBC", "EBA"]
Modules = range(1,65)
Method = 1

# Absolute Threshold Study
absolute_threshold_list = [9.9, 10, 10, 10.1, 10.2, 10.3]
#absolute_threshold_list = [10]

total_list = []
signal_list = []
purity_list = []

for index, Cut in enumerate(absolute_threshold_list): 
	results = Loop(Partitions, Modules, Method, Cut)
	total_list.append(results[3])
	signal_list.append(results[0])
	purity_list.append(1.*results[0] / results[3])
	#purity_list.append(Loop(Partitions, Modules, Method, Cut))

print "Total number of candidate PWC: ", total_list
print "Total number of overcurrents with a MB run: ", signal_list
#print absolute_threshold_list


# Purity Plot
purity_fig = plt.figure()
ax = purity_fig.add_subplot(111)
ax.set_xlim([9.5,11])
ax.set_ylim([0,1])
ax.plot(absolute_threshold_list, purity_list, 'ro')
ax.set_ylabel('purity (random values for now!)')
ax.set_xlabel('absolute threshold value')
plt.savefig('show/purity.png')

# End

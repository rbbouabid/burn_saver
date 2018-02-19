import sys
import matplotlib.pyplot as plt
from eventLoop import Loop


print "can you ever have too many different files"

# Parameters
Partitions = ["EBA"]
Modules = range(1,65)
Method = 1

# Absolute Threshold Study
absolute_threshold_list = [10, 10.1, 10.2]
#absolute_threshold_list = [10, 10.1]

total_list = []
signal_list = []
purity_list = []

for index, Cut in enumerate(absolute_threshold_list): 
	results = Loop(Partitions, Modules, Method, Cut)
	total_list.append(results[1])
	signal_list.append(results[0])
	purity_list.append(1.*results[0] / results[1])
	#purity_list.append(Loop(Partitions, Modules, Method, Cut))

print total_list
print absolute_threshold_list

plt.plot(absolute_threshold_list, purity_list, 'ro')

plt.ylabel('purity (random values for now!)')
plt.xlabel('absolute threshold value')

#plt.set_ylim([0,1])
#plt.set_xlim([9,11])

plt.savefig('show/purity.png')

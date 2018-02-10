import sys
print "i find peaks"


try:
	with open("data/EBA_LVPS_42_5VMB_OUTPUT_I.txt") as f:
		for line in f:
			print line


except IOError:
	print "Whoa there! You're trying to open a file you do not have..\n"

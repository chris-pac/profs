#!/usr/bin/python

import sys

targetName=sys.argv[1]

pinFile=targetName + '.pin.results'
cacheFile=targetName + '.cachegrind.thread.basic.results'
reportFile=targetName+'.temp.results.html'

##FILE1###
file1 = open(pinFile,'r')

next(file1)

pin_thread = []
runtime = []
locktime = []

for line in file1:
	temp = line.split()
	pin_thread.append("Thread " + str(temp[0]))
	runtime.append(float(temp[1]))
	locktime.append(float(temp[1])*(float(temp[2]))/100)

file1.close()

##FILE2###
file2 = open(cacheFile,'r')

cache_thread = []
instructions = []
read_misses = []
write_misses = []
pie_data = []

for line in file2:
	temp = line.split()
	cache_thread.append("Thread " + str(int(temp[0]) - 1))
	instructions.append(float(temp[1]))
	read_misses.append(float(temp[2]))
	write_misses.append(float(temp[3]))
	pie_data.append({"name" : "Thread " + str(temp[0]), "y" : float(temp[1])})

file2.close()

##FILE2###
file3= open(reportFile,'r')
reportData = file3.read()
file3.close()


###SUBSTITUTION###

template = open("template.html",'r')
content = template.read()
template.close()


content = content.replace('{{thread_names_pin}}', str(pin_thread))
content = content.replace('{{total_time}}', str(runtime))
content = content.replace('{{lock_time}}', str(locktime))
content = content.replace('{{thread_names_cache}}', str(cache_thread))
content = content.replace('{{instructions}}', str(instructions))
content = content.replace('{{read_misses}}', str(read_misses))
content = content.replace('{{write_misses}}', str(write_misses))
content = content.replace('{{pie_data}}', str(pie_data))
content = content.replace('{{report_data}}', reportData)

finalHTML = open(targetName+'.html', 'w+')

finalHTML.write( content )
finalHTML.close()

#!/usr/bin/python

import sys

targetName=sys.argv[1]

pinFile=targetName + '.pin.results'
cacheFile=targetName + '.cachegrind.thread.basic.results'

file1 = open(pinFile,'r')

next(file1)

thread = []
runtime = []
locktime = []

for line in file1:
	temp = line.split()
	thread.append("Thread " + str(temp[0]))
	runtime.append(float(temp[1]))
	locktime.append(float(temp[1])*(float(temp[2]))/100)

file1.close()

template_pin = open("template_pin.html",'r')
content = template_pin.read()
template_pin.close()

fo = open(targetName+'_pin.html', 'w+')

content = content.replace('{{thread_names}}', str(thread))
content = content.replace('{{total_time}}', str(runtime))
content = content.replace('{{lock_time}}', str(locktime))

fo.write( content )
fo.close()

##############################
file2 = open(cacheFile,'r')

thread = []
instructions = []
read_misses = []
write_misses = []
pie_data = []

for line in file2:
	temp = line.split()
	thread.append("Thread " + str(int(temp[0]) - 1))
	instructions.append(float(temp[1]))
	read_misses.append(float(temp[2]))
	write_misses.append(float(temp[3]))
	pie_data.append({"name" : "Thread " + str(temp[0]), "y" : float(temp[1])})

file2.close()

template_cache = open("template_cache.html",'r')
content = template_cache.read()
template_cache.close()

fo = open(targetName+'_cache.html', 'w+')

content = content.replace('{{thread_names}}', str(thread))
content = content.replace('{{instructions}}', str(instructions))
content = content.replace('{{read_misses}}', str(read_misses))
content = content.replace('{{write_misses}}', str(write_misses))
content = content.replace('{{pie_data}}', str(pie_data))

fo.write( content )
fo.close()

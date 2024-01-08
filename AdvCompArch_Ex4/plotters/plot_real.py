#!/usr/bin/env python

import sys, os
import itertools, operator
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
from pylab import rcParams

def get_params_from_basename(basename):
	tokens = basename.split('_')
	#print(tokens)
	threads = tokens[1].split('-')[0]
	#print(threads)
	grain = tokens[2].split('-')[0]
	grain = grain.split('.')[0]
	return (threads, grain)

def get_time_from_output_file(output_file):
	time = -999
	fp = open(output_file, "r")
	#print(output_file)
	line = fp.readline()
	line = line.split()[1]
	line = line.split(':')[1]
	print(line)
	time = float(line)

	#print(output_file)
	if "MUTEX" in output_file:
		mechanism = "MUTEX"
	elif "/TAS_TS" in output_file:
		mechanism = "TAS_TS"
	elif "/TAS_CAS" in output_file:
		mechanism = "TAS_CAS"
	elif "TTAS_TS" in output_file:
		mechanism = "TTAS_TS"
	elif "TTAS_CAS" in output_file:
		mechanism = "TTAS_CAS"
	#print(mechanism)

	fp.close()

	return time, mechanism

def tuples_by_mechanism(tuples):
	ret = []
	tuples_sorted = sorted(tuples, key=operator.itemgetter(0))
	for key,group in itertools.groupby(tuples_sorted,operator.itemgetter(0)):
		ret.append((key, zip(*map(lambda x: x[1:], list(group)))))
	return ret

global_threads = [1,2,4]

if len(sys.argv) < 2:
	print "usage:", sys.argv[0], "<output_directories>"
	sys.exit(1)

results_tuples = []

#print("hola")

for dirname in sys.argv[1:]:
	path = os.getcwd();
	#print(path)
	basename = os.path.basename(dirname)
	#print(basename)
	output_file1 = path + "/MUTEX/"    + dirname 
	output_file2 = path + "/TAS_CAS/"  + dirname
	output_file3 = path + "/TAS_TS/"   + dirname
	output_file4 = path + "/TTAS_CAS/" + dirname
	output_file5 = path + "/TTAS_TS/"  + dirname 

	(threads, grain) = get_params_from_basename(basename)
	
	(time, mechanism) = get_time_from_output_file(output_file1)
	results_tuples.append((mechanism, threads, time))
	
	(time, mechanism) = get_time_from_output_file(output_file2)
	results_tuples.append((mechanism, threads, time))
	
	(time, mechanism) = get_time_from_output_file(output_file3)
	results_tuples.append((mechanism, threads, time))
	
	(time, mechanism) = get_time_from_output_file(output_file4)
	results_tuples.append((mechanism, threads, time))
	
	(time, mechanism) = get_time_from_output_file(output_file5)
	results_tuples.append((mechanism, threads, time))
	

rcParams['figure.figsize'] = 10, 10
markers = ['.', 'o', 'v', '*', 'D']
fig = plt.figure()
plt.grid(True)
ax = plt.subplot(111)
ax.set_xlabel("$Number of Threads$")
ax.set_ylabel("$Execution Time$")

#print("hola2")

i = 0
tuples_by_mech = tuples_by_mechanism(results_tuples)
print(tuples_by_mech)
for tuple in tuples_by_mech:
	mechanism = tuple[0]
	cycles_axis = tuple[1][1]
	x_ticks = np.arange(0, len(global_threads))
	x_labels = map(str, global_threads)
	ax.xaxis.set_ticks(x_ticks)
	ax.xaxis.set_ticklabels(x_labels)

	print x_ticks
	print cycles_axis
	ax.plot(x_ticks, cycles_axis, label=str(mechanism), marker=markers[i%len(markers)])
	i = i + 1
plt.title("Grain Size = " + grain)

lgd = ax.legend(ncol=len(tuples_by_mech), bbox_to_anchor=(0.9, -0.1), prop={'size':8})
plt.savefig("Grain_Size-"+grain+'-real.png', bbox_extra_artists=(lgd,), bbox_inches='tight')

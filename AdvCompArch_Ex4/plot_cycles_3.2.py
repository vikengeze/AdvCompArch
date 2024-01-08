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
	return (threads, grain)

def get_cycles_from_output_file(output_file):
	cycles = -999
	fp = open(output_file, "r")
	#print(output_file)
	line = fp.readline()
	while line:
		if "Cycles" in line:
			cycles = float(line.split()[2])
		line = fp.readline()

	fp.close()
	#print(output_file)
	if "MUTEX" in output_file:
		version = "MUTEX"
	elif "/TAS_TS" in output_file:
		version = "TAS_TS"
	elif "/TAS_CAS" in output_file:
		version = "TAS_CAS"
	elif "TTAS_TS" in output_file:
		version = "TTAS_TS"
	elif "TTAS_CAS" in output_file:
		version = "TTAS_CAS"

	if "share_all" in output_file:
		communism = "share_all"
	elif "share_L3" in output_file:
		communism = "share_L3"
	elif "share_nothing" in output_file:
		communism = "share_nothing"

	#print(version)

	cycles = cycles / pow(10,5)
	return cycles, version, communism

def tuples_by_version(tuples):
	ret = []
	tuples_sorted = sorted(tuples, key=operator.itemgetter(0))
	for key,group in itertools.groupby(tuples_sorted,operator.itemgetter(0)):
		ret.append((key, zip(*map(lambda x: x[1:], list(group)))))
	return ret

global_threads = ["Share_All", "Share_L3", "Share_Nothing"]

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
	output_file1 = path + "/MUTEX/"    + dirname + "/sim.out"
	output_file2 = path + "/TAS_CAS/"  + dirname + "/sim.out"
	output_file3 = path + "/TAS_TS/"   + dirname + "/sim.out"
	output_file4 = path + "/TTAS_CAS/" + dirname + "/sim.out"
	output_file5 = path + "/TTAS_TS/"  + dirname + "/sim.out"

	#(threads, grain) = get_params_from_basename(basename)
	threads = 4
	grain = 1
	
	(cycles, version, communism) = get_cycles_from_output_file(output_file1)
	results_tuples.append((version, communism, cycles))
	
	(cycles, version, communism) = get_cycles_from_output_file(output_file2)
	results_tuples.append((version, communism, cycles))
	
	(cycles, version, communism) = get_cycles_from_output_file(output_file3)
	results_tuples.append((version, communism, cycles))
	
	(cycles, version, communism) = get_cycles_from_output_file(output_file4)
	results_tuples.append((version, communism, cycles))
	
	(cycles, version, communism) = get_cycles_from_output_file(output_file5)
	results_tuples.append((version, communism, cycles))

rcParams['figure.figsize'] = 10, 10
markers = ['.', 'o', 'v', '*', 'D']
fig = plt.figure()
plt.grid(True)
ax = plt.subplot(111)
ax.set_xlabel("$Topologies$")
ax.set_ylabel("$Number of Cycles(x10^5)$")

#print("hola2")

i = 0
tuples_by_vs = tuples_by_version(results_tuples)
print(tuples_by_vs)
for tuple in tuples_by_vs:
	version = tuple[0]
	cycles_axis = tuple[1][1]
	x_ticks = np.arange(0, len(global_threads))
	x_labels = map(str, global_threads)
	ax.xaxis.set_ticks(x_ticks)
	ax.xaxis.set_ticklabels(x_labels)

	print x_ticks
	print cycles_axis
	ax.plot(x_ticks, cycles_axis, label=str(version), marker=markers[i%len(markers)])
	i = i + 1
plt.title("Cycles per Topology")

lgd = ax.legend(ncol=len(tuples_by_vs), bbox_to_anchor=(0.9, -0.1), prop={'size':8})
plt.savefig("Cycles"+'.png', bbox_extra_artists=(lgd,), bbox_inches='tight')

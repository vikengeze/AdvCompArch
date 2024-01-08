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

def get_time_from_output_file(output_file):
	time = -999
	fp = open(output_file, "r")
	line = fp.readline()
	while line:
		if "Time" in line:
			time = float(line.split()[3])
		line = fp.readline()

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

	fp.close()
	return time, version

def get_energy_from_output_file(output_file):
	energy = 0
	flag=False
	unit = "J"
	fp = open(output_file, "r")
	line = fp.readline()
	while line:
		if "total" in line:
			energy = float(line.split()[3])
			unit = line.split()[4]
		line = fp.readline()

	fp.close()
	if unit=="mJ":
		flag = True
	return (energy,flag)

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
	#print(version)

	cycles = cycles / pow(10,6)
	return cycles, version

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

	output_file1b = path + "/MUTEX/"    + dirname + "/power.total.out"
	output_file2b = path + "/TAS_CAS/"  + dirname + "/power.total.out"
	output_file3b = path + "/TAS_TS/"   + dirname + "/power.total.out"
	output_file4b = path + "/TTAS_CAS/" + dirname + "/power.total.out"
	output_file5b = path + "/TTAS_TS/"  + dirname + "/power.total.out"

	#(threads, grain) = get_params_from_basename(basename)
	threads = 4
	grain = 1
	
	(time, version) = get_time_from_output_file(output_file1)
	(energy,flag) = get_energy_from_output_file(output_file1b)
	time = time / pow(10,6)	
	if flag :
		energy = energy /1000
	edp = energy * time	
	results_tuples.append((version, threads, edp))


	(time, version) = get_time_from_output_file(output_file2)
	(energy,flag) = get_energy_from_output_file(output_file2b)
	time = time / pow(10,6)	
	if flag :
		energy = energy /1000
	#print(edp)
	#print(time)
	edp = energy * time	
	results_tuples.append((version, threads, edp))

	(time, version) = get_time_from_output_file(output_file3)
	(energy,flag) = get_energy_from_output_file(output_file3b)
	time = time / pow(10,6)	
	if flag :
		energy = energy /1000
	edp = energy * time	
	results_tuples.append((version, threads, edp))

	(time, version) = get_time_from_output_file(output_file4)
	(energy,flag) = get_energy_from_output_file(output_file4b)
	time = time / pow(10,6)	
	if flag :
		energy = energy /1000
	edp = energy * time	
	results_tuples.append((version, threads, edp))

	(time, version) = get_time_from_output_file(output_file5)
	(energy,flag) = get_energy_from_output_file(output_file5b)
	time = time / pow(10,6)	
	if flag :
		energy = energy /1000
	edp = energy * time	
	results_tuples.append((version, threads, edp))

rcParams['figure.figsize'] = 10, 10
markers = ['.', 'o', 'v', '*', 'D']
fig = plt.figure()
plt.grid(True)
ax = plt.subplot(111)
ax.set_xlabel("$Topologies$")
ax.set_ylabel("$EDP(/10^3)$")

#print("hola2")

i = 0
tuples_by_vs = tuples_by_version(results_tuples)
#print(tuples_by_vs)
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
plt.title("EDP per Topology")

lgd = ax.legend(ncol=len(tuples_by_vs), bbox_to_anchor=(0.9, -0.1), prop={'size':8})
plt.savefig("EDP.png", bbox_extra_artists=(lgd,), bbox_inches='tight')

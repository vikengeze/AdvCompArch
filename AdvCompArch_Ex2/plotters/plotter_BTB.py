#!/usr/bin/env python

import sys
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

## For nbit predictors
predictors_to_plot = [ "  BTB"]

x_Axis = []
mpki_Axis = []
tpki_Axis = []

fp = open(sys.argv[1])
line = fp.readline()
while line:
	tokens = line.split()
	if line.startswith("Total Instructions:"):
		total_ins = long(tokens[2])
	else:
		for pred_prefix in predictors_to_plot:
			if line.startswith(pred_prefix):
				#print('Here')
				predictor_string = tokens[0].split(':')[0]
				correct_predictions = long(tokens[1])
				incorrect_predictions = long(tokens[2])
				target_predictions = long(tokens[3])
				x_Axis.append(predictor_string)
				mpki_Axis.append(incorrect_predictions / (total_ins / 1000.0))
				tpki_Axis.append(target_predictions / (total_ins / 1000.0))

	line = fp.readline()

fig, ax1 = plt.subplots()
ax1.grid(True)

xAx = np.arange(len(x_Axis))
ax1.xaxis.set_ticks(np.arange(0, len(x_Axis), 1))
ax1.set_xticklabels(x_Axis, rotation=45)
ax1.set_xlim(-0.5, len(x_Axis) - 0.5)
ax1.set_ylim(min(mpki_Axis) - 0.05, max(mpki_Axis) + 0.05)
ax1.set_ylabel("$MPKI$")
line1 = ax1.plot(mpki_Axis, label="mpki", color="red",marker='x')

ax2 = ax1.twinx()
ax2.xaxis.set_ticks(np.arange(0, len(x_Axis), 1))
ax2.set_xticklabels(x_Axis, rotation=45)
ax2.set_xlim(-0.5, len(x_Axis) - 0.5)
ax2.set_ylim(min(tpki_Axis) - 0.05 * min(tpki_Axis), max(tpki_Axis) + 0.05 * max(tpki_Axis))
ax2.set_ylabel("$TargetPKI$")
line2 = ax2.plot(tpki_Axis, label="TargetPKI", color="black",marker='o')

lns = line1 + line2
labs = [l.get_label() for l in lns]

savename = sys.argv[1].split(".")
#print(savename[0])
plt.title(savename[0] + '.' + savename[1] + " - MPKI/TargetPKI")
plt.savefig(savename[0] + '.' + savename[1] + '_BTB' +'.png' ,bbox_inches="tight")

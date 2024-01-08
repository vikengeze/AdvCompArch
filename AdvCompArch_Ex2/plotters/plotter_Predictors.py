#!/usr/bin/env python

import sys
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

## For 4.5, all predictors
predictors_to_plot = [ "  Static Taken", "  Static BTFNT", "  Nbit", "  Pentium-M", "  LocalHistory", "  GlobalHistory", "  Tournament"]

x_Axis = []
mpki_Axis = []
i=0

fp = open(sys.argv[1])
line = fp.readline()
while line:
	tokens = line.split()
	if line.startswith("Total Instructions:"):
		total_ins = long(tokens[2])
	else:
		for pred_prefix in predictors_to_plot:
			if line.startswith(pred_prefix):
				if pred_prefix == "  Static Taken":
					predictor_string = tokens[0] + tokens[1].split(':')[0]
					correct_predictions = long(tokens[2])
					incorrect_predictions = long(tokens[3])
					x_Axis.append(predictor_string)
					mpki_Axis.append(incorrect_predictions / (total_ins / 1000.0))
				if pred_prefix == "  Static BTFNT":
					predictor_string = tokens[0] + tokens[1].split(':')[0]
					correct_predictions = long(tokens[2])
					incorrect_predictions = long(tokens[3])
					x_Axis.append(predictor_string)
					mpki_Axis.append(incorrect_predictions / (total_ins / 1000.0))
				if pred_prefix == "  Nbit":
					predictor_string = tokens[0].split(':')[0]
					correct_predictions = long(tokens[1])
					incorrect_predictions = long(tokens[2])
					x_Axis.append(predictor_string)
					mpki_Axis.append(incorrect_predictions / (total_ins / 1000.0))
				if pred_prefix == "  Pentium-M":
					predictor_string = tokens[0].split(':')[0]
					correct_predictions = long(tokens[1])
					incorrect_predictions = long(tokens[2])
					x_Axis.append(predictor_string)
					mpki_Axis.append(incorrect_predictions / (total_ins / 1000.0))
				if pred_prefix == "  LocalHistory":
					kapa = tokens[0].split(':')[1]
					keepo = kapa.split('(')[2]
					kapa = kapa.split('-')[0]
					keepo = keepo.split(')')[0]
					predictor_string = tokens[0].split('H')[0] + '-' + kapa + '-(' + keepo + ')' 
					correct_predictions = long(tokens[1])
					incorrect_predictions = long(tokens[2])
					x_Axis.append(predictor_string)
					mpki_Axis.append(incorrect_predictions / (total_ins / 1000.0))
				if pred_prefix == "  GlobalHistory":
					kapa = tokens[0].split(':')[1]
					keepo = kapa.split('(')[2]
					kapakeepo = kapa.split('(')[1]
					kapakeepo = kapakeepo.split(')')[0]
					kapa = kapa.split('-')[0]
					keepo = keepo.split(')')[0]
					predictor_string = tokens[0].split('H')[0] + '-' + kapa + '-(' + kapakeepo + ')-('+ keepo + ')' 
					correct_predictions = long(tokens[1])
					incorrect_predictions = long(tokens[2])
					x_Axis.append(predictor_string)
					mpki_Axis.append(incorrect_predictions / (total_ins / 1000.0))				
				if pred_prefix == "  Tournament":
					#print(tokens)
					kapa = tokens[0].split('e')[0] + 'e' + tokens[0].split('e')[1] + '-'
					keepo = tokens[0].split('(')[1]
					keepo = keepo.split('H')[0]
					kapakeepo = tokens[0].split(':')[1]
					kapakeepo = kapakeepo.split('-')[0]
					delta = tokens[0].split('(')[2]
					delta = delta.split(')')[0]
					cyka = tokens[0].split('(')[3]
					cyka = cyka.split(')')[0]
					#print(kapa)
					#print(keepo)
					#print(kapakeepo)
					#print(delta)
					#print(cyka)
					if keepo.startswith("Nbit"):
						keepo1 = keepo.split(',')[0]
						keepo2 = keepo.split(',')[1]
						predictor_string = kapa + keepo1 + '-' + keepo2 + ':' + kapakeepo + '-(' + delta + ')-(' + cyka + ')'
					if keepo.startswith("Local"):
						test = tokens[0].split(',')[3]
						test = test.split('H')[0]
						test1 = tokens[0].split(':')[2]
						test1 = test1.split('-')[0]
						test2 = tokens[0].split('(')[4]
						test2 = test2.split(')')[0]
						test3 = tokens[0].split('(')[5]
						test3 = test3.split(')')[0]
						#print(test3)
						predictor_string = kapa + keepo + ':' + kapakeepo + '-(' + delta + ')-(' + cyka + ')' + '-' + test + ':' + test1 + '-(' + test2 + ')-(' + test3 + ')'
					if keepo.startswith("Global"):
						test = tokens[0].split(',')[2]
						#print(test)
						test = test.split('H')[0]
						test1 = tokens[0].split(':')[2]
						test1 = test1.split('-')[0]
						test2 = tokens[0].split('(')[4]
						test2 = test2.split(')')[0]
						test3 = tokens[0].split('(')[5]
						test3 = test3.split(')')[0]
						#print(test3)
						predictor_string = kapa + keepo + ':' + kapakeepo + '-(' + delta + ')-(' + cyka + ')' + '-' + test + ':' + test1 + '-(' + test2 + ')-(' + test3 + ')'
					#print(predictor_string)
					correct_predictions = long(tokens[1])
					incorrect_predictions = long(tokens[2])
					if i==0:
						predictor_str = 'Alpha'
					else:
						predictor_str = predictor_string.split('-')[0] + str(i)
						print(predictor_string)
					i+=1
					x_Axis.append(predictor_str)
					mpki_Axis.append(incorrect_predictions / (total_ins / 1000.0))
					#TelikoLegend = mpatches.Patc
					#plt.legend(handles = [predictor_string])
	line = fp.readline()

fig, ax1 = plt.subplots()
ax1.grid(True)

xAx = np.arange(len(x_Axis))
ax1.xaxis.set_ticks(np.arange(0, len(x_Axis), 1))
ax1.set_xticklabels(x_Axis, rotation=90)
ax1.set_xlim(-0.5, len(x_Axis) - 0.5)
ax1.set_ylim(min(mpki_Axis) - 0.05, max(mpki_Axis) + 0.05)
ax1.set_ylabel("$MPKI$")
line1 = ax1.plot(mpki_Axis, label="mpki", color="red",marker='x')

savename = sys.argv[1].split(".")
#print(savename[0])
plt.title(savename + " - MPKI")
plt.savefig(savename[0] + '.' + savename[1] + '_Predictors' +'.png' ,bbox_inches="tight")


#!/bin/bash

SNIPER_EXE=/home/viken/sniper-7.3/run-sniper
CONF_DIR=/home/viken/advanced-ca-Spring-2020-ask4-helpcode/ask4.cfg
LOCK_DIR=/home/viken/advanced-ca-Spring-2020-ask4-helpcode/locks
OUT_DIR=/home/viken/advanced-ca-Spring-2020-ask4-helpcode/outputs/3.1.1/MUTEX

for threads in 1 2 4 8 16 ; do
for grain in 1 10 100; do

	if [ "$threads" -le 4 ]
	then
		outDir=$(printf "threads_%02d-grain_%03d-L2_%02d-L3_%02d.out" $threads $grain $threads $threads)
		outDir="${OUT_DIR}/${outDir}"
		sniper_cmd="${SNIPER_EXE} -c ${CONF_DIR} -d ${outDir} -n $threads --roi -g --perf_model/l2_cache/shared_cores=$threads -g --perf_model/l3_cache/shared_cores=$threads -- ${LOCK_DIR} $threads 1000 $grain"
	elif [ "$threads" -eq 8 ]
	then
		outDir=$(printf "threads_%02d-grain_%03d-L2_04-L3_%02d.out" $threads $grain $threads)
		outDir="${OUT_DIR}/${outDir}"
		sniper_cmd="${SNIPER_EXE} -c ${CONF_DIR} -d ${outDir} -n $threads --roi -g --perf_model/l2_cache/shared_cores=4 -g --perf_model/l3_cache/shared_cores=$threads -- ${LOCK_DIR} $threads 1000 $grain"
	else
		outDir=$(printf "threads_%02d-grain_%03d-L2_01-L3_08.out" $threads $grain)
		outDir="${OUT_DIR}/${outDir}"
		sniper_cmd="${SNIPER_EXE} -c ${CONF_DIR} -d ${outDir} -n $threads --roi -g --perf_model/l2_cache/shared_cores=1 -g --perf_model/l3_cache/shared_cores=8 -- ${LOCK_DIR} $threads 1000 $grain"
	fi
	/bin/bash -c "$sniper_cmd"

done
done
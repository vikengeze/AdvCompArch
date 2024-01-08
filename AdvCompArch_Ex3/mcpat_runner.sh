#!/bin/bash

for BENCH in $@; do

for dw in 01 02 04 08 16 32; do
for ws in 016 032 064 096 128 192 256 384; do

./advcomparch_mcpat.py -d /home/viken/advanced-ca-Spring-2020-ask3-helpcode/"$BENCH"/"$BENCH".DW_"$dw"-WS_"$ws".out -t total -o /home/viken/advanced-ca-Spring-2020-ask3-helpcode/"$BENCH"/"$BENCH".DW_"$dw"-WS_"$ws".out/power > /home/viken/advanced-ca-Spring-2020-ask3-helpcode/"$BENCH"/"$BENCH".DW_"$dw"-WS_"$ws".out/power.total.out

done
done
done
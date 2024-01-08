#!/bin/bash

cd gcc
./plot_ipc.py gcc.DW_*-WS_*.out
cd ..

cd mcf	
./plot_ipc.py mcf.DW_*-WS_*.out
cd ..

cd soplex
./plot_ipc.py soplex.DW_*-WS_*.out
cd ..

cd xalancbmk
./plot_ipc.py xalancbmk.DW_*-WS_*.out
cd ..

cd cactusADM
./plot_ipc.py cactusADM.DW_*-WS_*.out
cd ..

cd sjeng
./plot_ipc.py sjeng.DW_*-WS_*.out
cd ..

cd GemsFDTD
./plot_ipc.py GemsFDTD.DW_*-WS_*.out
cd ..

cd omnetpp
./plot_ipc.py omnetpp.DW_*-WS_*.out
cd ..

cd zeusmp
./plot_ipc.py zeusmp.DW_*-WS_*.out
cd ..

cd hmmer
./plot_ipc.py hmmer.DW_*-WS_*.out
cd ..

cd gobmk
./plot_ipc.py gobmk.DW_*-WS_*.out
cd ..

cd astar
./plot_ipc.py astar.DW_*-WS_*.out
cd ..
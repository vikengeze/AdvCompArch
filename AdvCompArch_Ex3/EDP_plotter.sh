#!/bin/bash

cd gcc
./energy.py gcc.DW_*-WS_*.out
cd ..

cd mcf	
./energy.py mcf.DW_*-WS_*.out
cd ..

cd soplex
./energy.py soplex.DW_*-WS_*.out
cd ..

cd xalancbmk
./energy.py xalancbmk.DW_*-WS_*.out
cd ..

cd cactusADM
./energy.py cactusADM.DW_*-WS_*.out
cd ..

cd sjeng
./energy.py sjeng.DW_*-WS_*.out
cd ..

cd GemsFDTD
./energy.py GemsFDTD.DW_*-WS_*.out
cd ..

cd omnetpp
./energy.py omnetpp.DW_*-WS_*.out
cd ..

cd zeusmp
./energy.py zeusmp.DW_*-WS_*.out
cd ..

cd hmmer
./energy.py hmmer.DW_*-WS_*.out
cd ..

cd gobmk
./energy.py gobmk.DW_*-WS_*.out
cd ..

cd astar
./energy.py astar.DW_*-WS_*.out
cd ..
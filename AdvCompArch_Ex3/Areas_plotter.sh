#!/bin/bash

cd gcc
./area.py gcc.DW_*-WS_*.out
cd ..

cd mcf	
./area.py mcf.DW_*-WS_*.out
cd ..

cd soplex
./area.py soplex.DW_*-WS_*.out
cd ..

cd xalancbmk
./area.py xalancbmk.DW_*-WS_*.out
cd ..

cd cactusADM
./area.py cactusADM.DW_*-WS_*.out
cd ..

cd sjeng
./area.py sjeng.DW_*-WS_*.out
cd ..

cd GemsFDTD
./area.py GemsFDTD.DW_*-WS_*.out
cd ..

cd omnetpp
./area.py omnetpp.DW_*-WS_*.out
cd ..

cd zeusmp
./area.py zeusmp.DW_*-WS_*.out
cd ..

cd hmmer
./area.py hmmer.DW_*-WS_*.out
cd ..

cd gobmk
./area.py gobmk.DW_*-WS_*.out
cd ..

cd astar
./area.py astar.DW_*-WS_*.out
cd ..
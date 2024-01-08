#!/bin/bash


/home/viken/sniper-7.3/run-sniper -c /home/viken/advanced-ca-Spring-2020-ask4-helpcode/ask4.cfg -d /home/viken/advanced-ca-Spring-2020-ask4-helpcode/outputs/3.2/TTAS_CAS/share_all -n 4 --roi -g --perf_model/l2_cache/shared_cores=4 -g --perf_model/l3_cache/shared_cores=4 -- /home/viken/advanced-ca-Spring-2020-ask4-helpcode/locks 4 1000 1


/home/viken/sniper-7.3/run-sniper -c /home/viken/advanced-ca-Spring-2020-ask4-helpcode/ask4.cfg -d /home/viken/advanced-ca-Spring-2020-ask4-helpcode/outputs/3.2/TTAS_CAS/share_L3 -n 4 --roi -g --perf_model/l2_cache/shared_cores=1 -g --perf_model/l3_cache/shared_cores=4 -- /home/viken/advanced-ca-Spring-2020-ask4-helpcode/locks 4 1000 1


/home/viken/sniper-7.3/run-sniper -c /home/viken/advanced-ca-Spring-2020-ask4-helpcode/ask4.cfg -d /home/viken/advanced-ca-Spring-2020-ask4-helpcode/outputs/3.2/TTAS_CAS/share_nothing -n 4 --roi -g --perf_model/l2_cache/shared_cores=1 -g --perf_model/l3_cache/shared_cores=1 -- /home/viken/advanced-ca-Spring-2020-ask4-helpcode/locks 4 1000 1

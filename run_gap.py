import os

#shell var


'''
bench_name = ['bfs-twitter','bfs-web','bfs-road','bfs-kron','bfs-urand',
'cc-twitter','cc-web','cc-kron','cc-road','cc-urand',
'bc-twitter','bc-web','bc-road','bc-kron','bc-urand',
'pr-twitter','pr-web','pr-road','pr-kron','pr-urand',
'sssp-twitter','sssp-web','sssp-road','sssp-kron','sssp-urand']
'''

bench_name = ['bfs-twitter','bfs-web','bfs-road','bfs-kron','bfs-urand','cc-twitter','cc-web','cc-kron','cc-road','cc-urand','bc-twitter','bc-web','bc-road','bc-kron','bc-urand','pr-web','pr-road',
'sssp-twitter','sssp-web','sssp-road','sssp-kron','sssp-urand']

#bench_name = ['bc-kron','bc-twitter','bc-urand','bfs-urand','cc-kron','cc-twitter','sssp-twitter','sssp-urand']
output = "./result/LLC_way_10/"
trace = "./gapbs_traces/"
warmup = "250000000"
simul  = "1000000000"

simdir ="../bin/champsim"


#shell command
for name in bench_name:
    os.system("srun nohup ./bin/champsim -warmup_instructions "+warmup+" -simulation_instructions "+simul+" -traces "+trace+name+".champsim.gz > "+output+name+" &")


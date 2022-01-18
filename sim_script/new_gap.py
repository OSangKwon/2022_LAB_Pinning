import os


#shell var

outdir ="../result/new/gap/bpwc/"
simdir ="../bin/champsim"
tracedir = "../trace/"

bench_name = ['bfs-twitter','bfs-web','bfs-kron','bfs-urand','tc-twitter','tc-web','tc-road','tc-kron','tc-urand','bc-twitter','bc-web','bc-kron','bc-urand']
'''
bench_name = ['bfs-twitter','bfs-web','bfs-road','bfs-kron','bfs-urand','cc-twitter','cc-web','cc-kron','cc-road','cc-urand','bc-twitter','bc-web'
,'bc-road','bc-kron','bc-urand','pr-twitter','pr-web','pr-road','pr-kron','pr-urand','tc-twitter','tc-web','tc-road','tc-kron','tc-urand','sssp-twitter','sssp-web','sssp-road','sssp-kron','sssp-urand']
'''


#shell command
for name in bench_name:
    os.system("nohup " + simdir + " -warmup_instructions 500000000 -simulation_instructions 500000000 -traces " + tracedir + name +"-0-1.gz > " + outdir + name +" &")





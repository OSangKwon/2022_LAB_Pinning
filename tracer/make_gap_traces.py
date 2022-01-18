import os


'''
bench_name = ['bfs-twitter','bfs-web','bfs-road','bfs-kron','bfs-urand',
'cc-twitter','cc-web','cc-kron','cc-road','cc-urand',
'bc-twitter','bc-web','bc-road','bc-kron','bc-urand',
'pr-twitter','pr-web','pr-road','pr-kron','pr-urand',
'tc-twitter','tc-web','tc-road','tc-kron','tc-urand',
'sssp-twitter','sssp-web','sssp-road','sssp-kron','sssp-urand']
command = ['-s 1500000000 -t 2000000000 -- ~/benchmark/gapbs/bfs -f ~/benchmark/gapbs/benchmark/graphs/twitter.sg -n1',
'-s 1000000000 -t 2000000000 -- ~/benchmark/gapbs/bfs -f ~/benchmark/gapbs/benchmark/graphs/web.sg -n1',
'-s 500000000 -t 2000000000 -- ~/benchmark/gapbs/bfs -f ~/benchmark/gapbs/benchmark/graphs/road.sg -n1',
'-s 2000000000 -t 2000000000 -- ~/benchmark/gapbs/bfs -f ~/benchmark/gapbs/benchmark/graphs/kron.sg -n1',
'-s 2000000000 -t 2000000000 -- ~/benchmark/gapbs/bfs -f ~/benchmark/gapbs/benchmark/graphs/urand.sg -n1',
'-s 1000000000 -t 2000000000 -- ~/benchmark/gapbs/cc -f ~/benchmark/gapbs/benchmark/graphs/twitter.sg -n1',
'-s 1000000000 -t 2000000000 -- ~/benchmark/gapbs/cc -f ~/benchmark/gapbs/benchmark/graphs/web.sg -n1',
'-s 2000000000 -t 2000000000 -- ~/benchmark/gapbs/cc -f ~/benchmark/gapbs/benchmark/graphs/kron.sg -n1',
'-s 500000000 -t 2000000000 -- ~/benchmark/gapbs/cc -f ~/benchmark/gapbs/benchmark/graphs/road.sg -n1',
'-s 4500000000 -t 2000000000 -- ~/benchmark/gapbs/cc -f ~/benchmark/gapbs/benchmark/graphs/urand.sg -n1',
'-s 2000000000 -t 2000000000 -- ~/benchmark/gapbs/bc -f ~/benchmark/gapbs/benchmark/graphs/twitter.sg -i4 -n1',
'-s 1000000000 -t 2000000000 -- ~/benchmark/gapbs/bc -f ~/benchmark/gapbs/benchmark/graphs/web.sg -i4 -n1',
'-s 2000000000 -t 2000000000 -- ~/benchmark/gapbs/bc -f ~/benchmark/gapbs/benchmark/graphs/road.sg -i4 -n1',
'-s 2000000000 -t 2000000000 -- ~/benchmark/gapbs/bc -f ~/benchmark/gapbs/benchmark/graphs/kron.sg -i4 -n1',
'-s 2000000000 -t 2000000000 -- ~/benchmark/gapbs/bc -f ~/benchmark/gapbs/benchmark/graphs/urand.sg -i4 -n1',
'-s 2000000000 -t 2000000000 -- ~/benchmark/gapbs/pr -f ~/benchmark/gapbs/benchmark/graphs/twitter.sg -i1000 -t1e-4 -n1',
'-s 1000000000 -t 2000000000 -- ~/benchmark/gapbs/pr -f ~/benchmark/gapbs/benchmark/graphs/web.sg -i1000 -t1e-4 -n1',
'-s 1000000000 -t 2000000000 -- ~/benchmark/gapbs/pr -f ~/benchmark/gapbs/benchmark/graphs/road.sg -i1000 -t1e-4 -n1',
'-s 2000000000 -t 2000000000 -- ~/benchmark/gapbs/pr -f ~/benchmark/gapbs/benchmark/graphs/kron.sg -i1000 -t1e-4 -n1',
'-s 2000000000 -t 2000000000 -- ~/benchmark/gapbs/pr -f ~/benchmark/gapbs/benchmark/graphs/urand.sg -i1000 -t1e-4 -n1',
'~/benchmark/gapbs/tc -f ~/benchmark/gapbs/benchmark/graphs/twitterU.sg -n3',
'~/benchmark/gapbs/tc -f ~/benchmark/gapbs/benchmark/graphs/webU.sg -n3',
'~/benchmark/gapbs/tc -f ~/benchmark/gapbs/benchmark/graphs/roadU.sg -n3',
'~/benchmark/gapbs/tc -f ~/benchmark/gapbs/benchmark/graphs/kronU.sg -n3',
'~/benchmark/gapbs/tc -f ~/benchmark/gapbs/benchmark/graphs/urandU.sg -n3',
'-s 500000000 -t 2000000000 -- ~/benchmark/gapbs/sssp -f ~/benchmark/gapbs/benchmark/graphs/twitter.wsg -n1 -d2',
'-s 500000000 -t 2000000000 -- ~/benchmark/gapbs/sssp -f ~/benchmark/gapbs/benchmark/graphs/web.wsg -n1 -d2',
'-s 1000000000 -t 2000000000 -- ~/benchmark/gapbs/sssp -f ~/benchmark/gapbs/benchmark/graphs/road.wsg -n1 -d2',
'-s 1000000000 -t 2000000000 -- ~/benchmark/gapbs/sssp -f ~/benchmark/gapbs/benchmark/graphs/kron.wsg -n1 -d2',
'-s 500000000 -t 2000000000 -- ~/benchmark/gapbs/sssp -f ~/benchmark/gapbs/benchmark/graphs/urand.wsg -n1 -d2']
'''
bench_name= ['pr-twitter','pr-web','pr-road','pr-kron','pr-urand']
command = ['-s 2000000000 -t 2000000000 -- ~/benchmark/gapbs/pr -f ~/benchmark/gapbs/benchmark/graphs/twitter.sg -i1000 -t1e-4 -n1',
'-s 1000000000 -t 2000000000 -- ~/benchmark/gapbs/pr -f ~/benchmark/gapbs/benchmark/graphs/web.sg -i1000 -t1e-4 -n1',
'-s 1000000000 -t 2000000000 -- ~/benchmark/gapbs/pr -f ~/benchmark/gapbs/benchmark/graphs/road.sg -i1000 -t1e-4 -n1',
'-s 2000000000 -t 2000000000 -- ~/benchmark/gapbs/pr -f ~/benchmark/gapbs/benchmark/graphs/kron.sg -i1000 -t1e-4 -n1',
'-s 2000000000 -t 2000000000 -- ~/benchmark/gapbs/pr -f ~/benchmark/gapbs/benchmark/graphs/urand.sg -i1000 -t1e-4 -n1']





#shell command
for i in range(len(command)):
    os.system("nohup pin -t obj-intel64/champsim_tracer.so -o traces/"+bench_name[i]+".champsim " +command[i]+" &")

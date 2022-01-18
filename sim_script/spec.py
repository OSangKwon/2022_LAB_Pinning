import os


#shell var

outdir ="../result/new/spec/init10/"
simdir ="../bin/champsim"
tracedir = "../dpc3_traces/"

file_name = [
'600.perlbench_s-210B.champsimtrace.xz'
,'602.gcc_s-734B.champsimtrace.xz'
,'603.bwaves_s-3699B.champsimtrace.xz','605.mcf_s-665B.champsimtrace.xz','607.cactuBSSN_s-2421B.champsimtrace.xz'
,'619.lbm_s-4268B.champsimtrace.xz'
,'620.omnetpp_s-874B.champsimtrace.xz'
,'621.wrf_s-575B.champsimtrace.xz'
,'623.xalancbmk_s-700B.champsimtrace.xz'
,'625.x264_s-18B.champsimtrace.xz'
,'627.cam4_s-573B.champsimtrace.xz'
,'628.pop2_s-17B.champsimtrace.xz'
,'631.deepsjeng_s-928B.champsimtrace.xz'
,'638.imagick_s-10316B.champsimtrace.xz'
,'641.leela_s-800B.champsimtrace.xz'
,'644.nab_s-5853B.champsimtrace.xz'
,'648.exchange2_s-1699B.champsimtrace.xz'
,'649.fotonik3d_s-1176B.champsimtrace.xz'
,'654.roms_s-842B.champsimtrace.xz'
,'657.xz_s-3167B.champsimtrace.xz']

bench_name = ['perlbench','gcc','bwaves','mcf','cactuBSSN','lbm','omnetpp','wrf','xalancbmk','x264','cam4','pop2','deepsjeng','imagick','leela','nab','exchange','fotonik3d','roms','xz']



#shell command
for i in range(len(file_name)):
    os.system("nohup " + simdir + " -warmup_instructions 10000000000 -simulation_instructions 1000000000 -traces " + tracedir + file_name[i] +"  > " + outdir + bench_name[i] +" &")





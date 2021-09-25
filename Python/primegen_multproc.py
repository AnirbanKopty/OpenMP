# parallelizing the primegen.py code
# multiprocessing

import multiprocessing
from sympy import sieve

import os
os.chdir('C:\\Users\\sapta\\Downloads\\Anirban')

import time

starttime = time.perf_counter()

n = 10**8                            # The Upper limit of prime number

file = open('primeno_thread.txt','w')

def work(p,q):
    for i in sieve.primerange(p,q):
        file.write(str(i)+'\n')

processes = []

for i in range(4):
    p = multiprocessing.Process(target=work, args=[int(i* n/4), int((i+1)* n/4)])
    p.start()
    processes.append(p)

for process in processes:
    process.join()


finishtime = time.perf_counter()

file.write(f'\n\n\n\nThe script finished in {finishtime - starttime} secs')
# parallelizing the primegen.py code

import threading
from sympy import sieve

# import os
# os.chdir('C:\\Users\\sapta\\Downloads\\Anirban')

import time

starttime = time.perf_counter()

n = 10**8                            # The Upper limit of prime number

file = open('primeno_thread.txt','w')

def work(p,q):
    for i in sieve.primerange(p,q):
        file.write(str(i)+'\n')

threads = []

for i in range(4):
    t = threading.Thread(target=work, args=[int(i* n/4), int((i+1)* n/4)])
    t.start()
    threads.append(t)

for thread in threads:
    thread.join()

# print(threads)

finishtime = time.perf_counter()

print(f'\n\n\n\nThe script finished in {finishtime - starttime} secs')

# The script finished in 77.4185289 secs
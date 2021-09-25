from sympy import sieve

import os
os.chdir('C:\\Users\\sapta\\Downloads\\Anirban')

import time

starttime = time.perf_counter()

n = 10**8                            # The Upper limit of prime number

file = open('primeno.txt','w')

for i in sieve.primerange(0,n):
    file.write(str(i)+'\n')

finishtime = time.perf_counter()

file.write(f'\n\n\n\nThe script finished in {finishtime - starttime} secs')

# 35.8870287 sec for [0,10**8) prime number generation and storing that in the text
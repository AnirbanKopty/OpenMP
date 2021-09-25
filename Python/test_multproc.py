import multiprocessing, time

starttime = time.perf_counter()

def do_something():
    print('Sleeping for 1 sec')
    time.sleep(1)
    print("done sleeping")

p1 = multiprocessing.Process(target=do_something)
p2 = multiprocessing.Process(target=do_something)

p1.start()
p2.start()

p1.join()
p2.join()

finishtime = time.perf_counter()

print(f"\nThe script ran in {finishtime - starttime} sec")
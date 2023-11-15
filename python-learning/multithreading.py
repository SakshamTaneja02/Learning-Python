import threading, time

def sleep(second):
    print(f"Going to sleep for {second} seconds")
    time.sleep(second)

#Normal code
# time1 = time.perf_counter()
# sleep(4)
# sleep(2)
# sleep(1)
# time2 = time.perf_counter()
# print(time2-time1)

#Code using threads
time1 = time.perf_counter()
t1 = threading.Thread(target=sleep,args=[4])
t2 = threading.Thread(target=sleep,args=[2])
t3 = threading.Thread(target=sleep,args=[1])
t1.start()
t2.start()
t3.start()
# t1.join()
# t2.join()
# t3.join()
time2 = time.perf_counter()
print(time2-time1)
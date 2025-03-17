import threading 
import time
def fun(seconds):
    print(f"time remaining is {seconds} seconds.")
    time.sleep(seconds)

time1 = time.perf_counter()
t1 =threading.Thread(target=fun, args=[3])
t2=threading.Thread(target=fun, args=[9])


t1.start()
t2.start()

t1.join()
t2.join()

time2 = time.perf_counter()
print(time2-time1)



# print(threading.currentThread().getName())
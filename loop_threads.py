import time
import threading


def loop(num):
    for i in range(num):
        pass


num = 50000000

# Single Thread
start = time.time()
loop(num)
loop(num)
end = time.time()
print('[Single Thread] total time : {}'.format(end - start))

# Multi Thread
start = time.time()
thread1 = threading.Thread(target=loop, args=(num,))
thread2 = threading.Thread(target=loop, args=(num,))
thread1.start()
thread2.start()
thread1.join()
thread2.join()
end = time.time()
print('[Multi Thread] total time : {}'.format(end - start))

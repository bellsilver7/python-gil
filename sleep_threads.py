import time
import threading


def sleep_for_seconds(num):
    time.sleep(num)


num = 2

# Single Thread
start = time.time()
sleep_for_seconds(num)
sleep_for_seconds(num)
end = time.time()
print('[Single Thread] total time : {}'.format(end - start))

# Multi Thread
start = time.time()
thread1 = threading.Thread(target=sleep_for_seconds, args=(num,))
thread2 = threading.Thread(target=sleep_for_seconds, args=(num,))
thread1.start()
thread2.start()
thread1.join()
thread2.join()
end = time.time()
print('[Multi Thread] total time : {}'.format(end - start))

import threading
import time

class MyThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.counter = 0
        self.stop_flag = False

    def run(self):
        lock.acquire()
        self.stop_flag = self.cal_count()
        lock.release()

    def cal_count(self):
        while True:
            self.counter += 1
            time.sleep(1)

            if self.counter == 3:
                stop_flag = True
                return stop_flag

def infinite_loop():
    thread1 = MyThread()
    thread1.start()

    while not thread1.stop_flag:        
        print("run infinite loop...")
        time.sleep(1)
        
    thread1.join()

if __name__ == '__main__':
    global lock
    lock = threading.Lock()

    infinite_loop()
    print("Done.")
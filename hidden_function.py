import threading 
import time 

class MyThread(threading.Thread): 
    def __init__(self): 
        super(MyThread, self).__init__() 
        self._stopper = threading.Event() 
  
    def stop_it(self): 
        self._stopper.set()
  
    def stopped(self): 
        return self._stopper.is_set() 
  
    def run(self): 
        while not self.stopped(): 
            print("run infinite loop...")
            time.sleep(1)

def second_thread_job():
    counter = 0
    while True:
        counter += 1
        time.sleep(1)

        if counter == 3:
            return

if __name__ == '__main__':
    thread1 = MyThread()
    thread1.start()

    thread2 = threading.Thread(target = second_thread_job)
    thread2.start()
    thread2.join()

    if not thread2.is_alive():
        thread1.stop_it()
        thread1.join()

    print("Done.")
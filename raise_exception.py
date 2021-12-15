import threading
import time
import ctypes

class MyThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.counter = 0

    def run(self):
        # target function of the thread class
        while True:
            print("run infinite loop...")
            self.counter += 1
            time.sleep(1)

            if self.counter == 3:
                self.raise_exception()

    def get_id(self): 
        # returns id of the respective thread 
        if hasattr(self, '_thread_id'): 
            return self._thread_id 
        for id, thread in threading._active.items(): 
            if thread is self: 
                return id

    def raise_exception(self): 
        thread_id = self.get_id()
        res = ctypes.pythonapi.PyThreadState_SetAsyncExc(thread_id, 
              ctypes.py_object(SystemExit)) 
        if res > 1: 
            ctypes.pythonapi.PyThreadState_SetAsyncExc(thread_id, 0) 
            print('Exception raise failure')

if __name__ == '__main__':
    thread1 = MyThread()
    thread1.start()
    thread1.join()
    print("Done.")
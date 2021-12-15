import sys 
import trace 
import threading 
import time 

class MyThread(threading.Thread):
    def __init__(self, *args, **keywords):
        threading.Thread.__init__(self, *args, **keywords)
        self.killed = False
  
    def start(self): 
        self.__run_backup = self.run 
        self.run = self.__run       
        threading.Thread.start(self) 
    
    def __run(self): 
        sys.settrace(self.globaltrace) 
        self.__run_backup() 
        self.run = self.__run_backup 
    
    def globaltrace(self, frame, event, arg): 
        if event == 'call': 
            return self.localtrace 
        else: 
            return None
    
    def localtrace(self, frame, event, arg): 
        if self.killed: 
            if event == 'line': 
                raise SystemExit() 
        return self.localtrace 
    
    def kill(self): 
        self.killed = True

def infinite_loop():
    # first thread job
    while True:
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
    thread1 = MyThread(target = infinite_loop)
    thread1.start()

    thread2 = threading.Thread(target = second_thread_job)
    thread2.start()
    thread2.join()

    if not thread2.is_alive():
        thread1.kill()
        thread1.join()
        
    print("Done.")
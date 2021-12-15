import threading 
import time 
import sys 

def thread_job():
    # infinite_loop
    while True:        
        print("run infinite loop...")
        time.sleep(1)  
    
if __name__ == '__main__':
    counter = 0
    thread1 = threading.Thread(target = thread_job)
    thread1.daemon = True
    thread1.start()

    while True:
        counter += 1
        time.sleep(1)

        if counter == 3:
            sys.exit()

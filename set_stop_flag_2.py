import threading
import time

def thread_job(stop_flag):
    # infinite_loop
    while True:        
        print("run infinite loop...")
        time.sleep(1)

        if stop_flag():
            break

if __name__ == '__main__':
    counter = 0
    stop_flag = False
    thread1 = threading.Thread(target = thread_job, args = (lambda : stop_flag, ))
    thread1.start()

    while True:
        counter += 1
        time.sleep(1)

        if counter == 3:
            stop_flag = True
            break

    thread1.join()
    print("Done.")
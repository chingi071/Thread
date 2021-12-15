import threading 
import time 
import ctypes
import inspect
 
def _async_raise(tid, exctype):
    """raises the exception, performs cleanup if needed"""
    tid = ctypes.c_long(tid)
    if not inspect.isclass(exctype):
        exctype = type(exctype)
    res = ctypes.pythonapi.PyThreadState_SetAsyncExc(tid, ctypes.py_object(exctype))
    if res == 0:
        raise ValueError("invalid thread id")
    elif res != 1:
        # """if it returns a number greater than one, you're in trouble,
        # and you should call it again with exc=NULL to revert the effect"""
        ctypes.pythonapi.PyThreadState_SetAsyncExc(tid, None)
        raise SystemError("PyThreadState_SetAsyncExc failed")
 
def stop_thread(thread):
    _async_raise(thread.ident, SystemExit)

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
 
if __name__ == "__main__":
    thread1 = threading.Thread(target = infinite_loop)
    thread1.start()

    thread2 = threading.Thread(target = second_thread_job)
    thread2.start()
    thread2.join()

    if not thread2.is_alive():
        stop_thread(thread1)
        thread1.join()
        
    print("Done.")
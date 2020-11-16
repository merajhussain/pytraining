import threading

import time

def myfunc():
    print("start a thread")
    time.sleep(3)
    print("end a thread")
    
 
threads =[]
 
for i in range(5):
    th = threading.Thread(target=myfunc)
    th.start()
    threads.append(th)
    
    
for th in threads:
    th.join()
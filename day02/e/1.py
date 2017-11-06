#!/usr/bin/python3.5

import threading
import time

class MyThread(threading.Thread):
    def __init__(self,name,run_time):
        super(MyThread,self).__init__()
        self.name = name
        self.run_time = run_time
    def run(self):
        print("running task:",self.name)
        time.sleep(self.run_time)
        a = time.time()
        print("task %s done" %self.name)
        b = time.time() -a
        print(b)
thread_instance = [MyThread(i,1)for i in range(8)]

for a in thread_instance:
    a.start()

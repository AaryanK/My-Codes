import multiprocessing
import concurrent.futures
from functools import partial
import threading
import sys

def make_thread(func,args=None):
    t=threading.Thread(target=func,args=args)
    t.start()    


def make_processes(func,args=None):
    a = multiprocessing.Process(target=func,args=args)
    a.start()
    a.join()
    a.terminate()

'''def execute1(func,args=None):
    with concurrent.futures.ProcessPoolExecutor() as executor:
        f1=executor.submit(func,*args)
        return f1.result()'''

def execute(func,args=None):
    with concurrent.futures.ProcessPoolExecutor() as executor:
        f1=executor.submit(func,args)
        return f1.result()
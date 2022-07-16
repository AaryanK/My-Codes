import concurrent.futures

def execute_threads(func,args=None):
    with concurrent.futures.ThreadPoolExecutor() as executor:
        f1=executor.submit(func,*args)
        return f1.result()

def execute1(func,args=None):
    with concurrent.futures.ProcessPoolExecutor() as executor:
        f1=executor.submit(func,*args)
        return f1.result()

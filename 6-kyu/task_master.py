import threading
import queue

def task_master(slow_functions):
    result_queue = queue.Queue()
    
    def worker(func):
        result_queue.put(func())
    
    threads = []
    for func in slow_functions:
        t = threading.Thread(target=worker, args=(func,))
        t.start()
        threads.append(t)
    
    for t in threads:
        t.join()
    
    total = 0
    while not result_queue.empty():
        total += result_queue.get()
    
    return total

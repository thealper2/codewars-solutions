from concurrent.futures import ThreadPoolExecutor

def task_master(array):
    with ThreadPoolExecutor() as executor:
        results = list(executor.map(lambda f: f(), array))
        
    return sum(results)

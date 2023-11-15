import multiprocessing

def my_func():
    print("Hello",multiprocessing.current_process().name)
process = multiprocessing.Process(target=my_func)
process.start()
process.join()
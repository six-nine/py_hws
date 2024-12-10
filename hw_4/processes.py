from multiprocessing import Process
from fib import fibonacci


if __name__ == "__main__":
    processes = []
    for i in range(10):
        processes.append(Process(target=fibonacci, args=(1000000 + 100 * i,), daemon=True))
        processes[-1].start()

    for process in processes:
        process.join()

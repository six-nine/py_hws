import threading
from fib import fibonacci


if __name__ == "__main__":
    threads = []
    for i in range(10):
        threads.append(threading.Thread(target=fibonacci, args=(1000000 + 100 * i,), daemon=True))
        threads[-1].start()

    for thread in threads:
        thread.join()

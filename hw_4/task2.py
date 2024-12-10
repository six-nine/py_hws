from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
from integrate_func import integrate
import math
import time


if __name__ == "__main__":
    WORKERS = 8
    for workers in range(1, 33):
        for pool_executor_cls in (ThreadPoolExecutor, ProcessPoolExecutor):
            start = time.time()
            with pool_executor_cls(max_workers=workers) as executor:
                futures = []
                for i in range(workers):
                    futures.append(executor.submit(
                        integrate,
                        math.cos,
                        0, math.pi / 2,
                        n_jobs=workers,
                        shift=i
                    ))
                print(sum(map(lambda f: f.result(), futures)))
            end = time.time()
            print(f"Num of workers: {workers}, pool type: {pool_executor_cls}, time: {end - start}")

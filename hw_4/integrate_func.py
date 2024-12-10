def integrate(f, a, b, *, n_jobs=1, shift=0, n_iter=10000000):
    acc = 0
    step = (b - a) / n_iter
    print(f"Starting job, shift = {shift}")
    for i in range(shift, n_iter, n_jobs):
        acc += f(a + i * step) * step
    print(f"End job, shift = {shift}")
    return acc

# factorize.py

from multiprocessing import Pool, cpu_count

def factorize_worker(number):
    factors = [i for i in range(1, number + 1) if number % i == 0]
    return factors

def factorize_parallel(numbers):
    with Pool() as pool:
        result = pool.map(factorize_worker, numbers)
    return result

def get_cpu_count():
    return cpu_count() or 1
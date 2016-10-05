import time
from correcthorse import *

def test(runs, func, *args, **kwargs):
    start_time =  time.time()
    for _ in range(runs):
        func(*args, **kwargs)
    elapsed_time = time.time() - start_time
    average_time = elapsed_time / runs
    print('Test result: elapsed time = %s, average time = %s seconds' % (elapsed_time, average_time))

if __name__ == '__main__':
    with open('20k.txt') as file:
        test(100, get_random_lines, file=file, num_of_lines=3)

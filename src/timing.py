from contextlib import contextmanager
import time

@contextmanager
def timeit_context(name):
    start_time = time.time()
    yield
    elapsed_time = time.time() - start_time
    print('\t[{}] finished in {} ms'.format(name, int(elapsed_time * 1_000)))
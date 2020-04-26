import time


def time_performance(function):
    def timed_function(*args, **kwargs):
        start = time.perf_counter()
        result = function(*args, **kwargs)
        fin = time.perf_counter()
        print("{0}: Ran in  {1:0.4f} seconds".format(function.__name__, fin - start))
        return result

    return timed_function

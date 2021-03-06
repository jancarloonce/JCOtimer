import time


def timer(some_function):

    """
    Outputs the time a function takes
    to execute.
    """

    def wrapper(*args, **kwargs):
        t1 = time.time()
        some_function(*args, **kwargs)
        t2 = time.time()
        return "Time it took to run the function: %.20f secs" % float(t2 - t1)
    return wrapper


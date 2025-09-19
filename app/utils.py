import time
from functools import wraps

def timestamp_log(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        start = time.time()
        response = f(*args, **kwargs)
        end = time.time()
        print(f"Request took {end - start:.4f} seconds")
        return response
    return wrapper

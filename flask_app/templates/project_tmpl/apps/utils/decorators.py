import time
from functools import wraps
from flask import jsonify


def fixture(when=['before'], caller=None, fargs=[], fkwargs={}):
    def warp(func):
        @wraps(func)
        def inner(*args, **kwargs):
            if 'before' in when:
                print('before')
                caller(*fargs, **fkwargs)

            ts = time.time()
            ret = func(*args, **kwargs)
            te = time.time()
            if isinstance(ret, dict):
                ret['time_cost'] = te - ts

            if 'after' in when:
                print('after')
                caller(*fargs, **fkwargs)

            return jsonify(ret)
        return inner
    return warp

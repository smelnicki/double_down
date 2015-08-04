from functools import wraps


def double_down(f):
    @wraps(f)
    def wrapped(*args, **kwargs):
        """ Call to function once before returning. """
        f(*args, **kwargs)
        return f(*args, **kwargs)

    return wrapped

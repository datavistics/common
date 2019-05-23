from functools import wraps
from pprint import pformat
from timeit import default_timer as timer


# https://stackoverflow.com/a/26151604
def parametrized(dec):
    def layer(*args, **kwargs):
        def repl(f):
            return dec(f, *args, **kwargs)

        return repl

    return layer


@parametrized
def log_args(f, module_logger):
    @wraps(f)
    def wrapper(*args, **kwargs):
        result = f(*args, **kwargs)
        if args:
            module_logger.info(f"Args: {pformat(*args)}", extra={'name_override': f.__name__})
        if kwargs:
            module_logger.info(f"KWArgs: {pformat(**kwargs)}", extra={'name_override': f.__name__})
        return result

    return wrapper


@parametrized
def log_speed(f, module_logger):
    @wraps(f)
    def wrapper(*args, **kwargs):
        start = timer()
        result = f(*args, **kwargs)
        end = timer()
        module_logger.info(f'{f.__name__} - elapsed time: {end - start:.4f} seconds')
        return result

    return wrapper

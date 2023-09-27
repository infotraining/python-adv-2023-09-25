from functools import wraps
from typing import Callable, TypeVar

def nullable(func: Callable) -> Callable:

    @wraps(func)
    def _nullable(x):
        if x is None:
            return None
        else:
            return func(x)
        
    return _nullable
    

@nullable
def square(x: float) -> float:
    return x * x

def test_nullable():
    assert square(None) is None
    assert square(2.0) == 4.0


#########################################################

class bad_char_remove:
    def __init__(self, *args):
        self.chars_to_remove = args

    def __call__(self, func):

        def _bad_char_remove_decorator(currency: str):
            for char in self.chars_to_remove:
                currency = currency.replace(char, '')
            return func(currency)

        return _bad_char_remove_decorator


@bad_char_remove("$", ",")
def currency_to_float(text: str) -> float:
    return float(text)

# currency_to_float = bad_char_remove("$", ",")(currency_to_float)

def test_bad_char_remove():
    assert currency_to_float("13") == 13
    assert currency_to_float("$3.14") == 3.14
    assert currency_to_float("$1,701.99") == 1701.99
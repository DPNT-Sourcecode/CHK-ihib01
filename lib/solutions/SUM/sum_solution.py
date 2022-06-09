# noinspection PyShadowingBuiltins,PyUnusedLocal
def compute(x: int, y: int):
    if type(x) != int or type(y) != int:
        raise ValueError
    else:
        return x + y


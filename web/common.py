import os


def from_root(*args):
    root = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(root, *args)


def is_int(string):
    try:
        int(string)
        return True
    except ValueError:
        return False

import sys
from .config import Settings, Config

def _exception_hook(exception_type, value, traceback):
    if Settings.traceback:
        sys.__excepthook__(exception_type, value, traceback)
    else:
        print(f"{exception_type.__name__}: {value}")

sys.excepthook = _exception_hook

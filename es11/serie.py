import numpy 
import ctypes

_libserie = numpy.ctypeslib.load_library('libserie', '.')

url = "."

_libserie.fibonacci.argtypes = [ctypes.c_int]
_libserie.fibonacci.restype  = ctypes.c_double

def fibonacci (n) :
    return _libserie.fibonacci(int(n))

import numpy as np
import ctypes
import matplotlib.pyplot as plt

def read_camera():
    mycamera = np.ctypeslib.load_library('libmycamera', '.')
    width = 1536
    height = 1024
    size = width * height*2

    buffer = ctypes.create_string_buffer(size)

    dati = np.frombuffer(buffer, dtype = np.uint8)
    image = np.zeros((height, width), dtype=np.uint16)
    for j in range (0, len(dati), 2):
        pixel = dati[j] + (dati[j+1]<<8)
        y = (j // 2) // width
        x = (j // 2) % width
        image [y,x] = pixel

    return image
import matplotlib.pyplot as plt
from camera import read_camera

try:
    image = read_camera()
    print('ok')
except RuntimeError as e:
    print('errore {e}')
    exit(1)

plt.imshow(image, cmap='gray')
plt.colorbar()
plt.show()
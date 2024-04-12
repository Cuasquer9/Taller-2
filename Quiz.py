import numpy as np
import pandas as pd
import scipy.io as sio

#punto 1
matriz_4d = np.random.rand(15,20,40,100)

#punto 2
matriz_3d = matriz_4d.copy()[:, :, 0]

#punto 3
print("Atributos de la matriz 3d: ")
print("Dimensiones: ", matriz_3d.ndim)
print("Tamaño: ", matriz_3d.size)
print("Forma: ", matriz_3d.shape)
print("Tipo de datos: ", matriz_3d.dtype)

#punto 4
matriz_2d = matriz_3d.reshape((15*20,100))
print("Tamaño: ", matriz_2d.size)
# print("Forma: ", matriz_2d.shape)
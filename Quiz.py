import numpy as np
import pandas as pd
import scipy.io as sio

#punto 1
matriz_4d = np.random.rand(15,20,40,100)

#punto 2
matriz_3d = matriz_4d.copy()[:, :, 0]

#punto 3
print("Atributos de la Matriz 3D: ")
print("Dimensiones: ", matriz_3d.ndim)
print("Tamaño 3D: ", matriz_3d.size)
print("Forma 3D: ", matriz_3d.shape)
print("Tipo de datos: ", matriz_3d.dtype)

#punto 4
matriz_2d = matriz_3d.reshape((15*20,100))
print("Atributos Matriz 2D")
print("Dimensiones: ", matriz_2d.ndim)
print("Tamaño 2D: ", matriz_2d.size)
print("Forma 2D: ", matriz_2d.shape)

#punto 5
def matriz_a_df(matriz_2d):
    df = pd.DataFrame(matriz_2d)
    return df

#punto 6
def cargar_archivo_mat(archivo):
    datos = sio.loadmat(archivo)
    return datos
def cargar_archivo_csv(archivo):
    datos = pd.read_csv(archivo)
    return datos
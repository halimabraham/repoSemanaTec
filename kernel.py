import numpy as np
import cv2
import matplotlib.pyplot as plt
from convolution import convolution
from scipy import signal


def sobel(img, tam, verbose=False):
    # EN ESTA PARTE DEFINIMOS LOS PARAMETROS INICIALES DE KERNEL (3X3)
    ver = np.array([[1],[2],[1]])
    hor = np.array([[1,0,-1]])
    filtro3 = ver*hor

    # CUANDO KERNEL ES MAYOR QUE 3X3, SE LE AGREGARA LA FUNCION 
    # QUE MULTIPLICA KERNEL PARA SABER SI KERNEL ES MAYOR
    if tam == 3:
        filtro = filtro3
    else:
        filtro = filtro3
        while tam > 3:
            hor2 = np.array([[1,2,1]])
            filtro = signal.convolve2d(ver*hor2, filtro)
            print("METODO SOBEL : ")
            print(filtro)
            tam = tam - 2
    
    # CONVOLUCIONAMOS EL KERNEL QUE SE NOS INDICA Y NOS MUESTRA EL RESULTADO ('X' 'Y')
    nuevaImg = convolution(img, filtro, verbose)

    if verbose:
        plt.imshow(nuevaImg, cmap='gray')
        plt.title("Borde Horizontal")
        plt.show()

    new_img_y = convolution(img, np.flip(filtro.T, axis=0), verbose)

    if verbose:
        plt.imshow(new_img_y, cmap='gray')
        plt.title("Borde Vertical")
        plt.show()

    # CALCULAMOS EL GRADIANTE KERNEL
    magnitud = np.sqrt(np.square(nuevaImg) + np.square(new_img_y))

    magnitud *= 255.0 / magnitud.max()
    
    if verbose:
        plt.imshow(magnitud, cmap='gray')
        plt.title("Magnitud del Gradiante")
        plt.show()

    return magnitud

sobel()

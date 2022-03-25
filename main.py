import numpy as np
import cv2
import argparse
import matplotlib.pyplot as plt
import math
from convolution import convolution
from sobel import metodo_sobel
from simple import metodo_simple
from mexicanHat import metodo_MexHat
import urllib.request as urllib

#Lee la imagen desde el internet y lo convierte a una matriz
resp = urllib.urlopen("https://as01.epimg.net/meristation/imagenes/2020/09/09/noticias/1599647767_244123_1599647831_noticia_normal.jpg")
image = np.asarray(bytearray(resp.read()), dtype="uint8")
image = cv2.imdecode(image, cv2.IMREAD_GRAYSCALE)

#Agrega un padding de 50 pixeles a la imagen en todas las direcciones
def pad_with(vector, pad_width, iaxis, kwargs):
        pad_value = kwargs.get('padder', 10)
        vector[:pad_width[0]] = pad_value
        vector[-pad_width[1]:] = pad_value

image = np.pad(image, 50, pad_with, padder=0)

size=int(input("Longitud del kernel que se desea: "))
if size % 2 == 0:
    size = size + 1
    
#Metodo_Sobel
metodo_sobel(image, size, verbose=True)

#Metodo_Simple
metodo_simple(image, size, verbose=True)

#Mexican_Hat
metodo_MexHat(image, size, 4, verbose=True)
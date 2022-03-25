# Función Kernel
### repoSemanaTec

## Integrantes del equipo
Santiago Alberto Sorzano Mongel
Carlos Emilio Murillo Millán
Halim Abraham Hamanoiel Galindo

***Para nuestra semana Tec se nos pidió realizar una evidencia en la cual se realice un código de python el cual realice una función de Kernel, la cual se definirán y describirán a continuación.***

## ¿Qué es la Convolución?
Una **operación matemática** con dos funciones, que es la representación más general del proceso de filtrado lineal *(invariante)*. La **convolución** puede ser aplicada a dos funciones cualesquiera de tiempo o espacio *(u otras variables)* para arrojar una tercera función, la salida de la **convolución**. Si bien la definición matemática es simétrica con respecto a las dos funciones de entrada, es común en el procesamiento de las señales decir que una de las funciones es un filtro que actúa sobre la *otra función*. La respuesta de muchos sistemas físicos puede ser representada matemáticamente mediante una **convolución**. *Por ejemplo, una convolución puede ser utilizada para modelar el filtrado de la energía sísmica por las diversas capas de rocas;* La deconvolución se utiliza extensivamente en el procesamiento sísmico para contrarrestar ese filtrado.

![Kernel](https://upload.wikimedia.org/wikipedia/commons/thumb/2/21/Comparison_convolution_correlation.svg/1200px-Comparison_convolution_correlation.svg.png)

La forma matemática de la convolución de dos funciones, un filtro f(t) y una serie de tiempo x(t), es:

y(t) = ∫ f(t−τ)x(τ)dτ,

donde y(t) es el resultado de la convolución.

En el dominio de la frecuencia, la convolución es simplemente el producto de las transformadas de Fourier (FT) de las dos funciones:

Y(ω) = F(ω)*X(ω),

donde
X(ω) = FT de la serie de tiempo x(t)
F(ω) = FT del filtro f(t)
Y(ω) = FT del resultado y(t)
ω = frecuencia angular.

>*Link a la cita* https://glossary.oilfield.slb.com/es/terms/c/convolution

## ¿Qué es un Kernel?
**Las Funciones Kernel**. Son funciones *matemáticas* que se emplean en las Máquinas de Soporte Vectorial. Estas funciones son las que le permiten convertir lo que sería un problema de clasificación no lineal en el espacio dimensional original, a un sencillo problema de clasificación lineal en un espacio dimensional mayor.
>*Link a la cita* https://www.ecured.cu/Funci%C3%B3n_Kernel

![Kernel](https://www.ecured.cu/images/9/9b/Kernel1.jpg)

## Sobel
El operador de Sobel se utiliza en el procesamiento de imágenes, especialmente en algoritmos de detección de bordes. Técnicamente, es un operador diferencial discreto que calcula una aproximación del gradiente de la función de intensidad de la imagen. Para cada punto de la imagen a procesar, el resultado del operador de Sobel es tanto el vector de gradiente correspondiente como la norma de este vector.
>*Referencia* https://docs.gimp.org/2.8/es/plug-in-sobel.html 

![sobel](https://www.researchgate.net/profile/Jose-Fernandez-Gallego/publication/287409519/figure/fig6/AS:401495624306693@1472735424645/RESULTADO-DE-APLICAR-EL-OPERADOR-SOBEL-SOBRE-LA-IMAGEN-EN-EL-DISPOSITIVO-ZEUS-EPIC-520.png)

## Simple
El módulo Simple.py que usa numpy, matplotlib y la biblioteca de convolución es el último módulo que construimos. El código implementa la función simple method, que se encarga de solicitar tres parámetros correspondientes a imagen, size, verbose=False, para no destruir la estructura de otros kernels. Esta función nos permite usar el kernel para calcular el tamaño del tamaño previamente solicitado creando un arreglo, y el kernel usado antes es 1/size^2, mostrando así el efecto en la imagen por convolución y el kernel ya obtenido.

![simple](https://d500.epimg.net/cincodias/imagenes/2016/07/28/lifestyle/1469730076_088143_1469730170_noticia_normal.jpg)

## Mexican Hat
En las matemáticas y las analíticas numéricas, el Sombrero Mexicano o también conocido como la wavelet de Ricker es la segunda derivada negativa normalizada de una función gaussiana, es decir, a escala y normalización, la segunda función de Hermite. Es un caso especial de la familia de ondículas continuas conocidas como ondículas herminitanas. 
El Sombrero Mexicano se emplea con frecuencia para modelar datos sísmicos y como un término fuente de amplio espectro en electrodinámica computacional.

>*Referencia* https://wiki.seg.org/wiki/Dictionary:Ricker_wavelet 

![lol](https://www.mariowiki.com/Sombrero_Guy)

## Resultados

Horizontal Edge
![Horizontal edge]https://drive.google.com/file/d/19c5PW277VF9m-0so9RGR0hyZ1MTOmC0x/view)

Vertical Edge
![Vertical edge](https://drive.google.com/file/d/1ECVdlosisxTmkariPlYvN8jOy1ssBJz5/view)

Gradient Magnitude
![Gradient Magnitude](https://drive.google.com/file/d/1ss1de4rjOIiOLqQafibITZuwonKyGR6m/view)

Simple
![Simple](https://drive.google.com/file/d/1MvPNuE7v4KZUEXKT70_9YXYcj3uDY5sS/view)

Kernel Mexican Hat
![Kernel Mexican Hat](https://drive.google.com/file/d/1h5eh-nQd66AbkeRcJmD_vjZDAbiW67du/view)

Mexican Hat con convolución
![Mexican Hat con convolución](https://drive.google.com/file/d/1wLoQjw7XzxqK2_4fs2R0g1wiXZL4l48a/view)

# Función Kernel
### repoSemanaTec

***Para nuestra semana Tec se nos pidió realizar una evidencia en la cual se realice un código de python el cual realice una función de Kernel, la cual se definirá y describirá a continuación.***

## ¿Qué es la Convolución?
Una **operación matemática** con dos funciones, que es la representación más general del proceso de filtrado lineal *(invariante)*. La **convolución** puede ser aplicada a dos funciones cualesquiera de tiempo o espacio *(u otras variables)* para arrojar una tercera función, la salida de la **convolución**. Si bien la definición matemática es simétrica con respecto a las dos funciones de entrada, es común en el procesamiento de las señales decir que una de las funciones es un filtro que actúa sobre la *otra función*. La respuesta de muchos sistemas físicos puede ser representada matemáticamente mediante una **convolución**. *Por ejemplo, una convolución puede ser utilizada para modelar el filtrado de la energía sísmica por las diversas capas de rocas;* la deconvolución se utiliza extensivamente en el procesamiento sísmico para contrarrestar ese filtrado.

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


## Función Kernel ...
![sobel](https://i.stack.imgur.com/iShhS.png)

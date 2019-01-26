#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math # Импорт библиотек math, numpy и подбиблиотеки matplotlib.pyplot
import numpy  # с использованием последней с именем mpp
import matplotlib.pyplot as mpp 


if __name__=='__main__': # Условие позволяющее импортировать последующий код
    arguments = numpy.r_[0:200:0.1] #Задание массива аргументов от 0 до 200 с шагом 0.1
                                    #с помощью библиотеки numpy 
    mpp.plot( # Вызов создания графика с помощью подбиблиотеки matplotlib.pyplot
        arguments, # Задание аргументов и значений равных sin(x)*sin(x/20.0)
        [math.sin(a) * math.sin(a/20.0) for a in arguments] 
    ) # Это несмайлик не удоляй подумой 
    mpp.show() # Показат график

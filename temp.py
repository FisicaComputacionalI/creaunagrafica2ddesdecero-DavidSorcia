import numpy as np
import pylab as pl

x = [1,2,3,4]
y = [8.5, 8.25, 8.4, 8]

pl.title('Promedio por semestres a lo largo de la carrera', fontsize = 18, color = 'blue')
pl.xlabel('Numero de Semestre', fontsize = 12, color = 'red')
pl.ylabel('Promedio Obtenido', fontsize = 12, color = 'green')

pl.axis([1,4, 8,9])
pl.plot(x,y)

pl.savefig('templ.png')
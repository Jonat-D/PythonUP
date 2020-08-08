#Built-in Functions /  Funciones integradas
print(x, sep='y') #prints x objects separated by y / imprime x objetos separados por y

input(s) #prints s and waits for an input that will be returned / imprime sy espera una entrada que será devuelta

len(x) #returns the length of x (s, L or D) / Devuelve la longitud de x (s, L o D)

min(L) #returns the minimun value in L / devuelve el valor mínimo en L

max(L) #returns the maximun values in L / devuelve el valor maximo en L

sum(L) #returns the sum of the values in L / devuelve la suma de los valores en L

range(n1,n2,n3) #returns a sequence of numbers from n1 to n2 in steps of n / returns a sequence of numbers from n1 to n2 in steps of n

abs(n) #returns the absolute value of n / devuelve el valor absoluto de n

round(n1,n) #returns the n1 number rounded to n digits / devuelve el número n1 redondeado a n dígitos

type(x) #returns the type of x (string, float,list,dict...) / devuelve el tipo de x (string, float, list, dict ...)

str(x) #converts x to a string / convierte x en una cadena

list(x) #converts x to a list / convierte x en una lista

int(x) #converts x to a integer / convierte x en entero

float(x) #converts x to float number / convierte x en número flotante

help(s) #prints help about x / imprime ayuda sobre x

map(function, L) #applies function to values in L / aplica la función a los valores en L

#Conditionals statem,ents / Declaraciones condicionales

if <condition>:
    <code>
    else if<condition>
        <code>
    ...
    else:
        <code>

if<value>in<list>:

#Data validation / Validacion de datos
try:
    <code>
except<error>:
    <code>
else:
    <code>

#Working with files and folders / Trabajar con archivos y carpetas
import os
os.getcwd()
os.makedirs(<path>)
os.chdir(<path>)
os.listdir(<path>)

#Loops / Bucles
while<condition>:
    <code>

for<variable>in<list>:
    <code>

for<variable>in
    range(start,stop,step):
    <code>
for key, value in
    dict.tems():
    <code>

#Loop Control statements / Declaraciones de control de bucle
break #finishes loop / termina lazo

continue #jumps to next iteration / salta a la siguiente iteración

pass #does nothing / no hace nada

#running externals programs / ejecutar programas externos
import os
os.system(<command>)

#Functions / Las funciones
def function(<params>):
    <code>
    return<data>

#Modules / Modulos
import module
module.function()

from module import*
function()

#reading and writing files / leer y escribir archivos
f=open(<path>,'r')
f.read(<size>)
f.readline(<size>)
f.close()

f=open(<path>,'r')
for line in f:
    <code>
f.close()
f=open(<path>,'W')
f.write(<str>)
f.close()

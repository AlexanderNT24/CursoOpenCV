import numpy as np

#Lista de valores
lista=[1,2,3]
#Convertimos a array
array=np.array(lista)
print(array)
print(array[1])

#np.arange(desde,hasta,saltos)
arrayDel0al20=np.arange(0,20,2)

print(arrayDel0al20)

matrizUnos=np.ones(shape=(5,4))
print(matrizUnos)

#np.random.randint(entre,entre,cuantos)
aleatorios=np.random.randint(2,100,50)
print(aleatorios)
#Poscion valor max
posValorMayor=aleatorios.argmax()
print(posValorMayor)
#Poscion valor min
posValorMin=aleatorios.argmin()
print(posValorMin)
#Valor max
valorMayor=aleatorios.max()
print(valorMayor)
#Valor min
valorMenor=aleatorios.min()
print(valorMenor)
#Forma
forma=aleatorios.shape
print(forma)
#Cambiar forma reshape(filas,colomunas)
aleatorios=aleatorios.reshape(10,5)
print(aleatorios)


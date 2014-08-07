import random

def burbuja(lista):
  for pasada in range(1,  len(lista)-1):
    for i in range(0, len(lista)-1):
      if lista[i] > lista[i+1]:
        lista[i], lista[i+1] = lista[i+1], lista[i]
  return lista


def seleccion (lista):
  for i in range(0, len(lista)-1):
    indiceMenor = i
    for j in range(i+1, len(lista)):
      if lista[j] < lista[indiceMenor]:
        indiceMenor = j
    if i!= indiceMenor:
      lista[i], lista[indiceMenor] = lista[indiceMenor], lista[i]
  return lista



def crearLista (largoLista):
    lista = []
    contador = 0
    while (contador != largoLista) :
        num = random.randrange(largoLista)
        lista.append(num)
        contador += 1
    return lista

listaPrueba1 = crearLista(1000)
listaPrueba2 = crearLista(5000)
listaPrueba3 = crearLista(10000)

#print(burbuja(listaPrueba1))
#print(burbuja(listaPrueba2))
#print(burbuja(listaPrueba3))



#print(seleccion(listaPrueba1))
#print(seleccion(listaPrueba2))

print(seleccion(listaPrueba3))
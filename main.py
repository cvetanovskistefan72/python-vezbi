##main


lista = [1,2,3,4,5,6]


#TODO sortiranje na lista
lista.reverse()
#TODO izvadi parni neparni

parni = []
for item in lista:
    if item % 2 == 0:
        parni.append(item)


print(parni)
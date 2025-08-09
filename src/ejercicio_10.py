def suma_tuplas(tupla1, tupla2):
    suma = tuple(tupla1[i] + tupla2[i] for i in range(len(tupla1)))
    return suma


print(suma_tuplas((1, 2, 3), (4, 5, 6)))

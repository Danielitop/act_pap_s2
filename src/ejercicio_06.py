import random
import math

def puntos_en_circulo():
    puntos = tuple((random.uniform(-10, 10), random.uniform(-10, 10)) for _ in range(10))
    dentro = []

    for x, y in puntos:
        distancia = math.sqrt(x**2 + y**2)
        if distancia <= 5:
            dentro.append((x, y))
    
    print("Puntos generados:", puntos)
    print("Dentro del círculo:", dentro)


puntos_en_circulo()

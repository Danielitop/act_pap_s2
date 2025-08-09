def buscar_palabras(lista_palabras):
    letra = input("Ingresa una letra para buscar: ").lower()
    encontradas = []

    for palabra in lista_palabras:
        for caracter in palabra:
            if caracter.lower() == letra:
                encontradas.append(palabra)
                break
    return encontradas


palabras = ["casa", "perro", "gato", "elefante", "avion"]
print("Palabras encontradas:", buscar_palabras(palabras))

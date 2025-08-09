def sistema_calificaciones():
    calificaciones = []
    while True:
        entrada = input("Ingresa una calificación o 'fin' para terminar: ")
        if entrada.lower() == 'fin':
            break
        try:
            calificaciones.append(float(entrada))
        except ValueError:
            print("Por favor, ingresa un número válido.")

    if calificaciones:
        promedio = sum(calificaciones) / len(calificaciones)
        print("Promedio:", promedio)
        print("Nota más alta:", max(calificaciones))
        print("Nota más baja:", min(calificaciones))
    else:
        print("No se ingresaron calificaciones.")


sistema_calificaciones()

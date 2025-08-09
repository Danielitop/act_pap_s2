def filtrar_estudiantes(estudiantes):
    filtrados = tuple(est for est in estudiantes if est[2] > 8.0)
    return filtrados


estudiantes = (
    ("Ana", 20, 9.1),
    ("Luis", 22, 7.8),
    ("Maria", 19, 8.5)
)
print("Estudiantes con promedio > 8.0:", filtrar_estudiantes(estudiantes))

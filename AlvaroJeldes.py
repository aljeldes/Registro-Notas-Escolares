import os
import json

def cargar_datos():
    datos = {}
    if os.path.exists("estudiantes.json"):
        with open("estudiantes.json", "r") as f:
            datos = json.load(f)
    return datos


def guardar_datos(datos):
    with open("estudiantes.json", "w") as f:
        json.dump(datos, f, indent=4)

def registrar_estudiante(datos):
    nombre = input("Ingrese el nombre del estudiante: ")
    apellido = input("Ingrese el apellido del estudiante: ")
    matematicas = float(input("Ingrese la nota de Matemáticas del estudiante: "))
    ciencias = float(input("Ingrese la nota de Ciencias del estudiante: "))
    historia = float(input("Ingrese la nota de Historia del estudiante: "))

    promedio = (matematicas + ciencias + historia) / 3

    estudiante = {
        "nombre": nombre,
        "apellido": apellido,
        "notas": {
            "matematicas": matematicas,
            "ciencias": ciencias,
            "historia": historia
        },
        "promedio": promedio
    }


    nombre_completo = f"{nombre} {apellido}"
    datos[nombre_completo] = estudiante

    guardar_datos(datos)
    
    print(f"\nEstudiante {nombre_completo} registrado correctamente.\n")

def buscar_estudiante(datos):
    nombre_buscar = input("Ingrese el nombre del estudiante a buscar: ")
    
    if nombre_buscar in datos:
        estudiante = datos[nombre_buscar]
        print("\nDatos del estudiante encontrado:")
        print(f"Nombre: {estudiante['nombre']} {estudiante['apellido']}")
        print(f"Notas: Matemáticas: {estudiante['notas']['matematicas']}, Ciencias: {estudiante['notas']['ciencias']}, Historia: {estudiante['notas']['historia']}")
        print(f"Promedio: {estudiante['promedio']}\n")
    else:
        print(f"\nEstudiante {nombre_buscar} no encontrado.\n")

def mostrar_lista_estudiantes(datos):
    if datos:
        print("\nLista de Estudiantes:")
        for nombre_completo, estudiante in datos.items():
            print(f"{nombre_completo}: Promedio {estudiante['promedio']}")
        print()
    else:
        print("\nNo hay estudiantes registrados.\n")

def main():
    datos = cargar_datos()
    
    while True:
        print("\nBienvenido al Registro de Notas Escolares\n")
        print("[1] Registrar nuevo estudiante")
        print("[2] Buscar estudiante por nombre")
        print("[3] Mostrar lista de estudiantes")
        print("[4] Salir del programa")
        
        opcion = input("Seleccione una opción (1-4): ")
        
        if opcion == "1":
            registrar_estudiante(datos)
        elif opcion == "2":
            buscar_estudiante(datos)
        elif opcion == "3":
            mostrar_lista_estudiantes(datos)
        elif opcion == "4":
            print("\nGracias por usar el programa. ¡Hasta luego!\n")
            break
        else:
            print("\nOpción no válida. Por favor, seleccione una opción del 1 al 4.\n")


    guardar_datos(datos)

if __name__ == "__main__":
    main()

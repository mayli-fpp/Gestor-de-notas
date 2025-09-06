notas = []

def registrar_curso_y_nota():
   curso = input("Ingrese el nombre del curso: ").strip()

   if curso == "":
       print("El nombre del curso no puede estar vacío.")
       return
   
   entrada = input("Ingrese la nota del curso (0-100): ")
## Validar que la entrada sea un número
   if not entrada.isnumeric():
         print("La nota debe ser un número entre 0 y 100.")
         return 
  ## Convertir la entrada a entero y validar el rango      
   nota = int(entrada)
   if 0 <= nota <= 100:
       notas.append({"curso": curso, "nota": nota})
       print("curso y nota registrados exitosamente.")
   else:
       print("La nota debe estar entre 0 y 100.")

## Función para mostrar todas las notas registradas
def mostrar_notas():
    if len(notas) == 0:
        print("No hay notas registradas.")
    else:
        print("Notas registradas:")
        contador = 1
        for registro in notas:
            print(f"{contador}. Curso: {registro['curso']}, Nota: {registro['nota']}")
            contador += 1

##funcion para calcular y mostrar el promedio de las notas
def calcular_promedio():
    if len(notas) == 0:
        print("No hay notas registradas para calcular el promedio.")
    else:
        suma = 0
        for registro in notas:
            suma += registro['nota']
            ptomedio = suma / len(notas)
        print(f"El promedio de las notas es: {ptomedio:.2f}")

## Funcion para buscar un curso por su nombre
def buscar_curso():
    if len(notas) == 0:
        print("No hay notas registradas para buscar.")
        return
    
    curso_buscar = input("Ingrese el nombre del curso que desea buscar: ").strip()

    for registro in notas:
        if registro["curso"].lower() == curso_buscar.lower():
            print(f"Curso encontrado: {registro['curso']}, Nota: {registro['nota']}")
            return
    print("Curso no encontrado.")

## Funcion para actualizar notas existentes
def actualizar_nota():
    if len(notas) == 0:
        print("No hay notas registradas para actualizar.")
        return
    
    mostrar_notas()
    posicion = input("Ingrese el número del curso que desea actualizar: ")
    
    if not posicion.isnumeric():
        print("Entrada inválida. Por favor, ingrese un número válido.")
        return
    
    posicion = int(posicion)
    if 1 <= posicion <= len(notas):
        nueva_nota = input("Ingrese la nueva nota (0-100): ")
        if not nueva_nota.isnumeric():
            print("La nota debe ser un número entre 0 y 100.")
            return
        
        nueva_nota = int(nueva_nota)
        if 0 <= nueva_nota <= 100:
            notas[posicion - 1]['nota'] = nueva_nota
            print("Nota actualizada exitosamente.")
        else:
            print("La nota debe estar entre 0 y 100.")

## menu principal
while True:
    print("\nMenú de opciones:")
    print("1. Registrar curso y nota")
    print("2. Mostrar notas registradas")
    print("3. Calcular promedio de notas")
    print("4. buscar curso")
    print("5. Actualizar nota de un curso")
    print("6. Salir")
    
    opcion = input("Seleccione una opción (1-5): ")
    
    if opcion == "1":
        registrar_curso_y_nota()
    elif opcion == "2":
        mostrar_notas()
    elif opcion == "3":
        calcular_promedio()
    elif opcion == "4":
        buscar_curso()
    elif opcion == "5":
        actualizar_nota()    
    elif opcion == "6":
        print("Saliendo del programa.")
        break
    else:
        print("Opción inválida. Por favor, seleccione una opción del 1 al 6.")
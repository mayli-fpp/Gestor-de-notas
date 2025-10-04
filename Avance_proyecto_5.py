notas = []
historial = []
revision = []

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

## eliminar cursos
def eliminar_curso():
    if len(notas) == 0:
        print("no hay cursos registrados")
        return
    
    mostrar_notas()
    posicion = input("Ingrese numero del curso que desea eliminar: ")

    if not posicion.isnumeric():
        print("Debe ingresar un numero valido")
        return
    posicion = int(posicion)
    if 1 <= posicion <= len(notas):
        eliminado = notas.pop(posicion - 1)
        print(f"Curso {eliminado['curso']} eliminado exitosamente.")
    else:
        print("Posición inválida.")

## pila y cola
def ver_historial():
    if len(historial) == 0:
        print("El historial esta vacio")
    else:
        print("historial de acciones (ultimas primero):")
        for accion in reversed(historial):
            print(f"- {accion}")

def agregar_revision():
    curso = input("Ingrese el nombre del curso para revisión: ").strip()
    if curso == "":
        print("Error: el curso no puede estar vacio")
        return
    revision.append(curso)
    print(f"El curso {curso} agregado a la cola de revisión.")

def procesar_revision():
    if len(revision) == 0:
        print("No hay cursos en la cola de revisión.")
    else:
        curso = revision.pop(0)
        print(f"Revision de curso: {curso}")
       
## funciones de ordenamiento
def ordenar_burbuja():
    if len(notas) == 0:
        print("No hay notas registradas.")
        return

    lista = notas.copy()
    n = len(lista)
    for i in range(n):
        for j in range(0, n-i-1):
            if lista[j]['nota'] > lista[j+1]['nota']:
                lista[j], lista[j+1] = lista[j+1], lista[j]

    print("cursos ordenados por nota (menor a mayor) con burbuja:")
    for registro in lista:
        print(f"- {registro['curso']}: {registro['nota']}")

def ordenar_insercion():
    if len(notas) == 0:
        print("No hay notas registradas para ordenar.")
        return

    lista = notas.copy()
    for i in range(1, len(lista)):
        key = lista[i]
        j = i-1
        while j >= 0 and key['nota'] < lista[j]['nota']:
            lista[j + 1] = lista[j]
            j -= 1
        lista[j + 1] = key

    print("cursos ordenados por nota (mayor a menor) con insercion:")
    for registro in lista:
        print(f"- {registro['curso']}: {registro['nota']}")                        

## menu principal
def menu():
 while True:
    print("\nMenú de opciones:")
    print("1. Registrar curso y nota")
    print("2. Mostrar notas registradas")
    print("3. Calcular promedio de notas")
    print("4. buscar curso")
    print("5. Actualizar nota de un curso")
    print("6. Eliminar curso")
    print("7. Ver historial")
    print("8. Agregar curso a revisión")
    print("9. Procesar revisión de curso")
    print("10. Ordenar notas (burbuja)")
    print("11. Ordenar notas (inserción)")
    print("12. Salir")
    
    opcion = input("Seleccione una opción (1-12): ")
    
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
        eliminar_curso() 
    elif opcion == "7":
        ver_historial() 
    elif opcion == "8":
        agregar_revision()
    elif opcion == "9":
        procesar_revision()
    elif opcion == "10":
        ordenar_burbuja()
    elif opcion == "11":
        ordenar_insercion()
    elif opcion == "12":
        print("Saliendo del programa.")
        break
    else:
        print("Opción inválida. Por favor, seleccione una opción del 1 al 12.")

menu()

import datetime #para fecha y hora 

notas = []
historial = []
revision = []

def add_historial(accion): 
    #Agrega una entrada con fecha/hora al historial
    ts = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    historial.append(f"{ts} - {accion}")

def registrar_curso_y_nota():
   print("===Registrar curso y nota===")
   curso = input("Ingrese el nombre del curso: ").strip()

   if curso == "":
       print("El nombre del curso no puede estar vacío.")
       return
   
   entrada = input("Ingrese la nota del curso (0-100): ")
   # Validar que la entrada sea un número
   if not entrada.isnumeric():
         print("La nota debe ser un número entre 0 y 100.")
         return 
   # Convertir la entrada a entero y validar el rango      
   nota = int(entrada)
   if 0 <= nota <= 100:
       notas.append({"curso": curso, "nota": nota})
       print("curso y nota registrados exitosamente.")
       add_historial(f"Registró curso '{curso}' con nota {nota}")
   else:
       print("La nota debe estar entre 0 y 100.")

## Función para mostrar todas las notas registradas

def mostrar_notas():
    print("===Notas registradas===")
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
    print("===Calcular promedio de notas===")
    if len(notas) == 0:
        print("No hay notas registradas para calcular el promedio.")
    else:
        suma = sum(reg['nota'] for reg in notas)
        ptomedio = suma / len(notas)
        print(f"El promedio de las notas es: {ptomedio:.2f}")
        add_historial("Calculó promedio de notas")

##funcion contar cursos aprobados y reprobados
def contar_aprobados_reprobados():
    aprobados = sum(1 for reg in notas if reg['nota'] >= 60)
    reprobados = sum(1 for reg in notas if reg['nota'] < 60)
    add_historial(f"Contó cursos: {aprobados} aprobados, {reprobados} reprobados")
    print(f"Cursos aprobados: {aprobados}")
    return aprobados, reprobados

## Funcion para buscar un curso por su nombre

def buscar_curso():
    print("===Buscar curso===")
    if len(notas) == 0:
        print("No hay notas registradas para buscar.")
        return
    
    curso_buscar = input("Ingrese el nombre del curso que desea buscar: ").strip()

    for registro in notas:
        if registro["curso"].lower() == curso_buscar.lower():
            print(f"Curso encontrado: {registro['curso']}, Nota: {registro['nota']}")
            add_historial(f"Buscó curso '{registro['curso']}' - encontrado")
            return
    print("Curso no encontrado.")
    add_historial(f"Buscó curso '{curso_buscar}' - no encontrado")

## Funcion para actualizar las notas existentes

def actualizar_nota():
    print("===Actualizar nota de un curso===")
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
            curso_nombre = notas[posicion - 1]['curso']
            notas[posicion - 1]['nota'] = nueva_nota
            print("Nota actualizada exitosamente.")
            add_historial(f"Actualizó nota de '{curso_nombre}' a {nueva_nota}")
        else:
            print("La nota debe estar entre 0 y 100.")
    else:
        print("Posición inválida.")

## eliminar cursos

def eliminar_curso():
    print("===Eliminar curso===")
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
        add_historial(f"Eliminó curso '{eliminado['curso']}'")
    else:
        print("Posición inválida.")

## pila y cola
def ver_historial():
    print("===Historial de acciones===")
    if len(historial) == 0:
        print("El historial esta vacio")
    else:
        print("Historial de acciones (más recientes primero):")
        for i, accion in enumerate(reversed(historial), start=1):
            print(f"{i}. {accion}")

def agregar_revision():
    print("===Agregar curso a revisión===")
    curso = input("Ingrese el nombre del curso para revisión: ").strip()
    if curso == "":
        print("Error: el curso no puede estar vacio")
        return
    revision.append(curso)
    print(f"El curso {curso} agregado a la lista de revisión.")
    add_historial(f"Agregó a revisión '{curso}'")

def procesar_revision():
    print("===Procesar revisión de curso===")
    if len(revision) == 0:
        print("No hay cursos en la lista de revisión.")
    else:
        curso = revision.pop(0)
        print(f"Procesando revisión del curso: {curso}")
        add_historial(f"Procesó revisión de '{curso}'")

## funciones de ordenamiento

def ordenar_burbuja():
    print("===Ordenar notas (burbuja)===")
    if len(notas) == 0:
        print("No hay notas registradas para ordenar.")
        return

    lista = notas.copy()
    n = len(lista)
    for i in range(n):
        for j in range(0, n-i-1):
            if lista[j]['nota'] > lista[j+1]['nota']:
                lista[j], lista[j+1] = lista[j+1], lista[j]

    print("cursos ordenados por nota (burbuja):")
    for registro in lista:
        print(f"- {registro['curso']}: {registro['nota']}")
    add_historial("Ordenó notas con burbuja")

def ordenar_insercion():
    print("===Ordenar notas (inserción)===")
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

    print("cursos ordenados por nota (insercion):")
    for registro in lista:
        print(f"- {registro['curso']}: {registro['nota']}")
    add_historial("Ordenó notas por inserción")

## menu principal

def menu():
    while True:
        print("\n===GESTOR DE NOTAS ACADEMICAS===")

        print("1. Registrar curso y nota")
        print("2. Mostrar notas registradas")
        print("3. Calcular promedio de notas")
        print("4. cursos Aprobados y Reprobados")
        print("5. buscar curso")
        print("6. Actualizar nota de un curso")
        print("7. Eliminar curso")
        print("8. Ver historial")
        print("9. Agregar curso a revisión")
        print("10. Procesar revisión de curso")
        print("11. Ordenar notas (burbuja)")
        print("12. Ordenar notas (inserción)")
        print("13. Salir")
        
        opcion = input("Seleccione una opción (1-12): ")
        
        if opcion == "1":
            registrar_curso_y_nota()
        elif opcion == "2":
            mostrar_notas()
        elif opcion == "3":
            calcular_promedio()
        elif opcion == "4":
            contar_aprobados_reprobados()
        elif opcion == "5":
            buscar_curso()
        elif opcion == "6":
            actualizar_nota()
        elif opcion == "7":
            eliminar_curso() 
        elif opcion == "8":
            ver_historial() 
        elif opcion == "9":
            agregar_revision()
        elif opcion == "10":
            procesar_revision()
        elif opcion == "11":
            ordenar_burbuja()
        elif opcion == "12":
            ordenar_insercion()
        elif opcion == "13":
            print("Saliendo del programa, graciaspor usar nuestro sitema....")
            break
        else:
            print("Opción inválida. Por favor, seleccione una opción del 1 al 13.")

if __name__ == "__main__":
    menu()

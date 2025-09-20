###Gestor de Notas Académicas

## Descripción del proyecto
El *Gestor de Notas Académicas* es un programa en *Python* que permite a los estudiantes y docentes llevar un control básico de los cursos y sus calificaciones.  
Su objetivo es brindar una herramienta simple y práctica para registrar, consultar, modificar y eliminar notas, así como calcular el promedio general.

El sistema se ejecuta en *consola* y está diseñado con *estructuras básicas de programación* (listas, bucles, condicionales y funciones).
## Funcionalidades principales
El programa cuenta con un menú interactivo que permite:

1. *Registrar curso y nota*  
   - El usuario ingresa el nombre de un curso y la nota obtenida.  
   - Se validan entradas vacías y rangos de notas (0 a 100).  

2. *Mostrar cursos y notas*  
   - Se listan todos los cursos registrados con sus notas.  

3. *Calcular promedio*  
   - Se obtiene el promedio de todas las notas registradas.  

4. *Buscar curso (búsqueda lineal)*  
   - Permite buscar un curso por su nombre y muestra la nota asociada.  

5. *Actualizar nota de un curso*  
   - El usuario selecciona un curso y modifica la calificación.  

6. *Eliminar curso*  
   - Se puede eliminar un curso junto con su nota de la lista.  

7. *Salir del sistema*  
   - Termina la ejecución del programa.  

## Requisitos del sistema

- *Lenguaje:* Python 3.x  
- *Entorno:* Consola/Terminal  

## Organización del código

El programa está dividido en funciones para facilitar su comprensión y modularidad:

- registrar_curso_y_nota() → Registra un curso con su nota.  
- mostrar_notas() → Muestra la lista completa de cursos y notas.  
- calcular_promedio() → Calcula y muestra el promedio general.  
- buscar_curso() → Busca un curso por nombre (búsqueda lineal).  
- actualizar_nota() → Permite modificar la nota de un curso existente.  
- eliminar_curso() → Elimina un curso de la lista.  
- menu() → Despliega el menú principal y controla el flujo del programa.  

---

##  Ejecución

1. Guardar el código en un archivo llamado gestor_notas.py.  
2. Abrir una terminal en la carpeta donde se encuentra el archivo.  
3. Ejecutar el programa con:  

```bash
python gestor_notas.py

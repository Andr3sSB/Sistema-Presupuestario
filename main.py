'''
Objetivo: Realizar una aplicación en python que utilice estructuras de datos (diccionarios y listas) para estructurar 
y almacenar información.

Instrucciones:
Seleccione una estructura para almacenar registros de algo de la vida real, utilice un diccionario para almacenar los campos
en formato clave : valor.
Realice un menú de opciones donde la primera opción sea la creación de registros y que se almacenen en una lista.
La segunda opción debe mostrar un informe en formato filas y columnas donde la primera fila contiene las etiquetas de 
las claves y abajo de esta irán los valores de cada clave para formar los registros.
'''



registro_de_gasto =  { # Creacion del registro
    "descripcion" : "Uber",
    "categoria" : "Transporte",
    "monto" : 6000
}

lista_de_gastos = [] # Creacion de la lista

def crear_registro(lista):
    print("\nCreando Registro")
    descripcion = input("\nIngrese una descripcion: ")
    categoria = input("Ingrese una categoría:")
    while True:
        try:
             monto = int(input("Ingrese el monto: "))
             break
        except ValueError:
             print("Ingrese un monto válido")
             
    # Crear registro con los datos ingrsados
    nuevo_registro = {
        "descripcion" : descripcion,
        "categoria" : categoria,
        "monto" : monto
    }
             
    lista.append(nuevo_registro) # Agrega el registro a la lista
    print("Registro creado exitosamente")
    
    
def mostrar_informe():
    print("\n--- INFORME PRESUPUESTARIO ---")
    
    #Si la lista no tiene datos muestra que no hay registros
    if len(lista_de_gastos) == 0: 
        print("Todavia no hay registros")
        return # El return evita que imprima la lista vacía
        
    #Titulos de cada fila
    print(f"{'Descripcion':<20} {'Categoria':<15} {'Monto':<10}") #El :<20 es para que el texto ocupe 20 espacio y se alinen con su respectiva columna
    print("-" * 50) #Separa encabezado de datos
    
    #Filas con los regsitros
    for gasto in lista_de_gastos:
        print(f"{gasto['descripcion']:<20} {gasto['categoria']:<15} {gasto['monto']:<10}")
    
    
# Creacion del menú
while True:
    print("\n--- MENU PRINCIPAL ---")
    print("1. Crear Registro")
    print("2. Mostrar Informe de Presupuesto")
    print("3. Salir")
    
    opcion = input("Seleccione una opción: ")
    
    if opcion == "1":
        crear_registro(lista_de_gastos)
        
    elif opcion == "2":
        mostrar_informe()
        
    elif opcion == "3":
        
        print("\nSaliendo")
        print("¡Gracias por usar el Sistema Presupuestario!")
        break
    else:
        print("Opción inválida, digite una opcion valida para continuar.")
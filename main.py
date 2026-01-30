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
             
    id_gasto = len(lista) + 1
             
    # Crear registro con los datos ingrsados
    nuevo_registro = {
        "id": id_gasto,
        "descripcion" : descripcion,
        "categoria" : categoria,
        "monto" : monto
    }
    
    lista.append(nuevo_registro) # Agrega el registro a la lista
    print("Registro creado exitosamente")
    
def modificar_registro(lista):
    print("\n--- MODIFICAR REGISTRO ---")
    
     # Pedir ID del gasto
    try:
        id_buscar = int(input("Ingrese el ID del gasto que desea modificar: "))
    except ValueError:
        print("DEbe ingresar un número válido")
        return
    
    # Buscar el registro en la lista
    for gasto in lista:
        if gasto ["id"] == id_buscar:
            print ("\nRegistro encontrado:")
            print(gasto)
            
            # Menú de campos a modificar
            print("\n¿Qué desea modificar?")
            print("1. Descripcion")
            print("2. Categoría")
            print("3. Monto")
            
            opcion = input("Seleecione una opción: ")
            
            if opcion == "1":
                nueva_descripcion = input("Ingrese la nueva descripcion: ")
                gasto["descripcion"] = nueva_descripcion
                
            elif opcion == "2":
                nueva_categoria = input("Ingrese la nueva categoría: ")
                gasto["categoria"] = nueva_categoria
                
            elif opcion == "3":
                while True:
                    try:
                        nuevo_monto = int(input("Ingrese el nuevo monto: "))
                        gasto["monto"] = nuevo_monto
                        break
                    except ValueError:
                        print("Monto inválido, intente de nuevo.")
            else:
                print ("Opcion no valida")
                return
            
            print("\nRegistro modificado correctamente.")
            return
        
     # Si termina el for sin encontrarlo
    print("No se encontró ningún registro con ese ID.")
               
def mostrar_informe():
    print("\n--- INFORME PRESUPUESTARIO ---")
    
    #Si la lista no tiene datos muestra que no hay registros
    if len(lista_de_gastos) == 0: 
        print("Todavia no hay registros")
        return # El return evita que imprima la lista vacía
        
    #Titulos de cada fila
    print(f"{'ID':<5} {'Descripcion':<20} {'Categoria':<15} {'Monto':<10}") #El :<20 es para que el texto ocupe 20 espacio y se alinen con su respectiva columna
    print("-" * 55) #Separa encabezado de datos
    
    #Filas con los regsitros
    for gasto in lista_de_gastos:
        print(f"{gasto['id']:<5} {gasto['descripcion']:<20} {gasto['categoria']:<15} {gasto['monto']:<10}")
    
def eliminar_registro(lista):
    print("\n--- ELIMINAR REGISTRO ---")
    
    # Pedir ID del gasto a eliminar
    try:
        id_buscar = int(input("Ingrese el ID del gasto que desea eliminar: "))
    except ValueError:
        print("Debe ingresar un número válido.")
        return
    
    # Buscar el registro en la lista
    for gasto in lista:
        if gasto["id"] == id_buscar:

            print("\nRegistro encontrado:")
            print(gasto)

            # Confirmación antes de eliminar
            confirmar = input("¿Está seguro que desea eliminarlo? (s/n): ").lower()

            if confirmar == "s":
                lista.remove(gasto)
                print("\nRegistro eliminado correctamente.")
            else:
                print("\nEliminación cancelada.")

            return
        
    print("No se encontró ningun registro con ese ID")
    
# Creacion del menú
while True:
    print("\n--- MENU PRINCIPAL ---")
    print("1. Crear Registro")
    print("2. Mostrar Informe de Presupuesto")
    print("3. Modificar Registro")
    print("4. Eliminar Registro")
    print("5. Salir")

    opcion = input("Seleccione una opción: ")
    
    if opcion == "1":
        crear_registro(lista_de_gastos)
        
    elif opcion == "2":
        mostrar_informe()
        
    elif opcion == "3":
        modificar_registro(lista_de_gastos)
        
    elif opcion == "4":
        eliminar_registro(lista_de_gastos)
    
    elif opcion == "5":
         print("\nSaliendo...")
         print("¡Gracias por usar el Sistema Presupuestario!")
         break
        
    else:
        print("Opción inválida, digite una opcion valida para continuar.")
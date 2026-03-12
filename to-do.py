from datetime import date

opcion = 0
tareas = []

while opcion < 1 or opcion > 5:
    print("\n==== To-Do ====")
    print("\n------ Menu ------")
    print("1. Mostrar tareas.")
    print("2. Agregar tarea.")
    print("3. Editar tarea.")
    print("4. Eliminar tarea.")
    print("5. Salir.")
    print("------------------")

    opcion = int(input("\nSeleccione una opcion: "))
    
    if opcion < 1 or opcion > 5:
        print("\nOpcion invalida, intentelo nuevamente.....")
        
    match opcion:
        case 1:
            print("\n1. Mostrar tareas.\n")
            
            print("Id  -   tarea   -   objetivo   -   observaciones   -   fecha de registro")
            
            opcion = 0
            
            for item in tareas:
                print(item)
                
        case 2:
            print("\n2. Agregar tarea.\n")
            
            Id = len(tareas) + 1
            tarea = input("Ingrese la tarea: ")
            objetivo = input("Ingrese el objetivo de la tarea: ")
            observaciones = input("Observaciones: ")
            fecha = date.today()
            
            nueva_tarea = [Id, tarea, objetivo, observaciones, fecha]
            
            tareas.append(nueva_tarea)
            
            opcion = 0
            
        case 3:
            print("\n3. Editar tarea.")
        case 4:
            print("\n4. Eliminar tarea.")
        case 5:
            print("\n5. Cerraste sesion.")
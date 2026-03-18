from datetime import datetime

print("\n==== To-Do ====")

opcion = 0
tareas = []

while opcion < 1 or opcion > 5:
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
            
            if len(tareas) == 0:
                Id = 1
            
            else:
                Id = (tareas[len(tareas) - 1][0]) + 1
                
            tarea = input("Ingrese la tarea: ")
            objetivo = input("Ingrese el objetivo de la tarea: ")
            observaciones = input("Observaciones: ")
            fecha = datetime.now()
            formato = fecha.strftime("%d/%m/%y")
            
            nueva_tarea = [Id, tarea, objetivo, observaciones, formato]
            
            tareas.append(nueva_tarea)
            
            opcion = 0
            
        case 3:
            print("\n3. Editar tarea.")
            
            for item in tareas:
                print(item)
                
            buscar = input("\nIngrese la tarea que desea editar: ")
            conteo = 1

            # Condicional para identificar si el dato ingresado es un numero
            if buscar.isdigit():
                buscar = int(buscar)

            # Condicional para buscar la tarea que se va a editar.
            for I in tareas:
                if buscar in I:
                    print(f"{tareas[conteo - 1]}\n")
                    Id = conteo
                    tarea = input("Ingrese la nueva tarea: ")
                    objetivo = input("Ingrese el nuevo objetivo de la tarea: ")
                    observaciones = input("Observaciones: ")
                    fecha = datetime.now()
                    formato = fecha.strftime("%d/%m/%y")
                    
                    nueva_tarea = [Id, tarea, objetivo, observaciones, formato]
                    
                    print("\n---> Tarea editada con exito!!!\n")
                    
                    tareas[conteo - 1] = nueva_tarea                     
                    break
                
                else:
                    conteo += 1

            # Condicional para saber si se encontro la tarea o no.
            if conteo > len(tareas):
                print("\n => La tarea que ingreso no esta registrada en el sistema.")
            
            opcion = 0
            
        case 4:
            print("\n4. Eliminar tarea.")
            
            #Ciclo para mostrar todas las tareas.
            for item in tareas:
                print(item)
                
            buscar = input("\nIngrese la tarea que desea eliminar: ")
            print("")
            conteo = 1

            # Condicional para identificar si el dato ingresado es un numero
            if buscar.isdigit():
                buscar = int(buscar)

            # Condicional para buscar la tarea que se va a eliminar.
            for I in tareas:
                if buscar in I:
                    print(tareas[conteo - 1])
                    eliminar = input("Esta seguro de eliminar la siguiente tarea? si/no: ")
                    print("")
                    
                    # Convertimos todo a minuscula para que el usuario pueda ingresar la respuesta sin problemas
                    eliminar = eliminar.lower()
                    
                    if eliminar == "si":
                        tareas.remove(tareas[conteo - 1])
                        print("\n---> Tarea eliminada con exito!!!\n")
                        
                    else:
                        for item in tareas:
                            print(item)
                        
                    break
                else:
                    conteo += 1

            # Condicional para saber si no se encontro la tarea, entonces indicará que no esta registrada.
            if conteo > len(tareas):
                print("\nLa tarea que ingreso no esta registrada en el sistema.")
            
            opcion = 0
                
        case 5:
            print("\nCerraste sesion.")
            print("Muchas gracias.")
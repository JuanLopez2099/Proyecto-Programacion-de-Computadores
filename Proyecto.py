#Definir lista de empleados

lista_empleados = [{"nombre": "Juan Camilo Lopez Gonzalez", "numero_identificacion": 1110460138, "fecha_nacimiento": "20/05/2005" ,"edad": 20 , "sexo": "hombre", "numero_telefonico": 123456789, "cargo": "desarrollador", "fecha_ingreso": "29/07/2025", "tiene_hijos": "No", "tipo_contrato": "Idenfinido", "RH": "O+", "estado_civil": "Soltero"},
                   {"nombre": "Estefania Rodriguez", "numero_identificacion": 2220242033, "fecha_nacimiento": "01/01/2007", "edad": 18, "sexo": "mujer", "numero_telefonico": 987654321, "cargo": "analista", "fecha_ingreso": "02/07/2025",  "tiene_hijos": "No", "tipo_contrato": "Idenfinido", "RH": "B+",  "estado_civil": "Soltero"},
                   {"nombre": "Sarah Ulloque", "numero_identificacion": 2220242033, "fecha_nacimiento": "15/04/2004", "edad": 21, "sexo": "mujer", "numero_telefonico": 543219876, "cargo": "gerente", "fecha_ingreso": "01/07/2025", "tiene_hijos": "Si", "tipo_contrato": "Idenfinido", "RH": "A-", "estado_civil": "Casado" }
                   ] #Se agrupan diccionarios dentro de la lista con la informacion de cada empleado usando claves para acceder a los valores


#Definir funcion para mostrar a todos los empleados
def mostrar_empleados():
    for empleados in lista_empleados: #Bucle para recorrer la lista
        print(f"|{empleados['nombre']}|, |{empleados['numero_identificacion']}|, |{empleados['fecha_nacimiento']}|, |{empleados['edad']}|, |{empleados['sexo']}|, |{empleados['numero_telefonico']}|, |{empleados['cargo']}|, |{empleados['fecha_ingreso']}|, |{empleados['tiene_hijos']}|, |{empleados['tipo_contrato']}|, |{empleados['RH']}|, |{empleados['estado_civil']}|") #Imprimir la informacion de cada empleado por consola
    if lista_empleados == []:
        print("No hay empleados") 


#Definir funcion para buscar empleados
def buscar_empleados(numero_de_identificacion): #Definimos la funcion con los parametros que se solicitaran para la busqueda
    for empleado in lista_empleados:
        if numero_de_identificacion == empleado["numero_identificacion"]:  #Se compara si el numero de identificacion ingresado por el usuario es esta en la clave 'numero_identificacion'
            return empleado  #Si lo esta retorna el diccionario con toda la informacion del empleado
    if not numero_de_identificacion == empleado["numero_identificacion"]:
        return "El empleado no existe" #Si no retorna mensaje de señalando que el empleado buscado no existe


#Definir funcion para registrar nuevos empleados
def registrar_empleado(nombre, numero_identificacion, fecha_nacimiento, edad, sexo, numero_telefonico, cargo, fecha_ingreso, tiene_hijos, tipo_contrato, RH, estado_civil): #Se crea la funcion con los parametros que se solicitaran al usuario
    if nombre == "" or numero_identificacion == "" or not numero_identificacion.isdigit() or fecha_nacimiento == "" or edad == "" or not edad.isdigit() or numero_telefonico == "" or not numero_telefonico.isdigit() or cargo == "" or fecha_ingreso == "": #Mediante un if se comprueba si las cadenas estan vacias y si las cadenas de ciertos valores son unicamente numeros
        return "las opciones deben ser validas" #En caso de que cierta informacion este vacia o no solo contenga numeros la funcion devuelve un mensaje indicandolo
    numero_identificacion = int(numero_identificacion)
    edad = int(edad)                                            #Se transforman las cadenas numericas a enteros
    numero_telefonico = int(numero_telefonico)
    if numero_identificacion <= 0 or edad <= 0 or numero_telefonico <= 0:  #Una vez convertidas a enteros se verifica si algun valor es menor o igual a 0
        return "Las opciones deben ser validas"   #En caso de que si la funcion devuelve un mensaje indicandolo
    opciones_sexo_empleado = {1: "Hombre", 2: "Mujer", 3: "Otro"}
    sexo = opciones_sexo_empleado[sexo]
    opciones_tiene_hijos = {1: "Si", 2: "No"}                         #Se crean diccionarios que contengan las opciones que digite el usuario usando claves
    tiene_hijos = opciones_tiene_hijos[tiene_hijos]                   #La variable se convierte al valor de la clave del diccionario que dijite el usuario                                        
    opciones_tipo_contrato = {1: "Definido", 2: "Indefinido", 3: "Obra labor", 4: "Aprendizaje"}
    tipo_contrato = opciones_tipo_contrato[tipo_contrato]
    opciones_RH = {1: "A+", 2: "A-", 3: "B+", 4: "B-", 5: "AB+", 6: "AB-", 7: "O+", 8: "O-"}
    RH = opciones_RH[RH]
    opciones_estado_civil = {1: "Soltero", 2: "Casado", 3: "Union Libre", 4: "Divorciado", 5: "Viudo"}
    estado_civil = opciones_estado_civil[estado_civil]
    nuevo_empleado = {"nombre": nombre, "numero_identificacion": numero_identificacion, "fecha_nacimiento": fecha_nacimiento, "edad": edad, "sexo": sexo, "numero_telefonico": numero_telefonico, "cargo": cargo, "fecha_ingreso": fecha_ingreso, "tiene_hijos": tiene_hijos, "tipo_contrato":tipo_contrato, "RH": RH, "estado_civil": estado_civil} #Una vez que se hacen las comprobaciones se guardan los valores en este diccionario con su respectiva clave
    for empleado in lista_empleados: 
        if nuevo_empleado["nombre"] == empleado["nombre"] or nuevo_empleado["numero_identificacion"] == empleado["numero_identificacion"] or  nuevo_empleado["numero_telefonico"] == empleado["numero_telefonico"]: #Se recorre la lista de empleados y se comprueba que el nuevo empleado no tenga la misma informacion que un empleado ya existente 
            return "No puede haber empleados con la misma informacion nombre/id/numero telefonico" #En caso de que la tenga la funcion retorna indicandolo
    lista_empleados.append(nuevo_empleado) #Una vez hechas todas las comprobaciones se agrega el diccionario que contiene al nuevo empleado a la lista de empleados
    print("El empleado se ha registrado con exito!") #Se indica que se ha añadido con exito
    return nuevo_empleado  #Imprime el diccionario con la informacion del nuevo empleado


def eliminar_empleado():
    pass

   
def menu():  #Se define el menu dentru de una funcion para reutilizarlo
    print("""
1. Mostrar lista de todos los empleados
2. Buscar empleado
3. Registrar empleado
0. Salir
""")

print("\n Bienvenido al menu de JackDRipper Software") #Se imprime el titulo del menu fuera del bucle para que no se imprima en cada vuelta
while True:  
    menu()    #Se llama a la funcion del menu

    opcion = int(input("Digite una opcion 1-4: "))  #Se solicita la opcion al usuario, se le pide en numero entero

    match opcion:
        case 1:
            mostrar_empleados() #Opcion numero uno, se llama a la funcion para mostrar la lista de empleados
        case 2:
            numero_de_identificacion = int(input("Digite el numero de identificacion del empleado: ")) #Solicita al usuario el numero de identificacion como entero
            print(buscar_empleados(numero_de_identificacion)) #Llama a la funcion y devuelve el resultado
        case 3:
            nombre = input("Digite el nombre del nuevo empleado: ").capitalize().strip() #Se solicita al usuario el nombre del nuevo empleado, se eliminan espacios y se ponen las iniciales en mayusculas
            numero_identificacion = input("Digite el numero de identificacion del nuevo empleado: ") #Se pide el id como cadena
            fecha_nacimiento = input("Digite la fecha de nacimiento Dia/Mes/Año: ") #Se solicita la fecha de nacimiento
            edad = input("Digite la edad del nuevo empleado en años: ") #Se solicita la edad
            while True:  #Se crea un bucle para mostrar las opciones de este parametro
                print("Indique el sexo del empleado: \n "
                "1. Hombre \n" 
                "2. Mujer \n" 
                "3. Otro \n")
                sexo = int(input("Digite una opcion 1-3: "))  #Se le solicita al usuario elegir una opcion numerica
                if sexo == 1 or sexo == 2 or sexo == 3:
                    break     #Si las opcion es valida se rompe el bulce y se pasa al siguiente parametro
                else:
                    print("Digite una opcion valida")  #Si no se indica y se repite el bucle hasta que elija una opcion valida
            numero_telefonico = input("Digite el numero telefonico del nuevo empleado: ") #Se solicita el numero telefonico como cadena
            cargo = input("Digite el cargo del nuevo empleado: ")  #Se solicita el cargo del nuevo empleado
            fecha_ingreso = input("Digite la fecha de ingreso: ")  #Se solicita la fecha de ingreso
            while True:   #Bucle para mostrar las opciones del parametro 'tiene_hijos'
                print("""Tiene hijos?
                      1. Si
                      2. No
                      """)
                tiene_hijos = int(input("Escoja una opcion 1-2: "))  #Se le solicita al usuario que digite una opcion numerica
                if tiene_hijos == 1 or tiene_hijos == 2:
                    break    #Si la opcion es valida se rompe el bucle y se va al siguiente parametro
                else:
                    print("Digite una opcion valida")   #Si no se indica y el bucle se repite hasta escojer una opcion valida
            while True:   #Bucle para mostrar las opciones del parametro 'tipo_contrato'
                print("""Tipo de contrato:
                      1. Definido
                      2. Indefinido
                      3. Obra labor
                      4. Aprendizaje""")
                tipo_contrato = int(input("Digite una opcion 1-4: "))  #Se le solicita al usuario que digite una opcion numerica
                if tipo_contrato == 1 or tipo_contrato == 2 or tipo_contrato == 3 or tipo_contrato == 4: 
                    break    #Si la opcion es valida se rompe el bucle y se va al siguiente parametro
                else:
                    print("Digite una opcion valida")  #Si no se indica y el bucle se repite hasta escojer una opcion valida
            while True:  #Bucle para mostrar las opciones del parametro 'RH'
                print("""Tipo de RH:
                      1. A+
                      2. A-
                      3. B+
                      4. B-
                      5. AB+
                      6. AB-
                      7. O+
                      8. O-""")
                RH = int(input("Digite una opcion 1-8: "))
                if RH == 1 or RH == 2 or RH == 3 or RH == 4 or RH == 5 or RH == 6 or RH == 7 or RH == 8: #Si la opcion es valida se rompe el bucle y se va al siguiente parametro
                    break
                else:
                    print("Digite una opcion valida")  #Si no se indica y el bucle se repite hasta escojer una opcion valida
            while True: #Bucle para mostrar las opciones del parametro 'estado_civil'
                    print("""Indique estado civil:
                          1. Soltero
                          2. Casado
                          3. Union libre
                          4. Divorciado
                          5. Viudo""")
                    estado_civil = int(input("Escoja una opcion 1-5: ")) #Se le solicita al usuario que digite una opcion numerica
                    if estado_civil == 1 or estado_civil == 2 or estado_civil == 3 or estado_civil == 4 or estado_civil == 5: 
                        break #Si la opcion es valida se rompe el bucle y se va al siguiente parametro
                    else:
                        print("Digite una opcion valida") #Si no se indica y el bucle se repite hasta escojer una opcion valida
            print(registrar_empleado(nombre, numero_identificacion, fecha_nacimiento, edad, sexo, numero_telefonico, cargo, fecha_ingreso, tiene_hijos, tipo_contrato, RH, estado_civil)) #Se llama a la funcion

        case 0: 
            print("Tenga un buen dia!")    #Mensaje de despedida y romper el bucle
            break
        case _:
            print("Digite una opcion valida")  #Si el usuario digita una opcion no contemplada se imprime mensaje de error
    


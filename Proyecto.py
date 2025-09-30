#Definir lista de empleados

lista_empleados = [{"nombre": "Juan Camilo Lopez Gonzalez", "numero_identificacion": 1110460138, "fecha_nacimiento": "20/05/2005" ,"edad": 2025-2005 , "sexo": "hombre", "numero_telefonico": 123456789, "cargo": "desarrollador", "fecha_ingreso": "29/07/2025", "tiene_hijos": "No", "tipo_de_contrato": "Idenfinido", "RH": "O+", "estado_civil": "Soltero"},
                   {"nombre": "Estefania Rodriguez", "numero_identificacion": 2220242033, "fecha_nacimiento": "01/01/2007", "edad": 2025-2007, "sexo": "mujer", "numero_telefonico": 987654321, "cargo": "analista", "fecha_ingreso": "02/07/2025",  "tiene_hijos": "No", "tipo_de_contrato": "Idenfinido", "RH": "B+",  "estado_civil": "Soltero"},
                   {"nombre": "Sarah Ulloque", "numero_identificacion": 2220242033, "fecha_nacimiento": "15/04/2004", "edad": 2025-2004, "sexo": "mujer", "numero_telefonico": 543219876, "cargo": "gerente", "fecha_ingreso": "01/07/2025", "tiene_hijos": "Si", "tipo_de_contrato": "Idenfinido", "RH": "A-", "estado_civil": "Casado" }
                   ] #Se agrupan diccionarios dentro de la lista con la informacion de cada empleado usando claves para acceder a los valores


#Definir funcion para mostrar a todos los empleados
def mostrar_empleados():
    for empleados in lista_empleados: #Bucle para recorrer la lista
        print(f"|{empleados['nombre']}|, |{empleados['numero_identificacion']}|, |{empleados['fecha_nacimiento']}|, |{empleados['edad']}|, |{empleados['sexo']}|, |{empleados['numero_telefonico']}|, |{empleados['cargo']}|, |{empleados['fecha_ingreso']}|, |{empleados['tiene_hijos']}|, |{empleados['tipo_de_contrato']}|, |{empleados['RH']}|, |{empleados['estado_civil']}|") #Imprimir la informacion de cada empleado por consola
    if lista_empleados == []:
        print("No hay empleados") 


#Definir funcion para buscar empleados
def buscar_empleados(nombre, edad, sexo, numero, cargo): #Definimos la funcion con los parametros que se solicitaran para la busqueda
    coincidencias_busqueda = [] #Dentro de esta lista se almacenara el trabajador que coincida con la busqueda
    for empleado in lista_empleados:
        nombre_empleado = empleado["nombre"].lower()
        edad_empleado = str(empleado["edad"])                #Edad y numero se transforman a cadena para poder itearlos
        sexo_empleado = empleado["sexo"].lower()             #Dentro de cada variable se guarda por separado la clave de los diccionarios iterados         
        numero_empleado = str(empleado["numero telefonico"])
        cargo_empleado = empleado["cargo"].lower()

        #El usuario debe digitar la informacion del empleado y se evalua si coincide con las claves del diccionario iterado
        if nombre in nombre_empleado and edad in edad_empleado and sexo in sexo_empleado and numero in numero_empleado and cargo in cargo_empleado:
            coincidencias_busqueda.append(empleado) #Si esto resulta ser True se añade el diccionario que coincide a la lista de coincidencias             
            return coincidencias_busqueda #Retorna la lista
    if coincidencias_busqueda == []: #Si la lista de coincidencias permanece vacia, no existen el trabajador
        print("No existen coincidencias para el trabajador buscado")

     

#Definir funcion para registrar nuevos empleados
def registrar_empleado(nombre, edad, sexo, numerotelefonico, cargo): #Se ingresan los parametros de entrada
    nuevo_empleado = {"nombre": nombre , "edad": edad, "sexo": sexo , "numero telefonico": numerotelefonico , "cargo": cargo } #Se crea un diccionario para almacenar al nuevo empleado
    if nombre == "" or edad == "" or sexo == "" or numerotelefonico == "" or cargo == "": #Si el usuario no ingresa un dato la entrada es invalida
        return "Debe ingresar todos los datos solicitados" #Retorna mensaje de error
    if nombre != "" and edad != "" and sexo != "" and numerotelefonico != "" and cargo != "": #Si la entrada del usuario es diferente de ""
        print("Todos los datos ingresados correctamente") #Se imprimie un mensaje de confirmacion
        lista_empleados.append(nuevo_empleado)
        return nuevo_empleado #Imprime el diccionario con los datos ingresados


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
            nombre = input("Digite los nombres y apellidos del trabajdor: ").lower().strip()
            edad = input("Digite la edad del trabajador en años: ")             #Se le solicitan los parametros de entrada al usuario
            sexo = input("Digite el sexo del trabajador: ").lower().strip()     #Se lleva todo a minusculas y se quitan espacios para evitar errores
            numero =  input("Digite el numero del trabajador: ")
            cargo = input("Digite el cargo del trabajador: ").lower().strip()
            print(buscar_empleados(nombre, edad, sexo, numero, cargo))   #Se imprime la funcion ya que esta retorna un valor
        case 3:
            nombre = input("Digite los nombres y apellidos del trabajdor: ").lower().strip()
            edad = input("Digite la edad del trabajador en años: ")
            sexo = input("Digite el sexo del trabajador: ").lower().strip()
            numerotelefonico =  input("Digite el numero del trabajador: ")          #Se solicitan los datos de nuevo empleado
            cargo = input("Digite el cargo del trabajador: ").lower().strip()
            print(registrar_empleado(nombre, edad, sexo, numerotelefonico, cargo))   #Se imprime la funcion
        case 0: 
            print("Tenga un buen dia!")    #Mensaje de despedida y romper el bucle
            break
        case _:
            print("Digite una opcion valida")  #Si el usuario digita una opcion no contemplada se imprime mensaje de error
    


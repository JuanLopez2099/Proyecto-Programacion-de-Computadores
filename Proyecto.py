#Definir lista de empleados

lista_empleados = [{"nombre": "Juan Camilo Lopez Gonzalez", "edad": 20, "sexo": "hombre", "numero telefonico": 123456789, "cargo": "desarrollador"},
                   {"nombre": "Estefania Rodriguez", "edad": 18, "sexo": "mujer", "numero telefonico": 987654321, "cargo": "analista"},
                   {"nombre": "Sarah Ulloque", "edad": 21, "sexo": "mujer", "numero telefonico": 543219876, "cargo": "gerente"}
                   ] #Se agrupan diccionarios dentro de la lista con la informacion de cada empleado usando claves para acceder a los valores


#Definir funcion para mostrar a todos los empleados
def mostrar_empleados():
    for empleados in lista_empleados: #Bucle para recorrer la lista
        print(f"|{empleados["nombre"]}|, |{empleados["edad"]}|, |{empleados["sexo"]}|, |{empleados["numero telefonico"]}|, |{empleados["cargo"]}|") #Imprimir la informacion de cada empleado por consola
    if lista_empleados == []:
        print("No hay empleados") 


#Definir funcion para buscar empleados
def buscar_empleados(nombre, edad, sexo, numero, cargo): #Definimos la funcion con los parametros que se solicitaran para la busqueda
    coincidencias_busqueda = [] #Dentro de esta lista se almacenara el trabajador que coincida con la busqueda
    for empleado in lista_empleados:
        nombre_empleado = empleado["nombre"].lower()
        edad_empleado = empleado["edad"]
        sexo_empleado = empleado["sexo"].lower()             #Dentro de cada variable se guarda por separado la clave de los diccionarios iterados         
        numero_empleado = empleado["numero telefonico"]
        cargo_empleado = empleado["cargo"].lower()
        #El usuario debe digitar la informacion del empleado y se evalua si coincide con las claves del diccionario iterado
        if nombre in nombre_empleado and edad in edad_empleado and sexo in sexo_empleado and numero in numero_empleado and cargo in cargo_empleado:
            coincidencias_busqueda.append(empleado) #Si esto resulta ser True se añade el diccionario que coincide a la lista de coincidencias             

    if coincidencias_busqueda == []: #Si la lista de coincidencias permanece vacia, no existen el trabajador
        print("No existen coincidencias para el trabajador buscado")

    return coincidencias_busqueda #Retorna la lista






    


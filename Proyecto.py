import datetime as datetime #Se importa la libreria datetime

#Funcion para calcular edad de las personas 
def calcular_edad(fecha_nacimiento):  #Se define la funcion con el parametro que se le solicitara al usuario
    fecha_nac = datetime.datetime.strptime(fecha_nacimiento.strip(), "%d/%m/%Y") #Usando la libreria datetime convertimos la fecha de nacimiento de string a formato datetime
    fecha_actual = datetime.datetime.today()  #Usando la libreria datetime se llama a la fecha actual

    edad = fecha_actual.year - fecha_nac.year   #Al año actual se le resta el año de nacimiento del empleado

    return edad  #Retorna la edad



#Definir lista de empleados
lista_empleados = [{"nombre": "Juan Camilo Lopez Gonzalez", "numero_identificacion": 1110460138, "fecha_nacimiento": "20/05/2005" ,"edad": calcular_edad("20/05/2005"), "sexo": "hombre", "numero_telefonico": 123456789, "cargo": "desarrollador", "fecha_ingreso": "29/07/2025", "tiene_hijos": "No", "tipo_contrato": "Idenfinido", "RH": "O+", "estado_civil": "Soltero", "discapacidad": "No", "poblacion_vulnerable": "No"},
                   {"nombre": "Estefania Rodriguez", "numero_identificacion": 2220242033, "fecha_nacimiento": "03/06/2007", "edad": calcular_edad("01/01/2007") , "sexo": "mujer", "numero_telefonico": 987654321, "cargo": "analista", "fecha_ingreso": "02/07/2025",  "tiene_hijos": "No", "tipo_contrato": "Idenfinido", "RH": "B+",  "estado_civil": "Soltero", "discapacidad": "No", "poblacion_vulnerable": "No"},
                   {"nombre": "Sarah Ulloque", "numero_identificacion": 2220222033, "fecha_nacimiento": "15/04/2004", "edad":calcular_edad("15/04/2004") , "sexo": "mujer", "numero_telefonico": 543219876, "cargo": "psicologa", "fecha_ingreso": "01/07/2025", "tiene_hijos": "Si", "tipo_contrato": "Idenfinido", "RH": "A-", "estado_civil": "Casado", "discapacidad": "Si", "poblacion_vulnerable": "Si"},
                   {"nombre": "Jack El Destripador", "numero_identificacion": 2223335556, "fecha_nacimiento": "01/01/2007", "edad": calcular_edad("01/01/2007") , "sexo": "hombre", "numero_telefonico": 3054637387, "cargo": "CEO", "fecha_ingreso": "01/01/2025",  "tiene_hijos": "No", "tipo_contrato": "Idenfinido", "RH": "B+",  "estado_civil": "Viudo", "discapacidad": "No", "poblacion_vulnerable": "No"},
                   {"nombre": "Alex Sandro Silva Pereira", "numero_identificacion": 1330115133, "fecha_nacimiento": "07/07/1987", "edad": calcular_edad("07/07/1987") , "sexo": "hombre", "numero_telefonico": 3105550123, "cargo": "jefe de seguridad", "fecha_ingreso": "20/07/2025",  "tiene_hijos": "Si", "tipo_contrato": "Idenfinido", "RH": "AB+",  "estado_civil": "Casado", "discapacidad": "No", "poblacion_vulnerable": "No"},
                   {"nombre": "Thomas Paul Aspinall", "numero_identificacion": 4623812222, "fecha_nacimiento": "11/04/1993", "edad": calcular_edad("11/04/1993") , "sexo": "hombre", "numero_telefonico": 3012314512, "cargo": "ingeniero de telecomunicaciones", "fecha_ingreso": "13/07/2025",  "tiene_hijos": "Si", "tipo_contrato": "Definido", "RH": "O+",  "estado_civil": "Casado", "discapacidad": "No", "poblacion_vulnerable": "No"},
                   {"nombre": "Khamzat Khizarovich Chimaev", "numero_identificacion": 5712943456, "fecha_nacimiento": "01/05/1994", "edad": calcular_edad("01/05/1994") , "sexo": "hombre", "numero_telefonico": 3054560278, "cargo": "Analista de datos", "fecha_ingreso": "19/07/2025",  "tiene_hijos": "No", "tipo_contrato": "Obra labor", "RH": "O-",  "estado_civil": "Viudo", "discapacidad": "No", "poblacion_vulnerable": "Si"},
                   {"nombre": "Jack Della Madalena", "numero_identificacion": 99323346673, "fecha_nacimiento": "10/09/1996", "edad": calcular_edad("10/09/1996") , "sexo": "hombre", "numero_telefonico": 3023210391, "cargo": "Tecnico de hardware", "fecha_ingreso": "08/08/2025",  "tiene_hijos": "No", "tipo_contrato": "Aprendizaje", "RH": "A+",  "estado_civil": "Union libre", "discapacidad": "No", "poblacion_vulnerable": "No"},
                   {"nombre": "Ilia Topuria Bendeliani", "numero_identificacion": 1216080617, "fecha_nacimiento": "21/01/1997", "edad": calcular_edad("21/01/1997") , "sexo": "hombre", "numero_telefonico": 3114037721, "cargo": "Tecnico de seguridad", "fecha_ingreso": "20/08/2025",  "tiene_hijos": "Si", "tipo_contrato": "Definido", "RH": "AB-",  "estado_civil": "Casado", "discapacidad": "No", "poblacion_vulnerable": "Si"},
                   {"nombre": "Alexander Volkanovski", "numero_identificacion": 2415022999, "fecha_nacimiento": "29/09/1988", "edad": calcular_edad("29/09/1988") , "sexo": "hombre", "numero_telefonico": 3207774410, "cargo": "Cafeteria", "fecha_ingreso": "13/08/2025",  "tiene_hijos": "Si", "tipo_contrato": "Definido", "RH": "O+",  "estado_civil": "Soltero", "discapacidad": "No", "poblacion_vulnerable": "No"},
                   {"nombre": "Merab Dvalishvili", "numero_identificacion": 2019040323, "fecha_nacimiento": "10/01/1991", "edad": calcular_edad("10/01/1991") , "sexo": "hombre", "numero_telefonico": 3126582093, "cargo": "Diseñador grafico", "fecha_ingreso": "16/08/2025",  "tiene_hijos": "No", "tipo_contrato": "Obra labor", "RH": "B-",  "estado_civil": "Soltero", "discapacidad": "Si", "poblacion_vulnerable": "No"},
                   {"nombre": "Alexandre Pantoja Passidomo", "numero_identificacion": 1330081235, "fecha_nacimiento": "16/04/1990", "edad": calcular_edad("16/04/1990") , "sexo": "hombre", "numero_telefonico": 3154049901, "cargo": "Marketing", "fecha_ingreso": "17/08/2025",  "tiene_hijos": "No", "tipo_contrato": "Obra labor", "RH": "A-",  "estado_civil": "Casado", "discapacidad": "No", "poblacion_vulnerable": "No"},
                   {"nombre": "Kayla Jean Harrison", "numero_identificacion": 4223050728, "fecha_nacimiento": "02/07/1990", "edad": calcular_edad("02/07/1990") , "sexo": "mujer", "numero_telefonico": 3104827714, "cargo": "analista de datos", "fecha_ingreso": "28/08/2025",  "tiene_hijos": "No", "tipo_contrato": "Aprendizaje", "RH": "O+",  "estado_civil": "Soltero", "discapacidad": "No", "poblacion_vulnerable": "No"},
                   {"nombre": "Valentina Anatolievna Shevchenko", "numero_identificacion": 5234080412, "fecha_nacimiento": "07/03/1988", "edad": calcular_edad("07/03/1988") , "sexo": "mujer", "numero_telefonico": 3117994302, "cargo": "Jefe de recursos humanos", "fecha_ingreso": "29/08/2025",  "tiene_hijos": "No", "tipo_contrato": "Indefinido", "RH": "A-",  "estado_civil": "Soltero", "discapacidad": "No", "poblacion_vulnerable": "No"},
                   {"nombre": "Zhang Weili", "numero_identificacion": 3317060823, "fecha_nacimiento": "13/08/1989", "edad": calcular_edad("13/08/1989") , "sexo": "mujer", "numero_telefonico": 3205549810, "cargo": "desarrollador", "fecha_ingreso": "30/08/2025",  "tiene_hijos": "No", "tipo_contrato": "Definido", "RH": "B+",  "estado_civil": "Soltero", "discapacidad": "No", "poblacion_vulnerable": "No"},
                   {"nombre": "Islam Ramazanovich Makhachev", "numero_identificacion": 2224090925, "fecha_nacimiento": "27/09/1991", "edad": calcular_edad("27/09/1991") , "sexo": "hombre", "numero_telefonico": 3116675248, "cargo": "tecnico de hardware", "fecha_ingreso": "31/08/2025",  "tiene_hijos": "Si", "tipo_contrato": "Definido", "RH": "AB-",  "estado_civil": "Casado", "discapacidad": "Si", "poblacion_vulnerable": "No"},
                   {"nombre": "Magomed Gadzhievich Ankalaev", "numero_identificacion": 3318120924, "fecha_nacimiento": "02/09/1992", "edad": calcular_edad("02/09/1992") , "sexo": "hombre", "numero_telefonico": 3207784912, "cargo": "guardia de seguridad", "fecha_ingreso": "01/09/2025",  "tiene_hijos": "No", "tipo_contrato": "Obra labor", "RH": "AB+",  "estado_civil": "Soltero", "discapacidad": "No", "poblacion_vulnerable": "No"},
                   {"nombre": "Dricus du Plessis", "numero_identificacion": 3414021120, "fecha_nacimiento": "10/02/1994" ,"edad": calcular_edad("10/02/1994"), "sexo": "hombre", "numero_telefonico": 3129037741, "cargo": "jefe de contabilidad", "fecha_ingreso": "03/09/2025", "tiene_hijos": "No", "tipo_contrato": "Idenfinido", "RH": "A+", "estado_civil": "Soltero", "discapacidad": "No", "poblacion_vulnerable": "Si"},
                   {"nombre": "Jerome Maxwell Holloway", "numero_identificacion": 1023121225, "fecha_nacimiento": "04/12/1991" ,"edad": calcular_edad("04/12/1991"), "sexo": "hombre", "numero_telefonico": 3154408823, "cargo": "contador", "fecha_ingreso": "03/09/2025", "tiene_hijos": "Si", "tipo_contrato": "Idenfinido", "RH": "AB+", "estado_civil": "Divorciado", "discapacidad": "No", "poblacion_vulnerable": "No"},
                   {"nombre": "Ronda Jean Rousey", "numero_identificacion": 1521080215, "fecha_nacimiento": "01/02/1987" ,"edad": calcular_edad("01/02/1987"), "sexo": "mujer", "numero_telefonico": 3105597743, "cargo": "auxiliar de contabilidad", "fecha_ingreso": "04/09/2025", "tiene_hijos": "No", "tipo_contrato": "Aprendizaje", "RH": "O-", "estado_civil": "Soltero", "discapacidad": "No", "poblacion_vulnerable": "No"},
                   ] #Se agrupan diccionarios dentro de la lista con la informacion de cada empleado usando claves para acceder a los valores


#Crear funcion para mostrar a todos los empleados
def mostrar_empleados():
    for empleados in lista_empleados: #Bucle para recorrer la lista
        print(f"|{empleados['nombre']}|, |{empleados['numero_identificacion']}|, |{empleados['fecha_nacimiento']}|, |{empleados['edad']}|, |{empleados['sexo']}|, |{empleados['numero_telefonico']}|, |{empleados['cargo']}|, |{empleados['fecha_ingreso']}|, |{empleados['tiene_hijos']}|, |{empleados['tipo_contrato']}|, |{empleados['RH']}|, |{empleados['estado_civil']}|, |{empleados['discapacidad']}|, |{empleados['poblacion_vulnerable']}|") #Imprimir la informacion de cada empleado por consola
    if lista_empleados == []:
        print("No hay empleados") 


#Definir funcion para buscar empleados
def buscar_empleados(numero_de_identificacion): #Se define la funcion con los parametros que se solicitaran para la busqueda
    for empleado in lista_empleados:
        if numero_de_identificacion == empleado["numero_identificacion"]:  #Se compara si el numero de identificacion ingresado por el usuario es esta en la clave 'numero_identificacion'
            return empleado  #Si lo esta retorna el diccionario con toda la informacion del emplead
    return "El empleado no existe" #Si no retorna mensaje de señalando que el empleado buscado no existe


#Definir funcion para registrar nuevos empleados
def registrar_empleado(nombre, numero_identificacion, fecha_nacimiento, sexo, numero_telefonico, cargo, fecha_ingreso, tiene_hijos, tipo_contrato, RH, estado_civil, discapacidad, poblacion_vulnerable): #Se define la funcion con los parametros que se solicitaran al usuario
    if not nombre.replace(" ", "").isalpha() or numero_identificacion == "" or not numero_identificacion.isdigit() or fecha_nacimiento == ""  or  numero_telefonico == "" or not numero_telefonico.isdigit() or cargo == "" or fecha_ingreso == "": #Mediante un if se comprueba si las cadenas estan vacias y si las cadenas de ciertos valores son unicamente numeros
        return "las entradas deben ser validas" #En caso de que cierta informacion este vacia o no solo contenga numeros la funcion devuelve un mensaje indicandolo
    numero_identificacion = int(numero_identificacion) #Se transforman las cadenas a enteros
    numero_telefonico = int(numero_telefonico)
    if numero_identificacion <= 0  or numero_telefonico <= 0:  #Una vez convertidas a enteros se verifica si algun valor es menor o igual a 0
        return "Las entradas deben ser validas"   #En caso de que si la funcion devuelve un mensaje indicandolo
    if fecha_nacimiento.count("/") < 2 or fecha_nacimiento.count("/") > 2: #Se verifica mediante count que la cadena ingresada por el usuario contenga el formato especificado usando /
        return "La fecha de nacimiento debe estar separado por /" #Si no lo tiene se envia un mensaje indicandolo
    if fecha_ingreso.count("/") < 2 or fecha_ingreso.count("/") > 2:
        return "La fecha de ingreso debe estar separado por /"
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
    opciones_discapacidad = {1: "Si", 2: "No"}
    discapacidad = opciones_discapacidad[discapacidad]
    opciones_poblacion_vulnerable = {1: "Si", 2: "No"}
    poblacion_vulnerable = opciones_poblacion_vulnerable[poblacion_vulnerable]
    nuevo_empleado = {"nombre": nombre, "numero_identificacion": numero_identificacion, "fecha_nacimiento": fecha_nacimiento, "edad": calcular_edad(fecha_nacimiento), "sexo": sexo, "numero_telefonico": numero_telefonico, "cargo": cargo, "fecha_ingreso": fecha_ingreso, "tiene_hijos": tiene_hijos, "tipo_contrato":tipo_contrato, "RH": RH, "estado_civil": estado_civil, "discapacidad": discapacidad, "poblacion_vulnerable": poblacion_vulnerable } #Una vez que se hacen las comprobaciones se guardan los valores en este diccionario con su respectiva clave
    for empleado in lista_empleados: 
        if nuevo_empleado["nombre"] == empleado["nombre"] or nuevo_empleado["numero_identificacion"] == empleado["numero_identificacion"] or  nuevo_empleado["numero_telefonico"] == empleado["numero_telefonico"]: #Se recorre la lista de empleados y se comprueba que el nuevo empleado no tenga la misma informacion que un empleado ya existente 
            return "No puede haber empleados con la misma informacion nombre/id/numero telefonico" #En caso de que la tenga la funcion retorna indicandolo
    lista_empleados.append(nuevo_empleado) #Una vez hechas todas las comprobaciones se agrega el diccionario que contiene al nuevo empleado a la lista de empleados
    print("El empleado se ha registrado con exito!") #Se indica que se ha añadido con exito
    return nuevo_empleado  #Imprime el diccionario con la informacion del nuevo empleado


def eliminar_empleado(): #verificar si hay empleados
    if lista_empleados == []: #verificar si la lista esta vacia
        print("No hay empleados para eliminar")
        return #sale de la funcion si no hay empleados
    
    print("\n--- Lista de empleados ---") #mostrar la lista actual
    mostrar_empleados() #llama a la funcion mostrar_empleado
    
    nombre = input("Digite el nombre del trabajador a eliminar: ").lower().strip() #pedir nombre del empleado que va a ser eliminado
    
    empleado_encontrado = None #Guarda el diccionario del empleado si se encuentra
    posicion = -1 #Guardar el indice del empleado en la lista
    
    for i, empleado in enumerate(lista_empleados): #Recorre la lista de empleados para buscar coincidencias
        if empleado["nombre"].lower() == nombre: #Compara el nombre ingresado con el nombre del empleado actual
            empleado_encontrado = empleado #si hay coincidencia guarda el empleado y su posicion
            posicion = i #Guarda el indice donde esta el empleado
            break #salimos del bucle porque ya encontro el empleado
    
    if empleado_encontrado: #verifica si se encontro un empleado con ese nombre
        print(f"\nEmpleado encontrado: {empleado_encontrado['nombre']}") #muestra los datos del empleado encontrado
        confirmacion = input("¿Está seguro que desea eliminar este empleado? (si/no): ").lower().strip() #Pide confirmacion
        
        if confirmacion == "si": #Eliminar empleado de la lista usando su posicion
            lista_empleados.pop(posicion) #elimina el elemento en esa posicion
            print("Empleado eliminado")
        else: #Si el usuario no confirma se cancela la eliminacion
            print("Eliminación cancelada") #si el usuario no confirma se cancela
    else:
        print("No se encontró un empleado con ese nombre") #si no se encontro ningun empleado con ese nombre

#Definir funcion para modificar informacion de los empleados:
def modificar_empleado(numero_identificacion): #Se crea la funcion con el parametro que se le pedira al usuario
    for empleado in lista_empleados:  #Se recorre la lista de empleados y se guarda el diccionario de cada empleado en la variable empleado
        if numero_identificacion == empleado["numero_identificacion"]: #Si el numero de identificacion ingresado por el usuario coincide con un numero de identificacion dentro del diccionario de empleados
            while True:        #Mediante un bucle while se despliega el meenu de todos los parametros modificables
                print("""Escoja el dato que desea modificar:
                      1. Nombre
                      2. Numero de identificacion
                      3. Fecha de nacimiento
                      4. Cambiar sexo
                      5. Numero telefonico                                        
                      6. Cargo
                      7. Fecha de ingreso
                      8. Tiene hijos
                      9. Tipo de contrato
                      10. RH
                      11. Estado civil
                      12. Discapacidad
                      13. Poblacion vulnerable
                      0. Guardar y salir"""
                      )
                opcion = int(input("Digite una opcion 1: "))   #Se pide la opcion como numero entero
                match opcion:  #Mediante un switchcase
                    case 1:  #Reemplazar nombre
                        nombre = input("Digite el nuevo nombre: ").strip().title() #Se pide el nuevo nombre al usuario
                        if nombre.replace(" ", "").isalpha():   #Se quitan los espacios dentro del nombre y se comprueba si solo contiene caracteres alfabeticos
                            empleado["nombre"] = nombre    #Si se valida la condicin se remplaza la clave nombre dentro del diccionario con el nuevo nombre
                        else:
                            print("El nombre debe contener solo letras y no debe estar vacio")  #Si no se envia un mensaje avisando que el nombre debe contener solo letras y no se debe dejar vacio
                    case 2: #Reemplazar numero de identificacion
                        empleado_actual = empleado #Se guarda el empleado actual digitado por el usuario para diferenciarlo de los demas
                        numero_id = input("Digite el nuevo numero de identificacion: ").strip() #Se piede el nuevo numero de identificacion
                        numero_isdigit = False  
                        numero_mayor_0 = False                #Usando banderas se hacen validaciones
                        numero_no_repetido = False
                        if numero_id.isdigit(): #Si el numero de identificacion solo contiene digitos
                            numero_isdigit = True   #La bandera se convierte en true
                            numero_id = int(numero_id)   #Se convierte el numero de identificacion a entero
                        else:
                            print("El numero de id solo debe contener numeros y no debe tener espacios")  #Si los caracteres no son unicamente digitos se envia un mensaje indicandolo
                        if numero_isdigit and numero_id > 0: #Si el la bandera isdigit es True y el numero de identificacion es mayor a 0
                            numero_mayor_0 = True  #La bandera mayor a 0 se convierte a true
                        else:
                            print("El numero no puede ser menor o igual a 0")  #Si las condiciones anteriores no se cumplen se imprime un mensaje indicandolo
                        if numero_isdigit and numero_mayor_0:  #Si las banderas isdigit y numero mayor a 0 son true
                            repetido = False #Se crea una bandera local dentro del if
                            for emp in lista_empleados: #Se reocorre la lista nuevamente
                                if emp != empleado_actual and numero_id == emp["numero_identificacion"]: #Si el empleado es diferente al empleado que se esta modificando 
                                    print("El numero de identificacion ya existe")                       #Y el numero de identificacion del empleado iterado es igual al numero de id del empleado ingresado por el usuario
                                    repetido = True                                                      #Se imprime un mensaje indicando que el numero de id ya existe
                                    break                                                                #La bandera repetido se convierte a true y se rompe el bucle
                            if not repetido:               #Si la bandera repetido es False 
                                numero_no_repetido = True  #La bandera de numero de id no repetido se convierte a true
                        if numero_isdigit and numero_mayor_0 and numero_no_repetido:  #Si todas las banderas son True
                            empleado["numero_identificacion"] = numero_id            #Se remplaza la clave numero de identificacion con el numero de id ingresado por el usuario
                    case 3: #Remplazar fecha de nacimiento
                        fecha_nacimiento = input("Digite la nueva fecha de nacimiento Dia/Mes/Año: ").strip() #Se pide la fecha de nacimiento al usuario
                        if fecha_nacimiento.count("/") < 2 or fecha_nacimiento.count("/") > 2: #Se comprueba que el usuario siga la estructura de fechas contando el numero de /
                            print("La fecha de nacimiento debe estar separada por /")  #Si no lo sigue se imprime un mensaje indicandolo
                        else:
                            empleado["fecha_nacimiento"] = fecha_nacimiento  #Si la fecha pasa las validaciones se remplaza en el diccionario
                            empleado["edad"] = calcular_edad(fecha_nacimiento) #Se recalcula la edad con la nueva fecha de nacimiento
                    case 4: #Reemplazar sexo
                        print("""Escoja una opcion:  
                              1. Hombre
                              2. Mujer         
                              3. Otro """) #Se despliega un menu con las opciones disponibles
                        sexo = int(input("Digite una opcion 1-3: "))   #Se pide la opcion como numero entero
                        match sexo:  #Usando un switchcase
                            case 1:
                                empleado["sexo"] = "Hombre"  #Caso 1 se remplaza la clave sexo con hombre
                            case 2:
                                empleado["sexo"] = "Mujer" #Caso 2 se remplaza la clave sexo con mujer
                            case 3:
                                empleado["sexo"] = "Otro"  #Caso 3 se remplaza la clave sexo con otro
                            case _:
                                print("Escoja una opcion valida")  #Si el usuario coloca una opcion no contemplada se imprime un mensaje indicandolo
                    case 5: #Reemplazar numero telefonico
                        empleado_actual = empleado #Se guarda el empleado ingresado por el usuario en empleado actual
                        numero_telefonico = input("Digite el nuevo numero de telefono: ").strip() #Se solicita el nuevo numero telefonico
                        telefono_solo_numeros = False  
                        telefono_mayor_0 = False         #Mediante el uso de banderas se hacen las validaciones
                        telefono_no_repetido = False
                        if numero_telefonico.isdigit():  #Se comprueba que solo contenga digitos 
                            telefono_solo_numeros = True   #Si pasa la validacion la bandera de solo numeros se convierte a True
                            numero_telefonico = int(numero_telefonico)  #El numero telefonico se convierte a entero
                        else:
                            print("El numero telefonico debe contener solo numeros y no debe tener espacios") #Si no pasa la validacion se imprime un mensaje indicandolo
                        if telefono_solo_numeros and numero_telefonico > 0: #Si solo numeros es true y el numero telefoncio es mayor a 0
                            telefono_mayor_0 = True #La bandera mayor a 0 se convierte a true
                        else:
                            print("El numero debe ser mayor a 0")  #En caso de que no se imprime un mensaje indicandolo
                        if telefono_solo_numeros and telefono_mayor_0:
                            repetido = False     #Si el telefono ingresado solo contiene numeros y es mayor a 0 se crea una nueva bandera repetido
                            for emp in lista_empleados:  #Se recorre la lista nuevamente
                                if emp != empleado_actual and numero_telefonico == emp["numero_telefonico"]:  #Si el empleado iterado es diferente al ingresado por el usuario
                                    print("El numero de telefono ingresado ya existe")                        #Y el numero telefonico ingreado por el usuario es igual a uno ya existente
                                    repetido = True                           #Repetido se convierte en true y se rompe el bucle
                                    break
                            if not repetido:  #Si repetido es false
                                telefono_no_repetido = True  #Telefono no repedito se convierte a True
                        if telefono_solo_numeros and telefono_mayor_0 and telefono_no_repetido: #Si todas las validaciones anteriores son True
                            empleado["numero_telefonico"] = numero_telefonico   #El numero ingresado por el usuario remplaza al valor dentro de la clave del diccionario
                    case 6: #Reemplazar cargo
                        cargo = input("Digite el nuevo cargo: ") #Se solicita el nuevo cargo al usuario
                        if not cargo.replace(" ", "").isalpha():   #Se eliminan los espacios para comprobar si solo contiene caracteres alfabeticos
                            print("El cargo digitado debe contener solo letras")  #Si lo anterior es False se envia un mensaje indicandolo
                        else:
                            empleado["cargo"] = cargo  #En caso de que pase la comprobacion se remplaza el valor con la clave cargo dentro del diccionario del empleado
                    case 7: #Reemplazar fecha de ingreso
                        fecha_ingreso = input("Diigte la nueva fecha de ingreso Dia/Mes/Año: ") #Se solicita la nueva fecha de ingreso al usuario
                        if fecha_ingreso.count("/") < 2 or fecha_ingreso.count("/") > 2:  #Se valida que siga el formato estabelcido
                            print("La fecha de ingreso debe estar separada por /")  #En caso de no seguir el formato se envia un mensaje indicandolo
                        else:
                            empleado["fecha_ingreso"] = fecha_ingreso   #Si pasa la validacion se reemplaza el valor de la clave fecha de ingreso con la nueva fecha de ingreso
                    case 8: #Cambiar si tiene hijos o no
                        print("""Escoja un opcion: 
                              1. Si
                              2. No""")  #Se despliega un menu con las opciones
                        tiene_hijos = int(input("Digite una opcion 1-2: ")) #Se solicita la opcion como numero entero
                        match tiene_hijos:  #Mediante un switchcase
                            case 1:
                                empleado["tiene_hijos"] = "Si" #Caso 1 se reemplaza el valor de tiene hijos con un Si
                            case 2:
                                empleado["tiene_hijos"] = "No"  #Caso 2 Se reemplaza el valor de tiene hojos con un No
                            case _:
                                print("Escoja una opcion valida")  #En caso de ingresar una opcion no contemplada se imprime un mensaje indicandolo
                    case 9:  #Cambiar tipo de contrato
                        print("""Tipo de contrato:
                      1. Definido
                      2. Indefinido
                      3. Obra labor
                      4. Aprendizaje""")  #Se imprimen todos los tipos de contrato
                        tipo_contrato = int(input("Escoja una opcion 1-4: "))  #Se solicita una opcion como numero entero
                        match tipo_contrato:   
                            case 1:
                                empleado["tipo_contrato"] = "Definido"
                            case 2:
                                empleado["tipo_contrato"] = "Indefinido"    #Se remplaza el valor de la clave tipo de contrato dependiendo de la opcion escojida
                            case 3: 
                                empleado["tipo_contrato"] = "Obra labor"
                            case 4:
                                empleado["tipo_contrato"] = "Aprendizaje"
                            case _:
                                print("Escoja una opcion valida")  #En caso de ingresar una opcion no contemplada se imprime un mensaje indicandolo
                    case 10: #Reemplazar tipo de RH
                        print("""Tipo de RH:
                      1. A+
                      2. A-
                      3. B+
                      4. B-
                      5. AB+
                      6. AB-
                      7. O+  
                      8. O-""") #Se imprime un menu con todos los tipos de RH
                        RH = int(input("Digite una opcion 1-8: ")) #Se solicita la opcion como numero entero
                        match RH:
                            case 1:
                                empleado["RH"] = "A+"
                            case 2:
                                empleado["RH"] = "A-"
                            case 3:
                                empleado["RH"] = "B+"
                            case 4:
                                empleado["RH"] = "B-"      #Se reemplaza el valor de la clave RH dependiendo de la opcion ingresada
                            case 5:
                                empleado["RH"] = "AB+"
                            case 6:
                                empleado["RH"] = "AB-"
                            case 7:
                                empleado["RH"] = "O+"
                            case 8:
                                empleado["RH"] = "O-"
                            case _:
                                print("Digite una opcion valida") #En caso de ingresar una opcion no contemplada se imprime un mensaje indicandolo
                    case 11:
                        print("""Indique estado civil:
                          1. Soltero
                          2. Casado
                          3. Union libre
                          4. Divorciado
                          5. Viudo""")  # Se imprime un menu con todas las opciones de estado civil
                        estado_civil = int(input("Digite una opcion 1-5: "))  #Se solicita una opcion como numero entero
                        match estado_civil:
                            case 1:
                                empleado["estado_civil"] = "Soltero"
                            case 2:
                                empleado["estado_civil"] = "Casado"
                            case 3:                                                      #Se reemplaza el valor de la clave estado civil dependiendo de la opcion escogida
                                empleado["estado_civil"] = "Union libre"
                            case 4:
                                empleado["estado_civil"] = "Divorciado"
                            case 5:
                                empleado["estado_civil"] = "Viudo"
                            case _:
                                print("Digite una opcion valida") #En caso de ingresar una opcion no contemplada se imprime un mensaje indicandolo
                    case 12:
                        print("""El empleado cuenta con alguna discapacidad:
                      1. Si
                      2.No""") # Se imprime un menu con todas las opciones de discapacidad
                        discapacidad = int(input("Digite una opcion 1-2: ")) #Se solicita una opcion como numero entero
                        match discapacidad:
                            case 1:
                                empleado["discapacidad"] = "Si"   #Caso 1 se reemplaza el valor de la clave discapacidad con Si
                            case 2:
                                empleado["discapacidad"] = "No"   #Caso 2 se reemplaza el valor de la clave discapacidad con No
                            case _:
                                print("Digite una opcion valida") #En caso de ingresar una opcion no contemplada se imprime un mensaje indicandolo
                    case 13:
                        print("""El empleado pertenece a alguna poblacion vulnerable:
                      1. Si
                      2. No""") #Se imprime un menu con todas las opciones de poblacion vulnerable
                        poblacion_vulnerable = int(input("Digite una opcion 1-2: ")) #Se solicita una opcion como numero entero
                        match poblacion_vulnerable:
                            case 1:
                                empleado["poblacion_vulnerable"] = "Si" #Caso 1 se reemplaza el valor de la clave poblacion vulnerable con Si
                            case 2:
                                empleado["poblacion_vulnerable"] = "No" #Caso 2 se reemplaza el valor de la clave discapacidad con No
                            case _:
                                print("Digite una opcion valida") #En caso de ingresar una opcion no contemplada se imprime un mensaje indicandolo
                    case 0:
                        print("Los cambios se han realizado con exito")  #Una vez que los cambios se han realizado se sale del menu
                        return empleado  #Retorna el diccionario del empleado modificado con todos los cambios hechos para comprobar que todo este correcto
                    case _:
                        print("Digite una opcion valida") #En caso de ingresar una opcion no contemplada se imprime un mensaje indicandolo

    return "El empleado buscado no existe"  #En caso de ingresar el numero de identifiacion que no exista la funcion retorna indicandolo

#Funcion para filtrar empleados por edad especifica
def filtrar_edad_especifica(edad): #Se crea la funcion con el parametro solicitado 
    if edad.isdigit():
        edad = int(edad)
    else:
        return "La edad no puede contener letras"    #Se valida mediante condicionales que la edad solo contenga numeros y no sea menor o igual a 0
    if edad <= 0:
        return "La edad debe ser mayor a 0"
    coincidencias = []        #Se crea una lista para guardar las coincidencias
    for empleado in lista_empleados:    #Se recorre la lista de empleados
        if edad == empleado["edad"]:   #Si la edad ingresada coincide con edades dentro de la lista de empleados
            coincidencias.append(empleado)   #Se guardan los diccionarios que coincidan en la lista de coincidencias
    if coincidencias != []:    #Si la lista de coincidencias no esta vacia se imprime
        return coincidencias
    elif coincidencias == []:
        return"No existen empleados con la edad ingresada"  #Si esta vacia se imprime un mensaje indicando que no existe ningun empleado de la edad ingresada
#Funcion para filtrar empleados por rango de edad
def filtrar_edad_rango(edad_min, edad_max):   #Se crea la funcion con los parametros solicitados
    if edad_min.isdigit() and edad_max.isdigit():
        edad_min = int(edad_min)
        edad_max = int(edad_max)                         
    else:
        return "Las edades ingresadas no pueden contener letras"     #Mediante condicionales se valida que las edades sean solo numeros, no menores a 0 y que la edad minima no sea mayor a la maxima
    
    if edad_min <= 0 or edad_max <= 0:
        return "las edades ingresadas deben ser mayores a 0"
    if edad_max <= edad_min:
        return "La edad maxima no puede ser menor a la edad minima"
    coincidencias = []
    for empleado in lista_empleados:    #Se recorre la lista de empleados
        if empleado["edad"] in range(edad_min, edad_max + 1 ):   #Si hay edades en el diccionario de empleados que esten dentro del rango de la edad minima y maxima ingresada
            coincidencias.append(empleado)   #Se añaden a la lista de coincidencias
    
    if coincidencias != []:  
        return coincidencias  #Si la lista de coincidencias no esta vacia se imprime
    elif coincidencias == []:
        return "No existen empleados en los rangos de edad ingresados" #Si esta vacia se imprime un mensaje indicando que no existe ningun empleado de la edad ingresada

   
def menu():  #Se define el menu dentru de una funcion para reutilizarlo
    print("""
1. Mostrar lista de todos los empleados
2. Buscar empleado
3. Registrar empleado
4. Eliminar empleado
5. Modificar informacion de empleado
6. Filtrar empleados por edad
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
            nombre = input("Digite el nombre del nuevo empleado: ").title().strip() #Se solicita al usuario el nombre del nuevo empleado, se eliminan espacios y se ponen las iniciales en mayusculas
            numero_identificacion = input("Digite el numero de identificacion del nuevo empleado: ") #Se pide el id como cadena
            fecha_nacimiento = input("Digite la fecha de nacimiento Dia/Mes/Año: ") #Se pide la fecha de nacimiento 
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
            fecha_ingreso = input("Digite la fecha de ingreso Dia/Mes/Año: ")  #Se solicita la fecha de ingreso
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
            while True: 
                print("""El empleado cuenta con alguna discapacidad:
                      1. Si
                      2.No""")
                discapacidad = int(input("Digite una opcion 1-2: "))
                if discapacidad == 1 or discapacidad == 2:
                    break
                else:
                    print("Digite una opcion valida")
            while True:
                print("""El empleado pertenece a alguna poblacion vulnerable:
                      1. Si
                      2. No""")
                poblacion_vulnerable = int(input("Digite una opcion 1-2: "))
                if poblacion_vulnerable == 1 or poblacion_vulnerable == 2:
                    break
                else:
                    print("Digite una opcoon valida")
            print(registrar_empleado(nombre, numero_identificacion, fecha_nacimiento, sexo, numero_telefonico, cargo, fecha_ingreso, tiene_hijos, tipo_contrato, RH, estado_civil, discapacidad, poblacion_vulnerable)) #Se llama a la funcion

        case 4:
            eliminar_empleado() #llamar a la funcion eliminar empleado
        case 5:
            numero_identificacion = int(input("Digite el numero de identificacion del empleado: ")) #Pedir numero de identificacion del empleado a modificar
            print(modificar_empleado(numero_identificacion))  #Se llama a la funcion modificar empleado
        case 6:
            print("""Filtrar edad por:
                  1. Edad especifica
                  2. Rango de edad       
                  """)    #Se imprime menu indicando con opciones de filtrado
            opcion = int(input("Escoja una opcion 1-2: "))
            match opcion:
                case 1:
                    edad = input("Digite la edad del empleado en años: ")
                    print(filtrar_edad_especifica(edad))                  #En el primer caso se pide la edad especifica y se llama a la funcion
                case 2:
                    edad_min = input("Digire la edad minima: ")
                    edad_max = input("Digite la edad maxima: ")
                    print(filtrar_edad_rango(edad_min, edad_max))      #En el segundo caso se solicitan las dos edades y se llama a la funcion
        case 0: 
            print("Tenga un buen dia!")    #Mensaje de despedida y romper el bucle
            break
        case _:
            print("Digite una opcion valida")  #Si el usuario digita una opcion no contemplada se imprime mensaje de error
    



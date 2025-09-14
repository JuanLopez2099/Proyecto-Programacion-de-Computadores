#Definir lista de empleados

lista_empleados = [{"nombre": "Juan Camilo Lopez Gonzalez", "edad": 20, "sexo": "hombre", "numero telefonico": "123456789", "cargo": "desarrollador"},
                   {"nombre": "Estefania Rodriguez", "edad": 18, "sexo": "mujer", "numero telefonico": "987654321", "cargo": "analista"},
                   {"nombre": "Sarah Ulloque", "edad": 21, "sexo": "mujer", "numero telefonico": "543219876", "cargo": "gerente"}
                   ] #Se agrupan diccionarios dentro de la lista con la informacion de cada empleado usando claves para acceder a los valores


#Definir funcion para mostrar a todos los empleados
def mostrar_empleados():
    for empleados in lista_empleados: #Bucle para recorrer la lista
        print(f"|{empleados["nombre"]}|, |{empleados["edad"]}|, |{empleados["sexo"]}|, |{empleados["numero telefonico"]}|, |{empleados["cargo"]}|") #Imprimir la informacion de cada empleado por consola


import datetime as datetime #Se importa la libreria datetime
#Funcion para calcular edad de las personas 
def calcular_edad(fecha_nacimiento):  #Se define la funcion con el parametro que se le solicitara al usuario
    fecha_nac = datetime.datetime.strptime(fecha_nacimiento.strip(), "%d/%m/%Y") #Usando la libreria datetime convertimos la fecha de nacimiento de string a formato datetime
    fecha_actual = datetime.datetime.today()  #Usando la libreria datetime se llama a la fecha actual

    edad = fecha_actual.year - fecha_nac.year   #Al año actual se le resta el año de nacimiento del empleado

    return edad  #Retorna la edad

 

#Definir lista de empleados
lista_empleados = [{"nombre": "Juan Camilo Lopez Gonzalez", "numero_identificacion": 1110460138, "fecha_nacimiento": "20/05/2005" ,"edad": calcular_edad("20/05/2005"), "sexo": "hombre", "numero_telefonico": 1234567899, "cargo": "jefe de desarrollo", "fecha_ingreso": "29/07/2025", "tiene_hijos": "No", "tipo_contrato": "Indefinido", "RH": "O+", "estado_civil": "Soltero", "discapacidad": "No", "poblacion_vulnerable": "No"},
                   {"nombre": "Estefania Rodriguez", "numero_identificacion": 2220242033, "fecha_nacimiento": "03/06/2007", "edad": calcular_edad("01/01/2007") , "sexo": "mujer", "numero_telefonico": 9876543211, "cargo": "jefe de analistas", "fecha_ingreso": "02/07/2025",  "tiene_hijos": "No", "tipo_contrato": "Indefinido", "RH": "B+",  "estado_civil": "Soltero", "discapacidad": "No", "poblacion_vulnerable": "No"},
                   {"nombre": "Sarah Ulloque", "numero_identificacion": 2220222033, "fecha_nacimiento": "15/04/2004", "edad":calcular_edad("15/04/2004") , "sexo": "mujer", "numero_telefonico": 5432198767, "cargo": "psicologa", "fecha_ingreso": "01/07/2025", "tiene_hijos": "Si", "tipo_contrato": "Indefinido", "RH": "A-", "estado_civil": "Casado", "discapacidad": "Si", "poblacion_vulnerable": "Si"},
                   {"nombre": "Jack El Destripador", "numero_identificacion": 2223335556, "fecha_nacimiento": "01/01/2007", "edad": calcular_edad("01/01/2007") , "sexo": "hombre", "numero_telefonico": 3054637387, "cargo": "ceo", "fecha_ingreso": "01/01/2025",  "tiene_hijos": "No", "tipo_contrato": "Indefinido", "RH": "B+",  "estado_civil": "Viudo", "discapacidad": "No", "poblacion_vulnerable": "No"},
                   {"nombre": "Alex Sandro Silva Pereira", "numero_identificacion": 1330115133, "fecha_nacimiento": "07/07/1987", "edad": calcular_edad("07/07/1987") , "sexo": "hombre", "numero_telefonico": 3105550123, "cargo": "jefe de seguridad", "fecha_ingreso": "20/07/2025",  "tiene_hijos": "Si", "tipo_contrato": "Indefinido", "RH": "AB+",  "estado_civil": "Casado", "discapacidad": "No", "poblacion_vulnerable": "No"},
                   {"nombre": "Thomas Paul Aspinall", "numero_identificacion": 4623812222, "fecha_nacimiento": "11/04/1993", "edad": calcular_edad("11/04/1993") , "sexo": "hombre", "numero_telefonico": 3012314512, "cargo": "ingeniero de telecomunicaciones", "fecha_ingreso": "13/07/2025",  "tiene_hijos": "Si", "tipo_contrato": "Definido", "RH": "O+",  "estado_civil": "Casado", "discapacidad": "No", "poblacion_vulnerable": "No"},
                   {"nombre": "Khamzat Khizarovich Chimaev", "numero_identificacion": 5712943456, "fecha_nacimiento": "01/05/1994", "edad": calcular_edad("01/05/1994") , "sexo": "hombre", "numero_telefonico": 3054560278, "cargo": "Analista de datos", "fecha_ingreso": "19/07/2025",  "tiene_hijos": "No", "tipo_contrato": "Obra labor", "RH": "O-",  "estado_civil": "Viudo", "discapacidad": "No", "poblacion_vulnerable": "Si"},
                   {"nombre": "Jack Della Madalena", "numero_identificacion": 9932334667, "fecha_nacimiento": "10/09/1996", "edad": calcular_edad("10/09/1996") , "sexo": "hombre", "numero_telefonico": 3023210391, "cargo": "tecnico de hardware", "fecha_ingreso": "08/08/2025",  "tiene_hijos": "No", "tipo_contrato": "Aprendizaje", "RH": "A+",  "estado_civil": "Union libre", "discapacidad": "No", "poblacion_vulnerable": "No"},
                   {"nombre": "Ilia Topuria Bendeliani", "numero_identificacion": 1216080617, "fecha_nacimiento": "21/01/1997", "edad": calcular_edad("21/01/1997") , "sexo": "hombre", "numero_telefonico": 3114037721, "cargo": "tecnico de seguridad", "fecha_ingreso": "20/08/2025",  "tiene_hijos": "Si", "tipo_contrato": "Definido", "RH": "AB-",  "estado_civil": "Casado", "discapacidad": "No", "poblacion_vulnerable": "Si"},
                   {"nombre": "Alexander Volkanovski", "numero_identificacion": 2415022999, "fecha_nacimiento": "29/09/1988", "edad": calcular_edad("29/09/1988") , "sexo": "hombre", "numero_telefonico": 3207774410, "cargo": "cafeteria", "fecha_ingreso": "13/08/2025",  "tiene_hijos": "Si", "tipo_contrato": "Definido", "RH": "O+",  "estado_civil": "Soltero", "discapacidad": "No", "poblacion_vulnerable": "No"},
                   {"nombre": "Merab Dvalishvili", "numero_identificacion": 2019040323, "fecha_nacimiento": "10/01/1991", "edad": calcular_edad("10/01/1991") , "sexo": "hombre", "numero_telefonico": 3126582093, "cargo": "diseñador grafico", "fecha_ingreso": "16/08/2025",  "tiene_hijos": "No", "tipo_contrato": "Obra labor", "RH": "B-",  "estado_civil": "Soltero", "discapacidad": "Si", "poblacion_vulnerable": "No"},
                   {"nombre": "Alexandre Pantoja Passidomo", "numero_identificacion": 1330081235, "fecha_nacimiento": "16/04/1990", "edad": calcular_edad("16/04/1990") , "sexo": "hombre", "numero_telefonico": 3154049901, "cargo": "marketing", "fecha_ingreso": "17/08/2025",  "tiene_hijos": "No", "tipo_contrato": "Obra labor", "RH": "A-",  "estado_civil": "Casado", "discapacidad": "No", "poblacion_vulnerable": "No"},
                   {"nombre": "Kayla Jean Harrison", "numero_identificacion": 4223050728, "fecha_nacimiento": "02/07/1990", "edad": calcular_edad("02/07/1990") , "sexo": "mujer", "numero_telefonico": 3104827714, "cargo": "analista de datos", "fecha_ingreso": "28/08/2025",  "tiene_hijos": "No", "tipo_contrato": "Aprendizaje", "RH": "O+",  "estado_civil": "Soltero", "discapacidad": "No", "poblacion_vulnerable": "No"},
                   {"nombre": "Valentina Anatolievna Shevchenko", "numero_identificacion": 5234080412, "fecha_nacimiento": "07/03/1988", "edad": calcular_edad("07/03/1988") , "sexo": "mujer", "numero_telefonico": 3117994302, "cargo": "jefe de recursos humanos", "fecha_ingreso": "29/08/2025",  "tiene_hijos": "No", "tipo_contrato": "Indefinido", "RH": "A-",  "estado_civil": "Soltero", "discapacidad": "No", "poblacion_vulnerable": "No"},
                   {"nombre": "Zhang Weili", "numero_identificacion": 3317060823, "fecha_nacimiento": "13/08/1989", "edad": calcular_edad("13/08/1989") , "sexo": "mujer", "numero_telefonico": 3205549810, "cargo": "desarrollador", "fecha_ingreso": "30/08/2025",  "tiene_hijos": "No", "tipo_contrato": "Definido", "RH": "B+",  "estado_civil": "Soltero", "discapacidad": "No", "poblacion_vulnerable": "No"},
                   {"nombre": "Islam Ramazanovich Makhachev", "numero_identificacion": 2224090925, "fecha_nacimiento": "27/09/1991", "edad": calcular_edad("27/09/1991") , "sexo": "hombre", "numero_telefonico": 3116675248, "cargo": "tecnico de hardware", "fecha_ingreso": "31/08/2025",  "tiene_hijos": "Si", "tipo_contrato": "Definido", "RH": "AB-",  "estado_civil": "Casado", "discapacidad": "Si", "poblacion_vulnerable": "No"},
                   {"nombre": "Magomed Gadzhievich Ankalaev", "numero_identificacion": 3318120924, "fecha_nacimiento": "02/09/1992", "edad": calcular_edad("02/09/1992") , "sexo": "hombre", "numero_telefonico": 3207784912, "cargo": "guardia de seguridad", "fecha_ingreso": "01/09/2025",  "tiene_hijos": "No", "tipo_contrato": "Obra labor", "RH": "AB+",  "estado_civil": "Soltero", "discapacidad": "No", "poblacion_vulnerable": "No"},
                   {"nombre": "Dricus du Plessis", "numero_identificacion": 3414021120, "fecha_nacimiento": "10/02/1994" ,"edad": calcular_edad("10/02/1994"), "sexo": "hombre", "numero_telefonico": 3129037741, "cargo": "jefe de contabilidad", "fecha_ingreso": "03/09/2025", "tiene_hijos": "No", "tipo_contrato": "Indefinido", "RH": "A+", "estado_civil": "Soltero", "discapacidad": "No", "poblacion_vulnerable": "Si"},
                   {"nombre": "Jerome Maxwell Holloway", "numero_identificacion": 1023121225, "fecha_nacimiento": "04/12/1991" ,"edad": calcular_edad("04/12/1991"), "sexo": "hombre", "numero_telefonico": 3154408823, "cargo": "contador", "fecha_ingreso": "03/09/2025", "tiene_hijos": "Si", "tipo_contrato": "Indefinido", "RH": "AB+", "estado_civil": "Divorciado", "discapacidad": "No", "poblacion_vulnerable": "No"},
                   {"nombre": "Ronda Jean Rousey", "numero_identificacion": 1521080215, "fecha_nacimiento": "01/02/1987" ,"edad": calcular_edad("01/02/1987"), "sexo": "mujer", "numero_telefonico": 3105597743, "cargo": "auxiliar de contabilidad", "fecha_ingreso": "04/09/2025", "tiene_hijos": "No", "tipo_contrato": "Aprendizaje", "RH": "O-", "estado_civil": "Soltero", "discapacidad": "No", "poblacion_vulnerable": "No"},
                   {"nombre": "Conor Anthony McGregor", "numero_identificacion": 7482915630, "fecha_nacimiento": "14/07/1988" ,"edad": calcular_edad("14/07/1988"), "sexo": "hombre", "numero_telefonico": 3014218608, "cargo": "programador backend", "fecha_ingreso": "05/09/2025", "tiene_hijos": "Si", "tipo_contrato": "Aprendizaje", "RH": "O+", "estado_civil": "Union libre", "discapacidad": "No", "poblacion_vulnerable": "No"},
                   {"nombre": "José Aldo da Silva Oliveira Júnior", "numero_identificacion": 3928471056, "fecha_nacimiento": "09/09/1986" ,"edad": calcular_edad("09/09/1986"), "sexo": "hombre", "numero_telefonico": 3124567890, "cargo": "Analista de RH", "fecha_ingreso": "10/09/2025", "tiene_hijos": "Si", "tipo_contrato": "Obra labor", "RH": "AB+", "estado_civil": "Casado", "discapacidad": "Si", "poblacion_vulnerable": "No"},
                   {"nombre": "Jonathan Dwight Jones", "numero_identificacion": 5817392046, "fecha_nacimiento": "19/07/1987" ,"edad": calcular_edad("19/07/1987"), "sexo": "hombre", "numero_telefonico": 3215678943, "cargo": "Desarrollador Full-Stack", "fecha_ingreso": "15/09/2025", "tiene_hijos": "No", "tipo_contrato": "Obra labor", "RH": "B+", "estado_civil": "Viudo", "discapacidad": "No", "poblacion_vulnerable": "No"},
                   {"nombre": "Khabib Abdulmanápovich Nurmagomédov", "numero_identificacion": 6704928135, "fecha_nacimiento": "20/09/1988" ,"edad": calcular_edad("20/09/1988"), "sexo": "hombre", "numero_telefonico": 3876543210, "cargo": "Contador Financiero", "fecha_ingreso": "19/09/2025", "tiene_hijos": "Si", "tipo_contrato": "Definido", "RH": "AB+", "estado_civil": "Casado", "discapacidad": "No", "poblacion_vulnerable": "No"},
                   {"nombre": "Bryce Andrew Mitchell", "numero_identificacion": 2491057384, "fecha_nacimiento": "04/10/1994" ,"edad": calcular_edad("04/10/1994"), "sexo": "hombre", "numero_telefonico": 3456789012, "cargo": "Soporte Tecnico", "fecha_ingreso": "23/09/2025", "tiene_hijos": "No", "tipo_contrato": "Obra labor", "RH": "A-", "estado_civil": "Soltero", "discapacidad": "No", "poblacion_vulnerable": "No"},
                   {"nombre": "Shavkat Bakhtibaevich Rakhmonov", "numero_identificacion": 8213465970, "fecha_nacimiento": "23/10/1994", "edad": calcular_edad("23/10/1994"), "sexo": "hombre", "numero_telefonico": 3987654321, "cargo": "Ingeniero de Software", "fecha_ingreso": "15/09/2025", "tiene_hijos": "No", "tipo_contrato": "Indefinido", "RH": "O+", "estado_civil": "Soltero", "discapacidad": "No", "poblacion_vulnerable": "No"},
                   {"nombre": "Arman Tsarukyan", "numero_identificacion": 4567891230, "fecha_nacimiento": "11/10/1996", "edad": calcular_edad("11/10/1996"), "sexo": "hombre", "numero_telefonico": 3214567890, "cargo": "Analista de Datos", "fecha_ingreso": "20/10/2025", "tiene_hijos": "Sí", "tipo_contrato": "Definido", "RH": "A+", "estado_civil": "Casado", "discapacidad": "No", "poblacion_vulnerable": "Si"},
                   {"nombre": "Belal Muhammad", "numero_identificacion": 6739201458, "fecha_nacimiento": "09/04/1988", "edad": calcular_edad("09/04/1988"), "sexo": "hombre", "numero_telefonico": 3456789123, "cargo": "Supervisor de tareas", "fecha_ingreso": "10/11/2025", "tiene_hijos": "No", "tipo_contrato": "Obra labor", "RH": "B+", "estado_civil": "Casado", "discapacidad": "No", "poblacion_vulnerable": "No"},
                   {"nombre": "Karen Alexa Grasso Montes", "numero_identificacion": 3091748265, "fecha_nacimiento": "09/08/1993", "edad": calcular_edad("09/08/1993"), "sexo": "mujer", "numero_telefonico": 3123456789, "cargo": "Psicologa", "fecha_ingreso": "25/09/2025", "tiene_hijos": "No", "tipo_contrato": "Aprendizaje", "RH": "O-", "estado_civil": "Soltera", "discapacidad": "No", "poblacion_vulnerable": "No"},
                   {"nombre": "Tracy Cortez", "numero_identificacion": 1478923065, "fecha_nacimiento": "10/12/1993", "edad": calcular_edad("10/12/1993"), "sexo": "mujer", "numero_telefonico": 3789123456, "cargo": "Diseñadora UX/UI", "fecha_ingreso": "30/10/2025", "tiene_hijos": "No", "tipo_contrato": "Definido", "RH": "AB-", "estado_civil": "Soltera", "discapacidad": "No", "poblacion_vulnerable": "No"},
                   {"nombre": "Ailín Luciana Pérez", "numero_identificacion": 9274031586, "fecha_nacimiento": "16/11/1994", "edad": calcular_edad("16/11/1994"), "sexo": "mujer", "numero_telefonico": 3876543210, "cargo": "Especialista en Marketing Digital", "fecha_ingreso": "18/09/2025", "tiene_hijos": "No", "tipo_contrato": "Aprendizaje", "RH": "A+", "estado_civil": "Soltera", "discapacidad": "No", "poblacion_vulnerable": "No"},
                   {"nombre": "Miesha Theresa Tate", "numero_identificacion": 5041287369, "fecha_nacimiento": "18/08/1986", "edad": calcular_edad("18/08/1986"), "sexo": "mujer", "numero_telefonico": 3567891234, "cargo": "Auxiliar de RH", "fecha_ingreso": "22/10/2025", "tiene_hijos": "Sí", "tipo_contrato": "Indefinido", "RH": "O+", "estado_civil": "Casada", "discapacidad": "No", "poblacion_vulnerable": "No"},
                   {"nombre": "Aline Silva Pereira Celso", "numero_identificacion": 6812394075, "fecha_nacimiento": "06/06/1990", "edad": calcular_edad("06/06/1990"), "sexo": "mujer", "numero_telefonico": 3412567890, "cargo": "Desarrolladora Backend", "fecha_ingreso": "15/11/2025", "tiene_hijos": "No", "tipo_contrato": "Definido", "RH": "B-", "estado_civil": "Soltera", "discapacidad": "No", "poblacion_vulnerable": "No"},
                   {"nombre": "Youssef Zalal", "numero_identificacion": 4728193065, "fecha_nacimiento": "04/09/1996", "edad": calcular_edad("04/09/1996"), "sexo": "hombre", "numero_telefonico": 3891234567, "cargo": "Analista de Seguridad Informática", "fecha_ingreso": "12/09/2025", "tiene_hijos": "No", "tipo_contrato": "Definido", "RH": "A-", "estado_civil": "Soltero", "discapacidad": "No", "poblacion_vulnerable": "Si"},
                   {"nombre": "Joshua James Emmett", "numero_identificacion": 7502938214, "fecha_nacimiento": "04/03/1985", "edad": calcular_edad("04/03/1985"), "sexo": "hombre", "numero_telefonico": 3546789123, "cargo": "Supervisor de operaciones", "fecha_ingreso": "28/10/2025", "tiene_hijos": "Sí", "tipo_contrato": "Indefinido", "RH": "O+", "estado_civil": "Casado", "discapacidad": "Si", "poblacion_vulnerable": "No"},
                   {"nombre": "Tagir Ulanbekov", "numero_identificacion": 3165987402, "fecha_nacimiento": "08/07/1991", "edad": calcular_edad("08/07/1991"), "sexo": "hombre", "numero_telefonico": 3678901234, "cargo": "Desarrollador Frontend", "fecha_ingreso": "05/11/2025", "tiene_hijos": "No", "tipo_contrato": "Obra labor", "RH": "B+", "estado_civil": "Soltero", "discapacidad": "No", "poblacion_vulnerable": "No"},
                   {"nombre": "Sean Daniel O'Malley", "numero_identificacion": 8923465170, "fecha_nacimiento": "24/10/1994", "edad": calcular_edad("24/10/1994"), "sexo": "hombre", "numero_telefonico": 3765432109, "cargo": "Auxiliar de Ciberseguridad", "fecha_ingreso": "20/09/2025", "tiene_hijos": "Sí", "tipo_contrato": "Aprendizaje", "RH": "A+", "estado_civil": "Union Libre", "discapacidad": "No", "poblacion_vulnerable": "No"},
                   {"nombre": "Marlon Andrés Vera Delgado", "numero_identificacion": 2497813065, "fecha_nacimiento": "02/12/1992", "edad": calcular_edad("02/12/1992"), "sexo": "hombre", "numero_telefonico": 3451236789, "cargo": "Analista de Sistemas", "fecha_ingreso": "15/10/2025", "tiene_hijos": "Sí", "tipo_contrato": "Indefinido", "RH": "O-", "estado_civil": "Casado", "discapacidad": "No", "poblacion_vulnerable": "No"},
                   {"nombre": "Dominick Reyes", "numero_identificacion": 6712048359, "fecha_nacimiento": "26/12/1989", "edad": calcular_edad("26/12/1989"), "sexo": "hombre", "numero_telefonico": 3894567123, "cargo": "Desarrollador Full-Stack", "fecha_ingreso": "10/11/2025", "tiene_hijos": "No", "tipo_contrato": "Obra labor", "RH": "B+", "estado_civil": "Soltero", "discapacidad": "No", "poblacion_vulnerable": "No"},
                   {"nombre": "Mackenzie Lynne Dern Santos", "numero_identificacion": 5839201746, "fecha_nacimiento": "24/03/1993", "edad": calcular_edad("24/03/1993"), "sexo": "mujer", "numero_telefonico": 3741289056, "cargo": "Especialista en Experiencia de Usuario", "fecha_ingreso": "25/09/2025", "tiene_hijos": "Sí", "tipo_contrato": "Indefinido", "RH": "A+", "estado_civil": "Casada", "discapacidad": "No", "poblacion_vulnerable": "No"},
                   {"nombre": "Jéssica Andrade", "numero_identificacion": 4293817506, "fecha_nacimiento": "25/09/1991", "edad": calcular_edad("25/09/1991"), "sexo": "mujer", "numero_telefonico": 3567890123, "cargo": "Servicios generales", "fecha_ingreso": "18/10/2025", "tiene_hijos": "No", "tipo_contrato": "Definido", "RH": "O+", "estado_civil": "Casada", "discapacidad": "No", "poblacion_vulnerable": "No"},
                   {"nombre": "Julianna Nicole Peña", "numero_identificacion": 7162938045, "fecha_nacimiento": "19/08/1989", "edad": calcular_edad("19/08/1989"), "sexo": "mujer", "numero_telefonico": 3892341678, "cargo": "Desarrolladora de flutter", "fecha_ingreso": "12/11/2025", "tiene_hijos": "Sí", "tipo_contrato": "Obra labor", "RH": "B-", "estado_civil": "Soltera", "discapacidad": "No", "poblacion_vulnerable": "No"},
                   {"nombre": "Rose Gertrude Namajunas", "numero_identificacion": 3749201586, "fecha_nacimiento": "29/06/1992", "edad": calcular_edad("29/06/1992"), "sexo": "mujer", "numero_telefonico": 3678902345, "cargo": "Diseñadora Gráfica", "fecha_ingreso": "22/09/2025", "tiene_hijos": "No", "tipo_contrato": "Indefinido", "RH": "A+", "estado_civil": "Casada", "discapacidad": "No", "poblacion_vulnerable": "No"},
                   {"nombre": "Tatiana Yadira Suarez Padilla", "numero_identificacion": 5081372946, "fecha_nacimiento": "19/12/1990", "edad": calcular_edad("19/12/1990"), "sexo": "mujer", "numero_telefonico": 3546789012, "cargo": "Analista de Calidad de Software", "fecha_ingreso": "17/10/2025", "tiene_hijos": "No", "tipo_contrato": "Definido", "RH": "O-", "estado_civil": "Soltera", "discapacidad": "No", "poblacion_vulnerable": "No"},
                   {"nombre": "Amanda Ribas", "numero_identificacion": 6923814705, "fecha_nacimiento": "26/08/1993", "edad": calcular_edad("26/08/1993"), "sexo": "mujer", "numero_telefonico": 3789012567, "cargo": "Especialista en Soporte Técnico", "fecha_ingreso": "08/11/2025", "tiene_hijos": "Sí", "tipo_contrato": "Obra labor", "RH": "B+", "estado_civil": "Soltera", "discapacidad": "No", "poblacion_vulnerable": "No"},
                   {"nombre": "Jiří Procházka", "numero_identificacion": 4839207516, "fecha_nacimiento": "14/10/1992", "edad": calcular_edad("14/10/1992"), "sexo": "hombre", "numero_telefonico": 3124567890, "cargo": "Ingeniero de Calidad", "fecha_ingreso": "20/09/2025", "tiene_hijos": "No", "tipo_contrato": "Indefinido", "RH": "O+", "estado_civil": "Soltero", "discapacidad": "Si", "poblacion_vulnerable": "No"},
                   {"nombre": "Khalil Rountree Junior", "numero_identificacion": 7592048136, "fecha_nacimiento": "26/02/1990", "edad": calcular_edad("26/02/1990"), "sexo": "hombre", "numero_telefonico": 3789012345, "cargo": "Especialista en DevOps", "fecha_ingreso": "15/10/2025", "tiene_hijos": "Sí", "tipo_contrato": "Definido", "RH": "A-", "estado_civil": "Casado", "discapacidad": "No", "poblacion_vulnerable": "No"},
                   {"nombre": "Michael Bisping", "numero_identificacion": 2918475063, "fecha_nacimiento": "24/02/1980", "edad": calcular_edad("24/02/1980"), "sexo": "hombre", "numero_telefonico": 3456789012, "cargo": "Contratista de seguridad", "fecha_ingreso": "10/11/2025", "tiene_hijos": "Sí", "tipo_contrato": "Obra labor", "RH": "B+", "estado_civil": "Casado", "discapacidad": "Si", "poblacion_vulnerable": "No"},
                   {"nombre": "Israel Adesanya", "numero_identificacion": 6374921085, "fecha_nacimiento": "22/04/1989", "edad": calcular_edad("22/04/1989"), "sexo": "hombre", "numero_telefonico": 3891234567, "cargo": "Analista de productos", "fecha_ingreso": "25/09/2025", "tiene_hijos": "No", "tipo_contrato": "Aprendizaje", "RH": "AB+", "estado_civil": "Soltero", "discapacidad": "No", "poblacion_vulnerable": "No"},
                   {"nombre": "Charles Do Bronx Oliveira", "numero_identificacion": 1057384926, "fecha_nacimiento": "17/10/1989", "edad": calcular_edad("17/10/1989"), "sexo": "hombre", "numero_telefonico": 3678901234, "cargo": "Analista Financiero", "fecha_ingreso": "30/10/2025", "tiene_hijos": "Sí", "tipo_contrato": "Definido", "RH": "O-", "estado_civil": "Casado", "discapacidad": "No", "poblacion_vulnerable": "Si"}] #Se agrupan diccionarios dentro de la lista con la informacion de cada empleado usando claves para acceder a los valores

#Definir lista de tablero kanban
tablero_kanban = [{"nombre": "Juan Camilo Lopez Gonzalez", "numero_identificacion": 1110460138, "numero_telefonico": 1234567899, "cargo": "jefe de desarrollo", "tarea_actual": "proyecto gestion de recursos humanos", "estado": "InProgress"},
                  {"nombre": "Estefania Rodriguez", "numero_identificacion": 2220242033, "numero_telefonico": 9876543211, "cargo": "jefe de analistas", "tarea_actual": "gestionar filtrado de datos", "estado": "InProgress"},
                  {"nombre": "Thomas Paul Aspinall", "numero_identificacion": 4623812222, "numero_telefonico": 3012314512, "cargo": "ingeniero de telecomunicaciones", "tarea_actual": "optimizar red interna", "estado": "ToDo"},
                  {"nombre": "Khamzat Khizarovich Chimaev", "numero_identificacion": 5712943456, "numero_telefonico": 3054560278, "cargo": "analista de datos", "tarea_actual": "elaborar informe de rendimiento", "estado": "InProgress"},
                  {"nombre": "Jack Della Madalena", "numero_identificacion": 9932334667, "numero_telefonico": 3023210391, "cargo": "tecnico de hardware", "tarea_actual": "revisar mantenimiento de servidores", "estado": "Done"},
                  {"nombre": "Zhang Weili", "numero_identificacion": 3317060823, "numero_telefonico": 3205549810, "cargo": "desarrollador", "tarea_actual": "crear módulo de autenticación", "estado": "ToDo"},
                  {"nombre": "Islam Ramazanovich Makhachev", "numero_identificacion": 2224090925, "numero_telefonico": 3116675248, "cargo": "tecnico de hardware", "tarea_actual": "instalar equipo en sala de pruebas", "estado": "Done"},
                  {"nombre": "Merab Dvalishvili", "numero_identificacion": 2019040323, "numero_telefonico": 3126582093, "cargo": "diseñador grafico", "tarea_actual": "diseño de interfaz grafica", "estado": "ToDo"},
                  {"nombre": "Kayla Jean Harrison", "numero_identificacion": 4223050728, "numero_telefonico": 3104827714, "cargo": "analista de datos", "tarea_actual": "analizar tendencias de clientes", "estado": "InProgress"},
                  {"nombre": "Alexandre Pantoja Passidomo", "numero_identificacion": 1330081235, "numero_telefonico": 3154049901, "cargo": "marketing", "tarea_actual": "ofertar el proyecto a empresas", "estado": "ToDo"},
                  {"nombre": "Conor Anthony McGregor", "numero_identificacion": 7482915630, "numero_telefonico": 3215678943, "cargo": "programador backend", "tarea_actual": "Arreglar bugs", "estado": "InProgress"},
                  {"nombre": "Jonathan Dwight Jones", "numero_identificacion": 5817392046, "numero_telefonico": 3215678943, "cargo": "Desarrollador Full-Stack", "tarea_actual": "Gestion de github", "estado": "InProgress"},
                  {"nombre": "Shavkat Rakhmonov", "numero_identificacion": 8213465970, "numero_telefonico": 3987654321, "cargo": "Ingeniero de Software", "tarea_actual": "Desarrollo de API para gestión de empleados", "estado": "InProgress"},
                  {"nombre": "Arman Tsarukyan", "numero_identificacion": 4567891230, "numero_telefonico": 3214567890, "cargo": "Analista de Datos", "tarea_actual": "Análisis predictivo para optimización de procesos", "estado": "ToDo"},
                  {"nombre": "Tracy Cortez", "numero_identificacion": 1478923065, "numero_telefonico": 3789123456, "cargo": "Diseñadora UX/UI", "tarea_actual": "Diseño de interface para tablero kanban", "estado": "Done"},
                  {"nombre": "Aline Silva Pereira Celso", "numero_identificacion": 6812394075, "numero_telefonico": 3412567890, "cargo": "Desarrolladora Backend", "tarea_actual": "Implementación de sistemas de atenticacion", "estado": "InProgress"},
                  {"nombre": "Youssef Zalal", "numero_identificacion": 4728193065, "numero_telefonico": 3891234567, "cargo": "Analista de Seguridad Informática", "tarea_actual": "Auditoría de seguridad para bases de datos", "estado": "ToDo"},
                  {"nombre": "Tagir Ulanbekov", "numero_identificacion": 3165987402, "numero_telefonico": 3678901234, "cargo": "Desarrollador Frontend", "tarea_actual": "Implementación de componentes React para dashboard interactivo", "estado": "Done"},
                  {"nombre": "Sean Daniel O'Malley", "numero_identificacion": 8923465170, "numero_telefonico": 3765432109, "cargo": "Auxiliar de Ciberseguridad", "tarea_actual": "Monitoreo de vulnerabilidades en sistema de autenticación", "estado": "InProgress"},
                  {"nombre": "Marlon Andrés Vera Delgado", "numero_identificacion": 2497813065, "numero_telefonico": 3451236789, "cargo": "Analista de Sistemas", "tarea_actual": "Optimización de base de datos para sistema de gestión de clientes", "estado": "ToDo"},
                  {"nombre": "Dominick Reyes", "numero_identificacion": 6712048359, "numero_telefonico": 3894567123, "cargo": "Desarrollador Full-Stack", "tarea_actual": "Desarrollo de sitio web empresarial", "estado": "Done"},
                  {"nombre": "Mackenzie Lynne Dern Santos", "numero_identificacion": 5839201746, "numero_telefonico": 3741289056, "cargo": "Especialista en Experiencia de Usuario", "tarea_actual": "Diseño de version movil de sitio web empresarial", "estado": "InProgress"},
                  {"nombre": "Julianna Nicole Peña", "numero_identificacion": 7162938045, "numero_telefonico": 3892341678, "cargo": "Desarrolladora de Flutter", "tarea_actual": "Soporte de app de gestion de recursos humanos en moviles", "estado": "ToDo"},
                  {"nombre": "Rose Gertrude Namajunas", "numero_identificacion": 3749201586, "numero_telefonico": 3678902345, "cargo": "Diseñadora Gráfica", "tarea_actual": "Creación de activos gráficos para e-commerce", "estado": "InProgress"},
                  {"nombre": "Tatiana Yadira Suarez Padilla", "numero_identificacion": 5081372946, "numero_telefonico": 3546789012, "cargo": "Analista de Calidad de Software", "tarea_actual": "Ejecución de pruebas automatizadas para funciones de filtrado", "estado": "Done"},
                  {"nombre": "Amanda Ribas", "numero_identificacion": 6923814705, "numero_telefonico": 3789012567, "cargo": "Especialista en Soporte Técnico", "tarea_actual": "Resolución de incidencias en sistema app movil", "estado": "ToDo"},
                  {"nombre": "Jiří Procházka", "numero_identificacion": 4839207516, "numero_telefonico": 3124567890, "cargo": "Ingeniero de Calidad", "tarea_actual": "Diseño de plan de pruebas para base de datos", "estado": "InProgress"},
                  {"nombre": "Khalil Rountree Junior", "numero_identificacion": 7592048136, "numero_telefonico": 3789012345, "cargo": "Especialista en DevOps", "tarea_actual": "Configuración de pipeline CI/CD para despliegue de microservicios", "estado": "Done"},
                  {"nombre": "Israel Adesanya", "numero_identificacion": 6374921085, "numero_telefonico": 3891234567, "cargo": "Analista de productos", "tarea_actual": "Definición de requisitos para nuevas funcionalidades", "estado": "ToDo"},
                  ] #Se agrupan diccionarios dentro de la lista con la informacion de contacto de cada empleado, tarea y estado de la tarea


# Definir función para imprimir una lista de empleados en formato de tabla
def imprimir_tablas(lista): # Se define la función con el parámetro que se solicitará, que es la lista de empleados a mostrar
    anchos = {} # Se crea un diccionario vacío para almacenar el ancho máximo de cada columna
    campos = ["nombre", "numero_identificacion", "fecha_nacimiento", "edad", "sexo", 
              "numero_telefonico", "cargo", "fecha_ingreso", "tiene_hijos", "tipo_contrato",   # Se define la lista de claves que se mostrarán como columnas
              "RH", "estado_civil", "discapacidad", "poblacion_vulnerable"]
    
     
    for campo in campos: # Se recorre cada campo de la lista de columnas
        ancho = len(campo)  # Se asigna el ancho con la longitud del nombre del campo
        for empleado in lista: # Se recorre cada empleado en la lista
            valor = len(str(empleado[campo])) # Se calcula la longitud del valor del campo convertido a cadena
            if valor > ancho: # Si el valor es más largo que el nombre del campo
                ancho = valor # Se actualiza el ancho máximo
        anchos[campo] = ancho # Se guarda el ancho máximo de cada campo en el diccionario
    
    
    resultado = "" # Se inicializa una cadena vacía donde se construirá la tabla
    
    # Construir la fila de encabezados con alineación basada en el ancho de cada columna
    for campo in campos: # Se recorre cada campo para crear los encabezados
        resultado += f"{campo:<{anchos[campo]}}  " # Se agrega el nombre del campo alineado a la izquierda
    resultado += "\n" # Se agrega un salto de línea después de los encabezados
     
    # Construir las filas con los datos de cada empleado
    for emp in lista: # Se recorre cada empleado en la lista 
        for campo in campos:  # Se recorre cada campo para obtener los valores
            resultado += f"{str(emp[campo]):<{anchos[campo]}}  " # Se agrega el valor alineado según el ancho de la columna
        resultado += "\n" # Se agrega un salto de línea al final de cada fila
    
    return resultado # Se retorna la tabla completa como cadena

# Definir función para imprimir tabla kanban en formato de tabla
def imprimir_kanban_tablas(lista):
    anchos = {} 
    campos = ["nombre", "numero_identificacion", "numero_telefonico", "cargo", "tarea_actual", "estado"] 
     
    for campo in campos: 
        ancho = len(campo)  
        for empleado in lista: 
            valor = len(str(empleado[campo])) 
            if valor > ancho: 
                ancho = valor 
        anchos[campo] = ancho 
    
    
    resultado = "" 
    
    
    for campo in campos:
        resultado += f"{campo:<{anchos[campo]}}   " 
    resultado += "\n" 
     
   
    for emp in lista: 
        for campo in campos:  
            resultado += f"{str(emp[campo]):<{anchos[campo]}}   " 
        resultado += "\n" 
    
    return resultado

#Crear funcion para mostrar a los empleados dentro del tablero kanban
def mostrar_tablero_kanban():
    if tablero_kanban != []:  #Si el la lista no esta vacia
        return imprimir_kanban_tablas(tablero_kanban)  #Se llama a la funcion para imprimir la lista como tabla
    if tablero_kanban == []:
        return "No hay empleados dentro del tablero kanban"  #Si lo esta se indica imprimiendo un mensaje

# Definir función para asignar una nueva tarea a un empleado en el tablero Kanban
def asignar_tarea(numero_de_id):  #Se define la función con el parámetro que se solicitará al usuario
    if not numero_de_id.isdigit():
        return "El numero de id solo debe contener numeros"    #Se valida si el número de identificación ingresado contiene solo numeros
    else:
        numero_de_id = int(numero_de_id) 
    for empleado in tablero_kanban:  # Se recorre la lista del tablero Kanban
        if numero_de_id == empleado["numero_identificacion"]: #Se compara el número de identificación con el de cada empleado
            print("Empleado encontrado exitosamente: \n")  #Se indica que se ha encontrado el empleado y se imprime informacion
            print("Nombre: ", empleado["nombre"])
            print("Numero de identificacion: ", empleado["numero_identificacion"])
            print("Tarea actual: ", empleado["tarea_actual"])
            print()
            nueva_tarea = input("Digite la nueva tarea a desempeñar: ")  # Se solicita la nueva tarea a desempeñar
            empleado["tarea_actual"] = nueva_tarea  #Se reemplaza el valor dentro del diccionario con la nueva tarea
            empleado["estado"] = "ToDo"  #Se asigna autoamticamente a ToDo
            return "Cambio exitoso"  #Retora un mensaje indicando que el cambio ha sido exitoso
    else:
        return "No existe el empleado" #Si no se encuentra el numero de identificacion se imprime un mensaje indicandolo

# Definir función para gestionar el estado de una tarea en el tablero Kanban
def gestionar_estado_tarea(numero_de_id):  # Se define la función con el parámetro numero_de_id
    if not numero_de_id.isdigit():  # Se valida que el número de identificación contenga solo dígitos
        return "El numero de id solo debe contener numeros"  # Si no, se retorna un mensaje de error
    else:
        numero_de_id = int(numero_de_id)  # Se convierte a entero
    for empleado in tablero_kanban:  # Se recorre la lista del tablero Kanban
        if numero_de_id == empleado["numero_identificacion"]:  # Si el número de identificación coincide
            print("Empleado encontrado exitosamente: \n")  # Se indica que se encontró el empleado
            print("Nombre: ", empleado["nombre"])
            print("Numero de identificacion: ", empleado["numero_identificacion"])
            print("Tarea actual: ", empleado["tarea_actual"])
            print("Estado actual: ", empleado["estado"])
            print()
            # Se muestra un menú con las opciones de estado disponibles
            print("""Seleccione el nuevo estado para la tarea: \n
                  1. ToDo
                  2. InProgress
                  3. Done
                  4. Sin tarea asignada
                  """)
            nuevo_estado_opcion = int(input("Digite una opcion 1-4: "))  # Se solicita la opción numérica
            opciones_estado = {1: "ToDo", 2: "InProgress", 3: "Done", 4: "Sin tarea asignada"}  # Diccionario con las opciones
            if nuevo_estado_opcion in opciones_estado:  # Si la opción es válida
                empleado["estado"] = opciones_estado[nuevo_estado_opcion]  # Se actualiza el estado en el diccionario
                return "Estado de la tarea actualizado exitosamente"  # Se retorna un mensaje de éxito
            else:
                return "Opcion no valida"  # Si la opción no es válida, se retorna un mensaje de error
    return "No existe el empleado en el tablero Kanban"  # Si no se encuentra el empleado, se retorna un mensaje

#Definir funcion para eliminar tareas
def eliminar_tarea(numero_de_id): #Se define la función con el parámetro que se solicitará al usuario
    if not numero_de_id.isdigit(): #Se valida que el numero de identtificacion ingresado sea solo numerico
        return "El numero de id solo debe contener numeros"   
    else:
        numero_de_id = int(numero_de_id)
    for empleado in tablero_kanban:  #Se recorre la lista del tablero kanban
        if numero_de_id == empleado["numero_identificacion"]:  #Si el numero de identificacion ingresado coincide
            print("Empleado encontrado exitosamente: \n")
            print("Nombre: ", empleado["nombre"])
            print("Numero de identificacion: ", empleado["numero_identificacion"])    #Se imprime la informacion del empleado 
            print("Tarea actual: ", empleado["tarea_actual"])
            print()
            print("""Seguro que desea eliminar la tarea actual: \n   
                  1. Si
                  2. No
                  """)  #Se imprime un mensaje para validar que el usuario esta seguro de eliminar la tarea
            eliminar_tarea = int(input("Digite una opcion 1-2: "))
            match eliminar_tarea:
                case 1:
                    empleado["tarea_actual"] = "Tarea sin asignar"   #Si digita que si se reemplaza la tarea actual por una sin asignar de igual forma el estado
                    empleado["estado"] = "Tarea sin asignar"
                    return "Tarea eliminada exitosamente"
                case 2:
                    return "Saliendo..."  #Si digita no sale del menu y queda intacto
                case _:
                    return "Ingrese una opcion valida"
    else:
        return "No existe el empleado"  #Si el numero de identificacion no coincide con ningun empleado se indica mediante un mensaje

#Definir funcion para filtrar las tareas ToDo
def filtrar_tareas_todo():
    coincidencias = [] # Se crea una lista vacía para almacenar los empleados que cumplan la condición
    for empleado in tablero_kanban:
        if empleado["estado"] == "ToDo": #Se compara si el estado de la tarea es "ToDo"
            coincidencias.append(empleado) #Si coincide, se agrega el empleado a la lista de coincidencias
    
    return imprimir_kanban_tablas(coincidencias) #Se retorna la impresión de la lista filtrada en formato tabla

# Definir función para filtrar tareas InProgress
def filtrar_tareas_InProgress():
    coincidencias = []  # Se crea una lista vacía para almacenar los empleados que cumplan la condición
    for empleado in tablero_kanban:
        if empleado["estado"] == "InProgress":  # Se compara si el estado de la tarea es "InProgress"
            coincidencias.append(empleado)  # Si coincide, se agrega el empleado a la lista de coincidencias
    return imprimir_kanban_tablas(coincidencias)  # Se retorna la impresión de la lista filtrada en formato tabla

#Definir funcion para filtrar las tareas Done
def filtrar_tareas_Done():
    coincidencias = [] #Se crea una lista vacía para almacenar los empleados que cumplan la condición
    for empleado in tablero_kanban:
        if empleado["estado"] == "Done": #Se compara si el estado de la tarea es "Done"
            coincidencias.append(empleado) #Si coincide, se agrega el empleado a la lista de coincidencias
    
    return imprimir_kanban_tablas(coincidencias) #Se retorna la impresión de la lista filtrada en formato tabla


#Definir funcion para mostrar a todos los empleados
def mostrar_empleados():
    if lista_empleados != []:  #Si el la lista no esta vacia
        print(imprimir_tablas(lista_empleados)) #Se llama a la funcion para imprimir la lista como tabla
    if lista_empleados == []:
        print("No hay empleados")  #Si lo esta se indica imprimiendo un mensaje


#Definir funcion para buscar empleados
def buscar_empleados(numero_de_identificacion): #Se define la funcion con los parametros que se solicitaran para la busqueda
    emp = []
    for empleado in lista_empleados:
        if numero_de_identificacion == empleado["numero_identificacion"]:  #Se compara si el numero de identificacion ingresado por el usuario es esta en la clave 'numero_identificacion'
            emp.append(empleado)
            return imprimir_tablas(emp)  #Si lo esta retorna el diccionario con toda la informacion del emplead
    return "El empleado no existe" #Si no retorna mensaje de señalando que el empleado buscado no existe


#Definir funcion para registrar nuevos empleados
def registrar_empleado(nombre, numero_identificacion, fecha_nacimiento, sexo, numero_telefonico, cargo, fecha_ingreso, tiene_hijos, tipo_contrato, RH, estado_civil, discapacidad, poblacion_vulnerable, añadir_kanban): #Se define la funcion con los parametros que se solicitaran al usuario
    emp = []
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
    opciones_sexo_empleado = {1: "hombre", 2: "mujer", 3: "otro"}
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
    emp.append(nuevo_empleado)
    nuevo_empleado_kanban  = {"nombre": nombre, "numero_identificacion": numero_identificacion, "numero_telefonico": numero_telefonico, "cargo": cargo, "tarea_actual": "Sin tarea asignada", "estado": "Sin tarea asignada" }
    if añadir_kanban == 1:
        tablero_kanban.append(nuevo_empleado_kanban)
    print()
    print("El empleado se ha registrado con exito!") #Se indica que se ha añadido con exito
    print()
    return imprimir_tablas(emp)  #Imprime el diccionario con la informacion del nuevo empleado


def eliminar_empleado():  # Verificar si hay empleados
    if lista_empleados == []:  # Verificar si la lista está vacía
        print("No hay empleados para eliminar")
        return  # Sale de la función si no hay empleados
    

    numero_identificacion = input("Digite el número de identificación del trabajador a eliminar: ").strip() # Pedir número de identificación del empleado que va a ser eliminado
    
    # Validar que sea un número
    if not numero_identificacion.isdigit():
        print("El número de identificación debe contener solo dígitos")
        return
    
    numero_identificacion = int(numero_identificacion)  # Convertir a entero
    
    empleado_encontrado = None  # Guarda el diccionario del empleado si se encuentra
    posicion = -1  # Guardar el índice del empleado en la lista
    
    # Recorre la lista de empleados para buscar coincidencias
    for i, empleado in enumerate(lista_empleados):
        if empleado["numero_identificacion"] == numero_identificacion:  # Compara el número ingresado
            empleado_encontrado = empleado  # Si hay coincidencia guarda el empleado y su posición
            posicion = i  # Guarda el índice donde está el empleado
            break  # Salimos del bucle porque ya encontró el empleado
    for i, empleado in enumerate(tablero_kanban):
        if empleado["numero_identificacion"] == numero_identificacion:
            empleado_encontrado = empleado
            posicion = i
            break
    
    if empleado_encontrado:  # Verifica si se encontró un empleado con ese número
        # Muestra los datos del empleado encontrado
        print(f"\nEmpleado encontrado:")
        print(f"Nombre: {empleado_encontrado['nombre']}")
        print(f"Cédula: {empleado_encontrado['numero_identificacion']}")
        print(f"Cargo: {empleado_encontrado['cargo']}")
        
        print("""\n¿Está seguro que desea eliminar este empleado?
              1. Si
              2. No""")
        confirmacion = int(input("Digite una opción 1-2: "))
        
        if confirmacion == 1:
            lista_empleados.pop(posicion)  # Elimina el elemento en esa posición
            tablero_kanban.pop(posicion)
            print("Empleado eliminado exitosamente")
        elif confirmacion == 2:
            print("Eliminación cancelada")
        else:
            print("Opción inválida. Eliminación cancelada")
    else:
        print("No se encontró un empleado con ese número de identificación")

#Definir funcion para modificar informacion de los empleados:
def modificar_empleado(numero_identificacion): #Se crea la funcion con el parametro que se le pedira al usuario
    tabla = []
    if not numero_identificacion.isdigit():    #Se valida que el numero de identificacion solo contenga numeros
        return "El numero de id solo debe contener numeros"   
    else:
        numero_identificacion = int(numero_identificacion)
    for empleado in lista_empleados:  #Se recorre la lista de empleados y se guarda el diccionario de cada empleado en la variable empleado
        if numero_identificacion == empleado["numero_identificacion"]: #Si el numero de identificacion ingresado por el usuario coincide con un numero de identificacion dentro del diccionario de empleados
            while True:        #Mediante un bucle while se despliega el meenu de todos los parametros modificables
                print()
                print("""Escoja el dato que desea modificar: \n
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
                print()
                opcion = int(input("Digite una opcion 1-13: "))   #Se pide la opcion como numero entero
                print()
                match opcion:  #Mediante un switchcase
                    case 1:  #Reemplazar nombre
                        nombre = input("Digite el nuevo nombre: ").strip().title() #Se pide el nuevo nombre al usuario
                        if nombre.replace(" ", "").isalpha():   #Se quitan los espacios dentro del nombre y se comprueba si solo contiene caracteres alfabeticos
                            empleado["nombre"] = nombre    #Si se valida la condicin se remplaza la clave nombre dentro del diccionario con el nuevo nombre
                            for elemento in tablero_kanban:
                                if elemento["numero_identificacion"] == numero_identificacion:
                                    elemento["nombre"] = empleado["nombre"]
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
                            empleado["numero_identificacion"] = numero_id          #Se remplaza la clave numero de identificacion con el numero de id ingresado por el usuario
                            for elemento in tablero_kanban:
                                if elemento["numero_identificacion"] == numero_identificacion:
                                    elemento["numero_identificacion"] = empleado["numero_identificacion"]
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
                                empleado["sexo"] = "hombre"  #Caso 1 se remplaza la clave sexo con hombre
                            case 2:
                                empleado["sexo"] = "mujer" #Caso 2 se remplaza la clave sexo con mujer
                            case 3:
                                empleado["sexo"] = "otro"  #Caso 3 se remplaza la clave sexo con otro
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
                            for elemento in tablero_kanban:
                                if elemento["numero_identificacion"] == numero_identificacion:
                                    elemento["numero_telefonico"] = empleado["numero_telefonico"]
                    case 6: #Reemplazar cargo
                        cargo = input("Digite el nuevo cargo: ") #Se solicita el nuevo cargo al usuario
                        if not cargo.replace(" ", "").isalpha():   #Se eliminan los espacios para comprobar si solo contiene caracteres alfabeticos
                            print("El cargo digitado debe contener solo letras")  #Si lo anterior es False se envia un mensaje indicandolo
                        else:
                            empleado["cargo"] = cargo  #En caso de que pase la comprobacion se remplaza el valor con la clave cargo dentro del diccionario del empleado
                            for elemento in tablero_kanban:
                                if elemento["numero_identificacion"] == numero_identificacion:
                                    elemento["cargo"] = empleado["cargo"]
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
                        print()
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
                        print()
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
                        print("""El empleado cuenta con alguna discapacidad: \n
                      1.Si
                      2.No""") # Se imprime un menu con todas las opciones de discapacidad
                        print()
                        discapacidad = int(input("Digite una opcion 1-2: ")) #Se solicita una opcion como numero entero
                        match discapacidad:
                            case 1:
                                empleado["discapacidad"] = "Si"   #Caso 1 se reemplaza el valor de la clave discapacidad con Si
                            case 2:
                                empleado["discapacidad"] = "No"   #Caso 2 se reemplaza el valor de la clave discapacidad con No
                            case _:
                                print("Digite una opcion valida") #En caso de ingresar una opcion no contemplada se imprime un mensaje indicandolo
                    case 13:
                        print("""El empleado pertenece a alguna poblacion vulnerable: \n
                      1. Si
                      2. No""") #Se imprime un menu con todas las opciones de poblacion vulnerable
                        print()
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
                        print()
                        tabla.append(empleado)
                        print()
                        return imprimir_tablas(tabla)  #Retorna el diccionario del empleado modificado con todos los cambios hechos para comprobar que todo este correcto
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
    if coincidencias != []:   #Si la lista de coincidencias no esta vacia se imprime
        return imprimir_tablas(coincidencias)   
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
        return imprimir_tablas(coincidencias)  #Si la lista de coincidencias no esta vacia se imprime
    elif coincidencias == []:
        return "No existen empleados en los rangos de edad ingresados" #Si esta vacia se imprime un mensaje indicando que no existe ningun empleado de la edad ingresada
    
#Definir funcion para filtrar empleados por una fecha de ingreso especifica
def filtrar_fecha_ingreso_especifica(fecha_ingreso): #Se define la funcion con el parametro que se solicitara al usuario
    if fecha_ingreso.count("/") < 2 or fecha_ingreso.count("/") > 2: #Se valida que la fecha siga el formato Dia/Mes/Año contando el numero de "/"
        return "La fecha ingresada debe seguir el formato indicado" #Si no sigue el formato se retorna un mensaje indicandolo
    coincidencias = [] #Se crea una lista vacia para guardar los empleados que coincidan con la fecha de ingreso
    for empleado in lista_empleados:
        if fecha_ingreso == empleado["fecha_ingreso"]:   #Si la fecha ingresada coincide con la fecha de ingreso del empleado
            coincidencias.append(empleado)  #Se añade el empleado a la lista de coincidencias
    if coincidencias != []:
        return imprimir_tablas(coincidencias)    #Si no esta vacia se imprimen todas las coinidencias, si lo esta se indica que no hay empleados con la fecha ingresada
    elif coincidencias == []:
        return "No existen empleados con la fecha de ingreso ingresada"
    
#Definir funcion para filtrar empleados por el dia de su fecha de ingreso    
def filtrar_fecha_ingreso_dia(dia):  #Se define la funcion con el parametro que se solicitara al usuario
    if not dia.isdigit(): #Se valida que el dia ingresado contenga solo numeros
        return "Los parametros ingresados deben contener unicamente numeros"
    else:
        dia = int(dia)  #Si es valido, se convierte el valor de dia a entero
    coincidencias = []
    for empleado in lista_empleados: 
        fecha_ingreso_lista = datetime.datetime.strptime(empleado["fecha_ingreso"], "%d/%m/%Y") #Se convierte la fecha de ingreso del empleado de string a datetime
        if dia == fecha_ingreso_lista.day:  #Si el dia ingresado coincide con el dia de la fecha de ingreso del empleado
            coincidencias.append(empleado)  #Se añade el empleado a la lista de coincidencias
    if coincidencias != []:
        return imprimir_tablas(coincidencias)    #Si no esta vacia se imprimen todas las coinidencias, si lo esta se indica que no hay empleados con la fecha ingresada
    elif coincidencias == []:
        return "No existen empleados ingresados en el dia indicado"
    
#Definir funcion para filtrar empleados por el mes de su fecha de ingreso
def filtrar_fecha_ingreso_mes(mes): #Se define la funcion con el parametro que se solicitara al usuario
    if not mes.isdigit(): #Se valida que el mes ingresado contenga solo numeros
        return "Los parametros ingresados deben contener unicamente numeros"
    else:
        mes = int(mes)
    coincidencias = []
    for empleado in lista_empleados:
        fecha_ingreso_lista = datetime.datetime.strptime(empleado["fecha_ingreso"], "%d/%m/%Y") #Se convierte la fecha de ingreso del empleado de string a datetime
        if mes == fecha_ingreso_lista.month:  #Si el mes ingresado coincide con el mes de la fecha de ingreso del empleado
            coincidencias.append(empleado)  #Se añade el empleado a la lista de coincidencias
    if coincidencias != []:
        return imprimir_tablas(coincidencias) #Si no esta vacia se imprimen todas las coinidencias, si lo esta se indica que no hay empleados con la fecha ingresada
    elif coincidencias == []:
        return "No existen empleados ingresados en el mes indicado"

#Definir funcion para filtrar empleados por el año de su fecha de ingreso
def filtrar_fecha_ingreso_año(año): #Se define la funcion con el parametro que se solicitara al usuario
    if not año.isdigit():  #Se valida que el año ingresado contenga solo numeros
        return "Los parametros ingresados deben contener unicamente numeros" 
    else:
        año = int(año)
    coincidencias = []
    for empleado in lista_empleados:
        fecha_ingreso_lista = datetime.datetime.strptime(empleado["fecha_ingreso"], "%d/%m/%Y")  #Se convierte la fecha de ingreso del empleado de string a datetime
        if año == fecha_ingreso_lista.year:
            coincidencias.append(empleado)  #Se añade el empleado a la lista de coincidencias
    if coincidencias != []:
        return imprimir_tablas(coincidencias)   #Si no esta vacia se imprimen todas las coinidencias, si lo esta se indica que no hay empleados con la fecha ingresada
    elif coincidencias == []:
        return "No existen empleados ingresados en el año indicado"

# Definir función para filtrar empleados según su sexo
def filtrar_sexo(sexo): # Se crea la función con el parámetro que se pedirá al usuario
    opciones_sexo = {1: "hombre", 2: "mujer", 3: "otro"} # Se define un diccionario con las opciones disponibles para sexo
    sexo = opciones_sexo[sexo]
    coincidencias = []
    for empleado in lista_empleados: # Se recorre la lista de empleados
        if sexo == empleado["sexo"]:
            coincidencias.append(empleado) # Si coincide, se agrega el diccionario del empleado a la lista de coincidencias
    if coincidencias != []: 
        return imprimir_tablas(coincidencias) # Se retorna la lista con los empleados que cumplen la condición
    elif coincidencias == []:
        return "No hay empleados del sexo indicado"
    
#Definir funcion para filtrar empleados segun tipo de contrato
def filtrar_contrato(contrato): #se crea la función con el parámetro que se pedirá la usuario
    opciones_contrato = {1: "Indefinido", 2:"Definido", 3:"Obra labor", 4:"Aprendizaje"}
    contrato = opciones_contrato[contrato] 
    coincidencias = [] 
    for empleado in lista_empleados: #se recorre la lista de empleados 
        if contrato == empleado["tipo_contrato"]:
            coincidencias.append(empleado) #si coincide, se agrega el diccionario del empleado a la lista de coincidencias 
    if coincidencias != []: 
        return imprimir_tablas(coincidencias) # Se retorna la lista con los empleados que cumplen la condición
    elif coincidencias == []:
        return "No hay empleados con este tipo de contrato"         
            
    
# Definir función para filtrar empleados según si tienen hijos o no
def filtrar_hijos(hijos): # Se crea la función con el parámetro que se pedirá al usuario
    opciones_hijos = {1: "Si", 2: "No"} # Se define un diccionario con las opciones disponibles para indicar si el empleado tiene hijos
    hijos = opciones_hijos[hijos] # Se convierte la opción numérica ingresada por el usuario al valor correspondiente en texto
    coincidencias = []
    for empleado in lista_empleados:
        if hijos == empleado["tiene_hijos"]: # Se compara la opción seleccionada con el valor del empleado
            coincidencias.append(empleado) # Si coincide se agrega el diccionario del empleado a la lista de coincidencias
    if coincidencias != []:
        return imprimir_tablas(coincidencias) # Se retorna la lista con los empleados que cumplen la condición

#Definir función para filtrar empleados según si tienen discapacidades o no 
def filtrar_discapacidad(discapacidad): #se crea la función con el parámetro que se pedirá que se pedirá al usuario
    opciones__discapacidad = {1:"Si", 2:"No"} # Se define un diccionario con las opciones disponibles para indicar si el empleado tiene discapacidades
    discapacidad = opciones__discapacidad[discapacidad] # Se convierte la opción numérica ingresada por el usuario al valor correspondiente en texto
    coincidencias = []
    for empleado in lista_empleados:
        if discapacidad == empleado["discapacidad"]: # Se compara la opción seleccionada con el valor del empleado
            coincidencias.append(empleado)# Si coincide se agrega al diccionario del empleado a la lista de coincidencias
    if coincidencias != []:
        return imprimir_tablas(coincidencias) # Se retorna la lista con los empleados que cumplen la condición
        
# Definir función para filtrar empleados según su tipo de sangre
def filtrar_rh(RH): # Se define la función con el parámetro que se solicitará al usuario
    opciones_RH = {1: "A+", 2: "A-", 3: "B+", 4: "B-", 5: "AB+", 6: "AB-", 7: "O+", 8: "O-"} # Se crea un diccionario con las opciones disponibles para el tipo de sangre
    RH = opciones_RH[RH] # Se convierte la opción numérica ingresada por el usuario al valor correspondiente en texto
    coincidencias = []
    for empleado in lista_empleados:
        if RH == empleado["RH"]:  #Se compara el tipo de sangre del empleado con el valor ingresado
            coincidencias.append(empleado)
    if coincidencias != []:
        return imprimir_tablas(coincidencias) # Se retorna la lista con los empleados que cumplen la condición

# Definir función para filtrar empleados según su estado civil
def filtrar_estado_civil(estado_civil): # Se define la función con el parámetro que se solicitará al usuario
    opciones_estado_civil = {1: "Soltero", 2: "Casado", 3: "Union libre", 4: "Divorciado", 5: "Viudo"} # Se crea un diccionario con las opciones disponibles para estado civil
    estado_civil = opciones_estado_civil[estado_civil] # Se convierte la opción numérica ingresada por el usuario al valor correspondiente en texto
    coincidencias = []
    for empleado in lista_empleados:
        if estado_civil == empleado["estado_civil"]: # Se compara el estado civil del empleado con el valor ingresad
            coincidencias.append(empleado) # Si coincide, se agrega el diccionario del empleado a la lista de coincidencias

    if coincidencias != []:
        return imprimir_tablas(coincidencias)  #Se retorna la lista con los empleados que cumplen la condición

# Definir función para filtrar empleados según si pertenecen o no a una población vulnerable
def filtrar_poblacion_vulnerable(poblacion_vulnerable): # Se define la función con el parámetro que se solicitará al usuario
    opciones_poblacion_vulnerable = {1: "Si", 2: "No"}   # Se crea un diccionario con las opciones disponibles: Sí o No
    poblacion_vulnerable = opciones_poblacion_vulnerable[poblacion_vulnerable] # Se convierte la opción numérica ingresada por el usuario a su valor correspondiente en texto
    coincidencias = []
    for empleado in lista_empleados:
        if poblacion_vulnerable == empleado["poblacion_vulnerable"]: # Se compara el valor de la clave 'poblacion_vulnerable' del empleado con el ingresado por el usuario
            coincidencias.append(empleado) # Si coincide, se agrega el diccionario del empleado a la lista de coincidencias
    if coincidencias != []:
        return imprimir_tablas(coincidencias) # Se retorna la lista con los empleados que cumplen la condición

def menu():  #Se define el menu dentru de una funcion para reutilizarlo
    print("""
1. Mostrar lista de todos los empleados
2. Buscar empleado
3. Registrar empleado
4. Eliminar empleado
5. Modificar informacion de empleado
6. Filtrar empleados por edad
7. Filtrar empleados por fecha de ingreso
8. Filtrar empleados por sexo
9. Filtrar por hijos Si/No
10. Filtrar por RH
11. Filtrar por estado civil
12. Filtrar por poblacion vulnerable
13. Filtrar por tipo de Contrato
14. Filtrar por discapacidad
15. Gestion Proyecto Kanba
0. Salir
""")

print("\n ========== Bienvenido al menu de JackDRipper Software ==========") #Se imprime el titulo del menu fuera del bucle para que no se imprima en cada vuelta
while True:  
    menu()    #Se llama a la funcion del menu
    opcion = int(input("Digite una opcion 1-15: "))  #Se solicita la opcion al usuario, se le pide en numero entero
    print()

    match opcion:
        case 1:
            mostrar_empleados() #Opcion numero uno, se llama a la funcion para mostrar la lista de empleados
        case 2:
            numero_de_identificacion = int(input("Digite el numero de identificacion del empleado: ")) #Solicita al usuario el numero de identificacion como entero
            print()
            print(buscar_empleados(numero_de_identificacion)) #Llama a la funcion y devuelve el resultado
        case 3:
            nombre = input("Digite el nombre del nuevo empleado: ").title().strip() #Se solicita al usuario el nombre del nuevo empleado, se eliminan espacios y se ponen las iniciales en mayusculas
            numero_identificacion = input("Digite el numero de identificacion del nuevo empleado: ") #Se pide el id como cadena
            fecha_nacimiento = input("Digite la fecha de nacimiento Dia/Mes/Año: ") #Se pide la fecha de nacimiento 
            while True:  #Se crea un bucle para mostrar las opciones de este parametro
                print("""Indique el sexo del empleado: \n 
                 1. Hombre  
                 2. Mujer  
                 3. Otro""")
                print()
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
                print()
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
                print()
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
                    print()
                    estado_civil = int(input("Escoja una opcion 1-5: ")) #Se le solicita al usuario que digite una opcion numerica
                    if estado_civil == 1 or estado_civil == 2 or estado_civil == 3 or estado_civil == 4 or estado_civil == 5: 
                        break #Si la opcion es valida se rompe el bucle y se va al siguiente parametro
                    else:
                        print("Digite una opcion valida") #Si no se indica y el bucle se repite hasta escojer una opcion valida
            while True: 
                print("""El empleado cuenta con alguna discapacidad: \n
                      1. Si
                      2. No""")
                print()
                discapacidad = int(input("Digite una opcion 1-2: "))
                if discapacidad == 1 or discapacidad == 2:
                    break
                else:
                    print("Digite una opcion valida")
            while True:
                print("""El empleado pertenece a alguna poblacion vulnerable: \n
                      1. Si
                      2. No""")
                print()
                poblacion_vulnerable = int(input("Digite una opcion 1-2: "))
                if poblacion_vulnerable == 1 or poblacion_vulnerable == 2:
                    break
                else:
                    print("Digite una opcion valida")
            while True:
                print("""Desea añadir este empleado al tablero kanban: \n
                      1. Si
                      2. No
                      """)
                añadir_kanban = int(input("Digite una opcion 1-2: "))
                if añadir_kanban == 1 or añadir_kanban == 2:
                    break
                else:
                    print("Digite una opcion valida")
            print(registrar_empleado(nombre, numero_identificacion, fecha_nacimiento, sexo, numero_telefonico, cargo, fecha_ingreso, tiene_hijos, tipo_contrato, RH, estado_civil, discapacidad, poblacion_vulnerable, añadir_kanban)) #Se llama a la funcion

        case 4:
            eliminar_empleado() #llamar a la funcion eliminar empleado
        case 5:
            numero_identificacion = input("Digite el numero de identificacion del empleado: ") #Pedir numero de identificacion del empleado a modificar
            print()
            print(modificar_empleado(numero_identificacion))  #Se llama a la funcion modificar empleado
        case 6:
            print("""Filtrar edad por:
                  1. Edad especifica
                  2. Rango de edad       
                  """)    #Se imprime menu indicando con opciones de filtrado
            opcion = int(input("Escoja una opcion 1-2: "))
            match opcion:
                case 1:
                    edad = input("Digite la edad del empleado en años: ") #En el primer caso se pide la edad especifica y se llama a la funcion
                    print()
                    print(filtrar_edad_especifica(edad))             
                case 2:
                    edad_min = input("Digire la edad minima: ")     #En el segundo caso se solicitan las dos edades y se llama a la funcion
                    edad_max = input("Digite la edad maxima: ")
                    print()      
                    print(filtrar_edad_rango(edad_min, edad_max))
                case _:
                    print("Digite una opcion valida")
        case 7:
            print("""Filtrar fecha de ingreso por: \n
                  1. Fecha especifica
                  2. Dia
                  3. Mes
                  4. Año""")  #Se imprime el menu con las opciones disponibles para filtrar empleados por fecha de ingreso
            print()
            opcion = int(input("Digite una opcion 1-4: "))
            match opcion:
                case 1:   
                    fecha_ingreso = input("Digite una fecha de ingreso: ") #Se solicita al usuario la fecha completa para filtrar
                    print()
                    print(filtrar_fecha_ingreso_especifica(fecha_ingreso)) #Se llama a la funcion para filtrar por fecha especifica y se imprime el resultado
                case 2:
                    dia = input("Digite un dia: ") #Se solicita al usuario el dia para filtrar
                    print()
                    print(filtrar_fecha_ingreso_dia(dia)) #Se llama a la funcion para filtrar por dia y se imprime el resultado
                case 3:
                    mes = input("Digite un mes: ")  #Se solicita al usuario el mes para filtrar
                    print()
                    print(filtrar_fecha_ingreso_mes(mes)) #Se llama a la funcion para filtrar por mes y se imprime el resultado
                case 4:
                    año = input("Digite un año: ") #Se solicita al usuario el año para filtrar
                    print()
                    print(filtrar_fecha_ingreso_año(año)) #Se llama a la funcion para filtrar por año y se imprime el resultado
                case _:
                    print("Digite una opcion valida")
        case 8:
            print("""Filtrar por:
                  1. Hombre
                  2. Mujer
                  3. Otro""")   #Se imprime un menu con todas las opciones para filtrar
            print()
            sexo = int(input("Digite una opcion 1-3: "))
            print()
            print(filtrar_sexo(sexo))   #Se llama a la funcion
        case 9:
            print("""Tiene hijos:
                  1. Si
                  2. No""") #Se imprime un menu con todas las opciones para filtrar
            print()
            hijos = int(input("Digite una opcion 1-2: "))
            print()
            print(filtrar_hijos(hijos)) #Se llama a la funcion
        case 10:
            print("""Filtrar por RH:
                      1. A+
                      2. A-
                      3. B+
                      4. B-
                      5. AB+
                      6. AB-
                      7. O+  
                      8. O-""") #Se imprime un menu con todas las opciones para filtrar
            print()
            RH = int(input("Digite una opcion 1-8: "))
            print()
            print(filtrar_rh(RH)) #Se llama a la funcion
        case 11:
            print("""Filtrar por estado civil:
                          1. Soltero
                          2. Casado
                          3. Union libre
                          4. Divorciado
                          5. Viudo""")
            estado_civil = int(input("Digite una opcion 1-5: ")) #Se imprime un menu con todas las opciones para filtrar
            print()
            print(filtrar_estado_civil(estado_civil)) #Se llama a la funcion
            print()
        case 12:
            print("""Filtrar por poblacion vulnerable: \n
                          1. Si
                          2. No""")  #Se imprime un menu con todas las opciones para filtrar
            print()
            poblacion_vulnerable = int(input("Digite una opcion 1-2: "))
            print() 
            print(filtrar_poblacion_vulnerable(poblacion_vulnerable)) #Se llama a la funcion
        case 13:
            print("""Filtrar por:
                  1. indefinido
                  2. definido
                  3. Obra labor
                  4. aprendizaje""")   #Se imprime un menu con todas las opciones para filtrar
            print()
            contrato = int(input("Digite una opcion 1-4: "))
            print()
            print(filtrar_contrato(contrato))   #Se llama a la funcion 
        case 14: 
            print("""Filtrar por discapacidad: \n
                    1. Si
                    2. No""") # Se imrpime un menú con todas las opciones para filtrar
            print()
            discapacidad = int(input("Digite una opcion 1-2: "))
            print ()
            print(filtrar_discapacidad(discapacidad)) #Se llama a la función 
        case 15:
            while True:
                print()
                print("""Bienvenido al menu de gestion Kanban: \n
                      1. Mostrar tablero kanban
                      2. Asignar tarea
                      3. Gestionar estado de tarea
                      4. Eliminar tarea
                      5. Filtrar tareas ToDo
                      6. Filtrar tareas InProgress
                      7. Filtrar tareas Done
                      0. Salir
                      """)   #Se imprime un menu con las opciones del tablero kanban
                opcion = int(input("Escoja una opcion: ")) #Se solicita una opcion al usuario
                match opcion:
                    case 1:
                        print()
                        print(mostrar_tablero_kanban())  #Se llama a la funcion para mostrar el tablero kanban
                    case 2:
                        print()
                        numero_de_id = input("Digite el numero de identificacion del empleado: ") #Se pide el numero de identificacion del empleado
                        print()
                        print(asignar_tarea(numero_de_id)) #Se llama a la funcion para asignarle una nueva tarea
                    case 3:
                        print()
                        numero_de_id = input("Digite el numero de identificacion del empleado: ").strip()  # Se pide el numero de identificacion del empleado
                        print(gestionar_estado_tarea(numero_de_id))  # Se llama a la función para gestionar tareas
                    case 4:
                        print()
                        numero_de_id = input("Digite el numero de identificacion del empleado: ").strip() #Se solicita el numero de identificacion del empleado
                        print()
                        print(eliminar_tarea(numero_de_id))  #Se llama a la funcion para quitarle una tarea
                    case 5:
                        print()
                        print(filtrar_tareas_todo()) #Se llama a la funcion para filtrar tareas por ToDo
                    case 6:
                        print()
                        print(filtrar_tareas_InProgress())  # Se llama a la función para filtrar tareas InProgress
                    case 7:
                        print()
                        print(filtrar_tareas_Done()) #Se llama a la funcion para filtrar tareas por Done
                    case 0:
                        print()
                        print("Saliendo del tablero kanban...") #Se rompe el bucle y se sale del menu imprimiendo un mensaje
                        break
                    case _:
                        print()
                        print("Digite una opcion valida")  #Si se digita una opcion no valida se indica mediante un mensaje
        case 0: 
            print("Tenga un buen dia!")    #Mensaje de despedida y romper el bucle
            break
        case _:
            print("Digite una opcion valida")  #Si el usuario digita una opcion no contemplada se imprime mensaje de error
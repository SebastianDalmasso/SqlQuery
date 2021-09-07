import pyodbc 

print('*** Ejecutar consulta SQL *** \n')

servidor = input('Ingrese el Server: ')
base = input('Ingrese la Base de Datos: ')
usuario = input('Ingrese el Usuario: ')
contrasena = input('Ingrese la contraseña: ')

try:
    cnn = pyodbc.connect(driver='{SQL Server}', 
                         server=servidor,
                         database=base, 
                         uid=usuario,
                         pwd=contrasena)
                         #trusted_connection='yes' -> para auth win
    print('Conexión correcta \n')
except:
    print('Error al conectar')
    input('\n Enter para salir')
    exit()

print('Sólo se mostrará la primer columna de la primer fila')
print('---------------------------------------------------- \n')
consulta = input('Ingrese su consulta: ')
print('Resultado: \n')

cursor = cnn.cursor()
try:
    cursor.execute(consulta)

    resultado = cursor.fetchall()
    print (resultado[0][0])
except:
    print('Error al ejecutar')
    input('\n Enter para salir')
    exit()
finally:
    cursor.close()
    cnn.close()
    
input('\n Enter para salir ')
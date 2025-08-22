# Importamos la conexión de mysql en python
import mysql.connector
# Creamos una variable donde almacenamos la conexion a la base de datos
personas_db = mysql.connector.Connect(
    host = 'localhost',
    user = 'admin',
    password = 'admin',
    database = 'personas_db'
)
# Creamos al cursor que es el intermediario entre nosostros y la base de datos, nos ayuda con las consultas.
mi_cursor = personas_db.cursor()
# Ejecutamos una sentencia SELECT para mostrar el contenido de la base de datos
mi_cursor.execute('SELECT nombre, edad FROM personas') # Simplemente de cambia el * por las columnas que se desean mostrar
# Se almacenan los registros de la base de datos en una lista 
resultados = mi_cursor.fetchall()
# Iteramos la lsita de registros para imprimir cada uno de los elementos de la lista de manera presentable
for resultado in resultados:
    print(resultado)

personas_db.close()

# Salida esperada usando el ciclo for:
# (2, 'Sarha', 'Lee', 18)
# (3, 'Marcos', 'Lee', 18)
# etc.

# Sin el ciclo for:
#[(2, 'Sarha', 'Lee', 18), (3, 'Marcos', 'Lee', 18)]
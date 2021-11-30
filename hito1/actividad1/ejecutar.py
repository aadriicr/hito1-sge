import sqlite3
from sqlite3 import Error
try:
    con = sqlite3.connect('basededatos.db')
    print("Connection is established: Database is created in memory")
except Error:
    print(Error)
def crud(con):
        while True:
            def crearTabla(con):
                cursorObj.execute("drop table if exists cliente")
                cursorObj.execute(
                    "Create table cliente(id integer, nombre text, primerApellido text, segundoApellido text, ciudad text)")
                con.commit()
            print("========================")
            print("[1] Listar clientes     ")
            print("[2] Añadir cliente      ")
            print("[3] Modificar cliente   ")
            print("[4] Borrar cliente      ")
            print("[5] Salir               ")
            print("========================")
            option = input("> ")
            if option == '1':
                cursorObj = con.cursor()
                cursorObj.execute('SELECT * FROM cliente')

                rows = cursorObj.fetchall()
                for row in rows:
                    print(row)
            if option == '2':
                print("Nombre -")
                nombre = input()
                print("Primer Apellido -")
                primerApellido= input()
                print("Segundo Apellido -")
                segundoApellido = input()
                print("Ciudad -")
                ciudad = input()
                datos = (nombre, primerApellido, segundoApellido, ciudad)
                cursorObj = con.cursor()
                cursorObj.execute('INSERT INTO cliente(nombre, primerApellido, segundoApellido, ciudad) VALUES(?, ?, ?, ?)', datos)
                con.commit()

            if option == '3':
                cursorObj = con.cursor()
                print("Introduce el id que desees cambiar")
                numero0 = input()
                print("¿Que quieres modificar?")
                print("[1] nombre")
                print("[2] primer apellido")
                print("[3] segundo apellido")
                print("[4] ciudad")
                numero2=input()
                if numero2 == '1':
                    print("Introduce el nuevo nombre")
                    nombre_nuevo = input()
                    cursorObj.execute('UPDATE cliente SET nombre =? where id = ?;',(nombre_nuevo, numero0))
                elif numero2 =='2':
                    print("Introduce el nuevo apellido")
                    apellido1_nuevo = input()
                    cursorObj.execute('UPDATE cliente SET primerApellido =? where id = ?;',(apellido1_nuevo, numero0))
                elif numero2 == '3':
                    print("Introduce el nuevo apellido")
                    apellido2_nuevo = input()
                    cursorObj.execute('UPDATE cliente SET segundoApellido =? where id = ?;',(apellido2_nuevo, numero0))
                elif numero2 == '4':
                    print("Introduce la nueva ciudad")
                    ciudad_nuevo = input()
                    cursorObj.execute('UPDATE cliente SET ciudad =? where id = ?;',(ciudad_nuevo, numero0))
                else:
                    print("error")
                con.commit()
            if option == '4':
                cursorObj = con.cursor()
                print("Introduce la id que deseas borrar")
                numero0 = input()
                con.execute("DELETE from cliente where id ="+numero0)
                con.commit()
            if option == '5':
                print("Cerrando programa\n")
                return False
                break
            input("\nEnter para continuar")
crud(con)

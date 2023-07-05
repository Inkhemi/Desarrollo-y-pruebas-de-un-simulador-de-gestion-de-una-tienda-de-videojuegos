import pandas as pd
import admin
import client
import hashlib

inventario = pd.read_csv('../csv\inventario.csv', index_col='titulo')
usuarios = pd.read_csv("../csv/users.csv", index_col='usuario')

def login():
    u = input("ingrese su nombre de usuario: \n")
    p = input("ingrese contraseña: \n")
    p = hashlib.sha256(p.encode('utf-8')).hexdigest()
    if(usuarios.loc[u,'contrasena'] == p):
        tipo = usuarios.loc[u,'tipo']
        if(tipo == 'cliente'):
            return 1
        elif(tipo == 'administrador'):
            return 2

def sesion(user):    
    if(user == 1):
        print("inicio de sesión como usuario")
        while(True):
            n = int(input("ingrese 0 para cerrar sesión, 1 para ver el catalogo, 2 para comprar: \n"))
            if n == 0: #cerrar sesion
                break
            if n == 1:
                client.catalogo()
            if n == 2:
                t = input("Ingrese el titulo \n")
                c = int(input("Ingrese la cantidad \n"))
                client.comprar(t,c)
    elif(user == 2):
        print("inicio de sesión como administrador")
        while(True):
            n = int(input('1 para agregar un nuevo titulo, 2 para restock, 3 para vender, 4 para ver el stock, 5 para ver el reporte, 0 para cerrar sesion \n'))
            if n == 2:
                t = input("Ingrese el titulo \n")
                c = int(input("Cantidad \n"))
                admin.restock(t,c)
            if n == 1:
                t = input("Ingrese el titulo \n")
                c = int(input("Cantidad \n"))
                com = int(input("Coste de compre \n"))
                v = int(input("Precio de venta \n"))
                g = input("Ingrese genero \n")
                p = input("Ingrese plataforma \n")
                admin.agregar(t,c,com,v,g,p)
            if n == 3:
                t = input("Ingrese el titulo \n")
                c = int(input("Cantidad \n"))
                admin.vender(t,c)
            if n == 4:
                admin.stock()
            if n == 5:
                admin.reporte()
            if n == 0: #cerrar sesion
                break
            
sesion(login())
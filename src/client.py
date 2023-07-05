import pandas as pd
import admin

inventario = pd.read_csv("../csv/inventario.csv")

#Comprar juego
def comprar(titulo, cantidad):
    admin.vender(titulo,cantidad)

#Ver catalogo de juegos           
def catalogo():
    print(inventario.iloc[:,[0,1,3]].to_string(index=False))

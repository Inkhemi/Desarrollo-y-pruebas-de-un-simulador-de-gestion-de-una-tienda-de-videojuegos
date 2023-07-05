import pandas as pd

inventario = pd.read_csv("../csv/inventario.csv")

#Agregar un juego nuevo a la base de datos
def agregar(titulo, cantidad, compra, venta, genero, plataforma):
    if titulo in inventario.titulo.values:
        print("el titulo ya se encuentra agregado, si quieres agregar más utiliza restock")
        return
    if cantidad < 0 or titulo == '' or isinstance(compra, str) == True or isinstance(venta, str) == True:
        print("Información invalida")
        return
    rows = [{'titulo': titulo, 'cantidad':cantidad,'compra':compra,'venta':venta,'genero':genero,'plataforma':plataforma,'ccompra':0,'cventa':0,'ingreso':0}]
    add = pd.concat([inventario, pd.DataFrame(rows)], ignore_index=True)
    add.to_csv('../csv/inventario.csv', index=False)

#Venta de juegos
def vender(titulo, cantidad):
    inv = pd.read_csv("../csv/inventario.csv", index_col='titulo')
    if titulo not in inventario.titulo.values:
        print("El titulo no existe en el inventario")
        return
    if(isinstance(cantidad,int) == True):
        actual = inv.loc[titulo,'cantidad']
        if cantidad>=1:
            if(actual >= cantidad):
                inv.loc[titulo,['cantidad']] = actual - cantidad
                ventas = inv.loc[titulo,['cventa']]
                inv.loc[titulo, ['cventa']] = ventas + cantidad
                precio = inv.loc[titulo, 'venta']
                ingresos =  int(precio * cantidad)
                ingresoactual = inv.loc[titulo, 'ingreso']
                inv.loc[titulo, 'ingreso'] = int(ingresoactual) + ingresos
                inv.to_csv('../csv/inventario.csv')
            else:
                print("Solo quedan:" + str(actual) + " unidades")
        else:
            print("no se puede agregar una cantidad negativa")

#Compra de juegos
def restock(titulo,cantidad):
    inv = pd.read_csv("../csv/inventario.csv", index_col='titulo')
    if titulo not in inventario.titulo.values:
        print("El titulo no existe en el inventario")
        return
    if(isinstance(cantidad,int) == True):
        if cantidad>=1:
            actual = inv.loc[titulo,'cantidad']
            inv.loc[titulo,['cantidad']] = actual + cantidad
            compras = inv.loc[titulo,['ccompra']]
            inv.loc[titulo, ['ccompra']] = compras + cantidad
            precio = inv.loc[titulo, 'compra']
            costes =  int(precio * cantidad)
            ingresoactual = inv.loc[titulo, 'ingreso']
            inv.loc[titulo, 'ingreso'] = int(ingresoactual) - costes
            inv.to_csv('../csv/inventario.csv')
        else:
            print("no se puede agregar una cantidad negativa")

#Ver el inventario
def stock():
    print(inventario.iloc[:,[0,1,2,3,4,5]].to_string(index=False))
    
def reporte():
    print(inventario.iloc[:,[0,6,7,8]].to_string(index=False))
    
    # titulo = input()
    # cantidad = int(input)
    # compra = int(input)
    # venta = int(input)
    # genero = input()
    # plataforma = input()
    
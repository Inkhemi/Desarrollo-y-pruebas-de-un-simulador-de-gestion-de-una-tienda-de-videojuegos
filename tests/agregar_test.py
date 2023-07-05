import sys
sys.path.append('../src')
from admin import agregar
import pandas as pd


import pytest

class TestAgregar:
    # Tests de si se puede agregar un juego con información valida
    def test_agregar_juego(self):
        agregar('Mario Bros', 10, 20, 30, 'Plataformas', 'Nintendo')
        inv = pd.read_csv('../csv/inventario.csv')
        assert inv.loc[inv['titulo'] == 'Mario Bros'].iloc[-1]['cantidad'] == 10
        assert inv.loc[inv['titulo'] == 'Mario Bros'].iloc[-1]['compra'] == 20
        assert inv.loc[inv['titulo'] == 'Mario Bros'].iloc[-1]['venta'] == 30
        assert inv.loc[inv['titulo'] == 'Mario Bros'].iloc[-1]['genero'] == 'Plataformas'
        assert inv.loc[inv['titulo'] == 'Mario Bros'].iloc[-1]['plataforma'] == 'Nintendo'
        assert inv.loc[inv['titulo'] == 'Mario Bros'].iloc[-1]['ccompra'] == 0
        assert inv.loc[inv['titulo'] == 'Mario Bros'].iloc[-1]['cventa'] == 0
        assert inv.loc[inv['titulo'] == 'Mario Bros'].iloc[-1]['ingreso'] == 0

    # Tests no se puede agregar sin un titulo
    def test_titulo_vacio(self):
        agregar('', 10, 20, 30, 'Plataformas', 'Nintendo')
        inv = pd.read_csv('../csv/inventario.csv')
        assert len(inv.loc[inv['titulo'] == '']) == 0

    # Tests no se puede agregar con cantidad negativa
    def test_cantidad_negativa(self):
        agregar('Mario Bros 2', -10, 20, 30, 'Plataformas', 'Nintendo')
        inv = pd.read_csv('../csv/inventario.csv')
        assert len(inv.loc[inv['titulo'] == 'Mario Bros 2']) == 0

    # Tests no se puede agregar con numeros como string
    def test_numero_como_string(self):
        agregar('Wario Bros', 10, '20', 30, 'Plataformas', 'Nintendo')
        inv = pd.read_csv('../csv/inventario.csv')
        assert len(inv.loc[inv['titulo'] == 'Wario Bros']) == 0

    # Tests un juego se puede agregar con maximos numeros
    def test_valores_grandes(self):
        agregar('Mario Bros 3', 1000000, 999999999, 999999999, 'Plataformas', 'Nintendo')
        inv = pd.read_csv('../csv/inventario.csv')
        assert inv.loc[inv['titulo'] == 'Mario Bros 3'].iloc[-1]['cantidad'] == 1000000
        assert inv.loc[inv['titulo'] == 'Mario Bros 3'].iloc[-1]['compra'] == 999999999
        assert inv.loc[inv['titulo'] == 'Mario Bros 3'].iloc[-1]['venta'] == 999999999
        assert inv.loc[inv['titulo'] == 'Mario Bros 3'].iloc[-1]['genero'] == 'Plataformas'
        assert inv.loc[inv['titulo'] == 'Mario Bros 3'].iloc[-1]['plataforma'] == 'Nintendo'
        assert inv.loc[inv['titulo'] == 'Mario Bros 3'].iloc[-1]['ccompra'] == 0
        assert inv.loc[inv['titulo'] == 'Mario Bros 3'].iloc[-1]['cventa'] == 0
        assert inv.loc[inv['titulo'] == 'Mario Bros 3'].iloc[-1]['ingreso'] == 0
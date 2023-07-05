import sys
sys.path.append('../src')
import pandas as pd
from admin import vender
from admin import agregar


import pytest


class TestVender:
    # Tests de que funciona si se utiliza un titulo y cantidad normales.
    def test_funciona(self):
        inv = pd.read_csv('../csv/inventario.csv', index_col='titulo')
        cantidad_before = inv.loc['League of Legends', 'cantidad']
        cventa_before = inv.loc['League of Legends', 'cventa']
        ingreso_before = inv.loc['League of Legends', 'ingreso']
        
        vender('League of Legends', 2)
        
        inv = pd.read_csv('../csv/inventario.csv', index_col='titulo')
        cantidad_after = inv.loc['League of Legends', 'cantidad']
        cventa_after = inv.loc['League of Legends', 'cventa']
        ingreso_after = inv.loc['League of Legends', 'ingreso']
        
        assert cantidad_after == cantidad_before - 2
        assert cventa_after == cventa_before + 2
        assert ingreso_after == ingreso_before + 60

    # Tests de que vender 0 copias no modifica nada
    def test_cero(self):
        agregar('The Great Gatsby', 10, 5, 10, 'Fiction', 'Paperback')
        vender('The Great Gatsby', 0)
        inv = pd.read_csv('../csv/inventario.csv', index_col='titulo')
        assert inv.loc['The Great Gatsby', 'cantidad'] == 10
        assert inv.loc['The Great Gatsby', 'cventa'] == 0
        assert inv.loc['The Great Gatsby', 'ingreso'] == 0

    # Tests de que hay un mensaje de error si se intenta comprar más de lo que se encuentra
    def test_mayor_a_copias(self, capsys):
        vender('The Great Gatsby', 11)
        inv = pd.read_csv('../csv/inventario.csv', index_col='titulo')
        assert inv.loc['The Great Gatsby', 'cantidad'] == 10
        assert inv.loc['The Great Gatsby', 'cventa'] == 0
        assert inv.loc['The Great Gatsby', 'ingreso'] == 0
        captured = capsys.readouterr()
        assert 'Solo quedan:10 unidades' in captured.out

    # Tests de que no se puede comprar una cantidad negativa
    def test_negativo(self, capsys):
        vender('The Great Gatsby', -1)
        inv = pd.read_csv('../csv/inventario.csv', index_col='titulo')
        assert inv.loc['The Great Gatsby', 'cantidad'] == 10
        assert inv.loc['The Great Gatsby', 'cventa'] == 0
        assert inv.loc['The Great Gatsby', 'ingreso'] == 0
        captured = capsys.readouterr()
        assert 'no se puede agregar una cantidad negativa' in captured.out
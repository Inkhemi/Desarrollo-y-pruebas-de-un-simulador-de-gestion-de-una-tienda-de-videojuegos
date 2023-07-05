import sys
sys.path.append('../src')
import pandas as pd
from admin import agregar
from admin import restock


import pytest

class TestRestock:
    # Tests funciona correctamente
    def test_funciona(self):
        agregar('The Last of Us Part II', 5, 50, 60, 'Accion', 'PS4')
        inv_before = pd.read_csv('../csv/inventario.csv', index_col='titulo')
        quantity_before = inv_before.loc['The Last of Us Part II', 'cantidad']
        restock('The Last of Us Part II', 5)
        inv_after = pd.read_csv('../csv/inventario.csv', index_col='titulo')
        quantity_after = inv_after.loc['The Last of Us Part II', 'cantidad']
        assert quantity_after == quantity_before + 5

    # Tests revisar si se añade a ccompra (Cantidad comprada)
    def test_modifica_costo(self):
        restock('The Last of Us Part II', 5)
        inv = pd.read_csv('../csv/inventario.csv', index_col='titulo')
        ccompra_before = inv.loc['The Last of Us Part II', 'ccompra']
        restock('The Last of Us Part II', 5)
        inv = pd.read_csv('../csv/inventario.csv', index_col='titulo')
        ccompra_after = inv.loc['The Last of Us Part II', 'ccompra']
        assert ccompra_after == ccompra_before + 5

    # Tests modifica el ingreso
    def test_modifica_ingreso(self):
        restock('The Last of Us Part II', 5)
        inv = pd.read_csv('../csv/inventario.csv', index_col='titulo')
        expected_income = inv.loc['The Last of Us Part II', 'ingreso'] - 250
        restock('The Last of Us Part II', 5)
        inv = pd.read_csv('../csv/inventario.csv', index_col='titulo')
        assert inv.loc['The Last of Us Part II', 'ingreso'] == expected_income

    # Tests no hace nada al agregar un negativo
    def test_negativo(self):
        restock('The Last of Us Part II', -5)
        inv = pd.read_csv('../csv/inventario.csv', index_col='titulo')
        quantity_before_restock = inv.loc['The Last of Us Part II', 'cantidad']
        restock('The Last of Us Part II', 5)
        inv = pd.read_csv('../csv/inventario.csv', index_col='titulo')
        assert inv.loc['The Last of Us Part II', 'cantidad'] == quantity_before_restock + 5

    # Tests no hace nada al agregar un 0
    def test_cero(self):
        restock('The Last of Us Part II', 0)
        inv = pd.read_csv('../csv/inventario.csv', index_col='titulo')
        quantity_before_restock = inv.loc['The Last of Us Part II', 'cantidad']
        restock('The Last of Us Part II', 10)
        inv = pd.read_csv('../csv/inventario.csv', index_col='titulo')
        quantity_after_restock = inv.loc['The Last of Us Part II', 'cantidad']
        assert quantity_after_restock - quantity_before_restock == 10
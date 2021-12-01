from Domain.cheltuiala2 import get_suma
from Logic.CRUD import adauga_cheltuiala
from Logic.ordonare_descrescatoare_dupa_suma import ordonare_descrescatoare_dupa_suma


def test_ordonare_descrescatoare_dupa_suma():
    lista = []
    undo_list = []
    redo_list = []
    lista = adauga_cheltuiala(1, 23, 500, "12.02.2020", "intretinere", lista, undo_list, redo_list)
    lista = adauga_cheltuiala(2, 24, 100, "12.02.2020", "canal", lista, undo_list, redo_list)
    lista = adauga_cheltuiala(3, 23, 700, "13.02.2020", "intretinere", lista, undo_list, redo_list)
    lista = adauga_cheltuiala(4, 24, 2000, "12.02.2020", "canal", lista, undo_list, redo_list)

    lista = ordonare_descrescatoare_dupa_suma(lista, undo_list, redo_list)

    assert get_suma(lista[0]) == 2000
    assert get_suma(lista[1]) == 700
    assert get_suma(lista[2]) == 500
    assert get_suma(lista[3]) == 100


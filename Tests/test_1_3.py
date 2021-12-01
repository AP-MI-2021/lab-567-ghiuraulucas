from Domain.cheltuiala2 import get_suma
from Logic.CRUD import adauga_cheltuiala, get_by_id
from Logic.adunare_valoare_data_citita import adunarea_unei_valori_la_toate_cheltuielile_data


def test_functionalitate_1_punct_3():
    lista = []
    undo_list = []
    redo_list = []
    lista = adauga_cheltuiala(1, 23, 500, "12.02.2020", "intretinere", lista, undo_list, redo_list)
    lista = adauga_cheltuiala(2, 24, 100, "12.02.2020", "canal", lista, undo_list, redo_list)
    lista = adauga_cheltuiala(3, 23, 500, "13.02.2020", "intretinere", lista, undo_list, redo_list)

    assert get_suma(get_by_id(1, lista)) == 500
    assert get_suma(get_by_id(2, lista)) == 100

    lista = adunarea_unei_valori_la_toate_cheltuielile_data(33, "12.02.2020", lista, undo_list, redo_list)

    assert get_suma(get_by_id(1, lista)) == 533
    assert get_suma(get_by_id(2, lista)) == 133
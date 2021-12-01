from Logic.CRUD import adauga_cheltuiala
from Logic.cea_mai_mare_suma_tip import cea_mai_mare_suma_dupa_intretinere, cea_mai_mare_suma_dupa_canal, \
    cea_mai_mare_suma_dupa_alte_cheltuieli


def test_cea_mai_mare_suma_dupa_tip():
    lista = []
    undo_list =[]
    redo_list = []
    lista = adauga_cheltuiala(1, 23, 500, "12.02.2020", "intretinere", lista, undo_list, redo_list)
    lista = adauga_cheltuiala(2, 24, 100, "12.02.2020", "canal", lista, undo_list, redo_list)
    lista = adauga_cheltuiala(3, 23, 700, "13.02.2020", "intretinere", lista, undo_list, redo_list)
    lista = adauga_cheltuiala(4, 24, 2000, "12.02.2020", "canal", lista, undo_list, redo_list)

    assert cea_mai_mare_suma_dupa_intretinere(lista) == 700
    assert cea_mai_mare_suma_dupa_canal(lista) == 2000
    assert cea_mai_mare_suma_dupa_alte_cheltuieli(lista) == 0

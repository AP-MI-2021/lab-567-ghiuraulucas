from Domain.cheltuiala2 import get_nr_apartament, get_suma, get_data, get_tip
from Logic.CRUD import adauga_cheltuiala, get_by_id, sterge_cheltuiala, modifica_cheltuiala


def test_adauga_cheltuiala():
    lista = []
    lista = adauga_cheltuiala(1, 23, 150, "20.02.2018", "intretinere", lista)

    assert len(lista) == 1
    assert get_nr_apartament(get_by_id(1, lista)) == 23
    assert get_suma(get_by_id(1, lista)) == 150
    assert get_data(get_by_id(1, lista)) == "20.02.2018"
    assert get_tip(get_by_id(1, lista)) == "intretinere"

def test_sterge_cheltuiala():
    lista = []
    lista = adauga_cheltuiala(1, 23, 150, "20.02.2018", "intretinere", lista)
    lista = adauga_cheltuiala(2, 14, 150, "20.02.2018", "intretinere", lista)

    lista = sterge_cheltuiala(1, lista)

    assert len(lista) == 1
    assert get_by_id(1, lista) is None
    assert get_by_id(2, lista) is not None

    try:
        lista = sterge_cheltuiala(30, lista)
        assert False
    except ValueError:

        assert len(lista) == 1
        assert get_by_id(2, lista) is not None

def test_modifica_cheltuiala():
    lista = []
    lista = adauga_cheltuiala(1, 23, 150, "20.02.2018", "intretinere", lista)
    lista = adauga_cheltuiala(2, 14, 200, "20.02.2018", "canal", lista)

    lista = modifica_cheltuiala(1, 23, 800, "20.02.2018", "alte cheltuieli", lista)

    assert get_suma(get_by_id(1, lista)) == 800
    assert get_tip(get_by_id(1, lista)) == "alte cheltuieli"
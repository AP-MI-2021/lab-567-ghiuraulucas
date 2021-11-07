from Domain.cheltuiala import get_nr_apartament, get_suma, get_data, get_tip
from Logic.CRUD import adauga_cheltuiala, get_by_nr_apartament_si_data, sterge_cheltuiala


def test_adauga_cheltuiala():
    lista = []
    lista = adauga_cheltuiala(23, 150, "20.02.2018", "intretinere", lista)

    assert len(lista) == 1
    assert get_nr_apartament(get_by_nr_apartament_si_data(23, "20.02.2018", lista)) == 23
    assert get_suma(get_by_nr_apartament_si_data(23, "20.02.2018", lista)) == 150
    assert get_data(get_by_nr_apartament_si_data(23, "20.02.2018", lista)) == "20.02.2018"
    assert get_tip(get_by_nr_apartament_si_data(23, "20.02.2018", lista)) == "intretinere"

def test_sterge_cheltuiala():
    lista = []
    lista = adauga_cheltuiala(23, 150, "20.02.2018", "intretinere", lista)
    lista = adauga_cheltuiala(14, 150, "20.02.2018", "intretinere", lista)

    lista = sterge_cheltuiala(23, "20.02.2018", lista)

    assert len(lista) == 1
    assert get_by_nr_apartament_si_data(23, "20.02.2018", lista) is None
    assert get_by_nr_apartament_si_data(14, "20.02.2018", lista) is not None

    lista = sterge_cheltuiala(1000, "20.02.2018", lista)

    assert len(lista) == 1
    assert get_by_nr_apartament_si_data(14, "20.02.2018", lista) is not None


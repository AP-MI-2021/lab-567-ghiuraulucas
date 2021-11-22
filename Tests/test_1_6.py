from Logic.CRUD import adauga_cheltuiala
from Logic.sume_lunare_dupa_apartament import sume_lunare_dupa_apartament


def test_sume_lunare_dupa_apartament():
    lista = []
    lista = adauga_cheltuiala(1, 23, 500, "12.02.2020", "intretinere", lista)
    lista = adauga_cheltuiala(2, 24, 100, "12.02.2020", "canal", lista)
    lista = adauga_cheltuiala(3, 23, 700, "13.02.2020", "intretinere", lista)
    lista = adauga_cheltuiala(4, 24, 2000, "12.02.2020", "canal", lista)

    print(sume_lunare_dupa_apartament(lista))
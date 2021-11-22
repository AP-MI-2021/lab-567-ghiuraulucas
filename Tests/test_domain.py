from Domain.cheltuiala2 import creeaza_cheltuiala, get_nr_apartament, get_suma, get_data, get_tip, get_id


def test_cheltuiala():
    cheltuiala = creeaza_cheltuiala(1, 23, 150, "20.02.2018", "intretinere")

    assert get_id(cheltuiala) == 1
    assert get_nr_apartament(cheltuiala) == 23
    assert get_suma(cheltuiala) == 150
    assert get_data(cheltuiala) == "20.02.2018"
    assert get_tip(cheltuiala) == "intretinere"

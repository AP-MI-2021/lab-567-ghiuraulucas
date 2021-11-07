from Domain.cheltuiala import creeaza_cheltuiala, get_nr_apartament, get_suma, get_data, get_tip


def test_cheltuiala():
    cheltuiala = creeaza_cheltuiala(23, 150, "20.02.2018", "intretinere")

    assert get_nr_apartament(cheltuiala) == 23
    assert get_suma(cheltuiala) == 150
    assert get_data(cheltuiala) == "20.02.2018"
    assert get_tip(cheltuiala) == "intretinere"

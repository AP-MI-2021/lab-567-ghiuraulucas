from Tests.test_1_3 import test_functionalitate_1_punct_3
from Tests.test_1_4 import test_cea_mai_mare_suma_dupa_tip
from Tests.test_1_5 import test_ordonare_descrescatoare_dupa_suma
from Tests.test_1_6 import test_sume_lunare_dupa_apartament
from Tests.test_CRUD import test_adauga_cheltuiala, test_sterge_cheltuiala, test_modifica_cheltuiala
from Tests.test_domain import test_cheltuiala


def run_all_tests():
    test_cheltuiala()
    test_adauga_cheltuiala()
    test_sterge_cheltuiala()
    test_modifica_cheltuiala()
    test_functionalitate_1_punct_3()
    test_cea_mai_mare_suma_dupa_tip()
    test_ordonare_descrescatoare_dupa_suma()


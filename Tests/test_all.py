from Tests.test_CRUD import test_adauga_cheltuiala, test_sterge_cheltuiala
from Tests.test_domain import test_cheltuiala


def run_all_tests():
    test_cheltuiala()
    test_adauga_cheltuiala()
    test_sterge_cheltuiala()
from Logic.CRUD import adauga_cheltuiala, get_by_id
from Logic.undo_redo import do_undo, do_redo


def test_undo_redo():
    lista = []
    undo_list = []
    redo_list = []
    lista = adauga_cheltuiala(1, 23, 500, "12.02.2020", "intretinere", lista, undo_list, redo_list)
    lista = adauga_cheltuiala(2, 24, 100, "12.02.2020", "canal", lista, undo_list, redo_list)
    lista = adauga_cheltuiala(3, 23, 700, "13.02.2020", "intretinere", lista, undo_list, redo_list)

    lista = do_undo(undo_list, redo_list, lista)
    assert get_by_id(3, lista) is None
    assert get_by_id(1, lista) is not None
    assert get_by_id(2, lista) is not None

    lista = do_undo(undo_list, redo_list, lista)
    assert get_by_id(2, lista) is None

    lista = do_undo(undo_list, redo_list, lista)
    assert lista == []

    lista = adauga_cheltuiala(1, 23, 500, "12.02.2020", "intretinere", lista, undo_list, redo_list)
    lista = adauga_cheltuiala(2, 24, 100, "12.02.2020", "canal", lista, undo_list, redo_list)
    lista = adauga_cheltuiala(3, 23, 700, "13.02.2020", "intretinere", lista, undo_list, redo_list)

    lista = do_redo(undo_list, redo_list, lista)
    assert get_by_id(1, lista) is not None
    assert get_by_id(2, lista) is not None
    assert get_by_id(3, lista) is not None

    lista = do_undo(undo_list, redo_list, lista)
    lista = do_undo(undo_list, redo_list, lista)
    assert get_by_id(1, lista) is not None
    assert get_by_id(2, lista) is None
    assert get_by_id(3, lista) is None

    lista = do_redo(undo_list, redo_list, lista)
    assert get_by_id(1, lista) is not None
    assert get_by_id(2, lista) is not None
    assert get_by_id(3, lista) is None

    lista = do_redo(undo_list, redo_list, lista)
    assert get_by_id(1, lista) is not None
    assert get_by_id(2, lista) is not None
    assert get_by_id(3, lista) is not None

    lista = do_undo(undo_list, redo_list, lista)
    lista = do_undo(undo_list, redo_list, lista)
    assert get_by_id(1, lista) is not None
    assert get_by_id(2, lista) is None
    assert get_by_id(3, lista) is None

    lista = adauga_cheltuiala(4, 9, 1000, "01.01.1998", "canal", lista, undo_list, redo_list)
    assert get_by_id(4, lista) is not None
    assert get_by_id(3, lista) is None

    lista = do_undo(undo_list, redo_list, lista)
    assert get_by_id(4, lista) is None

    lista = do_undo(undo_list, redo_list, lista)
    assert lista == []

    lista = do_redo(undo_list, redo_list, lista)
    lista = do_redo(undo_list, redo_list, lista)
    assert get_by_id(1, lista) is not None
    assert get_by_id(4, lista) is not None

    lista = do_redo(undo_list, redo_list, lista)
    assert get_by_id(1, lista) is not None
    assert get_by_id(4, lista) is not None




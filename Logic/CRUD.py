from Domain.cheltuiala2 import creeaza_cheltuiala, get_id


def adauga_cheltuiala(id, nr_apartament, suma, data, tip, lista, undo_list, redo_list):
    '''
    Adauga o cheltuiala intr-o lista
    :param id: int
    :param nr_apartament: int
    :param suma: float
    :param data: string
    :param tip: string
    :param lista: lista de cheltuieli
    :return: o lista continand atat elementele vechi cat si noua cheltuiala
    '''
    if get_by_id(id, lista) is not None:
        raise ValueError("Exista deja o cheltuiala cu acest id.")
    cheltuiala = creeaza_cheltuiala(id, nr_apartament, suma, data, tip)
    undo_list.append(lista)
    redo_list.clear()
    return lista + [cheltuiala]

def get_by_id(id, lista):
    '''
    Returneaza o cheltuiala din lista cu numarul apartamentului dat
    :param id: int
    :param lista: lista de cheltuieli
    :return: cheltuiala cu numarul de apartament dat din lista, sau None, daca aceasta nu exista
    '''
    for cheltuiala in lista:
        if get_id(cheltuiala) == id:
            return cheltuiala
    return None

# AM PRESUPUS CA NU SE POT EFECTUA 2 CHELTUIELI LA UN APARTAMENT IN ACEEASI ZI (altfel, ca sa obtin o cheltuiala trebuia sa bag
# toate specificatiile: nr apartament, suma, data, tip, deoarece ar fi posibil orice.
# Ce mai puteam sa fac aici e sa iau dupa un singur criteriu (get_by_nr_apartament) si sa returnez O LISTA de cheltuieli efectuate
# la acelasi apartament; dar vreau sa pot lua o singura cheltuiala dupa nr apartamentului si data.

def sterge_cheltuiala(id, lista, undo_list, redo_list):
    l=[]
    '''
    Sterge o cheltuiala din lista
    :param id: int
    :param lista: lista de cheltuieli
    :return: Lista fara cheltuiala care a fost scoasa
    '''
    if get_by_id(id, lista) is None:
        raise ValueError("Nu exista o cheltuiala cu acest id.")
    for cheltuiala in lista:
        if get_id(cheltuiala) == id:
            pass
        else:
            l.append(cheltuiala)
    undo_list.append(lista)
    redo_list.clear()
    return l


def modifica_cheltuiala(id, nr_apartament, suma, data, tip, lista, undo_list, redo_list):
    # Am bagat aici toti acesti parametri pentru ca ei sunt parametrii noi si cheltuielii. Evident, nr_apartament si data raman la fel.
    '''
    Modifica o lista dupa id
    :param id: int
    :param nr_apartament: int
    :param suma: float
    :param data: string
    :param tip: string
    :param lista: lista de cheltuieli
    :return: Lista cu cheltuiala ceruta modificata
    '''

    if get_by_id(id, lista) is None:
        raise ValueError("Nu exista o cheltuiala cu acest id.")
    lista_noua = []
    for cheltuiala in lista:
        if get_id(cheltuiala) == id:
            cheltuiala_noua = creeaza_cheltuiala(id, nr_apartament, suma, data, tip)
            lista_noua.append(cheltuiala_noua)
        else:
            lista_noua.append(cheltuiala)
    undo_list.append(lista)
    redo_list.clear()
    return lista_noua


def creeaza_cheltuiala(id, nr_apartament, suma, data, tip):
    '''
    Creeaza o lista ce contine datele unei cheltuieli.
    :param id: int
    :param nr_apartament: int
    :param suma: float
    :param data: string
    :param tip: string
    :return: O lista ce contine datele unei cheltuieli.
    '''
    l=[0,0,0,0,0]

    l[0] = id
    l[1] = nr_apartament
    l[2] = suma
    l[3] = data
    l[4] = tip

    return l

def get_id(cheltuiala):
    return cheltuiala[0]

def get_nr_apartament(cheltuiala):
    '''
    Returneaza numarul unui apartament din lista datelor unei cheltuieli
    :param lista: lista cu datele unei cheltuieli
    :return: nr apartament - int
    '''
    return cheltuiala[1]

def get_suma(cheltuiala):
    return cheltuiala[2]

def get_data(cheltuiala):
    return cheltuiala[3]

def get_tip(cheltuiala):
    return cheltuiala[4]

def to_string(cheltuiala):
    return "ID:" + str(cheltuiala[0]) + " Nr. apartament:" + str(cheltuiala[1]) + " Suma:" + str(cheltuiala[2]) + " Data:" + str(cheltuiala[3]) + " Tipul:" + str(cheltuiala[4])


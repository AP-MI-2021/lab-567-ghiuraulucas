

def creeaza_cheltuiala(nr_apartament, suma, data, tip):
    '''
    Creeaza o lista ce contine datele unei cheltuieli.
    :param nr_apartament: int
    :param suma: float
    :param data: string
    :param tip: string
    :return: O lista ce contine datele unei cheltuieli.
    '''
    l=[0,0,0,0]

    l[0] = nr_apartament
    l[1] = suma
    l[2] = data
    l[3] = tip

    return l

def get_nr_apartament(cheltuiala):
    '''
    Returneaza numarul unui apartament din lista datelor unei cheltuieli
    :param lista: lista cu datele unei cheltuieli
    :return: nr apartament - int
    '''
    return cheltuiala[0]

def get_suma(cheltuiala):
    return cheltuiala[1]

def get_data(cheltuiala):
    return cheltuiala[2]

def get_tip(cheltuiala):
    return cheltuiala[3]

def to_string(cheltuiala):
    return "Nr. apartament:" + str(cheltuiala[0]) + " Suma:" + str(cheltuiala[1]) + " Data:" + str(cheltuiala[2]) + " Tipul:" +str(cheltuiala[3]) + " "


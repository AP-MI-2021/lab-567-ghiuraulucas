
def do_undo(undo_list, redo_list, current_list):
    '''
    :param undo_list:
    :param redo_list:
    :param current_list:
    :return:
    '''
    if len(undo_list) > 0:
        redo_list.append(current_list)
        return undo_list.pop()
    else:
        return None

def do_redo(undo_list, redo_list, current_list):
    '''
    :param undo_list:
    :param redo_list:
    :param current_list:
    :return:
    '''
    if len(redo_list) > 0:
        undo_list.append(current_list)
        return redo_list.pop()
    else:
        return current_list
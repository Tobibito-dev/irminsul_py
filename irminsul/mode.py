mode = 'rest'


def change_mode(new_mode):
    global mode
    if new_mode == 'rest':
        mode = 'rest'
    elif new_mode == 'rest':
        mode = 'local'
    else:
        print('Mode does not exist. Keeping', mode, 'mode.', sep=' ')


def get_mode():
    return mode

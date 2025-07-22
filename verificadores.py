import crud

def check_user_exists(idUser: int):
    user_list = crud.table.read_user()

    for users in user_list:
        if idUser in users:
            return True
    return False

def check_sub_option(update_option):
    if update_option in ("n", "p", "a"):
        return True
    else:
        print("\nSelecione uma opção válida.")

def check_input(username: None, profession: None):
    if username is not None and not username.replace(" ", "").isalpha():
        return False
    elif profession is not None and not profession.replace(" ", "").isalpha():
        return False
    return True
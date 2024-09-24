import os

def getById(id,arr):
    #obtiene entidades por su id, el cual esta en la posicion 0.
    filtered = list(filter(lambda value : value[0]==id,arr))
    return filtered[0] if (filtered != None and len(filtered)>0 )else -1

clear = lambda: os.system('cls')


# TODAS LAS "ENTIDADES" EN SU PRIMER CAMPO TIENE EL ID
    # [
    #     [id,nombre,duracion],
    #     [id,nombre,duracion],
    #     [id,nombre,duracion],
    # ]
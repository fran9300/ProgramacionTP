from entities.utils import getById, clear
from repositories.repository import addEntity, updateEntity, getEntityById, loadData, deleteById, printEntities
from entities import EntitiesFields
from entities.EntitiesFields import USERS_FIELDS





def getUsers():
    return None

def addUser(): 
    newUser = {
        "type": "USER",
        USERS_FIELDS[1]:input("Ingrese el nombre de usuario:"),
        USERS_FIELDS[2]: input("Ingrese el nombre del usuario: "),
        USERS_FIELDS[3]: input("Ingrese el apellido del usuario: "),
        USERS_FIELDS[4]: input("Ingrese la contraseña: "),
        USERS_FIELDS[5]: int(input("Ingrese el rol (1=Admin, 2=Usuario): ")),
        USERS_FIELDS[6]: input("Ingrese el correo electrónico: "),
        USERS_FIELDS[7]: float(input("Ingrese el saldo inicial: "))
    }
    
    addEntity(newUser)
    print("\nNuevo usuario agregado al sistema.\n")


def editUser():
    userId = int(input("Ingrese el ID del usuario a editar: "))
    userToEdit = getEntityById("USER", userId)

    if not userToEdit:
        print("No se encontró ningún usuario con ID:", userId)
    else:
        editing = True
        while editing:
            print("\nEditando el usuario:", userToEdit)
            print("Seleccione el campo que desea editar:")
            for index in range(1, len(USERS_FIELDS)):
                field = USERS_FIELDS[index]
                print(f"{index}. {field.capitalize()}")
            print(f"{len(USERS_FIELDS)}. Terminar de editar\n")

            choice = int(input("Elige una opción: "))
            if choice == len(USERS_FIELDS):
                editing = False
                print("\nEdición finalizada.")
            elif 1 <= choice < len(USERS_FIELDS):
                field = USERS_FIELDS[choice]
                newValue = input(f"Ingrese el nuevo valor para {field}: ")
                
                # Conversión de tipo según el campo
                if field == "role":
                    newValue = int(newValue)
                elif field == "credit":
                    newValue = float(newValue)

                userToEdit[field] = newValue
            else:
                print("Opción no válida.")

        # Guardar los cambios en el archivo
        updateEntity(userToEdit)
        print("\nUsuario con ID", userId, "ha sido actualizado en el sistema.\n")



def deleteUser():
    userId = int(input("Ingrese el ID del usuario a eliminar: "))
    deleteById("USER", userId)
    print("\nUsuario con ID", userId, "ha sido eliminado del sistema.\n")

def printUsers():
    printEntities(EntitiesFields.USER)


def checkIfUserExist(userName):
    #Función que chequea si el usuario existe. Como parametro le pasamos el nombre de usuario
    #TODO:REFACTOR que quede como validation
    filtered = list(filter(lambda value : value[1]==userName,getUsers()))
    if(filtered):
        return True
    else:
        return False

def checkUserAndPass(user,password):
    #Función para chequear si el usuario o la clave son correctas

    filtered = list(filter(lambda value : value["username"]==user,loadData(EntitiesFields.USER)))

    if len(filtered) == 0:
        clear()
        print("\nUsuario o contraseña incorrecta, intente nuevamente\n")
        return None 

    user = filtered[0]
    if(user["password"] == password):
        return user
    else:
        clear()
        print("\nUsuario o contraseña incorrecta, intente nuevamente\n")

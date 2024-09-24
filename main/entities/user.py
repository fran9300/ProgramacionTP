from numeration import getNumberFromSecuence
from entities.utils import getById, clear

users= [
    [1,"fpelli","Franco","Pelli","contraseña",2,"20020325","fpelli@uade.edu.ar",100000],
    [2,"ipelli","Ivan","Pelli","contraseña123",2,"20061010","ipelli@uade.edu.ar",50000],
    [3,"admin","","","admin",1,"20000101","admin@uade.edu.ar",100000]
]


def getUsers():
    return users



def addUser():
    #Función para agregar usuario
    global users
    newUser = []
    newUser.append(getNumberFromSecuence("userNumeration"))
    userName = input("Ingrese nombre de usuario: ")
    while checkIfUserExist(userName):
        print("Nombre de usuario no disponible, ingrese otro")
        userName = input("Ingrese nombre de usuario: ")
    newUser.append(userName)
    newUser.append(input("Ingrese nombre: "))
    newUser.append(input("Ingrese apellido: "))
    newUser.append(input("Ingrese contraseña: "))    
    newUser.append(2) ## le agrega el rol
    newUser.append(input("Ingrese fecha de nacimiento(formato YYYYMMDD): "))
    newUser.append(input("Ingrese correo electronico: "))
    newUser.append(int(input("Ingrese saldo: ")))    
    users.append(newUser)
    clear()
    print("\nNuevo usuario agregado\n")


def checkIfUserExist(userName):
    #Función que chequea si el usuario existe. Como parametro le pasamos el nombre de usuario

    filtered = list(filter(lambda value : value[1]==userName,getUsers()))
    if(filtered):
        return True
    else:
        return False

def checkUserAndPass(user,password):
    #Función para chequear si el usuario o la clave son correctas

    filtered = list(filter(lambda value : value[1]==user,getUsers()))

    if len(filtered) == 0:
        clear()
        print("\nUsuario o contraseña incorrecta, intente nuevamente\n")
        return None 

    user = filtered[0]
    if(user[4] == password):
        return user
    else:
        clear()
        print("\nUsuario o contraseña incorrecta, intente nuevamente\n")



def editUser(users):
    #Función para editar usuarios. Le pasamos la matriz users. Puede editar mas de un campo a la vez y finalizar la edicion cuando el usuario lo desee
    print("Ingrese el ID del usuario que desea editar:")
    user_id = int(input())

    user = None
    for u in users:
        if u[0] == user_id:
            user = u
    
    if not user:
        print("Usuario no encontrado.")
    else:
        bandera=True
        while bandera:
            clear()
            print("usuario a editar: ", user)
            print() 
            print("Seleccione el campo que desea editar:")
            print("1. Nombre de usuario")
            print("2. Nombre")
            print("3. Apellido")
            print("4. Contraseña")
            print("5. Fecha de nacimiento")
            print("6. Correo electrónico")
            print("7. Saldo")
            print ("8. Finalizar la edición")
            print()
            choice = int(input())

            if choice == 1:
                user[1] = input("Ingrese el nuevo nombre de usuario:")
            elif choice == 2:
                user[2] = input("Ingrese el nuevo nombre:")
            elif choice == 3:
                user[3] = input("Ingrese el nuevo apellido:")
            elif choice == 4:
                user[4] = input("Ingrese la nueva contraseña:")
            elif choice == 5:
                user[6] = input("Ingrese la nueva fecha de nacimiento (formato YYYYMMDD):")
            elif choice == 6:
                user[7] = input("Ingrese el nuevo correo electrónico:")
            elif choice == 7:
                user[8] = int(input("Ingrese el nuevo saldo:"))
            elif choice==8:
                bandera=False
                clear()
                print ("\nHa finalizado la edición")
            else:
                print("Opción no válida.")
                return

    print("\nDatos del usuario actualizados:", user, "\n")


def deleteUser(usuarioId, usuarios):
    #Función para eliminar usuario. Reutilizamos la función getById

    userToDelete = getById(usuarioId, usuarios)
    
    if userToDelete == -1:
        print("No se encontró ningún usuario con ID: ", usuarioId)
    else:
        users.remove(userToDelete)
        print("Usuario con ID ",usuarioId, "ha sido eliminado.")

    return users

def imprimirUsuarios(usuarios):
    #imprime los usuarios registrados, esta funcion solo existe para facilitar la eliminacion o modificacion de usuarios.
    print("ID | Usuario | Nombre | Apellido | Mail")
    for usuario in usuarios:
        print(f"{usuario[0]} | {usuario[1]} | {usuario[2]}  | {usuario[3]} | {usuario[6]}")
    print()
    return None

#Programa principal:
#print (editUser(users))


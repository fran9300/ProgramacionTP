import json

#Los hice separados pero capaz podemos juntar las funciones para crear el archivo y editarlo

def loadUsers():
    with open('users.json', 'r') as file:
        users = json.load(file)
    return users

def loadMovies():
    with open('movies.json', 'r') as file:
        movies = json.load(file)
    return movies

def loadRooms():
    with open('rooms.json', 'r') as file:
        rooms = json.load(file)
    return rooms

def loadPaymentMethods():
    with open('payment_methods.json', 'r') as file:
        payment_methods = json.load(file)
    return payment_methods

#Para editarlos (Administrador)

def saveUsers(users):
    with open('users.json', 'w') as file:
        json.dump(users, file, indent=4)


def saveMovies(movies):
    with open('movies.json', 'w') as file:
        json.dump(movies, file, indent=4)

def saveRooms(rooms):
    with open('rooms.json', 'w') as file:
        json.dump(rooms, file, indent=4)

def savePaymentMethods(payment_methods):
    with open('payment_methods.json', 'w') as file:
        json.dump(payment_methods, file, indent=4)

#Para cargar cosas:

users = loadUsers()
new_user = {"id": 3, "name": "Agustina", "email": "agustina@hotmail.com"}
users.append(new_user)  # Agregas el nuevo usuario a la lista
saveUsers(users)  # Guardas la lista actualizada

#Lo ideal es despues pasarlo a inputs. Que el adminitrador elija que editar y agregar


def logicDelete():
    #Se debe permitir eliminar una entidad de manera logica. Evitar borrado fisco.
    return None

def createTransaction():
    #@fpelli: se debe crear concepto de transaccionalidad.
    return None

def autoInsertId(entidad):
    #@aMieres: se debe crear una funcion que cuando le llegue una entidad, busque la secuencia y obtenga su valor, se lo asigne a la entidad y devuelva la entidad
    #seria hacer lo de numeration pero con archivos (o sea, lo de secuence ponerlo en archivo)


    
    return entidad


def updateEntity():
    #debe permitir modificar una entidad y savear el archivo. Tiene que remplazar la entidad. por ejemplo si se cambia el campo duracion de 90 -> 120. 
    # Tiene que aparecer 120 en el archivo. pero no crear un nuevo movie sino que remplazar el existente
    return None

# agrgar a todas las entidades un campo deleted para hacer borrado logico.
# EN las entidades agregar un campo que discrimine que tipo es. Luego se busca el path del archivo correspondiente por el tipo de entidad y se guarda ahi.
#  Esto lo vamos a usar para hcer un metodo generico de creacion de entidad
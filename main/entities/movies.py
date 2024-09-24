from numeration import getNumberFromSecuence
from entities.utils import getById, clear


# [id,nombre,duracion,descripcion,genero,edad,fechaDeEstreno]
movies = [
    [1,"DeadPool",127,"Superheroes","Accion","18","20/07/2024"],
    [2,"Alien",112,"Pelicula de alien","Suspenso","16","20/09/2024"],
    [3,"Longlegs",100,"pelicula de terror","Terror","13","20/08/2024"]
]


def getMovies():
    return movies


#Función para agregar películas al sistema
def addMovie():
    clear()
    global movies
    newMovie = []
    newMovie.append(getNumberFromSecuence("movieNumeration"))
    newMovie.append(input("Ingrese nombre de pelicula: "))
    newMovie.append(int(input("Ingrese duracion: ")))
    newMovie.append(input("Ingrese descripcion: "))    
    newMovie.append(input("Ingrese género: "))
    newMovie.append(input("Ingrese edad: "))
    newMovie.append(input("Ingrese fecha de estreno (formato DD/MM/YYYY): "))
    clear()
    print(newMovie)
    movies.append(newMovie)
    print("\nNueva pelicula agregada\n")


#Función para editar películas. Como parametro el pasamos el id de la película Puede editar mas de un campo a la vez y
#finalizar la edicion cuando el usuario lo desee
def editMovie():
    global movies
    movieId = int(input("ingrese id de pelicula a editar\n"))
    movieToEdit = None
    for movie in movies:
        if movie[0] == movieId:
            movieToEdit = movie

    if not movieToEdit:
        print("No se encontró ninguna película con ID:", movieId)
        clear()
    else:
        clear()
        bandera = True
        while bandera:
            print("Editando la película:", movieToEdit ,"\n")
            print("Seleccione el campo que desea editar:\n")
            print("1. Nombre de la película")
            print("2. Duración")
            print("3. Descripción")
            print("4. Género")
            print("5. Edad recomendada")
            print("6. Fecha de estreno")
            print("7. Terminar de editar\n")

            choice = int(input())  # Esta línea debe estar dentro del bucle
            print()
            if choice == 1:
                movieToEdit[1] = input("Ingrese el nuevo nombre de la película:")
            elif choice == 2:
                movieToEdit[2] = int(input("Ingrese la nueva duración:"))
            elif choice == 3:
                movieToEdit[3] = input("Ingrese la nueva descripción:")
            elif choice == 4:
                movieToEdit[4] = input("Ingrese el nuevo género:")
            elif choice == 5:
                movieToEdit[5] = input("Ingrese la nueva edad recomendada:")
            elif choice == 6:
                movieToEdit[6] = input("Ingrese la nueva fecha de estreno (formato YYYYMMDD):")
            elif choice == 7:
                bandera = False
                print("Edición finalizada")
            else:
                print("Opción no válida.")

            clear()
            print("\nPelícula con ID", movieId, "ha sido actualizada.\n")
            print("Resultado:", movieToEdit)

    return movies


def deleteMovie(peliculaId, peliculas):
    #Función para eliminar película. Reutilizamos la función getById

    movieToDelete = getById(peliculaId, peliculas)
    
    if movieToDelete == -1:
        clear()
        print("No se encontró ninguna película con ID: ", peliculaId)
    else:
        clear()
        peliculas.remove(movieToDelete)
        print("\nPelícula con ID ",peliculaId, " ha sido eliminada.\n")

    return peliculas


def imprimirPeliculas(peliculas):
    #Función que muestra la cartelera
    print("ID | Nombre | Duración | Género | Clasificación")
    for pelicula in peliculas:
        print(f"{pelicula[0]} | {pelicula[1]} | {pelicula[2]} minutos | {pelicula[4]} | +{pelicula[5]}")
    print()
    return None



from entities.movies import getMovies,addMovie,imprimirPeliculas,deleteMovie,editMovie, movies
from numeration import getSecuences, getNumberFromSecuence 
from entities.user import getUsers,addUser,checkUserAndPass,editUser, deleteUser,imprimirUsuarios, users
from entities.utils import clear
import os
import re


#Arrays y variables con datos hardcodeados ----------------------------------------------------------------------------------------

currentMenu = {}
mainMenu = {}

#[id,nombre,filas,columnas]
salas = [
    [1,"1",25,30],
    [2,"2",20,25],
    [3,"3",30,25]
]

#[id,idSala,horario,fecha]
horarios = [
    [1,1,"1400","0903"],
    [1,2,"1200","0904"],
    [1,2,"1500","0904"],
    [1,3,"1800","0905"]
]

roles = [
    [1,"admin"],
    [2,"client"]
]

# [id,userId,metodoDePagoId]
userPayment = [
    [1,1,1],
    [2,1,3],
    [3,2,2]
]

valorEntrada = 2000

descuentos = {
    "Cash": 0.30,     # 30% descuento
    "Transfer": 0.20, # 20% descuento
    "Debt": 0.10,     # 10% descuento
    "Credit": 0.02,   # 2% descuento
    # Para "Points" se manejará en una función aparte
}

METODOS_DE_PAGO = {
    1: "Cash",
    2: "Transfer",
    3: "Debt",
    4: "Credit",
    5: "Points"
}

#-----------------------------------------------------------------------------------------------------------------------------------------

def getValorEntrada():
    return valorEntrada

def setValorEntrada(number):
    global valorEntrada
    valorEntrada = number

def  login():
    # TODO: login
    return None

def asignarPeliculaASala():
    imprimirPeliculas()
    # TODO: tiene que mostrar los horarios disponibles en una fecha para sala y poder reservarla
    return None




#Funciones para el manejo de las películas------------------------------------------------------------------------------------------------

def cargarPelicula():
    #Función para cargar una nueva película en el sistema
    # TODO: cargar pelicula tiene nombre, duración, edad, descripcion, genero, fecha de estreno y se guarda en un array de peliculas(matriz)
    addMovie()
    return None

def consultarPeliculas():
    #Función para consultar y mostrar la lista de películas disponibles en el sistema
    # TODO: Lee el archivo de peliculas y muestra la informacion quiza podemos distinguir entre usuario y admin
    clear()
    imprimirPeliculas(movies)

def editarPeliculas():
    clear()
    imprimirPeliculas(movies)
    editMovie()

def eliminarPelicula():
    #Funcion para eliminar una película del sistema. Muestra las películas disponibles y permite que el usuario seleccione una para eliminar
    clear()
    imprimirPeliculas(movies)
    movieId=int(input("Ingrese el ID de la película que desea eliminar:"))

    deleteMovie(movieId,movies)
    

#Funciones para el manejo de las salas---------------------------------------------------------------------------------------------------

def crearMatrizSala():
    #Función para crear una matriz que representa la dispocion de asientos en una sala de cine

    #pregunta por filas  y columnas y crea la matriz
    filas = int(input("introduzca el número de filas desdeadas para la sala: "))
    columnas = int(input("introduzca el número de columnas desdeadas para la sala: "))

    matrizSala = []
    continuar = True
    
    while continuar:
        if filas <= 0 or columnas <= 0:
            print("Las filas y columnas deben ser mayores que 0.")
            filas = int(input("Introduce el número de filas: "))
            columnas = int(input("Introduce el número de columnas: "))
        else:
            continuar = False

    for i in range(filas):
        fila_matriz = []  
        for j in range(columnas):
            fila_matriz.append("O")
        matrizSala.append(fila_matriz)

    return matrizSala

def cargarHorarios():
    #Funcion que le permite al usuario agregar horiarios disponibles para una sala de cine
    arrayHorarios = []
    patron = r'^([01]\d|2[0-3]):([0-5]\d)$'
    continuar = True

    while continuar:
        horario = input("Agregue un horario en la forma de HH:MM, escriba '-1' para salir: ")
        
        if horario == '-1':
            continuar = False
        elif re.match(patron, horario):
            arrayHorarios.append(horario)
        else:
            print("Formato de horario inválido. Por favor, use HH:MM (ejemplo: 09:30, 14:45).")

    return arrayHorarios

def liberarSala():
    #TODO: una vez se cargo una pelicula: se requiere restablecer la sala
    #@fran9300
    return None

def cargarSala():
    #Función para cargar una nueva sala en el sistema con su matriz de asientos y horarios
    # TODO: sala: cantidad de filas, cantidad de columnas, horario, pelicula
    clear()
    matrizSala = crearMatrizSala()
    horariosSala = cargarHorarios()

    sala = [matrizSala, horariosSala, "pelicula"]

    return sala

def imprimirSala():
    #TODO: imprime el estado actual de la sala
    #@fpelliStudent
    return None

def crearSala():
    global salas
    clear()
    newSala = []
    newSala.append(getNumberFromSecuence("salaNumeration"))
    newSala.append(input("Ingrese nombre de sala: "))
    newSala.append(int(input("Ingrese la cantidad de filas: ")))
    newSala.append(input("Ingrese la cantidad de columnas: "))
    print()
    print(newSala)
    salas.append(newSala)
    print("\nNueva sala agregada\n")

def consultarSalas():
        global salas
        clear()
        print("ID | Nombre | Filas | Columnas ")
        for sala in salas:
            print(f"{sala[0]} | {sala[1]} | {sala[2]} | {sala[3]} ")
        print()
        return None


#Funciones para el manejo de los usuarios------------------------------------------------------------------------------------------------

def Registro():
    #Funcion para registrar a un nuevo usuario en el sistema
    clear()
    addUser()

def edicionDeUsuario():
    clear()
    imprimirUsuarios(users)
    editUser(users)

def eliminarUsuario():
    # removeUser
    userId=int(input("Ingrese el ID del usuario que desea eliminar: "))
    deleteUser(userId, users)
    return None

def consultarUsuarios():
    clear()
    imprimirUsuarios(users)

def configDescuentoPorTipoDePago(metodo):
    #Función para configurar el descuento aplicado según el tipo de pago seleccionado
    if metodo in descuentos:
        return descuentos[metodo]
    else:
        return 0.0

def imprimirDescuentos():
    #Función que muestra los descuentos
    global descuentos
    clear()
    for key in descuentos:
        print(f"{key}: {descuentos[key]*100}% descuento")
    print()

def clientConfig():
    #TODO: permite modificar los datos del cliente, y su metodo de pago
    return None


#Funciones para el manejo de la compra de entradas-----------------------------------------------------------------------------------------

def elegirButacas():
    #TODO: retorna la posicion de la butaca elegida formato letra-numero(fila-columna)
    #@AgustinaMieres
    return None

def calcularTotal(cantidadEntradas):
    #Función para calcular el costo total de las entradas seleccionadas
    total = getValorEntrada() * cantidadEntradas
    return total

def pedirMetodoDePago():
    #Función que le solicita al usuario el metodo de pago que quiere utilizar
    
    while True:
        print("Opciones de método de pago:")
        
        
        for numero in METODOS_DE_PAGO:
            metodo = METODOS_DE_PAGO[numero]
            print(numero, metodo)
        
        opcion = input("Ingrese el número del método de pago: ")
        
        if opcion.isdigit():  
            opcion = int(opcion)  
            
            if opcion in METODOS_DE_PAGO:  
                return opcion
            else:
                print("El número ingresado no es válido. Ingrese otro número.")
                
        else:
            print("Debe ingresar un número válido. Por favor, intente de nuevo.")

def aplicarDescuento (total,metodoID):
    #Función para aplicar desucento al total según el metodo de pago seleccionado
    if metodoID==5:
        return total
    else:
        descuento=configDescuentoPorTipoDePago(metodoID)
        valorTotal = total * (1-descuento)
        return valorTotal

def ingresarCuponDescuento(total, codigoDescuento):
    # TODO: if si el codigo es igual a 'DESCUENTO' aplica descuento
    #@fran9300
    return None

def chequeoPago(usuario):
    #TODO: recibe el usuario([]) y
    #TODO: chequea que el cliente tenga saldo disponible para pagar la cantidad de entradas que desea comprar(aplica a todos los tipo de pago)
    # @fran9300
    return None

def reservarButaca():
    #recibe nro de butaca y la reserva en array de la sala (lo marca o con 1 o con los datos del cliente)
    #@fran9300
    return None

def imprimirFactura():
     #@fran9300
    #TODO: generacionFactura()
    #TODO: Imprime los detalles de la compra, datos del cliente, y que butacas se reservaron
    return None

def aplicarPuntos(total):
    #Funcion para aplicar los puntos al total de la compra. Resta los puntos al total
    while True:
        puntos = input("Ingrese la cantidad de puntos a utilizar (1 punto = 1 peso, o ingrese 0 para no utilizar puntos): ")
        if puntos.isdigit():
            puntos = int(puntos)
            if puntos <= total:
                totalPoints=total-puntos
                return totalPoints
            else:
                print(f"No puede utilizar más puntos de los que corresponden al total ({total} puntos). Intente de nuevo.")
        else:
            print("Debe ingresar un número válido de puntos. Por favor, intente de nuevo.")

def comprarEntrada():
    #FLUJO DE COMPRAR PELICULA
    #Esto es el flujo pero no esta implementado
    consultarPeliculas()
    #elegir pelicula
    #elegir horario que tengan butacas disponibles: muestro todos los horarios  o solo los horarios con butacas disponibles
    # Consultar cantida de entradas
    imprimirSala() # para ver estado actual de la sala
    elegirButacas()
    calcularTotal()
    pedirMetodoDePago()
    aplicarDescuento()
    ingresarCuponDescuento()
    #confirmar
    chequeoPago()
    reservarButaca()
    imprimirFactura()
    return None

#Funciones para el manejo del menu interactivo-----------------------------------------------------------------------------------------

def imprimirMenu(menu):
    print("Ingrese el número de alguna de las siguientes opciones: \n")
    for key in menu.keys():
        print(f"{key}-{menu[key].__name__}")

def GestionPeliculas():
    clear()
    global currentMenu    
    currentMenu  = gestionPeliculas

def GestionUsuarios():
    clear()
    global currentMenu
    currentMenu = gestionUsuarios

def LoginMenu():
    clear()
    global currentMenu
    currentMenu = loginMenu

def GestionSalas():
    clear()
    global currentMenu
    currentMenu = gestionSalas


def IniciarSesion():
    global currentMenu,mainMenu
    user = None
    clear()
    while user == None:
        user = input("Ingrese usuario: ")
        password = input("Ingrese contraseña: ")
        user = checkUserAndPass(user,password)
    clear()
    if user[5] == 1:
        mainMenu = mainMenuAdmin        
    elif user[5] == 2:
        mainMenu = mainMenuUser
    currentMenu = mainMenu

#Programa principal
# metodoDePago=pedirMetodoDePago()
# print ("Metodo de pago seleccionado:", metodoDePago)

# cantEntradas=int(input("Ingrese la cantidad de entradas que desea comprar: "))

# montoTotal=calcularTotal(5)


# if MetodosDePago==5:
#     montoTotal=aplicarPuntos(montoTotal)


# totalFinal=aplicarDescuento(montoTotal,MetodosDePago)
# print ("El precio final es: ", totalFinal)
def volverMenuPrincipal():
    clear()
    global currentMenu
    currentMenu = mainMenu

gestionSalas = {
    "1":consultarSalas,
    "2":crearSala,
    "3":volverMenuPrincipal
}

gestionPeliculas = {
    "1":consultarPeliculas,
    "2":cargarPelicula,
    "3":eliminarPelicula,
    "4":editarPeliculas,
    "5":volverMenuPrincipal
}

gestionUsuarios = {
    "1": consultarUsuarios,
    "2": Registro,
    "3": edicionDeUsuario,
    "4": eliminarUsuario,
    "5": volverMenuPrincipal
}

# FLujo
# def adminManage():
#     login()
#     consultarPeliculas()
#     cargarPelicula()
#     eliminarPelicula()
#     cargarSala()
#     asignarPeliculaASala()
#     configDescuentoPorTipoDePago()
#     liberarSala()
#     return None


mainMenuAdmin = {
    "1":GestionPeliculas,
    "2":GestionSalas,
    "3":GestionUsuarios,
    "4":configDescuentoPorTipoDePago,
    "5":imprimirDescuentos,
    "6":liberarSala,
    "7":LoginMenu
}

#Flujo de cliente
# def clientManage():
#     consultarPeliculas()
#     comprarEntrada()
#     configuracionDelUsuario()
#     return ''

mainMenuUser = {
    #TODO agregar opciones para el usuario
    "1":consultarPeliculas,
    "2":LoginMenu
}

loginMenu = {
    "1":Registro,
    "2":IniciarSesion
}



# print("ejemplo getById")
# print(getById(2,getMovies()))      


currentMenu = loginMenu
option = ''
while option != 'exit':
    imprimirMenu(currentMenu)
    print()
    option = input()
    if option != 'exit':
        while not  option in currentMenu.keys() or option == 'exit':
                print("El valor ingresado no existe en el menu, vuelva a ingresar" )
                option = input()
        if option != 'exit':
            currentMenu[option]()
    

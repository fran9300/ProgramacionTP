# TODAS LAS "ENTIDADES" EN SU PRIMER CAMPO TIENE EL ID
    # [
    #     [id,nombre,duracion],
    #     [id,nombre,duracion],
    #     [id,nombre,duracion],
    # ]


# [id,nombre,duracion,descripcion,genero,edad,fechaDeEstreno]
peliculas = [
    [1,"DeadPool",127,"Superheroes","Accion","18","20/07/2024"],
    [2,"Alien",112,"Pelicula de alien","Suspenso","16","20/09/2024"],
    [3,"Longlegs",100,"pelicula de terror","Terror","13","20/08/2024"]
]
# [id,nombre,filas,columnas]
salas = [
    [1,"1",25,30],
    [2,"2",20,25],
    [3,"3",30,25]
]
# [id,idSala,horario,fecha]
horarios = [
    [1,1,"1400","0903"],
    [1,2,"1200","0904"],
    [1,2,"1500","0904"],
    [1,3,"1800","0905"]
]

MetodosDePago = [[
    [1,"Cash"],
    [2,"Transfer"],
    [3,"Debt"],
    [4,"Credit"],
    [5,"Points"]
]]
# [id,user,nombre,apellido,password,role,fechaNacimiento,email]
users= [
    [1,"fpelli","Franco","Pelli","contraseña",2,"20020325","fpelli@uade.edu.ar"],
    [2,"ipelli","Ivan","Pelli","contraseña123",2,"20061010","ipelli@uade.edu.ar"],
    [3,"admin","","","admin",1,"20000101","admin@uade.edu.ar"]
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

# TODO: hacer busqueda por id en array (onlyRead)

def getById(id,arr):
    filtered = list(filter(lambda value : value[0]==id,arr))
    return filtered[0] if (filtered != None and len(filtered)>0 )else -1 



def  login():
    # TODO: login
    return None

def imprimirPeliculas():
    # TODO: imprime los datos de archivo de peliculas
    # @AgustinaMieres
    # sale por pantalla:
    # id | nombre | duracion | edad | ..
    # 1| deadpool | 120 | +18
    # 2 | alien | 130 | +16
    return None

def asignarPeliculaASala():
    imprimirPeliculas()
    # TODO: tiene que mostrar los horarios disponibles en una fecha para sala y poder reservarla
    return None

def crearMatrizSala():
    # TODO: pregunta por filas  y columnas y crea la matriz
    # @fran9300
    return None

def cargarPelicula():
    # TODO: cargar pelicula tiene nombre, duración, edad, descripcion, genero, fecha de estreno y se guarda en un array de peliculas(matriz)
    #@fpelliStudent
    return None

def eliminarPelicula():
    imprimirPeliculas()
    #TODO: eliminar pelicula cargada por id. Llega un array y tiene que eliminar por id . mirar inicio del archivo
    #@fran9300


def cargarHorarios():
    # TODO: cargar horarios a una sala
    # @AgustinaMieres
    return None

def liberarSala():
    #TODO: una vez se cargo una pelicula: se requiere restablecer la sala
    #@fran9300
    return None

def cargarSala():
    # TODO: sala: cantidad de filas, cantidad de columnas, horario, pelicula
    crearMatrizSala()
    cargarHorarios()
    return None
def register():
    # TODO:registrar client y guardarlo en la ""BD"": TODO: definir campos de cliente
    #@fpelliStudent
    return None

def configDescuentoPorTipoDePago():
    # TODO: 
    # @AgustinaMieres
    return None

def adminManage():
    login()
    consultarPeliculas()
    cargarPelicula()
    eliminarPelicula()
    cargarSala()
    asignarPeliculaASala()
    configDescuentoPorTipoDePago()
    liberarSala()
    return None

def consultarPeliculas():
    imprimirPeliculas()
    # TODO: Lee el archivo de peliculas y muestra la informacion quiza podemos distinguir entre usuario y admin

def chequeoPago(usuario):
    #TODO: recibe el usuario([]) y
    #TODO: chequea que el cliente tenga saldo disponible para pagar la cantidad de entradas que desea comprar(aplica a todos los tipo de pago)
    # @fran9300
    return None

def imprimirSala():
    #TODO: imprime el estado actual de la sala
    #@fpelliStudent
    return None

def elegirButacas():
    #TODO: retorna la posicion de la butaca elegida formato letra-numero(fila-columna)
    #@AgustinaMieres
    return None
def reservarButaca():
    #recibe nro de butaca y la reserva en array de la sala (lo marca o con 1 o con los datos del cliente)
    #@fran9300
    return None


def calcularTotal(cantidadEntradas):
    #TODO: calcula el total de las entradas
    #@fpelliStudent
    return None

def aplicarDescuento(total,tipoDePago):
    # Aplica descuento segin tipo de pago. Retorna el valor final
    # @AgustinaMieres
    return None

def ingresarCuponDescuento(total, codigoDescuento):
    # TODO: if si el codigo es igual a 'DESCUENTO' aplica descuento
    #@fran9300
    return None

def imprimirFactura():
     #@fran9300
    # TODO: generacionFactura()
    #TODO: Imprime los detalles de la compra, datos del cliente, y que butacas se reservaron
    return None

def comprarEntrada():
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

def pedirMetodoDePago():
    # TODO: Ingresar metodo de pago
    # @AgustinaMieres
    return None

def clientConfig():
    #TODO: permite modificar los datos del cliente, y su metodo de pago
    return None


def adminConfig():
    # TODO: permite configurar al administrador por ejemplo : precio de entrada, descuentos
    # @fpelliStudent
    return None

def configuracionDelUsuario():
    # if (tipoUsuario)
    clientConfig()
    adminConfig()

def clientManage():
    consultarPeliculas()
    comprarEntrada()
    configuracionDelUsuario()
    return ''



# register()
# if ():
#     adminManage()
# else:
#     clientManage()

print("ejemplo getById")
print(getById(2,peliculas))
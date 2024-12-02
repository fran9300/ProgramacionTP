USER = "USER"
MOVIES = "MOVIES"
SECUENCE = "SECUENCE"
RESERVATION = "RESERVATION"
ROOM = "ROOM"
ROOM_CONFIGURATION = "ROOM_CONFIGURATION"
#general properties
ID = "id"
DELETED = "deleted"
TYPE = "type"


#Room properties

ROOM_NAME = "name"
ROOM_ROWS = "rows"
ROOM_COLUMNS = "columns"
ROOM_FIELDS = [ID,ROOM_NAME,ROOM_ROWS,ROOM_COLUMNS]
#Room configuration proeprties

CONFIG_ROOM_ID = "roomId"
CONFIG_DAY = "day"
CONFIG_TIME = "time"
CONFIG_MOVIE_ID = "movieId"
CONFIG_FIELDS = [ID,CONFIG_MOVIE_ID,CONFIG_ROOM_ID,CONFIG_DAY,CONFIG_TIME,]

# reservation properties

RESERVATION_ROOM_ID = "roomId"
RESERVATION_USER_ID = "userId"
RESERVATION_DAY = "day"
RESERVATION_TIME = "time"
RESERVATION_ROW = "row"
RESERVATION_COLUMN = "column"
RESERVATION_FIELDS = [ID,RESERVATION_ROOM_ID,RESERVATION_USER_ID,RESERVATION_DAY,RESERVATION_TIME,RESERVATION_ROW,RESERVATION_COLUMN]


MOVIE_TITLE="title"
MOVIE_DURATION="duration"
MOVIE_GENRE="genre"
MOVIE_CATEGORY="category"
MOVIE_RATING="rating"
MOVIE_RELEASEDATE="releaseDate"

MOVIES_FIELDS=[ID,MOVIE_TITLE,MOVIE_DURATION,MOVIE_GENRE,MOVIE_CATEGORY,MOVIE_RATING,MOVIE_RELEASEDATE]


USER_USERNAME="userName"
USER_NAME= "name"
USER_LASTNAME="lastName"
USER_PASSWORD="password"
USER_ROLE="role"
USER_EMAIL="email"
USER_CREDIT="credit"

USERS_FIELDS= [ID,USER_USERNAME,USER_NAME,USER_LASTNAME,USER_PASSWORD,USER_ROLE,USER_EMAIL,USER_CREDIT]



FIELDS = {
    USER: USERS_FIELDS,
    MOVIES: MOVIES_FIELDS,
    SECUENCE: "SECUENCE",
    RESERVATION: RESERVATION_FIELDS,
    ROOM: ROOM_FIELDS,
    ROOM_CONFIGURATION: CONFIG_FIELDS,
}

STRING = "string"
INTEGER = "integer"
FLOAT = "float"
DATE = "date"


def convertValue(value,type):
    match type:
        case "string":
            return value
        case "float":
            return float(value)
        case "integer":
            return int(value)
        case "date":
            return value
        

#Se agrega el field  y el tipo de campo que es
FIELDS_TYPES = {
    USER_USERNAME:STRING,
    USER_NAME:STRING,
    USER_LASTNAME:STRING,
    USER_PASSWORD:STRING,
    USER_ROLE:INTEGER,
    USER_EMAIL:STRING,
    USER_CREDIT:FLOAT,
    MOVIE_TITLE:STRING ,
    MOVIE_DURATION:INTEGER,
    MOVIE_GENRE:STRING,
    MOVIE_CATEGORY:STRING,
    MOVIE_RATING:INTEGER,
    MOVIE_RELEASEDATE:DATE,
    RESERVATION_ROOM_ID:STRING,
    RESERVATION_USER_ID:INTEGER,
    RESERVATION_DAY:STRING, 
    RESERVATION_TIME:STRING, 
    RESERVATION_ROW:INTEGER, 
    RESERVATION_COLUMN:INTEGER

}

# Payment Config Entity
USER_PAYMENT_FIELDS = [
    "id",            # ID único de la entrada (autoincremental)
    "user_id",       # ID del usuario
    "payment_type",  # Tipo de método de pago (ID o nombre)
    "balance"        # Saldo disponible para ese método de pago
]

# Opciones de método de pago
PAYMENT_METHODS = {
    1: "Cash",
    2: "Transfer",
    3: "Debit",
    4: "Credit",
    5: "Points"
}

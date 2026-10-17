"""DECLARACIÓN DE VARIABLES CONSTANTES DEL TABLERO"""

TAMANO_TABLERO: int = 8
LETRAS_VALIDAS: str = "abcdefgh"
NUMEROS_VALIDOS: str = "12345678"

#DECLARACIÓN DEL ESTADO

estado: str = "turno_blancas" #empezamos con las blancas porque siempre inician las partidas estas fichas

#TABLERO

tablero_simbolos: list[list[str]] = [
    ["\u265C", "\u265E", "\u265D", "\u265B", "\u265A", "\u265D", "\u265E", "\u265C"],  # fila 8 (piezas negras)
    ["\u265F", "\u265F", "\u265F", "\u265F", "\u265F", "\u265F", "\u265F", "\u265F"],  # fila 7 (peones negros)
    ["", "", "", "", "", "", "", ""],                  # fila 6 (vacia)
    ["", "", "", "", "", "", "", ""],                  # fila 5 (vacia)
    ["", "", "", "", "", "", "", ""],                  # fila 4 (vacia)
    ["", "", "", "", "", "", "", ""],                  # fila 3 (vacia)
    ["\u2659", "\u2659", "\u2659", "\u2659", "\u2659", "\u2659", "\u2659", "\u2659"],  # fila 2 (peones blancos)
    ["\u2656", "\u2658", "\u2657", "\u2655", "\u2654", "\u2657", "\u2658", "\u2656"],  # fila 1 (piezas blancas)
]

#Imprimimos el Tablero

#con este bucle construimos la línea de arriba del todo, con las letras de las columnas
encabezado: str = "  " #dejamos un espacio en blanco al principio para que las letras cuadren con los números cada fila
for indice_columna in range(TAMANO_TABLERO):
    letra_columna: str = LETRAS_VALIDAS[indice_columna] #de esta forma sacamos la letra que le toca aesta columna (la variable indice_columna recorre cada letra una por una)
    encabezado: str = encabezado + " " + letra_columna + " " #le metemos espacios antes y después de la letra para que quede bien alineado con las celdas de abajo
print(encabezado)

#ahora recorremos todas las filas del tablero para ir imprimiéndolas una a una
for indice_fila in range(TAMANO_TABLERO): #(8, recorrerá del 0 al 7)
    numero_fila: int = TAMANO_TABLERO - indice_fila #como la primera lista que representa la fila 1 en ajedrez es la fila 8, necesitamos restarle la variable indice_fila
    linea: str = str(numero_fila) + " " #aquí imprimimos el número como tal (un string de numero fila) y le sumamos un espacio para que no esté pegado al tablero
    for indice_columna in range(TAMANO_TABLERO): #(8, recorrerá del 0 al 7)
        simbolo: str = tablero_simbolos[indice_fila][indice_columna] #recorremos fila por fila el tablero entero
        if simbolo == "":
            celda: str = " . " #rellenamos cada vacío con un punto
        else:
            celda: str = " " + simbolo + " " #dejamos el símbolo como tal entre espacios para que quede más limpio
        linea: str = linea + celda #vamos pegando cada casilla a la línea hasta completar la fila entera
    print(linea)

#dejamos 2 espacios

print("")
print("")

while estado != "salir":

    if estado == "turno_blancas":
        print("Es el Turno de las Blancas")
        casilla: str = input("¿Qué casilla deseas comprobar? ")

        if casilla.lower() == "salir": #el .lower() corrige el problema de que el usuario escriba mayúsculas, convirtiendo todos los caracteres a minúscula
            estado = "salir" #cerramos programa

        elif len(casilla) == 2 and casilla.lower()[0] in LETRAS_VALIDAS and casilla.lower()[1] in NUMEROS_VALIDOS: #con esto comprobamos que la casilla introducida es parte del tablero

            """Nuestro problema principal es que queremos comprobar qué ficha tenemos en cada posición, pero en principio lo único que tenemos para buscarla es la respuesta
            del usuario. Por ello, extraeremos de la casilla indicada por el usuario los datos necesarios para encontrar la posición en el tablero. Concretamente, el número
            de la fila y la columna en la que se encuentra"""

            letra_casilla: str = casilla.lower()[0] #tenemos la LETRA de la casilla, que nos da la información clave para encontrar el número de la columna

            match letra_casilla: #analizamos todos los casos posibles y los convertimos al número de columna
                case "a": 
                    n_columna: int = 0
                case "b":
                    n_columna: int = 1
                case "c":
                    n_columna: int = 2
                case "d":
                    n_columna: int = 3
                case "e":
                    n_columna: int = 4
                case "f":
                    n_columna: int = 5
                case "g":
                    n_columna: int = 6
                case "h":
                    n_columna: int = 7

            numero_casilla: str = casilla.lower()[1] #ahora, buscamos el número de fila. Este es mucho más fácil porque el usuario ya nos lo da al escribir la casilla que busca

            n_fila: int = TAMANO_TABLERO - int(numero_casilla) #el int convierte a entero el string que nos ha dado el usuario inicialmente.

            #le restamos el número de ña fila al Tamaño del tablero porque en ajedrez, las filas se numeran del 8 al 1, pero por la forma en la que hemos
            #creado el tablero, están "invertidas". Nuestra primera fila (la fila 0), es la fila 8 del ajedrez. Con esta resta, coinciden la fila que el usuario
            #busca con la fila que lee el programa

            ficha: str = tablero_simbolos[n_fila][n_columna] #de esta forma "accedemos" al tablero y buscamos la ficha

            if ficha == "\u2654":
                nombre_ficha: str = "rey blanco"
                print(f"En la casilla {casilla} se encuentra {nombre_ficha}")
                estado = "turno_negras" #damos el turno a las negras
            elif ficha == "\u2655":
                nombre_ficha: str = "dama blanca"
                print(f"En la casilla {casilla} se encuentra {nombre_ficha}")
                estado = "turno_negras" #damos el turno a las negras
            elif ficha == "\u2656":
                nombre_ficha: str = "torre blanca"
                print(f"En la casilla {casilla} se encuentra {nombre_ficha}")
                estado = "turno_negras" #damos el turno a las negras
            elif ficha == "\u2657":
                nombre_ficha: str = "alfil blanco"
                print(f"En la casilla {casilla} se encuentra {nombre_ficha}")
                estado = "turno_negras" #damos el turno a las negras
            elif ficha == "\u2658":
                nombre_ficha: str = "caballo blanco"
                print(f"En la casilla {casilla} se encuentra {nombre_ficha}")
                estado = "turno_negras" #damos el turno a las negras
            elif ficha == "\u2659":
                nombre_ficha: str = "peón blanco"
                print(f"En la casilla {casilla} se encuentra {nombre_ficha}")
                estado = "turno_negras" #damos el turno a las negras
            elif ficha == "\u265A":
                nombre_ficha: str = "rey negro"
                print(f"En la casilla {casilla} se encuentra {nombre_ficha}")
                estado = "turno_negras" #damos el turno a las negras
            elif ficha == "\u265B":
                nombre_ficha: str = "dama negra"
                print(f"En la casilla {casilla} se encuentra {nombre_ficha}")
                estado = "turno_negras" #damos el turno a las negras
            elif ficha == "\u265C":
                nombre_ficha: str = "torre negra"
                print(f"En la casilla {casilla} se encuentra {nombre_ficha}")
                estado = "turno_negras" #damos el turno a las negras
            elif ficha == "\u265D":
                nombre_ficha: str = "alfil negro"
                print(f"En la casilla {casilla} se encuentra {nombre_ficha}")
                estado = "turno_negras" #damos el turno a las negras
            elif ficha == "\u265E":
                nombre_ficha: str = "caballo negro"
                print(f"En la casilla {casilla} se encuentra {nombre_ficha}")
                estado = "turno_negras" #damos el turno a las negras
            elif ficha == "\u265F":
                nombre_ficha: str = "peón negro"
                print(f"En la casilla {casilla} se encuentra {nombre_ficha}")
                estado = "turno_negras" #damos el turno a las negras
            else:
                print(f"La casilla está vacía")
                estado = "turno_negras" #damos el turno a las negras

        else:
            print("La casilla introducida no es válida.")
            print()
            estado = "turno_blancas" #volvemos a darle el turno a las blancas para que el bucle siga hasta que la casilla sea válida

    elif estado == "turno_negras":
            print("Es el Turno de las Negras")
            casilla: str = input("¿Qué casilla deseas comprobar? ")
    
            if casilla.lower() == "salir": #el .lower() corrige el problema de que el usuario escriba mayúsculas, convirtiendo todos los caracteres a minúscula
                estado = "salir" #cerramos programa
    
            elif len(casilla) == 2 and casilla.lower()[0] in LETRAS_VALIDAS and casilla.lower()[1] in NUMEROS_VALIDOS: #con esto comprobamos que la casilla introducida es parte del tablero
    
    
                letra_casilla: str = casilla.lower()[0] #tenemos la LETRA de la casilla, que nos da la información clave para encontrar el número de la columna
    
                match letra_casilla: #analizamos todos los casos posibles y los convertimos al número de columna
                    case "a": 
                        n_columna: int = 0
                    case "b":
                        n_columna: int = 1
                    case "c":
                        n_columna: int = 2
                    case "d":
                        n_columna: int = 3
                    case "e":
                        n_columna: int = 4
                    case "f":
                        n_columna: int = 5
                    case "g":
                        n_columna: int = 6
                    case "h":
                        n_columna: int = 7
    
                numero_casilla: str = casilla.lower()[1] #ahora, buscamos el número de fila. Este es mucho más fácil porque el usuario ya nos lo da al escribir la casilla que busca
    
                n_fila: int = TAMANO_TABLERO - int(numero_casilla) #el int convierte a entero el string que nos ha dado el usuario inicialmente[]
    
                ficha: str = tablero_simbolos[n_fila][n_columna] #de esta forma "accedemos" al tablero y buscamos la ficha
    
                if ficha == "\u2654":
                    nombre_ficha: str = "rey blanco"
                    print(f"En la casilla {casilla} se encuentra {nombre_ficha}")
                    estado = "turno_blancas" #damos el turno a las blancas
                elif ficha == "\u2655":
                    nombre_ficha: str = "dama blanca"
                    print(f"En la casilla {casilla} se encuentra {nombre_ficha}")
                    estado = "turno_blancas" #damos el turno a las blancas
                elif ficha == "\u2656":
                    nombre_ficha: str = "torre blanca"
                    print(f"En la casilla {casilla} se encuentra {nombre_ficha}")
                    estado = "turno_blancas" #damos el turno a las blancas
                elif ficha == "\u2657":
                    nombre_ficha: str = "alfil blanco"
                    print(f"En la casilla {casilla} se encuentra {nombre_ficha}")
                    estado = "turno_blancas" #damos el turno a las blancas
                elif ficha == "\u2658":
                    nombre_ficha: str = "caballo blanco"
                    print(f"En la casilla {casilla} se encuentra {nombre_ficha}")
                    estado = "turno_blancas" #damos el turno a las blancas
                elif ficha == "\u2659":
                    nombre_ficha: str = "peón blanco"
                    print(f"En la casilla {casilla} se encuentra {nombre_ficha}")
                    estado = "turno_blancas" #damos el turno a las blancas
                elif ficha == "\u265A":
                    nombre_ficha: str = "rey negro"
                    print(f"En la casilla {casilla} se encuentra {nombre_ficha}")
                    estado = "turno_blancas" #damos el turno a las blancas
                elif ficha == "\u265B":
                    nombre_ficha: str = "dama negra"
                    print(f"En la casilla {casilla} se encuentra {nombre_ficha}")
                    estado = "turno_blancas" #damos el turno a las blancas
                elif ficha == "\u265C":
                    nombre_ficha: str = "torre negra"
                    print(f"En la casilla {casilla} se encuentra {nombre_ficha}")
                    estado = "turno_blancas" #damos el turno a las blancas
                elif ficha == "\u265D":
                    nombre_ficha: str = "alfil negro"
                    print(f"En la casilla {casilla} se encuentra {nombre_ficha}")
                    estado = "turno_blancas" #damos el turno a las blancas
                elif ficha == "\u265E":
                    nombre_ficha: str = "caballo negro"
                    print(f"En la casilla {casilla} se encuentra {nombre_ficha}")
                    estado = "turno_blancas" #damos el turno a las blancas
                elif ficha == "\u265F":
                    nombre_ficha: str = "peón negro"
                    print(f"En la casilla {casilla} se encuentra {nombre_ficha}")
                    estado = "turno_blancas" #damos el turno a las blancas
                else:
                    print(f"La casilla está vacía")
                    estado = "turno_blancas" #damos el turno a las blancas
    
            else:
                print("La casilla introducida no es válida.")
                print()
                estado = "turno_negras" #volvemos a darle el turno a las negras para que el bucle siga hasta que la casilla sea válida
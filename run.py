
import random



def dibujarTablero(tablero):
    '''
     Esta función dibuja el tablero.
    '''

    print('   |   |')
    print(' ' + tablero[6] + ' | ' + tablero[7] + ' | ' + tablero[8])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + tablero[3] + ' | ' + tablero[4] + ' | ' + tablero[5])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + tablero[0] + ' | ' + tablero[1] + ' | ' + tablero[2])
    print('   |   |')


def solicitudJugador(tablero):
    '''
    le pide al usuario que elija una posicion
    chequea que sea numero de 0 a 8
    '''

    try:

        posicion=int(input("Ingrese el numero del casillero: "))
        print(posicion)
        if 0 <= posicion and posicion <= 8:
            casillaDisponible(posicion,1,tablero)
        else:
            print("numero no valido")
            print("numeros validos del 0 al 8")
    except ValueError:
        print("Limitese a ingresar solo numeros")
        print("numeros validos del 0 al 8")

def casillaDisponible(casilla,jugador,tablero):
    '''
    funcion que evalua si la casilla esta casillaDisponible
    si lo está la ocupa segun el jugador
    '''


    if tablero[casilla]==" ":
        print("casilla disponible")
        if 0==jugador:
            tablero[casilla] = "x"
        else:
            tablero[casilla] = "0"
        dibujarTablero(tablero)
    else:
        print("casilla ocupada")
        dibujarTablero(tablero)
        if 0==jugador:
            jugadorMaquina(tablero)
        elif 1==jugador:
            solicitudJugador(tablero)


def jugadorMaquina(tablero):

    num=random.randrange(0,8)
    posicion=int(num)
    if 0 <= posicion and posicion <= 8:
        casillaDisponible(posicion,0,tablero)



def inicio(turno):
    '''
    funcion que aleatoriamente decide quien inicia
    '''

    num=random.randrange(0,9)
    num=num%2
    print(num)
    if( 0==num):
        turno="maquina"
        return(0)
    else:
        turno="jugador"
        return(1)


def ganador(tablero):
    '''
    funcion que dice que dice si alguien gano
    '''
    #veo las filas
    fila=[0,3,6]
    for i in fila:
        if tablero[i]==tablero[i+1] and tablero[i+1]==tablero[i+2]:
            if "0"==tablero[i]:
                print("gano el jugador")
                return("jugador")
            elif "x"==tablero[i]:
                print("gano la maquina")
                return("maquina")

    columna=[0,1,2]
    for i in columna:
        if tablero[i]==tablero[i+3] and tablero[i+3]==tablero[i+6]:
            if "0"==tablero[i]:
                print("gano el jugador")
                return("jugador")
            elif "x"==tablero[i]:
                print("gano la maquina")
                return("maquina")

    #vel las diagonales[ 0,4,8]
    if tablero[0]==tablero[4] and tablero[4]==tablero[8]:
        if "0"==tablero[0]:
            print("gano el jugador")
            return("jugador")
        elif "x"==tablero[0]:
            print("gano la maquina")
            return("maquina")

    #vel las diagonales[ 2,4,6]
    if tablero[2]==tablero[4] and tablero[4]==tablero[6]:
        if "0"==tablero[2]:
            print("gano el jugador")
            return("jugador")

        elif "x"==tablero[2]:
            print("gano la maquina")
            return("maquina")


    return(0)





if __name__ == '__main__':
    TABLEROVACIO=[" "," "," "," "," "," "," "," "," "]
    CASILLASDELTABLERO=["0","1","2","3","4","5","6","7","8"]
    turno="maquina"
    punto =	{
      "maquina": 0,
      "jugador": 0,
      "empate": 0,
     }

    print(punto)


    tablero=CASILLASDELTABLERO.copy()
    dibujarTablero(tablero)
    print('+++++++++')
    partida=jugada=0

    while(1):
        jugada=0
        tablero=TABLEROVACIO.copy()
        dibujarTablero(tablero)
        inicio(turno)
        print("partida",partida)
        partida=partida+1

        #mientras haya ligares libres se juega
        while 0<tablero.count(" "):
            #si inicio el jugador
            if turno=="jugador":
                if tablero.count("0")<tablero.count("x"):
                    jugadorMaquina(tablero)
                else:
                    solicitudJugador(tablero)

            #si inicio la maquina
            if turno=="maquina":
                if tablero.count("0")>tablero.count("x"):
                    jugadorMaquina(tablero)
                else:
                    solicitudJugador(tablero)

            aux=ganador(tablero)
            print("aux",aux)
            if aux== "jugador" or aux=="maquina":
                punto[aux]=punto[aux]+1
                print(punto)
                break

            jugada=jugada+1
            print("jugada",jugada)

        punto["empate"]=punto["empate"]+1

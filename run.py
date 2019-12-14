
import random

TABLEROVACIO=[" "," "," "," "," "," "," "," "," "]
CASILLASDELTABLERO=["0","1","2","3","4","5","6","7","8"]
turno="maquina"
punto =	{
  "maquina": 0,
  "jugador": 0,
}

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


def solicitudJugador():
    '''
    le pide al usuario que elija una posicion
    chequea que sea numero de 0 a 9
    '''
    print("Ingrese el numero del casillero")
    posicion = input()

    try:
        posicion=int(posicion)
        if 0 <= posicion and posicion <= 9:
            casillaDisponible(posicion,1)
        else:
            print("numero no valido")
            print("numeros validos del 0 al 9")
    except ValueError:
        print("Limitese a ingresar solo numeros")
        print("numeros validos del 0 al 9")

def casillaDisponible(casilla,jugador):
    '''
    funcion que evalua si la casilla esta casillaDisponible
    si lo está la ocupa segun el jugador
    '''
    global tablero

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
            jugadorMaquina()
        else:
            solicitudJugador()


def jugadorMaquina():

    num=random.randrange(0,9)
    posicion=int(num)
    if 0 <= posicion and posicion <= 9:
        casillaDisponible(posicion,0)



def inicio():
    '''
    funcion que aleatoriamente decide quien inicia
    '''

    num=random.randrange(0,9)
    num=num%2
    print(num)
    if( 0==num):
        #es par inicia la maquina
        #jugadorMaquina()
        turno="maquina"
        return(0)
    else:
        #es impar inicia el jugador
        #solicitudJugador()
        turno="jugador"
        return(1)


def ganador():
    '''
    funcion que dice que dice si alguien gano
    '''
    global tablero
    #veo las filas
    fila=[0,3,6]
    for i in fila:
        if tablero[i]==tablero[i+1] and tablero[i+1]==tablero[i+2]:
            if "0"==tablero[i]:
                print("gano el jugador")
                puntos("jugador")
                return(1)
            elif "x"==tablero[i]:
                print("gano la maquina")
                puntos("maquina")
                return(1)

    columna=[0,1,2]
    for i in columna:
        if tablero[i]==tablero[i+3] and tablero[i+3]==tablero[i+6]:
            if "0"==tablero[i]:
                print("gano el jugador")
                tablero=TABLEROVACIO
                puntos("jugador")
                return(1)
            elif "x"==tablero[i]:
                print("gano la maquina")
                puntos("maquina")
                return(1)

    #vel las diagonales[ 0,4,8]
    if tablero[0]==tablero[4] and tablero[4]==tablero[8]:
        if "0"==tablero[0]:
            print("gano el jugador")
            puntos("jugador")
            return(1)
        elif "x"==tablero[0]:
            print("gano la maquina")
            puntos("maquina")
            return(1)

    #vel las diagonales[ 2,4,6]
    if tablero[2]==tablero[4] and tablero[4]==tablero[6]:
        if "0"==tablero[2]:
            print("gano el jugador")
            puntos("jugador")
            return(1)
        elif "x"==tablero[2]:
            print("gano la maquina")
            puntos("maquina")
            return(1)


def puntos(gano):
    global tablero

    punto[gano]=punto[gano]+1
    tablero=TABLEROVACIO
    print(punto)






if __name__ == '__main__':
    global tablero

    tablero=CASILLASDELTABLERO
    dibujarTablero(tablero)
    print('+++++++++')
    partida=jugada=0

    while(1):
        tablero=TABLEROVACIO
        dibujarTablero(tablero)
        inicio()
        print("partida",partida)
        partida=partida+1
        while jugada<=9:
            if turno=="maquina":
                turno="jugador"
                jugadorMaquina()
            else :
                turno="maquina"
                solicitudJugador()


            if 1==ganador():
                break
            jugada=jugada+1
            print("jugada",jugada)

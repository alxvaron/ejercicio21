from random import shuffle
import sys

def maso():
    return [2,2,2,2,3,3,3,3,4,4,4,4,5,5,5,5,6,6,6,6,7,7,7,7,8,8,8,8,9,9,9,9,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,11,11,11,11]

#suma las manos de cada jugador
def suma(maso):
    if maso==[]:
        return 0
    else:
        return maso[0] + suma(maso[1:])

 # def si es 1 o 11 mostrar A
def mostrarLetra (n):
    if(n==1 or n==11): 
        return 'A'
    else: 
        return str(n)
    
    
# def listas vacias manoJugador y manoCasa
def manoJugador():
    return []

def manoCasa():
    return []


#menu de seleccion
def menu():
    print("")
    print("")
    print("**************** BIENVENIDO A 21 ******************")
    print("*                                                 *")
    print("*   oprima 1 para pedir carta, 2 para plantarse:  *")
    print("*                                                 *")
    print("***************************************************")
    print("")

# lectura del dato obtenido de menu de seleccion
def leer():
    print ("")
    return int(input("1. carta / 2. plantarse : "))

# se sirve carta y la elimina del maso
def unaCarta(mano, baraja, jugador):
    mano.append(baraja.pop(0))
    print ("")
    print ("Mano",jugador,": ",mostrarLetra(mano))
    print("Suma: ",suma(mano))

# esta funcion evalua el ganador si la casa o el jugador
def ganador(manoJ, manoC):
    print ("")
    if suma(manoJ) < 21 and suma(manoC) < 21:
        if suma(manoJ) == suma(manoC):
            print ("La casa gana")
        elif suma(manoJ) < suma(manoC):
            print ("La casa gana")
        else:
            print ("Jugador gana")

# evalua si se paso de 21
def evaluar(mano, baraja):
    if suma(mano) < 21:
        return 1
    elif suma(mano) > 21:
        return 0

# evalua la mano y brinda opciones de carta
def pedirCarta(mano, baraja, jugador):
    
    while evaluar(mano,baraja) == 1 and leer() == 1:
        unaCarta(mano,baraja, jugador)
        evaluar(mano, baraja)
             
        
    if suma(mano) == 21:
        print (f"Gano {jugador}")
        return sys.exit(0)
    elif suma(mano) > 21:
        print ("")
        print(f"Total {jugador}: {suma(mano)} - Perdio {jugador}")
        return sys.exit(0)
    else:    
        print (f"{jugador} se planto en: {suma(mano)}")
        
        
        
#main
def repartir(manoCasa, manoJugador, baraja):    
    shuffle(baraja)
    print ("")
    manoCasa.append(baraja.pop(0))
    manoCasa.append(baraja.pop(0))
    manoJugador.append(baraja.pop(0))
    manoJugador.append(baraja.pop(0))
    
    print ("Mano Casa: ",mostrarLetra(manoCasa))
    print ('Suma: ',suma(manoCasa))
    print ("")
    print ("Mano Jugador: ",mostrarLetra(manoJugador))
    print("Suma: ",suma(manoJugador))
    print ("")

    print("******** TURNO JUGADOR ********")
    pedirCarta(manoJugador, baraja, "jugador")
    print ("")
    print("********* TURNO CASA **********")
    pedirCarta(manoCasa, baraja, "casa")
    ganador(manoJugador, manoCasa)

menu()
print("Se sirven cartas, buena suerte!!! ")
repartir(manoCasa(),manoJugador(),maso())



        
    

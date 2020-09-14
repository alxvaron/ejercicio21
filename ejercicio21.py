from random import shuffle
import sys

def maso():
    return [2,2,2,2,3,3,3,3,4,4,4,4,5,5,5,5,6,6,6,6,7,7,7,7,8,8,8,8,9,9,9,9,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,11,11,11,11]
 
 # def si es 1 o 11 mostrar A

def mostrarLetra (n):
    if(n==1 or n==11): return 'A'    
    return str(n)
    
# def listas vacías manoJugador y manoCasa
def manoJugador():
    return []

def manoCasa():
    return []
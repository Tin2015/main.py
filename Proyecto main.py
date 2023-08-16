#Saludo y bienvenida al proyecto
print ("Hola... por favor ingrese su nombre:")
nombre = input()
print(f"Bienvenido al reto {nombre}!")

#Proyecto integrador parte 2
import readchar
while True:
    keypress = readchar.readkey()
    if keypress == readchar.key.UP:
        break
    print(keypress)

#Proyecto integrador parte 3
import os

def borrar_terminal():
    numero_de_veces = 0
    print ("borrar terminal")
    while numero_de_veces <50:
        tecla = readchar.readkey()
        if ord(tecla)>0:
            os.system('cls' if os.name=='nt' else 'clear')
            numero_de_veces = numero_de_veces+1
            print (numero_de_veces)

if __name__ == "__main__":
    borrar_terminal()

#Proyecto integrador parte 4

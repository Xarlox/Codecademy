tablero = []

for x in range(0,5):
  tablero.append(["O"] * 5)

def print_tablero(tablero):
  for fila in tablero:
    print " ".join(fila)

print "¡Juguemos batalla naval!"
print_tablero(tablero)

def fila_aleatoria(tablero):
  return random.randint(0,len(tablero)-1)

def columna_aleatoria(tablero):
  return random.randint(0,len(tablero[0])-1)

barco_fila = fila_aleatoria(tablero)
barco_col = columna_aleatoria(tablero)
print barco_fila
print barco_col

#¡De aquí en adelante todo debería ir en tu bucle for!
#¡Asegúrate de indentar!
for turno in range(4):
    adivina_fila = input("Adivina fila:")
    adivina_columna = input("Adivina columna:")

    if adivina_fila == barco_fila and adivina_columna == barco_col:
        print "¡Felicitaciones! ¡Hundiste mi barco!"
    else:      
        if (adivina_fila < 0 or adivina_fila > 4) or (adivina_columna < 0 or adivina_columna > 4):
            print "Vaya, esto ni siquiera está en el océano."
        elif(tablero[adivina_fila][adivina_columna] == "X"):
            print "Ya dijiste esa."
        else:
            print "¡No impactaste mi barco!"
            tablero[adivina_fila][adivina_columna] = "X"
  # ¡Muestra (turno + 1) aquí! 
    break
print_tablero(tablero)
print "Estás en el turno:" + str(turno + 1) + " de 4"
if turno == 3:
    print "Terminó el juego" 



def contar(secuencia, item):
    return sum([1 for elem in secuencia if elem == item])
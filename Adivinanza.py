import random
# Se importa la libreria random al programa
print('Bienvenidos al juego de adivinar numeros') 
# Inicializamos el numero para adivinar 
number_to_guess = random.randint(1,10) 
# Inicializa el numero de intentos posibles 
count_number_of_tries = 1 
# Ingresar numero del usuario 
guess = int(input('Inserta un numero del 1 al 10: ')) 
while number_to_guess != guess: 
    print('Te equivocaste intenta de nuevo') 
    # Numero de intentos posibles
    # Cuenta el numero de intentos, si lo excede entonces se sale
    # Indica al usuario cuantos intentos le quedan
    if count_number_of_tries == 4: 
        break
    elif guess < number_to_guess: 
        print('Intenta con un numero mas alto') 
    else: 
        print('Intenta con un numero mas bajo') 

    # Intente de nuevo e ingrementa el contador de intentos 
    guess = int(input('Intenta adivinar de nuevo: ')) 
    count_number_of_tries += 1 
# Verifica si el numero que ingreso el usuario es el ganador 
if number_to_guess == guess: 
 print('Bien hecho, Ganaste!') 
 print('Usaste', count_number_of_tries , 'turno para completar el juego.') 
else: 
 print("Lo siento Perdiste") 
 print('El numero que necesitabas era...', number_to_guess) 
print('Fin del Juego!') 
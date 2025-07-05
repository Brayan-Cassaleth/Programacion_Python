"""Este es un juego sencillo de decir si los numeros que indique es par o impar.
Si la respuesta es correcta, el programa lo va aindicar, si es incorrecta, el programa termina.
Si se consiguen las 3 respuesta correctas, se dara un mensaje de felicitaciones.
"""

import random


print("\n=== PAR O IMPAR ===")

score = 0

print(f"\n=> Oportunidades: 3")
print(f"=> Score: {score}")
print("\n- Responde 'si' si el numero es par, de lo contrario 'no'")

for item in range(3):
    number = random.randint(1,100)
    respuesta = "si" if number % 2 == 0 else "no"
    print(f"\nNumero: {number}")
    respuesta_usuario = input("Respuesta: ").lower()
    
    if respuesta != respuesta_usuario:
        print(f"Lo siento, la respuesta era: {respuesta}")
        print("Sigue intentando.....")
        break
        
    print("Correcto!")
    score += 1
    
if score == 3:
    print("\n*** Felicitaciones lo lograste! ***")
        
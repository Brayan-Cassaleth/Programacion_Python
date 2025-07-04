"""Este es un juego sencillo de decir si los numeros que indique es par o impar.
Si la respuesta es correcta, el programa lo va aindicar, si es incorrecta, el programa termina.
Si se consiguen las 3 respuesta correctas, se dara un mensaje de felicitaciones.
"""

import random


print("\n=== PAR O IMPAR ===")

oportunidad = 3
score = 0

print(f"\n=> Oportunidades: {oportunidad}")
print(f"=> Score: {score}")
print("\n- Responde 'si' si el numero es par, de lo contrario 'no'")

while oportunidad > 0:
    number = random.randint(1,50)
    print(f"\nNumero: {number}")
    answer = input("Respuesta: ")
    
    if number % 2 == 0 and answer == "si":
        score += 1
        print("Correcto!")
        oportunidad -= 1

    elif number % 2 != 0 and answer == "no":
        score += 1
        print("Correcto!")
        oportunidad -= 1
        
    else:
        print("\nRespuesta incorrecta. Intentalo nuevamente!")
        print(f"Score = {score}")
        break

if score == 3:
    print("\n*** Felicitaciones lo lograste! ***")
        
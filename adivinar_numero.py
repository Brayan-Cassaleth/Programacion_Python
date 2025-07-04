import random

print("Adivina el numero!")

rango = int(input("\nIngresa el rango del numero: "))

if rango <= 10:
    oportunidad = 3

elif rango <= 30:
    oportunidad = 10

elif rango > 50:
    oportunidad = 15
    
number_random = random.randint(1,rango)

while oportunidad > 0:
    print(f"\nTienes {oportunidad} oportunidades....")
    number = int(input("Ingresa el numero: "))
    
    if number == number_random:
        print(f"**** Felicitaciones adivinaste, el numero era {number_random} ****")
        oportunidad = 0
    
    elif number > number_random:
        print("\n=> El numero es menor! <=")
        oportunidad -= 1
        
    elif number < number_random:
        print("\n=> El numero es mayor! <=")
        oportunidad -= 1

if number != number_random and oportunidad == 0:
    print(f"Lo siento, perdiste.... EL numero era: {number_random}")




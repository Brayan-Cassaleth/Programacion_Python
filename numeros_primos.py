# Programa para indicar si un numero es primo

numero = int(input("Ingrese un numero: "))

result = "Primo"

if numero > 2:
    for i in range(2, numero):
        resultado = numero / i
        
        if resultado.is_integer():
            result = "No primo"
            break
        
print(f"El numero {numero} es {result}")

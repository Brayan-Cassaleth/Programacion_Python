import random

print("------------------------")
print("GENERADOR DE CONTRASEÑAS")
print("------------------------")

characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890()}{#$%&?!¡/*-+"

range_pwd = int(input("\nIngrese el rango de la contraseña: "))
password = []

while range_pwd > 0:
    letter = random.randint(0, len(characters) - 1)
    password.append(characters[letter])
    range_pwd -= 1

password = "".join(password)
print(f"\nContraseña sugerida = {password}")
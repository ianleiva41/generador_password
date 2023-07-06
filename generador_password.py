import random
import string

def generar_contrasena(longitud, incluir_numeros, incluir_letras, incluir_caracteres_especiales, tipo_letras):
    caracteres = ''
    if incluir_numeros:
        caracteres += string.digits
    if incluir_letras:
        if tipo_letras == 'mayusculas':
            caracteres += string.ascii_uppercase
        elif tipo_letras == 'minusculas':
            caracteres += string.ascii_lowercase
        else:
            caracteres += string.ascii_letters
    if incluir_caracteres_especiales:
        caracteres += '#@$*-_+'
    contrasena = ''.join(random.choice(caracteres) for i in range(longitud))
    return contrasena

longitud = int(input("Ingrese la longitud de la contraseña: "))
incluir_numeros = input("¿Desea incluir números? (s/n): ").lower() == 's'
incluir_letras = input("¿Desea incluir letras? (s/n): ").lower() == 's'
if incluir_letras:
    tipo_letras = input("¿Desea que las letras sean en mayúsculas, en minúsculas o mezcladas? (mayusculas/minusculas/mezcladas): ").lower()
incluir_caracteres_especiales = input("¿Desea incluir caracteres especiales? (s/n): ").lower() == 's'

contrasena_generada = generar_contrasena(longitud, incluir_numeros, incluir_letras, incluir_caracteres_especiales, tipo_letras)
print("La contraseña generada es:", contrasena_generada)

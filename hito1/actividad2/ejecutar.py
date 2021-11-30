def codificar(mensaje, rotaciones):
    alfabeto = "abcdefghijklmnopqrstuvwxyz"
    alfabeto_mayusculas = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    longitud_alfabeto = len(alfabeto)
    codificado = ""
    for letra in mensaje:
        if not letra.isalpha() or letra.lower() == 'ñ':
            codificado += letra
            continue
        valor_letra = ord(letra)
        alfabeto_a_usar = alfabeto
        limite = 97
        if letra.isupper():
            limite = 65
            alfabeto_a_usar = alfabeto_mayusculas
        posicion = (valor_letra - limite + rotaciones) % longitud_alfabeto
        codificado += alfabeto_a_usar[posicion]
    return codificado
def decodificar(mensaje, rotaciones):
    alfabeto = "abcdefghijklmnopqrstuvwxyz"
    alfabeto_mayusculas = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    longitud_alfabeto = len(alfabeto)
    decodificado = ""
    for letra in mensaje:
        if not letra.isalpha() or letra.lower() == 'ñ':
            decodificado += letra
            continue
        valor_letra = ord(letra)
        alfabeto_a_usar = alfabeto
        limite = 97
        if letra.isupper():
            limite = 65
            alfabeto_a_usar = alfabeto_mayusculas
        posicion = (valor_letra - limite - rotaciones) % longitud_alfabeto
        decodificado += alfabeto_a_usar[posicion]
    return decodificado


print("¿Que texto quieres encriptar?")
mensaje = input()
print(f"El mensaje original es: {mensaje}")
print("¿Cuantas rotaciones quieres?")
rotaciones = int(input())
codificado = codificar(mensaje, rotaciones)
print("Encriptado: ", codificado)
decodificado = decodificar(codificado, rotaciones)
print("Desencriptado: ", decodificado)
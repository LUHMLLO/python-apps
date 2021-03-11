print(" ")
print("Digite un caracter en Mayuscula o Minuscula")
caracter = str(input())

if caracter.islower():
    print("el caracter que digito es una minuscula")
if caracter.isupper():
    print("el caracter que digito es una mayuscula")
if not caracter.islower() and not caracter.isupper():
    print("digito caracteres mixtos")

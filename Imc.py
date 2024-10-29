def imc(peso, altura):
    imc = peso / (altura ** 2)
    return imc

try:
    peso = float(input("Ingrese su peso en kilogramos: "))
    altura = float(input("Ingrese su altura en metros: "))

    ##llamo las funciones
    imcdef = imc(peso, altura)
    # resultados
    print(f"Su IMC es: {imcdef:.2f}")

except ValueError:"ingrese"


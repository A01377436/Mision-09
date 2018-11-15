def extraerPares(numeros):
    numeros2 = []
    for numero in range(0,len(numeros)):
        if numeros[numero] %2==0:
            numeros2.append(numeros[numero] )
    return numeros2


def extraerMayoresPrevio(numeros):
    numeros2 = []
    for numero in range(1,len(numeros)):
        if numeros[numero] > numeros[numero-1]:
            numeros2.append(numeros[numero])
    return numeros2


def intercambiarParejas(numeros):
    numeros2 = []
    for b in range(0,len(numeros)-1):
        if b % 2 == 0:
            b2 = numeros[b]
            a = numeros[b+1]
            numeros2.append(a)
            numeros2.append(b2)
    if len(numeros) % 2 != 0:
        numeros2.append(numeros[len(numeros)-1])
    return numeros2


def intercambiarMM(numeros):

    a = numeros.index(min(numeros))
    b = min(numeros)
    c = numeros.index(max(numeros))
    d = max(numeros)
    numeros[a] = d
    numeros[c] = b
    return numeros


def promediarCentro(numeros):

    if len(numeros) == 0:
        return numeros

    numeros2 = numeros
    numeros2.remove(numeros2[numeros2.index(min(numeros2))])
    numeros2.remove(numeros2[numeros2.index(max(numeros2))])
    promedio = int(sum(numeros2)/len(numeros2))
    return promedio


def calcularEstadistica(numeros):
    suma = []
    if len(numeros) == 0:
        media = 0
    else:
        media = sum(numeros) / len(numeros)

    if len(numeros)<2:
        return media,0

    for numero in range (0,len(numeros)):
        a = (numeros[numero] - media)**2
        suma.append(a)
    suma2 = sum(suma)
    desviacion = (suma2 / (len(numeros)-1))**0.5
    resultado = (media,desviacion)
    return resultado
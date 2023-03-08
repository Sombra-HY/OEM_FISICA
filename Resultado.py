from math import log10 , floor


def tranf(x):
    # a = x.split("*")
    # potencia = ''.join(a).split("^")
    #
    # numero = float(a[0])
    # pot = int(potencia[len(potencia)-1])
    #
    # print(numero, pot)
    # print(type(numero), type(pot))

    a = x.split("e")

    return (float(a[0])*(10**int(a[1])))


tranf("3.141516e-2")
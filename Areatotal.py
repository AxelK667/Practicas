lado=10
radio=10
base=10
altura=10

def areaC(lado):
    print("calculando area del cuadrado")
    return lado*lado

def areaCI(radio):
    print("Calculando area del circulo")
    return 3.1416*radio*radio

def areaT(base,Altura):
    print("Calculando area del Triangulo")
    return base*Altura/2

def areaMC(lado):
    print("Calculando area del Medio circulo")
    return lado*lado/2

def areaTotal():
    print(areaC())
    print(areaCI())
    print(areaT())
    print(areaMC())



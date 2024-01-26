
import time 
lado=10
radio=5
base=10
altura=10
def areaC(lado):
    return lado*lado
def areaCI(radio):
    return 3.1416*radio*radio
def areaT(base,altura):
    return base*altura/2
def areaMC(lado):
    return base*lado/2
print("Calculando....")
time.sleep (1)
print("espere pofa...")

areaTo=areaC(lado)+areaCI(radio)+areaT(base,altura)+areaMC(lado)
time.sleep(2)
print("el area total es:",areaTo)


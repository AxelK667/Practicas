def infoC():
    return "El area se calcula con : lado*lado"
def infoT():
    return "El area se calcula con : Base*Altura/2"
def infoCI():
    return "El area se calcula con : 3.1416*radio*radio"
def infoR():
    return "El area se calcula con : Base*Altura"
def menuFiguras(opcion):
    if(opcion==1):
        print(infoC())
    elif(opcion==2):
        print(infoT())
    elif(opcion==3):
        print(infoT())
    elif(opcion==4):
        print(infoR())
        
print("Bienvenido al menu de figuras seleccione una opcion del menu: ")
print("Menu...")
print("1. Cuadrado")
print("2. Triangulo")
print("3. Circulo")
print("4. Rectangulo")
opcion=int(input("Elige una opcion: "))
menuFiguras(opcion)






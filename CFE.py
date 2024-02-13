class Electrodomestico:
    def __init__(self,PrecioB,color,consumoE):
        self.PrecioB=PrecioB
        self.color=color
        self.consumoE=consumoE
    def datos (self):
        print(f"El precio es {self.PrecioB} el color {self.color} y el consumo es de{self.consumoE}. ")
c1=Electrodomestico("A","rojo","50")
c1.datos()
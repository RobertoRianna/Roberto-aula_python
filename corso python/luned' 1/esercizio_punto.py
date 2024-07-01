class Punto():
    x = 0
    y = 0

    def muovipunto (self,dx,dy) :
        self.x = dx
        self.y = dy

    def distanza(self):
        if self.x > 0 and self.y > 0:
            print("la distanza da zero è -->")
            print(self.x, self.y)
        
        if self.x > 0:
            print("la distanza da zero è -->")
            print(self.x)
        
        if self.y  > 0:
            print("La distanza da zero è -->")
            print(self.y)
        
oggetto_Punto = Punto()
oggetto_Punto.muovipunto(6,11)
oggetto_Punto.distanza()
    
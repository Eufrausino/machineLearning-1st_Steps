class triangulo:
    def __init__(self, l1,l2,l3,base,altura):
        self.l1 = l1
        self.l2 = l2
        self.l3 = l3
        self.base = base
        self.altura = altura
    
    def area(self):
        return (self.base * self.altura)/2
    
t1 = triangulo(6,7,9,6,8.5)
print(t1.area())

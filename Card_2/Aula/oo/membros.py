class contador:
    contador = 0 #atributo de classe
        
    @classmethod
    def inc(cls):
        cls.contador += 1
        return cls.contador
    
    @classmethod
    def dec (cls):
        cls.contador -= 1
        return cls.contador
    
c1 = contador()

print(c1.inc())
print(c1.inc())
print(c1.inc())
print(c1.dec())
print(c1.dec())
print(c1.dec())
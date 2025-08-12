class produto: 
    def __init__(self, nome, preco = 1.99, desc = 0):
        self.nome = nome
        self.__preco = preco
        self.desc = desc
    
    @property
    def nome(self):
        return self.__preco
    
    #@preco.setter
    #def preco(self, novo_preco):
    #    if novo_preco > 0:
    #        self.__preco = novo_preco
    
    @property #faz com que eu consiga acessar como um atributo 
    def preco_final(self):
        return (1 - self.desc) * self.__preco

p1 = produto('caneta', 5.99, 0.1)
p2 = produto('caderno', 12.99, 0.2)

print(p1.nome, p2.preco, p1.desc, p1.preco_final())
print(p2.nome, p2.preco, p2.desc, p2.preco_final())

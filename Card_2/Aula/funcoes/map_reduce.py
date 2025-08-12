from functools import reduce

def somar_nota(delta):
    def somar (nota):
        return nota + delta
    return somar

notas = [6.5, 7.8, 9.6, 3.2]
notas_finais_1 = map(somar_nota(1.5), notas)
notas_finais_2 = map(somar_nota(1.6), notas)

print(notas_finais_1)
print(notas_finais_2)

def somar(a,b):
    return a+b

total = reduce(somar,notas,0)
print(total)
    
    
  
#início do exemplo que será executado, mas com o uso de for 
#for i, nota in enumerate(notas):
#    notas[i] = nota + 1.5

#for i in range(len(notas)):
#    notas[i] = notas [i]+ 1.5
 
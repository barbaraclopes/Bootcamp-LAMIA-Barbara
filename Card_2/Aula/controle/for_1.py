#A função range exibe os número entre os intervalos que eu estabeleço, considerando uma posição que se inicia em 0, o treceiro número entre aspas representa de quanto em quanto eu pulo, o segundo é em que posição paro e o primeiro em qual posição começo
for i in range(10):
    print(i)
print(' ')
    
for i in range (1,11):
    print(i)
print(' ')
    
for i in range(1, 100, 10):
    print(i)
print(' ')

for i in range(20, 0, -3):
    print(i)
print(' ')

nums = [2, 4, 6, 8]
for n in nums:
    print(n, end=' ') #concede espaço entre os números
print(' ')

texto ='Python é muito massa!'
for letra in texto:
    print(letra, end=' ')
print(' ')

for n in {1, 2, 3, 4, 4, 4}: #set, que é conjunto, não aceita replicação, então não expõe todos os números 4
    print  (n, end=' ') 
print(' ')

##Percorrendo dicionários
produto = {
    'nome': 'Caneta',
    'preco': 5.50,
    'desc': 0.5
}
for atrib in produto:
    print(atrib,produto[atrib])
print(' ')
    
for atrib, valor in produto.items():
    print(atrib, '=>', valor)
print(' ') 
   
for valor in produto.values():
    print(valor, end=' ')
print(' ')
    
for atrib in produto.keys():
    print(atrib, end=' ')
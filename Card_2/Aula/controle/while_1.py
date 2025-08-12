#Os dois primeiros exemplos representam o uso do while sem uma quantidade determinada de repetições
#x = 0

#while x != -1:
#    x = float(input('Informe um número ou -1 para sair: '))

#print('Fim')

#total = 0.0
#qtde = 0
#nota = 0
#while nota != -1:
#    nota = float(input('Informa a nota ou -1 para sair: '))
#    if nota != -1:
#        qtde += 1
#        total += nota       
#print(f'A média da turma é {total/qtde}')    

#While com quantidade determinada de repetições, seria melhor usar o FOR... o While é melhor para usar quando a quantidade foi indetermianda mesmo, como nos exemplos acima
x = 10
while x:
    print(x)
    x -= 1
print('Fim!')
a = 7
b = 3.1

print(a+b)

texto = 'Sua idade é...'
idade = 23

#print(texto+str(idade))
print(f'{texto} {12+3}')

saudacao = 'bom dia'
print(3* saudacao)

PI = 3.1415
raio = float(input('Informa o raio da circ? '))
area = PI * raio *raio #aqui temos o mesmo que raio², então posso utilizar a função de potência, que seria, neste exemplo area = PI * pow(raio, 2)

print(f'A área da circ é {area} m²')
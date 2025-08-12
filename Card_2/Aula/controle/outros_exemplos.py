#Um FOR dentro de outro FOR
pessoas = ['Ana', 'Gui']
adj = ['Legal', 'Inteligente']

for p in pessoas:
    for a in adj:
        print(f'{p} é {a}!')

#Laço vazio
for i in [1, 2,3]:
    pass

#Continue
for i in range(1, 11):
    if i % 2:
        continue
    print(i, end=' ')        

#Break
for i in range(1,11):
    if i == 5:
        break
    print(i)

print('FIM!')

lockdown = False
grana = 30

status = 'Em casa' if lockdown or grana <= 5 else 'Uhuuuu'

print(f'O sastus é: {status}')

#é ternario porque tem a parte verdadeira, a parte de IF e a parte de ELSE
from functools import reduce

alunos = [
    {'nome': 'Ana', 'nota': 7.2},
    {'nome': 'Lucas', 'nota': 8.1},
    {'nome': 'Claudio', 'nota': 9},
    {'nome': 'Pedro', 'nota': 6.4},
    {'nome': 'Rafaela', 'nota': 6.7},
]

aluno_aprovado = lambda aluno: aluno['nota'] >= 7
#aluno_honra = lambda aluno: aluno['nota'] >= 9
obter_nota = lambda aluno: aluno['nota']
somar = lambda a, b: a+b

alunos_aprovados = filter(aluno_aprovado, alunos)
notas_alunos_aprovados = map(obter_nota, alunos_aprovados)
#alunos_honra = filter(aluno_honra, alunos)
total = reduce(somar, notas_alunos_aprovados, 0)

print(list(alunos_aprovados))
#print(list(alunos_honra))
print(alunos)
print(obter_nota(alunos[2]))
print(list(notas_alunos_aprovados))
print(total)


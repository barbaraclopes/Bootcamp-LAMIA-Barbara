#definindo funções
#pass definem funções vazias, sem parâmetros
#def saudacao(nome = 'pessoa'):
#    print(f'Bom dia {nome}!')
 
#definindo parâmetros   
def saudacao(nome = 'pessoa', idade = 25):
    print(f'Bom dia {nome}! \nVocê nem parece ter {idade} anos...')
    
#Posso definir a função neste arquivo e ao chamá-la, eu posso atribuir valores, especificações...então eu posso chamar as funções de formas diferentes.
#Não possso ter funções com o mesmo nome em um main space, porque não se sobrecarregam...

#eu posso definir que este arquivo seja o meu inicializador, fazendo com que esse código seja executado como o start da minha execução

#a variável A, tanto aqui quanto no main não tem problema porque dentro de def ela corresponde à uma e em main é outra
def soma_e_multiplicacao(a, b, x):
    return a + b * x

if __name__=='__main__':
    saudacao('Ana', idade = 18)
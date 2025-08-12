nums = [1,2,3] #lista
print(type(nums)) #imprime o tipo, no caso, lista

nums.append(3) #adiciona mais um elemento na lista
nums.append(4) #o número indica na verdade a posição do elemento, mas se eu não atribuo um valor, é o que aparece no meu print
nums.append(500)
print(len(nums)) #quantidade de elementos na minha lista

nums[3] = 100 #atribui um valor diferente, ou substitui no meu padrão de lista, então na posição 3, eu coloquei o número 100
nums.insert(0, -200) #outra forma de inserir um valor à uma posição

print(nums[6]) #pegar o último elemento da lista quando sei em qual posição ele está
print(nums[-1]) #pegar o último elemento da lista quando não sei a posição
print(nums[-2]) #pegar o penúltimo

print(nums)

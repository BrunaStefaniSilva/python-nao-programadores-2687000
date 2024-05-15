# Crie uma lista apenas com elementos numéricos
idade = [25, 30, 35, 40]
# Crie uma lista contendo todos os tipos e estrutura de dados que você aprendeu até agora
pessoa = ['python,' 'julia,' 'r,'], True, ['sara,' 'fortron,' 'java'], False
# Imprima na tela apenas os 5 primeiros elementos da lista
print(pessoa[:5])
# Crie um slice na lista para que imprima na tela os elementos de índice par
elementos_indice_par = pessoa[::2]
print(elementos_indice_par)
# Remova da lista o último item
pessoa.pop()
print(pessoa)
# Insira na lista um novo item
pessoa.append('c++')
print(pessoa)
# Remova da lista um item específico
pessoa.remove('julia')
print(pessoa)
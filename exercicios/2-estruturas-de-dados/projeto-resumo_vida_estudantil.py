# Nesse exercício coletaremos dados de uma estudante, armazenaremos em um dicionário e imprimiremos na tela esse dados em um formato amigável.

# 1. Solicite a estudante os seguintes dados: nome, ano que conheceu o LinkedIn, ano atual e os cursos realizados no LinkedIn Learning separados por virgula em ordem cronológica
estudante = {}
estudante ['nome'] = input ('Qual é o seu nome?') 
estudante['ano_conheceu_LinkedIn'] = int(input('Em qual ano você conheceu o LinkedIn?'))
estudante ['ano_atual'] = int(input('Qual é o ano atual?'))
cursos = input('Quais os cursos você já fez no LinkedIn Learning? (separe-os com vírgula)')

estudante['cursos'] = cursos.split (', ')
# 2. Armazene esses dados em um dicionário

# 3. Imprima na tela uma string com as informações de nome, ano_conheceu_linkedin, total de anos transcurridos, total de cursos realizados e (apenas) o primeiro e último curso.

total_anos = estudante['ano_atual'] - estudante['ano_conheceu_LinkedIn']
total_cursos = len(estudante['cursos'])

print(f"Oi {estudante['nome']}, desde {estudante['ano_conheceu_LinkedIn']} você conhece o LinkedIn. Nesses {total_anos} anos, você realizou {total_cursos} cursos, sendo o primeiro curso {estudante['cursos']} e o último curso {estudante['cursos']}")
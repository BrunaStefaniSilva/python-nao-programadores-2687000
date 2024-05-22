# Declare 4 variáveis do tipo numérica
x = 10
y = 2
a = 5
b = 15

# Crie uma estrutura condicional para comparar dois números

if x > a:
  print(True)
else:
  print(False)
    
# Se a condição for verdadeira, imprima na tela uma mensagem informando que a condição foi cumprida e informando o número de maior valor
  print(f'A condição foi cumprida. O número {x} é maior do que {a}')

# Se a condição não for cumprida, imprima na tela uma mensagem informando que a condição é negativa e informe o número de maior valor
if x > b:
  print(f'A condição foi comprida. O numero {x} é maior que {b}')
else:
  print(f'A condição não foi cumprida. Na verdade o numero {b} é maior do que {x}')
# Insira outras condições na estrutura condicional usando o elif
if x > b:
  print(f'A condição foi cumprida. O número {x} é maior do que {b}')
elif x > y:
  print(f'Nesse caso verificamos que {x} é maior do que {y}')
# Incremente a estrutura condicional já existente com expressões lógicas utilizando "and" ou "or"
if (x > y) or (x > a):
  print(f'A condição foi cumprida. O numero {x} é maior que {y} ou maior do que {a}')
elif (x == a) and (b > x):
  print('Nesse caso, verificamos que o numero {x} é igual a {a} e {b} é maior que {x}')

# Crie uma estrutura condicional onde mais de uma condição seja verdadeira, e use apenas a palavra reservada "if"
if x > a:
  print(f'A condição foi cumprida. O numero {x} é maior que {a}')
if y < b:
  print (f'Essa condição também é verdadeira, pois o numero {y} é mesmo menor que {b}')

'''
-Relsova com lista
- Desenvolva um programa que calcule a média aritmética de uma turma, onde cada aluno realizou um avaliação. 
Não sabemos a quantidade de alunos, por isso usaremos o valor "-1" como condição (flag) de saída. Na tela
de saída, mostre a média aritmética da turma e a quantidade de alunos da turma. Sempre que tivermos uma divisão,
temos que verificar se o divisor é diferente de zero.
'''

l_notas = []                               # Cria uma lista vazia
print('Digite[-1] para sair')
while True: 
    nota = float(input('Nota do aluno: ')) # Loop (laço) de repetição while. repete enquanto condição verdadeira
    if nota == -1:
        break             # Sai de uma estrutura
    l_notas.append(nota)  # Armazena o valor no final da lista
qtd_alunos = len(l_notas) # Quantidade de elementos na lista
soma_notas = sum(l_notas)
media = soma_notas/qtd_alunos
print('Quantidade de alunos:', qtd_alunos)
--

# FT 9:30/9:40
l_pares = []
l_impares = []
print('Digite [-1] para sair.')
while True:
    num = int(input('Valor: '))
    if num == -1:
        break
    if num % 2 == 0: # Número par
        l_pares.append(num)
    else:
        l_impares.append(num)

qtd_par = len(l_pares) # len faz o contador automático, já calcula q quantidade
if qtd_par > 0:
    soma_par = sum(l_pares)  # sum faz a soma
    media_par = soma_par/qtd_par 
    print('Média dos pares:', media_par)
else:
    print('Não tem número par.')

qtd_impar = len(l_impares)
if qtd_impar > 0:
    soma_impar = sum(l_impares)
    media_impar = soma_impar/qtd_impar 
    print('Média dos ímpares:', media_impar) # OU print('Média dos impares: %.2f' % media_impar) -> com dua casas decimais
else:
    print('Não tem número ímpar.')
--

# FT: 10:25/10:37
lista = list() # OU lista = []
print('Digite [-1] para sair')
while True:
    num = int(input('Valor inteiro: '))
    if num == -1:
        break
    lista.append(num)  # Armazena o valor final da lista, conforme vai lendo nesse caso
menor = min(lista)
maior = max(lista)
print('Menor:', menor)
print('Maior:', maior)


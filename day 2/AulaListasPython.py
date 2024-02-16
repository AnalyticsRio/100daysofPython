'''
#Listas
    # Armazenar mais de uma informação em variáveis
    # Manter a sequência dos dados em uma variável

cidade1 = 'Rio de Janeiro'
cidade2 = 'São Paulo'
cidade3 = 'Salvador'

cidades = ['Rio de janeiro', 'São Paulo', 'Salvador', 'Goiânia']

#cidades.append('Santa Catarina') >> acrescenta novo parâmetro na lista
#cidades.remove('Salvador') >> remove o parâmetro da lista
#cidades.insert(1, 'Santa Catarina') >> acrescenta novo parâmetro da lista através do index
#cidades.pop(0) >> remove o parâmetro da lista através do index
#cidades.sort() >> organiza a lista em ordem alfabética

print(cidades)

#Programas para o usuário interagir 

##Exemplo1

cor_cliente = input('Digite a cor desejada: ')
cores = ['amarelo', 'verde', 'azul', 'vermelho']

if cor_cliente in cores:
    print('Em estoque')
else:
    print('Não temos no estoque')

##Exemplo2

numero_camisa = input('Digite o número desejado: ')
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

if numero_camisa in str(numeros):
    print('Número escolhido corretamente!')
else:
    print('Esse número não é permitido, escolha um de 1 a 11!')


#Agregando duas listas (Ex1 com o Ex2) com zip:

cores = ['amarelo', 'verde', 'azul', 'vermelho']
numeros = [1, 2, 3, 4]

duas_listas = zip(cores, numeros)

print(list(duas_listas))

# Criar uma lista a partir do input do usuário:

itens_usuario = input('Digite o nome dos itens separados por virgula: ')

itens_lista = itens_usuario.split(', ')

print(itens_lista)
'''
# # Criando um dicionário vazio
# dicionario_vazio = {}

# # Criando um dicionário com elementos
# aluno = {"nome": "Alice", "idade": 20, "curso": "Ciências da Computação"}

# # Acessando elementos do dicionário
# print(aluno["nome"])    # imprime "Alice"
# print(aluno["idade"])   # imprime 20

# # Modificando elementos do dicionário
# aluno["idade"] = 21
# print(aluno)            # imprime {"nome": "Alice", "idade": 21, "curso": "Ciências da Computação"}

# a = "Adicionar Valor"
# b = "Sair"
# c = "Mostrar Dicionário"

# dicionario_vazio = {}
# contador = 1

# while True:
#     print(f"1 - {a}")
#     print(f"2 - {b}")
#     print(f"3 - {c}")
#     opcao = int(input("Digite a opção desejada: "))

#     if opcao == 1:
#         pessoa = {}
#         pessoa["Nome"] = input("Digite seu nome: ")
#         pessoa["Idade"] = input("Digite sua idade: ")
#         pessoa["Salario"] = input("Digite seu salario: ")

#         dicionario_vazio[f"Pessoa {contador}"] = pessoa
#         contador += 1
#         print("Informações adicionadas com sucesso!")
#     elif opcao == 2:
#         break
#     elif opcao == 3:
#         print(dicionario_vazio)
#     else:
#         print("Opção inválida")

#-----------ALGUNS EXEMPLOS DE LOOP COM WHILE PARA ESTUDAR-------------------------------------

#----------------------------------------------
# contador = 1

# while contador <= 5:
#     print("Número: ", contador)
#     contador += 1
#----------------------------------------------
# contador = 5

# while contador > 0:
#     print("Contagem", contador)
#     contador -= 1
# print("Fogo!")
#---------------------------------------------
# while True:
#     resposta = input("Digite 'sair' para encerrar: ")
#     if resposta.lower() == 'sair':
#         print("Encerrando...")
#         break
    # A função .lower() serve para converter as Strings maiusculas em minusculas para não dá erro na hora que o usuário inserir os dados masiusculos ou misturando ambos.
#----------------------------------------------
# senha_correta = "12345"
# tentativa = ""

# while tentativa != senha_correta:
#     tentativa = input("Digute a senha: ")
#     if tentativa == senha_correta:
#         print("Acesso permitido!")
#     else:
#         print("Acesso negado!")
#------------------------------------------------
# import random

# numero = 0

# while numero != 7:
#     numero = random.randint(1,10)
#     print("Número gerado: ", numero)
# print("Encontrado o número: ", numero)

# A biblioteca random serve para gerar números aleatórios de forma randomica segue exemplos de funções presentes:
# random.random(): Retorna um número de ponto flutuante aleatório entre 0.0 e 1.0
# random.randint(a, b): Retorna um número inteiro aleatório entre a e b (inclusive)
# random.uniform(a, b): Retorna um número de ponto flutuante aleatório entre a e b

# random.choice(sequencia): Seleciona aleatoriamente um elemento de uma sequência (lista, tupla, string)
# random.choices(sequencia, k=1): Seleciona k elementos da sequência com reposição (pode repetir elementos)
# random.sample(sequencia, k): Seleciona k elementos da sequência sem reposição (elementos únicos
# random.shuffle(lista): Embaralha os elementos de uma lista in-place (modifica a lista original)
#------------------------------------------------
# soma = 0

# while True:
#     numero = int(input("Digite um número (0 para sair:): "))
#     if numero == 0:
#         break
#     soma += numero
# print("Soma total é: ", soma)
#-----------------------------------------------
# nomes = ["Ualeson", "Natalia", "Edson", "Uilson", "Mamal"]
# indice = 0

# while indice < len(nomes):
#     print("Nome: ", nomes[indice])
#     indice += 1
# A variavel nomes está recebendo uma lista e já com valores atribuidos, podemos identificar pela abertura e fechamento dos [], no while utilizamos a função len() da lista para pegar o indice dela que começa com zero e atraves do loop passamos por todos os indices e mostrando no print para o usuário
#-------------------------------------------------
# numero = 2

# while numero <= 10:
#     print("Par: ", numero)
#     numero += 2
#--------------------------------------------------
# saldo = 1000
# while saldo > 0:
#     saque = float(input(f"Seu saldo é: {saldo}. Quando deseja sacar: "))
#     if saque > saldo:
#         print("Saldo insuficiente!")
#     else:
#         saldo -= saque
#         print(f"Saque efetuado com sucesso! Saldo restante: R${saldo}")
# print("Saldo zerado! Operações encerradas.")
#-------------------------------------------------
#Usando while com else
# contador = 1
# while contador <= 5000:
#     print("Executando:", contador)
#     contador += 1
# else:
#     print("Loop finalizado com sucesso!")
#-------------------------------------------------
# import time

# iniciar_time = time.time()

# contador = 1
# while contador <= 50000:
#     print("Executando:", contador)
#     contador += 1
# else:
#     print("Loop finalizado com sucesso!")

# final_time = time.time()

# duracao_time = final_time - iniciar_time

# print(f"O loop durou {duracao_time:.2f} segundos")
#-------------------------------------------------
# import datetime

# horario = datetime.datetime.now()
#print(horario)
# print("Horário de início: ", horario.strftime("%H:%M"), "Data: ", horario.strftime("%d/%m/%Y"))
#DateTime.now() é uma função que retorna a data e hora atual do sistema, e o strftime() é uma função que formata a data e hora de acordo com o formato especificado.
#-------------------------------------------------
# nomes = ["Ualeson", "Natalia", "Edson", "Uilson", "Mamal"]
# for nome in nomes:
#     print("Nome: ", nome)
# O for é um loop que percorre uma sequência de elementos (lista, tupla, string, etc.) e executa um bloco de código para cada elemento. No exemplo acima, a variável nome recebe cada elemento da lista nomes e imprime na tela.
#-------------------------------------------------
# for cont in range(10,0,-1):
#     print(cont)
# print("Fogo!")
#O range() é uma função que gera uma sequência de números, e é muito utilizada em loops for. O range() aceita até três argumentos: início, fim e passo. No exemplo acima, o loop for percorre a sequência de 10 a 1, com passo -1, ou seja, decrementando de 1 em 1.
#-------------------------------------------------
# palavra = "Estude Python!"

# for letra in palavra:
#     print(letra)
    #O loop for também pode ser utilizado para percorrer os caracteres de uma string. No exemplo acima, a variável letra recebe cada caractere da string palavra e imprime na tela.
#-------------------------------------------------
# for numero in range(2,11,2):
#     print("Par: ", numero)
#O loop for também pode ser utilizado para percorrer uma sequência de números. No exemplo acima, o loop for percorre a sequência de 2 a 10, com passo 2, ou seja, incrementando de 2 em 2.
#-------------------------------------------------
# numeros = [10, 20, 30, 40, 50]
# soma = 0

# for num in numeros:
#     soma += num
# print("Soma total: ", soma)
#O loop for também pode ser utilizado para percorrer os elementos de uma lista. No exemplo acima, a variável num recebe cada elemento da lista numeros e soma os valores.
#-------------------------------------------------
# dados = {
#     "Nome": "Ualeson",
#     "Idade": 35,
#     "Cidade": "Salvador"
# }

# for chave, valor in dados.items():
#     print(f"{chave}: {valor}")
#O loop for também pode ser utilizado para percorrer os itens de um dicionário. No exemplo acima, a variável chave recebe a chave e a variável valor recebe o valor de cada item do dicionário dados, e imprime na tela.
#-------------------------------------------------
# numeros = [1,2,3,4,5]

# dobrados = [num * 2 for num in numeros]
# print("Os números dobrados são: ", dobrados)
#A compreensão de listas (list comprehension) é uma forma concisa de criar listas em Python. No exemplo acima, a lista dobrados é criada a partir da lista numeros, onde cada elemento é dobrado (multiplicado por 2) utilizando a sintaxe [num * 2 for num in numeros].
#-------------------------------------------------
# numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# pares = [num for num in numeros if num % 2 == 0]
# print("Números pares:", pares)
#A compreensão de listas (list comprehension) também pode ser utilizada com condicionais. No exemplo acima, a lista pares é criada a partir da lista numeros, onde cada elemento é verificado se é par (num % 2 == 0) e adicionado à lista pares.
#-------------------------------------------------
# matriz = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]

# for linha in matriz:
#     for elemento in linha:
#         print(elemento, end=" ")
#     print()
#A compreensão de listas (list comprehension) também pode ser utilizada com listas aninhadas, como uma matriz. No exemplo acima, a matriz é percorrida utilizando dois loops for, onde o primeiro loop percorre as linhas e o segundo loop percorre os elementos de cada linha, imprimindo na tela.
#-------------------------------------------------
# num = 5
# for i in range(1, 11):
#     print(f"{num} x {i} = {num * i}")
#O loop for também pode ser utilizado para criar tabuadas. No exemplo acima, o loop for percorre a sequência de 1 a 10, e imprime a tabuada do número 5.
#-------------------------------------------------
# nomes = ["Ana", "Carlos", "Maria", "João"]
# for indice, nome in enumerate(nomes):
#     print(f"Índice {indice}: {nome}")
#O loop for também pode ser utilizado com a função enumerate() para obter o índice e o valor de uma lista. No exemplo acima, a função enumerate() retorna o índice e o nome de cada elemento da lista nomes, e imprime na tela.
#-------------------------------------------------
# nomes = ["Ana", "Carlos", "Maria"]
# idades = [25, 30, 22]

# for nome, idade in zip(nomes, idades):
#     print(f"{nome} tem {idade} anos.")
#O loop for também pode ser utilizado com a função zip() para combinar duas listas. No exemplo acima, a função zip() combina os elementos das listas nomes e idades, e imprime na tela o nome e a idade correspondente.
#-------------------------------------------------
# numeros = [10, 20, 30, 40, 50]
# for num in numeros:
#     if num == 40:
#         print("Número encontrado! Parando...")
#         break
#     print(num)
#O comando break é utilizado para interromper a execução de um loop for. No exemplo acima, o loop for percorre a lista numeros, e ao encontrar o número 40, o loop é interrompido com o comando break.
#-------------------------------------------------
# for i in range(1, 6):
#     if i == 3:
#         continue  # Pula o número 3
#     print(i)
#O comando continue é utilizado para pular a iteração atual de um loop for e continuar para a próxima iteração. No exemplo acima, o loop for percorre a sequência de 1 a 5, e ao encontrar o número 3, a iteração é pulada com o comando continue.
#-------------------------------------------------

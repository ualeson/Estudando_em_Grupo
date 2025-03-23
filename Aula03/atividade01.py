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


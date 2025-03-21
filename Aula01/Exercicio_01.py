#print("Hello World")

#mensagem = "Hello World"
#print(mensagem)


# nome = 'Ualeson'
# idade = 35
# altura = 1.75

# print("O nome é:" + nome + "a idade é:" + str(idade) + " anos"+ "e sua altura é:" + str(altura))

# toString(variavel) conversão no java
# str(variavel) conversão no python

# nome = input("Digite seu nome:")
# idade = int(input("Digite sua idade:"))
# altura = input("Digite sua altura:")

# dezanos = idade + idade

# print(dezanos)

#print("O nome é:" + nome + "a idade em 10 anos é:" + str(dezanos) + " anos"+ "e sua altura #é:" + altura)

# num1 = int(input("Digite o primeiro número:"))
# num2 = int(input("Digite o segundo número:"))
# num3 = int(input("Digite o terceiro número:"))
# num4 = int(input("Digite o quarto número:"))

# soma = num1 + num2 + num3 + num4
# media = soma / 4

# print("A média dos números é:" + str(media))

#import math

#raio = float(input("Digite o raio do círculo: "))
#area = math.pi * raio**2
#print("A área do círculo é", area)

# cigarros = int(input("Quantos cigarros você fuma por dia? "))
# anos = int(input("Há quantos anos você fuma? "))
# total_cigarros = anos * 365 * cigarros
# dias_perdidos = total_cigarros / 1440

# print("Você perdeu", dias_perdidos, "dias de vida")

# Solicita os dados do usuário
# cigarros_por_dia = int(input("Quantos cigarros você fuma por dia? "))
# anos_fumando = int(input("Há quantos anos você fuma? "))

# Define constantes
# MINUTOS_PERDIDOS_POR_CIGARRO = 10
# MINUTOS_POR_DIA = 1440  # 24 horas * 60 minutos

# Calcula o total de minutos perdidos
# total_cigarros = cigarros_por_dia * anos_fumando * 365
# minutos_perdidos = total_cigarros * MINUTOS_PERDIDOS_POR_CIGARRO

# Converte minutos para dias
# dias_perdidos = minutos_perdidos / MINUTOS_POR_DIA

# Exibe o resultado
# print(f"Você perdeu aproximadamente {dias_perdidos:.2f} dias de vida devido ao cigarro.")

#import math

#raio = float(input("Digite o raio do círculo: "))
#area = math.pi * raio**2
#print("A área do círculo é", area)
#print(math.pi)




#numero_inteiro = int(input("Digite um número inteiro: "))
#numero_inteiro2 = input("Digite outro número inteiro: ")

#print(f"Você inseriu um número inteiro e o valor digitado foi:{numero_inteiro}")




#Exibir de 1 a 10 na tela usando estrutura de repetição for
# for cont in range(1,11):
#     print(cont)
#
#     if cont % 2 == 0:
#         print("Número par")
#     else:
#         print("Número ímpar")

# numero =  int(input("Digite um número: "))  

# if numero % 2 == 0:
#     print("Número par")
# else:
#     print("Número ímpar")


# cont = 0

# while cont <= 10:

#     if cont % 2 == 0:
#         print(cont)
#     else:
#         print("Número ímpar")
#     cont += 1


# crie um script que irá solicitar ao  usuários dados de funcionários, mas você poderar cadastrar mais de uma informação ao mesmo tempo, de acordo com a necessidade (utilize somente o terminal)
    
# quantidade = int(input("Digite a quantidade de funcionários: "))

# nome = input("Digite o nome do funcionário: ")
# idade = int(input("Digite a idade do funcionário: "))
# salario = float(input("Digite o salário do funcionário: "))


# quantidade = int(input("Digite a quantidade de cadastros: ")) 

# for cont in range(0,quantidade):
#     nome = input("Digite o nome do funcionário: ")
#     idade = int(input("Digite a idade do funcionário: "))
#     salario = float(input("Digite o salário do funcionário: "))

    

#     print(f"O nome é: {nome}" " a idade é: ", idade , "e o salario: ", salario)


# lista_nomes = []
# lista_idade = []
# lista_salario = []

# quantidade = int(input("Digite a quantidade de dados para inserir na lista:"))

# for cont in range(quantidade):
#   preencher_nomes = input("Digite os nomes da lista:")
#   lista_nomes.append(preencher_nomes)

#   preencher_idade = input("Digite as idade da lista:")
#   lista_idade.append(preencher_idade)

#   preencher_salario = input("Digite os salarios da lista:")
#   lista_salario.append(preencher_salario)

# print(lista_nomes)
# print(lista_idade)
# print(lista_salario)


# lista_dados = []

# quantidade = int(input("Digite a quantidade de dados para inserir na lista:"))

# for cont in range(quantidade):
#   preencher_nome = input("Digite o nome: ")
#   preencher_idade = input("Digite a idade")
#   preencher_salario = input("Digite o salario:")

#   lista_dados.append(preencher_nome)
#   lista_dados.append(preencher_idade)
#   lista_dados.append(preencher_salario)


# print(lista_dados)

#@title Aula de Python: Part 2

# dicionario = {}  # Criar um dicionário vazio

# quantidade = int(input("Digite a quantidade de elementos a serem adicionados: "))

# for contador in range(quantidade):
#     chave = input("Digite a chave: ")
#     valor = input("Digite o valor: ")
#     dicionario[chave] = valor  # Adicionar a chave e valor ao dicionário

# print("O dicionário final é:", dicionario)

# print(dicionario.keys())
# print(dicionario.values())
# print(dicionario.items())
# print(dicionario.get("Nome"),dicionario.get("Idade") )
# print(dicionario.clear())
# print(dicionario)
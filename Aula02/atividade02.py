#Estrutura condicional (if/else)

# idade = int(input("Digite a sua idade: "))

# if idade >= 18:
#     print("Você é maior de idade!")
# else:
#     print("Você é menor de idade!")


# Solicitar ao usuário que digite 2 números em seguida verificar se o número 1 é maior que o número 2, se o número 2 é maior que o número ou se os números são iguais.


# numero1 = float(input("Digite o primeiro número: "))
# numero2 = float(input("Digite o segundo número: "))

# if numero1 > 0 and numero2 > 0:
#     print("Os dois números são positivos")
# elif numero1 < 0 and numero2 < 0:
#     print("Os dois números são negativos")
# elif numero1 < 0 and numero2 > 0:
#     print("O numero 1 é negativo e o número 2 é positivo")
# elif numero1 > 0 and numero2 < 0:
#     print("O numero 1 é positivo e o número 2 é negativo")
# elif numero1 == 0 and numero2 > 0:
#     print("Numero 1 é zero e número 2 é positivo")
# elif numero1 == 0 and numero2 < 0:
#     print("Numero 1 é zero e número 2 é negatiivo")
# elif numero2 == 0 and numero1 > 0:
#     print("Numero 2 é zero e número 1 é positivo!")
# elif numero2 == 0 and numero1 < 0:
#     print("Numero 2 é zero e número 1 é negatiivo!")
# else:
#     print("Os dois números são zeros!")



# if numero %2 == 0:
#     print("O número é par!")
# else:
    # print("O número é ímpar!")

# if numero > 0:
#     print("O número é positivo!")
# elif numero < 0:
#     print("O número é negativo")
# else:
#     print("O número é zero")


# for cont in range(1,6):
#     print(cont)

# cont = 0
# while cont < 11:
#     print(cont)
#     cont += 3

# numero = int(input("Digite o número: "))

# for cont in range (1, 11):
#     resultado = numero * cont
#     print(numero, "X", cont, "=", resultado)

# lista_nomes = []

# quantidade = int(input("Digite a quantidade de dados que vai enviar para a lista: "))

# for cont in range(quantidade):
#     prencher_lista = input(f"Digite o nome do funcionário {cont+1}: ")
#     lista_nomes.append(prencher_lista)

# print(lista_nomes)

# lista_nomes = []

# prencher_lista = input("Digite o nome do funcionário: ")
# lista_nomes.append(prencher_lista)

# print(lista_nomes)

# lista_nomes.clear()

# print(lista_nomes)

#------------------------------------------------------------

SENHA = "U@l3$0n"

valor = input("Digite a senha: ")

# while True:
#     if valor == SENHA:
#         print("Senha correta !")
#         break
#     else:
#         print("Senha incorreta !")
#         valor = input("Digite a senha: ")
#         continue

# Versão realizada pela IA (GTP4)
while SENHA != valor:
     print("Senha invalida !")
     valor = input("Digite a senha: ")

SENHA = 12345


print("Senha correta!", "A nova senha é:", SENHA)

#--------------------------------------------------------------

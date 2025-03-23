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
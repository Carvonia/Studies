# Por: Matheus Cunha Nogueira - 06004493

# Exercício 1:
for numero in range(10, 201, 2):
    print(numero)

# Exercício 2:
import random

numero_maior = 0
for _ in range(100):
    numero_aleatorio = random.randint(1, 1000)
    if numero_aleatorio > numero_maior:
        numero_maior = numero_aleatorio

print("O maior valor entre os 100 números sorteados é:", numero_maior)

# Exercício 3:
import random

for _ in range(50):
    numero_aleatorio = random.randint(1, 100)
    print(numero_aleatorio)

# Exercício 4:
num_pessoas = int(input("Quantas pessoas no grupo? "))
soma_idades = 0
maior_idade = -1
menor_idade = float('inf')
contagem_maiores_idade = 0

for i in range(num_pessoas):
    idade = int(input(f"Digite a idade da pessoa {i + 1}: "))
    soma_idades += idade
    if idade > maior_idade:
        maior_idade = idade
    if idade < menor_idade:
        menor_idade = idade
    if idade >= 18:
        contagem_maiores_idade += 1
media_idades = soma_idades / num_pessoas

print(f"Média das idades: {media_idades:.2f}")
print(f"Maior idade: {maior_idade}")
print(f"Menor idade: {menor_idade}")
print(f"Pessoas maiores de idade: {contagem_maiores_idade}")

# Exercício 5:
import random

numero_sorteado = random.randint(1, 100)
tentativas = 0

print("Esse é um jogo de adivinhação. Tente achar o valor de 1 a 100")
while tentativas < 10:
    tentativa = int(input("Tentativa {}/10: Digite um número: ".format(tentativas + 1)))

    if tentativa == numero_sorteado:
        print("Parabéns! Você adivinhou o número em {} tentativas.".format(tentativas + 1))
        break
    elif tentativa < numero_sorteado:
        print("Tente novamente. O número é maior.")
    else:
        print("Tente novamente. O número é menor.")

    tentativas += 1

if tentativas == 10:
    print("Você esgotou todas as tentativas")

# Exercício 6
soma_idade_homens = 0
soma_idade_mulheres = 0
casais_menos_de_2_anos = 0
total_casais = 2500

for _ in range(total_casais):
    idade_namorado = int(input("Digite a idade do namorado: "))
    idade_namorada = int(input("Digite a idade da namorada: "))
    tempo_de_namoro = int(input("Digite o tempo de namoro (em anos): "))

    soma_idade_homens += idade_namorado
    soma_idade_mulheres += idade_namorada

    if tempo_de_namoro < 2:
        casais_menos_de_2_anos += 1

media_idade_homens = soma_idade_homens / total_casais
media_idade_mulheres = soma_idade_mulheres / total_casais

print("Média de idade entre os homens:", media_idade_homens)
print("Média de idade entre as mulheres:", media_idade_mulheres)
print("Quantidade de casais com menos de 2 anos de namoro:", casais_menos_de_2_anos)

# Exercício 7
total_ingressos_disponiveis = 0
total_ingressos_vendidos = 0
total_jogos_90porcent_vendido = 0
total_jogos = 4

for jogo in range(1, total_jogos + 1):
    ingressos_disponiveis = int(input(f"Digite o total de ingressos disponíveis para o jogo {jogo}: "))
    ingressos_vendidos = int(input(f"Digite o total de ingressos vendidos para o jogo {jogo}: "))

    total_ingressos_disponiveis += ingressos_disponiveis
    total_ingressos_vendidos += ingressos_vendidos

    if ingressos_vendidos >= 0.9 * ingressos_disponiveis:
        total_jogos_90porcent_vendido += 1

total_ingressos_nao_vendidos = total_ingressos_disponiveis - total_ingressos_vendidos

print("Total de ingressos disponíveis na Copa:", total_ingressos_disponiveis)
print("Total de ingressos vendidos na Copa:", total_ingressos_vendidos)
print("Total de ingressos não vendidos na Copa:", total_ingressos_nao_vendidos)
print("Total de jogos com mais de 90% dos ingressos vendidos:", total_jogos_90porcent_vendido)

# Exercício 8
vendas_tipo_1 = 0
vendas_tipo_2 = 0
vendas_tipo_3 = 0
valor_vendas_tipo_1 = 0
valor_vendas_tipo_2 = 0
valor_vendas_tipo_3 = 0
valor_total_vendido = 0
maior_venda = 0

for _ in range(1000):
    tipo_produto = int(input("Digite o tipo de produto (1, 2 ou 3): "))
    valor_venda = float(input("Digite o valor da venda: "))

    if tipo_produto == 1:
        vendas_tipo_1 += 1
        valor_vendas_tipo_1 += valor_venda
    elif tipo_produto == 2:
        vendas_tipo_2 += 1
        valor_vendas_tipo_2 += valor_venda
    elif tipo_produto == 3:
        vendas_tipo_3 += 1
        valor_vendas_tipo_3 += valor_venda

    valor_total_vendido += valor_venda

    if valor_venda > maior_venda:
        maior_venda = valor_venda

print("Quantidade de vendas de tipo 1:", vendas_tipo_1)
print("Quantidade de vendas de tipo 2:", vendas_tipo_2)
print("Quantidade de vendas de tipo 3:", vendas_tipo_3)
print("Valor vendido de tipo 1:", valor_vendas_tipo_1)
print("Valor vendido de tipo 2:", valor_vendas_tipo_2)
print("Valor vendido de tipo 3:", valor_vendas_tipo_3)
print("Valor total vendido na loja:", valor_total_vendido)
print("Valor da maior venda:", maior_venda)

# Exercício 9
quantidade_trabalho = 0
valor_trabalho = 0
quantidade_heranca = 0
valor_heranca = 0
quantidade_sorte = 0
valor_sorte = 0
valor_total_fortunas = 0
maior_fortuna = 0

for _ in range(3):
    valor_fortuna = float(input("Digite o valor da fortuna: "))
    origem_fortuna = input("Digite a origem da fortuna (trabalho, herança ou sorte): ").lower()

    if origem_fortuna == "trabalho":
        quantidade_trabalho += 1
        valor_trabalho += valor_fortuna
    elif origem_fortuna == "herança":
        quantidade_heranca += 1
        valor_heranca += valor_fortuna
    elif origem_fortuna == "sorte":
        quantidade_sorte += 1
        valor_sorte += valor_fortuna

    valor_total_fortunas += valor_fortuna

    if valor_fortuna > maior_fortuna:
        maior_fortuna = valor_fortuna

print("Quantidade de fortunas conseguidas com trabalho:", quantidade_trabalho)
print("Valor das fortunas conseguidas com trabalho:", valor_trabalho)
print("Quantidade de fortunas conseguidas com herança:", quantidade_heranca)
print("Valor das fortunas conseguidas com herança:", valor_heranca)
print("Quantidade de fortunas conseguidas com sorte:", quantidade_sorte)
print("Valor das fortunas conseguidas com sorte:", valor_sorte)
print("Valor total da soma das 2000 fortunas:", valor_total_fortunas)
print("Valor da maior fortuna:", maior_fortuna)
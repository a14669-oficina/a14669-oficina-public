print("hello world!")

valorA = float(input("Insira um valor entre 1 - 10: "));
valorB = float(input("Insira um valor entre 1 - 10: "));
soma = float(valorA + valorB);
média = (soma / 2);
print("A média é: ", média);

----------------------------------------------------------------------------------------------------------------------

#EX0.1
"""
Declara uma variável chamada "idade" e atribuiu a tua idade.
Declara uma variável chamada "nome" e atribuiu o teu nome.
Imprima no ecrã a frase "O meu nome é [nome] e tenho [idade] anos."
"""
idade = input("Insira a sua idade: ");
nome = input("Insira o seu nome: ");
print(f"O meu nome é {nome} e tenho {idade} anos.");

----------------------------------------------------------------------------------------------------------------------

#EX0.2
"""
Escreve um programa que imprima "Olá, mundo!" no ecrã.
Cria uma variável chamada "fruta" e atribuiu o nome de uma fruta.
Imprime no ecrã a frase "Eu gosto de [fruta]."
"""
print("Olá, mundo!");
fruta = "Melancia";
print(f"Eu gosto de {fruta}.");

----------------------------------------------------------------------------------------------------------------------

#EX0.3 
"""
Solicita ao utilizador para digitar o nome.
Imprime no ecrã uma saudação personalizada utilizando o nome fornecido.
Pede ao utilizador para digitar um número inteiro.
Imprime o dobro desse número.
"""
nome= input("Digite o seu nome: ");
print(f"Bem-vindo {nome}.");
numero= int(input("Insira um numero inteiro: "));
dobro= numero * 2
print(f"O dobro de {numero} é {dobro}.");

----------------------------------------------------------------------------------------------------------------------

#EX1.1
"""
Elabora um programa que imprima a mensagem “Bem-vindos ao Python!”, precedida por uma linha em branco
"""
print("\nBem-vindos ao Python!");

----------------------------------------------------------------------------------------------------------------------

#EX1.2
"""
Elabora um programa que imprima a mensagem “José, bem-vindo ao Python!”, precedida por uma linha em branco
"""
print("\nJosé, bem-vindo ao Python!");

----------------------------------------------------------------------------------------------------------------------

#EX1.3
"""
Elabora um programa que atribua a mensagem a uma variável e, em seguida, imprima o valor da variável.
"""
mensagem = "Bem-vindos ao Python!";
print(mensagem);

----------------------------------------------------------------------------------------------------------------------

#EX1.4
"""
Elabora um programa que atribua o nome, a idade e a localidade de residência do aluno a três variáveis e imprima os valores dessas variáveis.
"""
nome = "Dinis";
idade = int("14");
localidade = "Porto";
print(f"{nome}, tem {idade} anos e mora no {localidade}.");

----------------------------------------------------------------------------------------------------------------------

#EX1.5
"""
Elabora um programa que intercale a designação da linguagem de programação e o nome do aluno na mensagem
"""
linguagemProg = "Python";
nome = "Dinis";
print(f"O {nome} sabe programar em {linguagemProg}.");

----------------------------------------------------------------------------------------------------------------------

#EX1.6
"""
Elabora um programa que alinhe à direita, à esquerda e ao centro a mensagem “Bem-vindo ao Python!” num campo de edição com 50 carateres.
"""
print(f"{'Bem-Vindo ao Python' : <50}");
print(f"{'Bem-Vindo ao Python' : ^50}");
print(f"{'Bem-Vindo ao Python' : >50}");

----------------------------------------------------------------------------------------------------------------------

#EX1.7
"""
Elabora um programa que desenvolva o algoritmo de um programa que permita calcular o perímetro e área de uma circunferência a partir do valor do raio.
"""
raio = float(input("Insira o valor do raio: "));
perimetro = 2 * 3.14 * raio;
area = 3.14 * (raio ** 2);
print(f"O perímetro é {perimetro} e a área é {area}.");

----------------------------------------------------------------------------------------------------------------------

#EX1.8
"""
Elabora um programa que imprima a data e horas correntes nos seguintes formatos:
02-10-2024
02-10-2024 16:11:20
10-02-2024 16:11:20
02/10/24
16:11:20
"""
import datetime
x = datetime.datetime.now()
dia = x.strftime("%d");
mes = x.strftime("%m");
ano = x.strftime("%y");
hora = x.strftime("%H");
minutos = x.strftime("%M");
segundos = x.strftime("%S");
print(f"{dia}-{mes}-{ano}")
print(f"{dia}-{mes}-{ano} {hora}:{minutos}:{segundos}")
print(f"{mes}-{dia}-{ano} {hora}:{minutos}:{segundos}")
print(f"{dia}/{mes}/{ano}")
print(f"{hora}:{minutos}:{segundos}")

----------------------------------------------------------------------------------------------------------------------

#EX1.9
"""
Elabora um programa que leia o número mecanográfico de um atleta, assim como a sua pontuação. O número é inteiro e a pontuação final é real.
Digite o número do atleta: 12304
Digite a pontuação final: 7.89
O atleta número 12304 obteve 7.89 pontos
"""
numero = input("Insira o seu número: ")
pontuacao = input("Insira a sua pontuação: ")
print(f"O atleta número {numero} obteve {pontuacao} pontos.")

----------------------------------------------------------------------------------------------------------------------

#EX1.10
"""
Elabora um programa que leia a data de nascimento de uma pessoa e imprima a sua idade à data atual.
"""
import datetime
dtnascimento = input("Insira a data do seu nascimento: ")
day,month,year = map(int, dtnascimento.split("-"))
today = datetime.date.today()
idade = today.year - year - ((today.month, today.day) < (month, day))
print("A tua idade é",idade,"anos.")

----------------------------------------------------------------------------------------------------------------------

#EX1.11
"""
Elabora um programa que desenvolva o algoritmo de um programa que permita converter libras em euros, considerando a taxa de conversão de 1,19 ( ou seja, 1 GBP = 1,19 EURO).
"""
libras = float(input("Insira o valor em libras: "))
euros = libras * 1.19
print(f"O valor em euros é {euros}.")

----------------------------------------------------------------------------------------------------------------------

#Trabalho de Autonomia
print("hello world!")

idade = int(input("Por favor, insira sua idade: "))

if idade < 18:
    print("Você é menor de idade.")
elif idade < 60:
    print("Você é maior de idade.")
else:
    print("Você é idoso.")
print("--FIM--")

----------------------------------------------------------------------------------------------------------------------

#Trabalho de Autonomia
import random

segredo = int(random.randint(1, 10))
#print(f"O número secreto é {segredo}")

numeroescolhido = int(input("Insira um número entre (1 e 10): "))

if numeroescolhido > segredo:
    print("O número escolhido é maior que o número secreto.")
elif numeroescolhido < segredo:
  print("O número escolhido é menor do que o meu")
else:
  print("Acertaste!")

----------------------------------------------------------------------------------------------------------------------

#Trabalho de Autonomia
"""
Escreva um programa que leia a velocidade de um carro.
Se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele foi multado
A multa vai custar 7,00€ por cada km acima do limite.
"""
nint = int(input("Insira a velocidade a que se movia: "))
if nint <= 80: 
  print("Tudo ok!")
else:
  print("Você foi multado!")

----------------------------------------------------------------------------------------------------------------------

#EX FP1
"""
Verificar se um número é positivo, negativo ou zero.
Escreve um programa em Python que peça ao utilizador para introduzir um número e verifica se ele é positivo, negativo ou igual a zero.
Dica: Usa as estruturas condicionais if, elif e else.
"""
numero = float(input("Insira um número: "))
if numero == 0:
  print("O número é igual a zero.")
elif numero < 0:
    print("O número é negativo.")
else:
  print("O número é positivo.")

----------------------------------------------------------------------------------------------------------------------

#EX FP2
"""
Verificar se um número é par ou ímpar.
Escreve um programa que peça ao utilizador um número inteiro e verifica se ele é par ou ímpar.
Dica: Para verificar se um número é par, utilize a operação de módulo %.
"""
numero = int(input("Insira um número: "))
if numero % 2 == 0:
  print("O número é par")
else: 
  print("O número é impar")

----------------------------------------------------------------------------------------------------------------------

#EX FP3
"""
Calcular a nota final de um aluno.
Elabora um programa que pergunte ao utilizador a nota final de um aluno e verifica a classificação de acordo com a seguinte tabela:

Nota inferior a 10: "Reprovado"
Nota entre 10 e 14: "Suficiente"
Nota entre 15 e 17: "Bom"
Nota superior a 17: "Muito Bom"
"""
nota = int(input("Qual foi a nota final do aluno: "))
if nota < 10:
  print("Reprovado!")
elif nota >= 10 and nota <= 14:
  print("Suficiente!")
elif nota >= 15 and nota <= 17:
  print("Bom!")
else:
  print("Muito Bom!")

----------------------------------------------------------------------------------------------------------------------

#EX FP4
"""
Conversor de temperaturas.
Cria um programa que pergunte ao utilizador uma temperatura em graus Celsius e a converta para Fahrenheit, Kelvin ou ambas. O utilizador deve escolher a unidade de destino (Fahrenheit ou Kelvin), e o programa deve exibir o valor convertido
"""
Celsius = float(input("Insira a temperatura em graus Celsius: "))
Fahrenheit = (Celsius * 9/5) + 32
kelvin = Celsius + 273.15
print(f"Em graus Fahrenheit fica: {Fahrenheit} e em Kelvin fica: {kelvin}!")

----------------------------------------------------------------------------------------------------------------------

#EX FP5
"""
Cálculo de impostos
Crie um programa que peça ao utilizador o seu salário mensal e calcule o imposto de acordo com a seguinte tabela:

Salário até 1000: isento de impostos
Salário entre 1001 e 2000: 10% de imposto
Salário superior a 2000: 20% de imposto
O programa deve exibir o salário após a dedução do imposto.
"""
salario = float(input("Insira o valor do seu salário mensal: "))
if salario <= 1000:
  print("Isento de Impostos!")
elif salario > 1000 and salario < 2000:
  imposto = salario * 0.10
  salarioImposto = salario - imposto
  print(f"O seu slário mensal com imposto de 10% é de: {salarioImposto:.2f}")
elif salario >= 2000:
  imposto = salario * 0.20
  salarioImposto = salario - imposto
  print(f"O seu slário mensal com imposto de 20% é de: {salarioImposto:.2f}")

----------------------------------------------------------------------------------------------------------------------

#Ex FP6
"""
Escreve um programa em Python que use um ciclo for para imprimir todos os números de 1 a 10.
"""
for i in range(1, 11):
  print(i)

----------------------------------------------------------------------------------------------------------------------

#Ex FP7
"""
Escreve um programa que use um ciclo while para calcular a soma de todos os números de 1 a 100.
"""
soma = 0
numero = 1
while numero <= 100:
    soma += numero
    numero += 1
print(f"A soma dos números de 1 a 100 é: {soma}")

----------------------------------------------------------------------------------------------------------------------

#Ex FP8
"""
Escreve um programa que peça ao utilizador para introduzir uma frase e utilize um ciclo for para contar quantas vogais (a, e, i, o, u) existem na frase.
"""
frase = input("Insira uma frase: ")
vogais = 0
for letra in frase:
  if letra.lower() in "aeiou":
    vogais += 1
print(f"A frase tem {vogais} vogais.")

----------------------------------------------------------------------------------------------------------------------

#EX FP9
"""
Escreve um programa que utilize um ciclo for para listar todos os múltiplos de 5 entre 1 e 50.
"""
for i in range(1, 51):
  if i % 5 == 0:
    print(i)

----------------------------------------------------------------------------------------------------------------------

#EX FP10
"""
Escreve um programa que crie uma lista de 5 números inteiros, pede ao utilizador para introduzir cada número e, em seguida, calcula e exibe a média desses números.
"""
numeros = []
for i in range(5):
    numero = int(input(f"Introduza o {i + 1}º número inteiro: "))
    numeros.append(numero)
media = sum(numeros) / len(numeros)
print(f"A média dos números introduzidos é: {media:.2f}")

----------------------------------------------------------------------------------------------------------------------

#EX FP11
"""
Escreve um programa que peça ao utilizador um número inteiro e verifique se ele é primo. Um número primo é divisível apenas por 1 e por ele mesmo. O programa deve utilizar um ciclo for para testar se o número é divisível por algum outro número.
"""
numero = int(input("Insira um número: "))
divisores = 0
for i in range(1, numero + 1):
  if numero % i == 0:
    divisores += 1
if divisores == 2:
  print(f"O {numero} é um número primo")
else:
  print(f"O {numero} não é um número primo")

----------------------------------------------------------------------------------------------------------------------

#EX FP12
"""
Cria um programa que utilize a função range() e um ciclo for para gerar uma lista com todos os números pares entre 1 e 20 e imprima a lista.
"""
lista = []
for i in range(1,21):
  if i % 2==0:
    lista.append(i)
print(f"Os números pares: {lista}")

----------------------------------------------------------------------------------------------------------------------

#EX FP13
"""
Escreve um programa que peça ao utilizador para introduzir uma palavra ou frase e utilize um ciclo para imprimir a string invertida.
"""
texto = str(input("Insira um texto: "))
textoinv = texto [::-1]
print (textoinv)

----------------------------------------------------------------------------------------------------------------------

#EX FP14
"""
Escreve um programa que gere a tabuada de multiplicação de um número introduzido pelo utilizador. O programa deve utilizar um ciclo for para calcular e exibir a tabuada até 10.
"""
num = int(input("Introduza um número: "))
for i in range(1,11):
  mult = num * i
  print(f"{num} x {i} = {mult}")

----------------------------------------------------------------------------------------------------------------------


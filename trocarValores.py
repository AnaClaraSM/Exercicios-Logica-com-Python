#Programa Python para trocar valores de variáveis
#16/07/2024

print("*****************************************************")
print("                        TROCA                        ")
print("   Este programa troca os valores de 2 variáveis.    ")
print("*****************************************************")

#Declaração das variáveis para armazenar valores do usuário e exibição dos valores
valorA = input("Digite o valor A: ")
print(f"Valor A: {valorA}")
valorB = input("Digite o valor B: ")
print(f"Valor B: {valorB}")

#Troca
#A <-> B
#Variável para intermediar a troca e impedir a perda de valores
# C <- A ;   A <- B;   B <- C .
valorC = valorA # O Valor de A é armazenado na variável intermediária valorC para que não se perca
valorA = valorB # A variável valorA já pode receber o valor da variável valorB
valorB = valorC # A variável valorB recebe o valor de A, que foi previamente armazenado na variável valorC

#Exibição dos valores trocados

print("Troca: ")
print(f"Valor A: {valorA}")
print(f"Valor B: {valorB}")

print ()
print ("Fim do Programa")
print("*****************************************************")
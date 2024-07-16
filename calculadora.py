#Programa Python para calcular as 4 operações básicas com 2 números
#15/07/2024

print("Este programa calcula as 4 operações básicas com 2 números")

valor1 = float(input("Digite o primeiro numero: "))
valor2 = float(input("Digite o segundo numero: "))

soma = valor1 + valor2
subtracao = valor1 - valor2
multiplicacao = valor1 * valor2
divisao = valor1 / valor2

#Não pode usar o + nesse caso -> devido as variáveis serem numéricas?
print("A soma é ", soma)
print("A subtração é ", subtracao)
print("A multiplicação é ", multiplicacao)
print("A divisão é ", divisao)
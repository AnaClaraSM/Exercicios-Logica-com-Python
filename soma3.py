#Programa Python para somar 3 números
#15/07/2024

print("*****************************************************")
print("                       SOMADOR                       ")
print("  Este programa realiza a soma de 5 numeros reais.  ")
print("*****************************************************")

#Declaração dos valores para entrada de usuário com conversão para float
valor1 = float(input("Digite o primeiro numero: "))
valor2 = float(input("Digite o segundo numero: "))
valor3 = float(input("Digite o terceiro numero: "))
valor4 = float(input("Digite o quarto numero: "))
valor5 = float(input("Digite o quinto numero: "))

#Calculo da soma
soma = valor1 + valor2 + valor3 + valor4 + valor5

#Exibição do resultado
print(f"O resultado da soma dos numeros {valor1}, {valor2}, {valor3}, {valor4} e {valor5} e igual a: {soma}")
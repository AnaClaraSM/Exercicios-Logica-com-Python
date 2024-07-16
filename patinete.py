#Programa Python para calcular a velocidade média de um patinete
#16/07/2024

print("****************************************************************************")
print("PATINETE ELÉTRICO")
print("Este programa calcula a velocidade média de um patinete elétrico.")
print()

#Declaração de variáveis para armazenar valores informados pelo usuário
distanciaM = float(input("Qual foi a distância percorrida, em metros?: "))
tempoMin = float(input("Quanto tempo, em minutos, o patinete levou para percorrer essa distância?: "))

#Cálculo da velocidade média
print("Calculando...")
velocidadeMedia = distanciaM/tempoMin

#Exibição do resultado - valor formatado com 1 casa decimal
print(f"O patinete atingiu uma velocidade média de {velocidadeMedia:.1f} m/min.")
print()
print("Fim do Programa! Reinicie para calcular novamente.")
print()
print("****************************************************************************")
#Peça ao usuário para inserir o capital, a taxa de juros e o tempo, e calcule o montante final usando a fórmula de juros simples.

capital = float(input("Digite o capital: "))
taxa_juros = float(input("Digite a taxa de juros: "))
tempo = float(input("Digite a quantidade de meses: "))
juros_simples = (capital * taxa_juros * tempo)
print (f"O valor do montante é {juros_simples}.")
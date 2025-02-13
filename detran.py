import random

def gerar_exercicio(simbolos1, simbolos2, num_linhas, simbolos_por_linha, num_exercicio):
    """Gera um exercício com símbolos aleatórios e informa quais símbolos serão usados."""

    exercicio = ""
    simbolos_usados = set()  # Usamos um set para evitar símbolos repetidos
    simbolos_a_marcar = []

    for i in range(num_linhas):
        linha = ""
        # Combina símbolos dos dois grupos de forma aleatória
        for _ in range(simbolos_por_linha):  # 25 símbolos por linha
            grupo = random.randint(1, 2)
            if grupo == 1:
                simbolo = random.choice(simbolos1)
            else:
                simbolo = random.choice(simbolos2)

            linha += simbolo
            simbolos_usados.add(simbolo)

        if num_exercicio == 3 and i > 0:  # Caso seja o exercício 3 e não seja a primeira linha
            linha += " 0"  # Coloca o número 0 indicando a troca de símbolo

        exercicio += linha + "\n"

    # Converte o conjunto de símbolos usados para uma lista e a ordena
    simbolos_usados_lista = list(simbolos_usados)
    random.shuffle(simbolos_usados_lista)  # Embaralha os símbolos usados

    # Define os símbolos a serem marcados com base no número do exercício
    if num_exercicio == 1:
        simbolos_a_marcar = simbolos_usados_lista[:1]  # Apenas 1 símbolo
    elif num_exercicio == 2:
        simbolos_a_marcar = simbolos_usados_lista[:2]  # Dois símbolos
    elif num_exercicio == 3:
        simbolos_a_marcar = simbolos_usados_lista[:1]  # No exercício 3, apenas 1 símbolo será trocado por linha
    else:
        simbolos_a_marcar = []

    return exercicio, simbolos_a_marcar

# Símbolos
simbolos1 = ["★", "☆", "✦", "✧", "✩", "✫", "✰", "☪"]
simbolos2 = ["𖣐", "𖠦", "𖡷", "𖢅", "𖣴", "𖣔", "𖣓", "𖤌"]

# Defina o número de linhas que o arquivo terá
num_linhas = 10  # Por exemplo, 10 linhas
simbolos_por_linha = 25  # 25 símbolos por linha

# Gera e imprime os exercícios
for i in range(1, 4):
    exercicio, simbolos_a_marcar = gerar_exercicio(simbolos1, simbolos2, num_linhas, simbolos_por_linha, i)
    print(f"Exercício {i}:\n{exercicio}")
    print(f"Símbolos a marcar serão: {', '.join(simbolos_a_marcar)}\n")

# Salva os exercícios em um arquivo de texto com encoding UTF-8
with open("exercicios.txt", "w", encoding="utf-8") as arquivo:
    for i in range(1, 4):
        exercicio, simbolos_a_marcar = gerar_exercicio(simbolos1, simbolos2, num_linhas, simbolos_por_linha, i)
        arquivo.write(f"Exercício {i}:\n{exercicio}\n")

        # Adiciona informações sobre os símbolos a marcar
        if i == 1:
            arquivo.write("Será marcado 1 símbolo.\n\n")
        elif i == 2:
            arquivo.write("Serão marcados 2 símbolos.\n\n")
        elif i == 3:
            arquivo.write("Será marcado 1 símbolo por linha. O número 0 indica a troca do símbolo a ser marcado a partir da próxima linha.\n\n")

        arquivo.write(f"Símbolos a marcar serão: {', '.join(simbolos_a_marcar)}\n\n")
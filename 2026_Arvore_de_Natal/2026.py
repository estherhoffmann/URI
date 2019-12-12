# Esther Calderan Hoffmann - RA: 743529

def prog_dinamica_mochila(num_itens, valor_itens, peso_itens, capacidade):
    matriz_valores = [[0 for i in range(0, capacidade+1)] for j in range(0, num_itens+1)]

    for i in range(1, num_itens+1): #acrescento um item de cada vez
        for j in range(0, capacidade+1): #vou aumentando a capacidade
    #então para cada aumento de 1 item, vejo se pega ele com todas as possibilidades de capacidade

            if j < peso_itens[i-1]:
            #se a capacidade for menor que o peso do item não faz
            #sentido pega-lo
                matriz_valores[i][j] = matriz_valores[i-1][j]
                #print("não peguei:", matriz_valores[i][j])

            else:
            #caso contrário, veja se é melhor aquela capacidade sem o novo item
            #ou  nao
                matriz_valores[i][j] = max(matriz_valores[i-1][j], matriz_valores[i-1][j - peso_itens[i-1]] + valor_itens[i-1])
                #print("peguei:", matriz_valores[i][j])

    return matriz_valores[num_itens][capacidade]


num_galhos = int(input())

for i in range(0, num_galhos):
    num_pacotes = int(input())
    qnt_enfeites = [None]*num_pacotes
    peso_pacote = [None]*num_pacotes
    capacidade_galho = int(input())

    for j in range(0, num_pacotes):
        qnt_enfeites[j], peso_pacote[j] = input().split()
    qnt_enfeites = list(map(int, qnt_enfeites))
    peso_pacote = list(map(int, peso_pacote))

    num_total = prog_dinamica_mochila(num_pacotes, qnt_enfeites, peso_pacote, capacidade_galho)

    num_pacotes = None
    capacidade_galho = None
    qnt_enfeites = []
    peso_pacote = []

    print("Galho " + str(i+1) + ":")
    print("Numero total de enfeites:", num_total)
    print()

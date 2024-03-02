def calcula_desconto(dias_alugado, preco):
    desconto = 0

    if(dias_alugado) > 3:
            desconto = 0.03 * preco

    if(dias_alugado) > 7:
        desconto = 0.05 * preco

    if(dias_alugado) > 10:
        desconto = 0.07 * preco

    return desconto

def print_to_file(output):
    with open('output.txt', 'a') as f:
        f.write(str(output))
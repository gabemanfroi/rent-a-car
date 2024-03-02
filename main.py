from utils import calcula_desconto
from constants import base_de_dados

# verificar se o input existe em alguma categoria
modelo_a_ser_encontrado = input('Escolha o seu modelo:').lower()
categoria_encontrada = None

for key, value in base_de_dados.items():

    if modelo_a_ser_encontrado in value['modelos']:
        categoria_encontrada = key

    if categoria_encontrada is not None:
        deseja_adicionar_seguro = input('Deseja adicionar seguro? s/n ')
        dias_alugado = int(input('Deseja alugar por quantos dias? '))

        preco_inicial = value['preco'] * dias_alugado
        preco_final = preco_inicial
        
        desconto = 0

        if(deseja_adicionar_seguro == 's'):
            preco_final = preco_inicial + value['seguro']
            # preco_final += 5
            # preco_final = preco_final + 5

        preco_final = preco_final - calcula_desconto(dias_alugado, preco_final)

        print(f"O valor para o modelo {modelo_a_ser_encontrado} para {dias_alugado} dias é de: ${preco_final}")
        break

if categoria_encontrada is None:
    print(f"O modelo {modelo_a_ser_encontrado.upper()} não está disponível.")

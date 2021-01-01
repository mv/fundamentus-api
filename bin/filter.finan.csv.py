#!/usr/bin/env python3
#

# import set_path_fundamentus

from fundamentus import get_resultado
from fundamentus import print_csv

from fundamentus import list_papel_setor


if __name__ == '__main__':

    data = get_resultado()

    # Filter by 'row'
    #   transpose 1: filter by row
    #   transpose 2: print by column
    setor = list_papel_setor(35)
    data2 = data.T[ setor ]
    data2 = data2.T

    print_csv( data2.sort_index() )


    ## Setores:
    ##  42 : Agropecuária
    ##  33 : Água e Saneamento
    ##  15 : Alimentos
    ##  16 : Bebidas
    ##  27 : Comércio
    ##  12 : Comércio
    ##  20 : Comércio e Distribuição
    ##  28 : Computadores e Equipamentos
    ##  13 : Construção e Engenharia
    ##  26 : Diversos
    ##  6  : Embalagens
    ##  32 : Energia Elétrica
    ##  9  : Equipamentos Elétricos
    ##  39 : Exploração de Imóveis
    ##  35 : Financeiros
    ##  17 : Fumo
    ##  34 : Gás
    ##  40 : Holdings Diversificadas
    ##  24 : Hoteis e Restaurantes
    ##  5  : Madeira e Papel
    ##  10 : Máquinas e Equipamentos
    ##  7  : Materiais Diversos
    ##  8  : Material de Transporte
    ##  23 : Mídia
    ##  2  : Mineração
    ##  41 : Outros
    ##  1  : Petróleo, Gás e Biocombustíveis
    ##  38 : Previdência e Seguros
    ##  18 : Prods. de Uso Pessoal e de Limpeza
    ##  29 : Programas e Serviços
    ##  4  : Químicos
    ##  19 : Saúde
    ##  36 : Securitizadoras de Recebíveis
    ##  11 : Serviços
    ##  37 : Serviços Financeiros Diversos
    ##  3  : Siderurgia e Metalurgia
    ##  21 : Tecidos, Vestuário e Calçados
    ##  43 : Telecomunicações
    ##  30 : Telefonia Fixa
    ##  31 : Telefonia Móvel
    ##  14 : Transporte
    ##  22 : Utilidades Domésticas
    ##  25 : Viagens e Lazer
    ##



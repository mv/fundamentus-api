#!/usr/bin/env python3
#
#

# import set_path_fundamentus

from fundamentus import get_papel
from fundamentus import print_csv

if __name__ == '__main__':

    my_list = [ 'VALE3','WEGE3','ABEV3','ITSA4','PETR4','SAPR11' ]
    my_cols = [ 'Cotacao'                ,
                'Data_ult_cot'           ,
                'Ult_balanco_processado' ,
                'Valor_da_firma'         ,
                'Nro_Acoes'              ,
                'Ativo'                  ,
                'Disponibilidades'       ,
                'Ativo_Circulante'       ,
                'Div_Bruta'              ,
                'Div_Liquida'            ,
                'Patrim_Liq'             ,
                'Receita_Liquida_3m'     ,
                'EBIT_3m'                ,
                'Lucro_Liquido_3m'       ,
                ]

    df1 = get_papel( my_list )
    df2 = df1[ my_cols ]

    print_csv(df2)



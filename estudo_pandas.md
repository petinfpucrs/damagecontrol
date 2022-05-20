**Pandas** - *panel data* - lib/biblioteca para manipulação de dados em formato de listas (data frame) em python

Series: tem apenas uma única lista (uma dimensão/uma coluna) 

data frame: dados alinhados em forma de tabela, com linhas e colunas; vários Seres (multi dimensional)
                          
                          import pandas as pd
                          vendas = {'data': ['15/07','18/9'] , 'valor':[60,70]}
                          tabela = pd.DataFrame(vendas)
                          print(tabela)
                          
                             data  valor
                          0  15/07     60
                          1   18/9     70

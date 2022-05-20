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

métodos visualizacão: 
  x = pd.read_excel('nomedoarquivo') --> para importar dados já criados no excel e transformar em um Data Frame
  vendas.head(x) --> mostra apenas o numero de linhas x da tabela 
  vendas.shape --> mostra quantas linhas e colunas tem na tabela\
  vendas.describe --> da o resumo da tabela 


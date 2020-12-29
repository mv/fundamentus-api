# Fundamentus

Linha de comando que captura os dados do site Fundamentus (www.fundamentus.com.br) em formato CSV.

Os dados são buscados a partir da página [**'Resultado'**](http://www.fundamentus.com.br/resultado.php) e podem ser filtrados.


## Dados completos

Para obter a listagem completa de todos os dados:

```bash
## Direto
$ bin/fundamentus.csv.py

## Alternativa
$ bin/fundamentus.csv.py > bovespa.csv
```

## Aplicando um filtro

A página de **'Busca avançada por empresa'** permite o uso de filtros para pesquisa:

```bash
## Usando um filtro customizado:
$ bin/filter.example.py

$ bin/filter.example.py > bovespa.filtered.csv
```

Os filtros são propriedades do DataFrame definido:

```python
# filter on DataFrame
data = data[ data.pl   > 0   ]
data = data[ data.pl   < 100 ]
data = data[ data.roe  > 0   ]
data = data[ data.roic > 0   ]
```

A lista completa dos filtros pode ser visualizada via IPython:
```python
In [1]: %run filter.example.py
In [2]: data.columns
Out[2]:
Index(['cotacao', 'pl', 'pvp', 'psr', 'dy', 'pa', 'pcg', 'pebit', 'pacl', 'evebit', 'evebitda', 'mrgebit', 'mrgliq', 'roic', 'roe', 'liqc', 'liq2m', 'patrliq', 'divbpatr', 'c5y'], dtype='object', name='Multiples')
```

A list entre os nomes web e os filtros/propriedades está [**aqui**](https://github.com/mv/fundamentus/blob/00e75054be3eeda643bc5f86540332df854ae1bc/fundamentus/resultado.py#L111).

## Internals

1. Requisicoes via `requests` são todas **CACHEABLE**.

2. *Wip...*


## IPython

*Wip...*



## Magic Formula: Joel Greenblatt

Obtendo uma lista filtrada dos dados, e aplicando o `ranking` da [**Magic Formula**](https://www.magicformulainvesting.com/Home/AboutTheBook) de Joel Greenblatt:

```bash
## Magic Formula
$ bin/magic_formula.simple.py

$ bin/magic_formula.simple.py > bovespa.ranking.csv
```

## Disclaimer

1. Inspirado no [script Fundamentus original](https://github.com/phoemur/fundamentus) de [Phoemur](https://github.com/phoemur)

2. Para saber mais sobre a **Magic Formula**:
  * https://en.wikipedia.org/wiki/Magic_formula_investing
  * https://www.magicformulainvesting.com/Home/AboutTheBook
  * https://www.investopedia.com/terms/m/magic-formula-investing.asp


## License

The MIT License (MIT)


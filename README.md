# Fundamentus

Linha de comando que captura os dados do site Fundamentus (www.fundamentus.com.br) em formato CSV.

Os dados são buscados a partir da página [**'Busca avançada por empresa'**](http://www.fundamentus.com.br/resultado.php) e podem ser filtrados.


## Dados completos

Para obter a listagem completa de todos os dados:

```bash
## Direto
$ ./fundamentus.csv.py

## Alternativa
$ ./fundamentus.csv.py > bovespa.csv
```


## Aplicando um filtro

A página de **'Busca avançada por empresa'** permite o uso de filtros para pesquisa:

```bash
## Usando um filtro customizado:
$ ./filter.example.py

$ ./filter.example.py > bovespa.filtered.csv
```


Os filtros são um [sub-grupo](https://github.com/mv/fundamentus/blob/b7b1f47ac98e09955ca01470b4636d1c7578af4c/filter.example.py#L11) dos parametros em Python:

```python
params = {'pl_min'  : '0',
          'pl_max'  : '100',
          'roic_min': '0',
          'roic_max': '',
          'roe_min' : '0',
          'roe_max' : '',
          }
```

A lista completa dos filtros está no script principal [`fundamentus.py`](https://github.com/mv/fundamentus/blob/b7b1f47ac98e09955ca01470b4636d1c7578af4c/fundamentus.py#L16).


## Magic Formula: Joel Greenblatt

Obtendo uma lista filtrada dos dados, e aplicando o `ranking` da [**Magic Formula**](https://www.magicformulainvesting.com/Home/AboutTheBook) de Joel Greenblatt:

```bash
## Magic Formula
$ ./magic_formula.simple.py

$ ./magic_formula.simple.py > bovespa.ranking.csv
```



## Disclaimer

Baseado no [script Fundamentus original](https://github.com/phoemur/fundamentus) de [Phoemur](https://github.com/phoemur)

Para saber mais sobre a **Magic Formula**:
* https://en.wikipedia.org/wiki/Magic_formula_investing
* https://www.magicformulainvesting.com/Home/AboutTheBook
* https://www.investopedia.com/terms/m/magic-formula-investing.asp


## License

The MIT License (MIT)


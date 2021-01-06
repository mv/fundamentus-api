# Python Fundamentus

[![version](https://img.shields.io/pypi/v/fundamentus.svg)](https://pypi.org/project/fundamentus/)
[![pyversions](https://img.shields.io/pypi/pyversions/fundamentus.svg)](https://pypi.org/project/fundamentus/)
[![license](https://img.shields.io/github/license/mv/fundamentus-api.svg)](https://pypi.org/project/fundamentus/)
[![TravisCI](https://travis-ci.org/mv/fundamentus-api.svg?branch=main)](https://travis-ci.org/github/mv/fundamentus-api)
[![Coverage](https://coveralls.io/repos/github/mv/fundamentus-api/badge.png?branch=main)](https://coveralls.io/github/mv/fundamentus-api?branch=main)


Python API to load data from **[Fundamentus](ww.fundamentus.com.br)** website.



## API usage

Main functions are named after each website functionality:
* `get_resultado` - https://www.fundamentus.com.br/resultado.php
* `get_papel`     - https://www.fundamentus.com.br/detalhes.php?papel=WEGE3

A specific `list` function is built from the following `setor` parameter:
* `list_papel_setor` - https://www.fundamentus.com.br/resultado.php?setor=27


## Examples

### `get_resultado`

`Return: -> DataFrame`

```python
>>> import fundamentus
>>> df = fundamentus.get_resultado()
>>> print(df.columns)

  Index(['cotacao', 'pl', 'pvp', 'psr', 'dy', 'pa', 'pcg', 'pebit', 'pacl',
         'evebit', 'evebitda', 'mrgebit', 'mrgliq', 'roic', 'roe', 'liqc',
         'liq2m', 'patrliq', 'divbpatr', 'c5y'],
        dtype='object', name='Multiples')

>>> print( df[ df.pl > 0] )

    papel   cotacao     pl   pvp  ...  divbpatr     c5y
    ABCB4     15.81   9.66  0.83  ...      0.00 -0.5287
    ABEV3     15.95  28.87  3.22  ...      0.09  0.0455
    AEDU11    37.35  20.13  1.13  ...      0.30  0.2090
    ...         ...    ...   ...  ...       ...     ...
    WIZS3      7.95   5.96  3.61  ...      0.00  0.1737
    WSON33    45.45  34.29  1.34  ...      1.11  0.0131
    YDUQ3     33.26  39.71  3.10  ...      1.45  0.0449
```

Columns names were simplified from the original web page to allow DataFrame filtering in a simplified way:

```python
# filter on DataFrame
df = df[ df.pl  > 0   ]
df = df[ df.pl  < 100 ]
df = df[ df.pvp > 0   ]
```

### `get_resultado_raw`

`Return: -> DataFrame`

```python
>>> import fundamentus
>>> df = fundamentus.get_resultado_raw()
>>> print(df.columns)

Index(['Cotação', 'P/L', 'P/VP', 'PSR', 'Div.Yield', 'P/Ativo', 'P/Cap.Giro',
       'P/EBIT', 'P/Ativ Circ.Liq', 'EV/EBIT', 'EV/EBITDA', 'Mrg Ebit',
       'Mrg. Líq.', 'Liq. Corr.', 'ROIC', 'ROE', 'Liq.2meses', 'Patrim. Líq',
       'Dív.Brut/ Patrim.', 'Cresc. Rec.5a'],
      dtype='object', name='Multiples')

>>> print( df[ df['P/L'] > 0] )

    papel   Cotação    P/L  P/VP  ...  Dív.Brut/ Patrim.  Cresc. Rec.5a
    ABCB4     15.81   9.66  0.83  ...               0.00        -0.5287
    ABEV3     15.95  28.87  3.22  ...               0.09         0.0455
    AEDU11    37.35  20.13  1.13  ...               0.30         0.2090
    ...         ...    ...   ...  ...                ...            ...
    WIZS3      7.95   5.96  3.61  ...               0.00         0.1737
    WSON33    45.45  34.29  1.34  ...               1.11         0.0131
    YDUQ3     33.26  39.71  3.10  ...               1.45         0.0449
```

In the `_raw` function, columns names are preserved as captured from the web page. Be aware that names are in `pt-br` and contain spaces and accents. Filtering must be made explicitly:

```python
# filter on DataFrame
df = df[ df['P/L'] > 0   ]
df = df[ df['P/L'] < 100 ]
df = df[ df['P/VP'] > 0  ]
```

The renaming list can be found [**here**](https://github.com/mv/fundamentus/blob/8075a6f7efc2aa29578624518ea79fa385444a35/src/fundamentus/resultado.py#L114).

### `get_papel`

`Return: -> DataFrame`

```python
>>> import fundamentus

>>> df = fundamentus.get_papel('WEGE3')  ## or...
>>> df = fundamentus.get_papel(['ITSA4','WEGE3'])

>>> print(df)

        Tipo       Empresa        Setor ... Receita_Liquida_3m    EBIT_3m Lucro_Liquido_3m
ITSA4  PN N1  ITAÚSA PN N1  Financeiros ...         1778000000  257000000       1784000000
WEGE3  ON N1  WEG SA ON N1  Máquinas e  ...         4801260000  946670000        644246000

```

### `list_papel_setor`

`Return: -> list`

```python
>>> import fundamentus

>>> fin = fundamentus.list_papel_setor(35)  # finance
>>> seg = fundamentus.list_papel_setor(38)  # seguradoras

>>> print(fin)
   ['ABCB4', 'BBAS3', 'BBDC3', 'BBDC4', ... ]

>>> print(seg)
   ['BBSE3', 'IRBR3', 'SULA4', 'WIZS3', ... ]
```

The full list of companies by `setor` can be found [here](https://github.com/mv/fundamentus/blob/1cab1cf965d99c02d05faa90807ebe7381cbc784/src/fundamentus/setor.py#L56)


## License

The MIT License (MIT)

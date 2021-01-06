
"""
Fundamentus:
  Info:
    Get data from http://fundamentus.com.br/ using Pandas.

  Ref:
    https://github.com/mv/fundamentus
"""


__all__ = [
        'get_resultado',
        'get_resultado_raw',
        'get_papel',
        'list_papel_setor',
        ]

__version__ = '0.1.0'


from fundamentus.resultado  import get_resultado
from fundamentus.resultado  import get_resultado_raw

from fundamentus.detalhes   import get_papel
from fundamentus.detalhes   import get_detalhes_papel
from fundamentus.detalhes   import get_detalhes_raw
from fundamentus.detalhes   import list_papel_all

from fundamentus.setor      import get_setor_id
from fundamentus.setor      import list_papel_setor
from fundamentus.setor      import print_setores

from fundamentus.utils      import print_csv
from fundamentus.utils      import print_table


# log setup/init
import fundamentus
from   fundamentus import logging
fundamentus.logging.log_init()



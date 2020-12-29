

import sys
import os

## insert '..' one level above
## (so I can import my code...)
##
sys.path.insert(0,
                os.path.abspath(
                    os.path.join(
                        os.path.dirname(__file__) , '../src/')
                    )
                )

import fundamentus
import fundamentus.detalhes as detalhes


detalhes.get_detalhes_papel('ITSA4')
detalhes.get_detalhes_papel('WEGE3')
detalhes.get_detalhes_list(['ITSA4','WEGE3'])

detalhes.get_detalhes('ITSA4')
detalhes.get_detalhes('WEGE3')
detalhes.get_detalhes(['ITSA4','WEGE3'])



#!/usr/bin/env python3
#
#

# import set_path_fundamentus

import fundamentus


if __name__ == '__main__':

    papel = 'VALE3'

    raw = fundamentus.get_detalhes_raw(papel)
    print("\n\nDetalhes: RAW\n")
    print(raw)


    det = fundamentus.get_papel(papel)
    print("\n\nDetalhes: transposed\n")
    print(det.T,"\n")



#!/usr/bin/env python3


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


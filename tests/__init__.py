#
# Ref:
#   https://github.com/navdeep-G/samplemod/
#

import sys
import os


## insert '..' one level above
## (so I can import my code...)
##
sys.path.insert(0,
                os.path.abspath(
                    os.path.join(
                        os.path.dirname(__file__) , '..')
                    )
                )

for p in sys.path[:3]:
    print(p)

import fundamentus


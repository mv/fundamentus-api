
"""
Logging:
    init logging.
"""

import logging
import os


log_fmt='%(asctime)-15s [%(module)s.%(funcName)s] %(levelname)s: %(message)s'

def log_init():

    # default: info
    log_level = os.environ.get('LOGLEVEL') or 'INFO'

    logging.basicConfig(format=log_fmt, level=log_level.upper())

    logging.info('LOGLEVEL={}'.format(log_level))

    return


# logging.debug('This is a debug message')
# logging.info('This is an info message')
# logging.warning('This is a warning message')
# logging.error('This is an error message')
# logging.critical('This is a critical message')



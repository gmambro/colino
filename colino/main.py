from __future__ import (absolute_import, division, print_function,
                        unicode_literals)

from colino.conf.loader import ConfLoader
from colino.conf.exceptions import ConfigurationException

import argparse
import logging
import os
import sys

# Warning: ALPHA quality main module


def load_conf(filename=None):

    # guess configuration location if none is given
    if filename is None:
        # TODO better default 
        filename = os.path.join("etc", "test.colino")

    try:
        loader = ConfLoader()
        conf = loader.load(filename)
    except IOError:
        print("error: cannot open configuration file %s" % filename)
        sys.exit(1)
    except ConfigurationException as e:
        print(e)
        sys.exit(1)
        
    return conf

def main():
    
    parser = argparse.ArgumentParser(description="Colino.")
    parser.add_argument('-c', '--configuration',
                        metavar="FILE",
                        help="the configuration file")
    args = parser.parse_args()
    
    load_conf(args.configuration)

    
        
if __name__ == '__main__':
    main()











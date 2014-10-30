from __future__ import (absolute_import, division,
                        print_function, unicode_literals)

from time import time


class Event(object):

    def __init__(self, message, timestamp=None):
        self.message = message
        if timestamp is not None:
            self.timestamp = time
        else:
            self.timestamp = time()

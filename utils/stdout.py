import sys
import subprocess

class __prev(object):

    _i = 3

    @property
    def i(self):
        return type(self)._i

    @i.setter
    def i(self,val):
        type(self)._i = val


def stdout_print(text: str):
    sys.stdout.flush()
    sys.stdout.write('{0}\r'.format(' '.join(['' for i in range(0, __prev().i)])))
    sys.stdout.flush()
    sys.stdout.write('{0}\r'.format(text))
    __prev().i = len(text)

def stdout_flush():
    sys.stdout.flush()
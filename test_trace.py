#!/usr/bin/env python

from Trace import *

class Dummy(Trace):

    def __init__(self):
        Trace.__init__(self)

        self.traceAdd("ding")

    def ding(self):
       self.trace("Ding called")

d = Dummy()

d.ding()

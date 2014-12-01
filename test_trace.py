#!/usr/bin/env python

from Trace import *

class Dummy(Trace):

    def __init__(self):
        Trace.__init__(self)

        self.traceAdd("ding")
        self.traceAdd("diddely")

    def ding(self):
       self.trace("Ding called")

    def dong(self):
        self.trace("Dong called")

    def diddely(self):
        self.trace("Diddely called")

d = Dummy()

d.ding()
d.dong()
d.diddely()

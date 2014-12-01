"""
Simple trace/print class with dynamic tracepoints

Jesper L. Nielsen <lyager|gmail.com>
"""

import traceback

class Trace:

    classname = None
    tracepoints = []

    def __init__(self):
        self.classname = self.__class__

    def traceAdd(self, funcname):
        """ Add @funcname to tracepoints """
        self.tracepoints.append(funcname)

    def trace(self, *arg):
        caller = traceback.extract_stack(limit=2)[0]
        if caller[2] in self.tracepoints:    # function name
            print("%s:%d - %s" % (self.classname, caller[1], arg[0])) # Line number plus args


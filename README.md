Trace for Python
================

A task often performed by me is to leave in small print statements within my
code. Either todo's or maybe from unexpected things happening. Often this can
get to a lot of output, which is nice to be able to disable fast.

Trace will give you output based on tracepoints. What you will have to do
is extend your class with Trace, and initilize it as usual. After that you can
add tracepoints, which are functionnames, for what you would like to see
output for. Have a look at the `test_trace.py` program for a simple example.

In the example you can see Trace prints for three class function, however only
2 of these gets actual output. This is because function `dong` doesn't have an
added tracepoint added with `traceAdd`.


Enjoy

Notes
-----

Somewhat inspireced by [TraceIt](https://github.com/lyager/traceit).

License: Not rocket science, but please share modifications and ideas back,
for others to enjoy.



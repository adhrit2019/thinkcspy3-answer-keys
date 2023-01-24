import sys

def test(did_pass):
    linenum = sys._getframe(1).f_lineno
    if did_pass:
        print("Test at line {0} passed.".format(linenum))
    else:
        print("Test at line {0} failed.".format(linenum))


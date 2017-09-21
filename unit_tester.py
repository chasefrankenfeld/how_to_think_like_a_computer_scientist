import sys


def test(did_pass):
    """ Print the rests of the test """
    linenum = sys._getframe(1).f_lineno  # gets the callers line number
    if did_pass:
        msg = "Test at line {} is ok.".format(linenum)
    else:
        msg = "Test at line {} FAILED.".format(linenum)
    print(msg)
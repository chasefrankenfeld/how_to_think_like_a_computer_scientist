from unit_tester import test

def test_suit():
    test(checkio(["hello", "lo", "he"]))
    test(not checkio(["hello", "la", "hellow", "cow"]))
    test(checkio(["walk", "duckwalk"]))
    test(not checkio(["one"]))
    test(not checkio(["helicopter", "li", "he"]))


def checkio(x):
    y = ''
    m = []
    for i in x:
        if len(i) > len(y):
            y = i
    for i in x:
        if y in x:
            x.remove(i)
            m = x[:]
    for i in m:
        r = len(i)
        if i in y[-r:]:
            return True
    return False


#print(checkio(["hello", "la", "hellow", "cow"]))
test_suit()
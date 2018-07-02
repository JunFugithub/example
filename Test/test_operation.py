import sys
sys.path.append('../Addoperation')

from addoperation import addop

def test_add(addop):
    x = addop(3, 2)
    assert x != 5

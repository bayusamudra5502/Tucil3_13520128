from lib.Node import Node
from lib.Table import Table

def test_cost():
  a = [1,2,16,4,5,6,3,8,9,10,7,11,13,14,15,12]
  b = [1,2,3,4,5,16,6,8,9,10,7,11,13,14,15,12]

  Ta = Table(a)
  Tb = Table(b)

  assert Node(1, Ta).cost() == 5
  assert Node(2, Tb).cost() == 6
from decimal import Underflow
from lib.Node import Node
from lib.PrioQueue import PrioQueue
from lib.Table import Table

def test_push_pop():
  tb = Table([1,2,3,4,5,6,16,8,9,10,7,11,13,14,15,12])
  
  pq = PrioQueue()
  parent = Node(tb)

  try:
    pq.pop()
    assert False
  except Underflow as e:
    pass
  except Exception as e:
    raise e

  pq.push(parent.moveUp())
  pq.push(parent.moveDown())
  pq.push(parent.moveLeft())
  pq.push(parent.moveRight())

  keluar = pq.pop()
  assert parent.moveDown() == keluar
  assert ["DOWN"] == keluar.getMove()

  keluar = pq.pop()
  assert ["UP"] == keluar.getMove()
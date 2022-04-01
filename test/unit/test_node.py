from lib.Node import Node
from lib.Table import Table

def test_cost():
  a = [1,2,16,4,5,6,3,8,9,10,7,11,13,14,15,12]
  b = [1,2,3,4,5,16,6,8,9,10,7,11,13,14,15,12]

  Ta = Table(a)
  Tb = Table(b)

  assert Node(Ta, ["UP"]).cost() == 5
  assert Node(Tb, ["DOWN","UP"]).cost() == 6

def test_move():
  pos = [  1, 2, 3, 4,
           5, 6,16, 8,
           9,10, 7,11,
          13,14,15,12]

  node = Node(Table(pos))
  up = node.moveUp()
  down = node.moveDown()
  left = node.moveLeft()
  right = node.moveRight()

  assert up.cost() == 5
  assert right.cost() == 5
  assert left.cost() == 5
  assert down.cost() == 3

  assert up.getMove() == ["UP"]
  assert left.getMove() == ["LEFT"]
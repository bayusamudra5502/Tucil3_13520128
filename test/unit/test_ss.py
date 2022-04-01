from lib.StateSave import StateSave
from lib.Table import Table
from lib.Node import Node

def test_state():
  tb = Table([1,2,3,4,5,6,16,8,9,10,7,11,13,14,15,12])
  
  parent = Node(tb)
  state = StateSave()

  state.addState(parent.getTable())
  state.addState(parent.getTable())
  state.addState(parent.moveDown().getTable())
  state.addState(parent.moveUp().getTable())

  assert state.isStateExist(parent.getTable())
  assert state.isStateExist(parent.moveDown().getTable())
  assert state.isStateExist(parent.moveUp().getTable())
  assert not state.isStateExist(parent.moveLeft().getTable())
  assert not state.isStateExist(parent.moveRight().getTable())

  assert state.getLength() == 3

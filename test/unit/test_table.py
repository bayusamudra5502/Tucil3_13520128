from lib.Table import Table
from lib.MoveException import MoveException

def test_comparison():
  a = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
  b = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
  c = [6,2,3,4,5,1,7,8,9,10,11,12,13,14,15,16]

  Ta = Table(a)
  Tb = Table(b)
  Tc = Table(c)

  assert Ta == Tb
  assert not Ta != Tb
  assert Ta < Tc
  assert Ta <= Tb
  assert Ta <= Tc
  assert Tc > Tb
  assert Ta >= Tb
  assert Tc >= Tb

def test_solve():
  a = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
  b = [1,3,4,15,2,16,5,12,7,6,11,14,8,9,10,13]
  c = [1,2,3,4,5,6,16,8,9,10,7,11,13,14,15,12]

  Ta = Table(a)
  Tb = Table(b)
  Tc = Table(c)

  assert Ta.isSolveable()
  assert not Tb.isSolveable()
  assert Tc.isSolveable()

  assert Ta.solvePoint() == 0
  assert Tb.solvePoint() == 37
  assert Tc.solvePoint() == 16

  assert Ta.isSolution()
  assert not Tb.isSolution()
  assert not Tc.isSolution()

def test_cost():
  a = [1,2,16,4,5,6,3,8,9,10,7,11,13,14,15,12]
  b = [1,2,3,4,5,6,8,16,9,10,7,11,13,14,15,12]
  c = [1,2,3,4,5,6,7,8,9,10,16,11,13,14,15,12]
  d = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]

  Ta = Table(a)
  Tb = Table(b)
  Tc = Table(c)
  Td = Table(d)

  assert Ta.prediction() == 4
  assert Tb.prediction() == 4
  assert Tc.prediction() == 2
  assert Td.prediction() == 0

def test_up():
  a = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
  b = [16,2,3,4,5,6,7,8,9,10,11,12,13,14,15,1]
  c = [1,2,3,4,5,6,7,8,9,16,11,12,13,14,15,10]
  d = [2,3,16,4,5,6,7,8,9,10,11,12,13,14,15,1]

  Ta = Table(a)
  Tb = Table(b)
  Tc = Table(c)
  Td = Table(d)

  ansA = [1,2,3,4,5,6,7,8,9,10,11,16,13,14,15,12]
  ansC = [1,2,3,4,5,16,7,8,9,6,11,12,13,14,15,10]

  Taa = Table(ansA)
  Tac = Table(ansC)

  assert Ta.toTop() == Taa
  
  try:
    Tb.toTop()
    assert False
  except MoveException as e:
    if e.args[0] != "The empty slot is in the top" or e.getMove() != "UP":
      raise e
  except Exception as e:
    raise e

  try:
    Td.toTop()
    assert False
  except MoveException as e:
    if e.args[0] != "The empty slot is in the top" or e.getMove() != "UP":
      raise e
  except Exception as e:
    raise e


  assert Tc.toTop() == Tac

def test_down():
  a = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
  b = [1,2,3,4,5,6,7,8,9,10,11,12,13,16,15,14]
  c = [ 1, 2, 3, 4,
        5, 6, 7, 8,
        9,10,16,12,
       13,14,15,11]
  d = [ 1,16, 3, 4,
        5, 6, 7, 8,
        9,10,11,12,
       13,14,15,2]

  Ta = Table(a)
  Tb = Table(b)
  Tc = Table(c)
  Td = Table(d)

  ansC = [ 1, 2, 3, 4,
        5, 6, 7, 8,
        9,10,15,12,
       13,14,16,11]
  ansD = [ 1,6, 3, 4,
           5, 16, 7, 8,
           9,10,11,12,
          13,14,15,2]
  
  TAnsC = Table(ansC)
  TAnsD = Table(ansD)

  try:
    Ta.toBottom()
    assert False
  except MoveException as e:
    if e.args[0] != "The empty slot is in the bottom" or e.getMove() != "DOWN":
      raise e
  except Exception as e:
    raise e

  try:
    Tb.toBottom()
    assert False
  except MoveException as e:
    if e.args[0] != "The empty slot is in the bottom" or e.getMove() != "DOWN":
      raise e
  except Exception as e:
    raise e

  assert Tc.toBottom() == TAnsC
  assert Td.toBottom() == TAnsD

def test_left():
  a = [ 1, 2, 3, 4,
        5, 6, 7, 8,
        9,10,11,12,
       13,14,15,16]
  b = [ 1, 2, 3, 4,
        5, 6, 7, 8,
       16,10,11,12,
       13,14,15,9]
  c = [ 1, 2, 3, 4,
        5, 6, 7, 8,
       10,16,11,12,
       13,14,15,9]

  ansA = [ 1, 2, 3, 4,
           5, 6, 7, 8,
           9,10,11,12,
          13,14,16,15]

  Ta = Table(a)
  Tb = Table(b)
  Tc = Table(c)
  TAnsA = Table(ansA)

  assert Ta.toLeft() == TAnsA
  assert Tc.toLeft() == Tb

  try:
    Tb.toLeft()
    assert False
  except MoveException as e:
    if e.args[0] != "The empty slot is in the leftmost" or e.getMove() != "LEFT":
      raise e
  except Exception as e:
    raise e

def test_right():
  b = [ 1, 2, 3, 4,
        5, 7, 8,16,
        9,10,11,12,
       13,14,15, 6]
  c = [ 1, 2, 3, 4,
        5, 7,16, 8,
        9,10,11,12,
       13,14,15, 6]
  d = [ 1, 2, 3, 4,
        5,16, 7, 8,
        9,10,11,12,
       13,14,15, 6]
  
  Tb = Table(b)
  Tc = Table(c)
  Td = Table(d)

  try:
    Tb.toRight()
    assert False
  except MoveException as e:
    if e.args[0] != "The empty slot is in the rightmost" or e.getMove() != "RIGHT":
      raise e
  except Exception as e:
    raise e
  
  assert Td.toRight() == Tc
  assert Tc.toRight() == Tb

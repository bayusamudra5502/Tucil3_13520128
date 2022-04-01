from lib.Table import Table

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

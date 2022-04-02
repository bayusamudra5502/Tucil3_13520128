from lib.Solver import Solver
from lib.Solver import Table
from lib.UnsolveableException import UnsolveableException

def test_success():
  fileInput = [1,2,3,4,5,6,16,8,9,10,7,11,13,14,15,12]
  inputTable = Table(fileInput)

  solver = Solver(inputTable)
  solver.solve()

  assert len(solver.getSolutions()) > 0
  assert solver.getSolutions()[0].getMove() == ["DOWN","RIGHT","DOWN"]

def test_failed():
  fileInput = [1,3,4,15,2,16,5,12,7,6,11,14,8,9,10,13]
  inputTable = Table(fileInput)

  solver = Solver(inputTable)
  try:
    solver.solve()
    assert False
  except UnsolveableException:
    assert True
  except Exception:
    assert False


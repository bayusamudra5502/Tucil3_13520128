from lib.Table import Table
from lib.PrioQueue import PrioQueue
from lib.StateSave import StateSave
from lib.Node import Node
from lib.Table import Table
from lib.MoveException import MoveException
from lib.UnsolveableException import UnsolveableException

class Solver:
  def __init__(self, start: Table, all=False) -> None:
    self.__start = Node(start)
    self.__prio = PrioQueue()
    self.__state = StateSave()
    self.__prio.push(
      self.__start
    )
    self.__solution: list[Node] = []
    self.__costLimit = -1
    self.__nodeNumber = 1
    self.__allSolution = all

  def solve(self):
    if not self.__start.getTable().isSolveable():
      raise UnsolveableException(self.__start)

    while not self.__prio.isEmpty():
      currentState = self.__prio.pop()

      if currentState.isSolution():
        if self.__costLimit > currentState.cost():
          self.__solution.clear()
          
        self.__solution.append(currentState)
        self.__costLimit = currentState.cost()

        if not self.__allSolution:
          return
        self.__prio = self.__prio.filterQueue(self.__costLimit)
        continue
      elif self.__costLimit != -1 and \
         currentState.cost() >= self.__costLimit:
        continue
      
      self.__state.addState(currentState.getTable())
      moves = ["UP","RIGHT","DOWN","LEFT"]

      for i in moves:
        try:
          newNode = currentState.move(i)
          if self.__state.isStateExist(newNode.getTable()):
            continue
          self.__prio.push(newNode)
          self.__nodeNumber += 1
        except MoveException as e:
          pass
        except Exception as e:
          raise e

  def getSolutions(self):
    return self.__solution

  def getMinimalCost(self):
    return self.__costLimit

  def getNodeNumber(self):
    return self.__nodeNumber

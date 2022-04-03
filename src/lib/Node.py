from lib.Table import Table

class Node:
  def __init__(self, table: Table, move: list = []) -> None:
      self.__move = move
      self.__table = table
      self.__level = len(move)
  
  def __eq__(self, __o: object) -> bool:
    return self.cost() == __o.cost() and self.getLevel() == __o.getLevel()

  def __ge__(self, __o:object) -> bool:
    return self.cost() >= __o.cost() or \
      (self.cost() == __o.cost() and self.getLevel() <= __o.getLevel())

  def __gt__(self, __o:object) -> bool:
    return self.cost() > __o.cost() or \
      (self.cost() == __o.cost() and self.getLevel() < __o.getLevel())

  def __le__(self, __o:object) -> bool:
    return self.cost() <= __o.cost() or \
      (self.cost() == __o.cost() and self.getLevel() >= __o.getLevel())

  def __lt__(self, __o:object) -> bool:
    return self.cost() < __o.cost() or \
      (self.cost() == __o.cost() and self.getLevel() > __o.getLevel())

  def getTable(self) -> Table:
    return self.__table

  def getLevel(self) -> int:
    return self.__level
  
  def getMove(self) -> list:
    return self.__move
  
  def cost(self) -> int:
    return self.__table.prediction() + self.getLevel()

  def isSolution(self) -> bool:
    return self.__table.isSolution()
  
  def moveUp(self):
    return Node(self.__table.toTop(), [*self.__move, "UP"])

  def moveDown(self):
    return Node(self.__table.toBottom(), [*self.__move, "DOWN"])

  def moveLeft(self):
    return Node(self.__table.toLeft(), [*self.__move, "LEFT"])

  def moveRight(self):
    return Node(self.__table.toRight(), [*self.__move, "RIGHT"])

  def move(self, move: str):
    if move == "UP":
      return self.moveUp()
    elif move == "DOWN":
      return self.moveDown()
    elif move == "LEFT":
      return self.moveLeft()
    elif move == "RIGHT":
      return self.moveRight()
    else:
      raise Exception("Move action unknown")

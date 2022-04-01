from lib.Table import Table

class Node:
  def __init__(self, level: int, table: Table) -> None:
      self.__level = level
      self.__table = table
  
  def getTable(self) -> list:
    return self.__table.getTable()
  
  def cost(self) -> int:
    return self.__table.prediction() + self.__level

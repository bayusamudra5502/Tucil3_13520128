from lib.Table import Table

class UnsolveableException(Exception):
  def __init__(self, table: Table) -> None:
      super().__init__("Unsolveable Exception")
      self.__table = table 

  def getTable(self) -> Table:
    return self.__table

from lib.MoveException import MoveException

class Table:
  def __init__(self, table: list) -> None:
    self.__table = []
    cnt = 0

    for i in table:
      self.__table.append(i)
      
      if i == 16:
        self.__pos = cnt
      
      cnt += 1
  
  def __eq__(self, __o: object) -> bool:
    return self.__table == __o.getTable()
  
  def __ge__(self, __o:object) -> bool:
    return self.__table >= __o.getTable()

  def __gt__(self, __o:object) -> bool:
    return self.__table > __o.getTable()

  def __le__(self, __o:object) -> bool:
    return self.__table <= __o.getTable()

  def __lt__(self, __o:object) -> bool:
    return self.__table < __o.getTable()

  def getTable(self) -> list:    
    return self.__table
  
  def solvePoint(self) -> int:
    kurang = (self.__pos + ((self.__pos // 4) % 2)) % 2

    for i in range(len(self.__table)):
      for j in range(i+1, len(self.__table)):
        if self.__table[i] > self.__table[j]:
          kurang += 1
    
    return kurang

  def isSolveable(self) -> bool:
    return (self.solvePoint() % 2) == 0
  
  def prediction(self) -> int:
    score = 0
    for i in range(len(self.__table)):
      if i + 1 != self.__table[i] and self.__table[i] != 16:
        score += 1
    
    return score
  
  def toLeft(self):
    j = self.__pos % 4

    if j == 0:
      raise MoveException("The empty slot is in the leftmost", "LEFT")

    cp = self.__table.copy()
    cp[self.__pos-1], cp[self.__pos] = cp[self.__pos], cp[self.__pos-1]

    return Table(cp)

  def toRight(self):
    j = self.__pos % 4

    if j == 3:
      raise MoveException("The empty slot is in the rightmost", "RIGHT")

    cp = self.__table.copy()
    cp[self.__pos+1], cp[self.__pos] = cp[self.__pos], cp[self.__pos+1]

    return Table(cp)
  
  def toTop(self):
    i = self.__pos // 4

    if i == 0:
      raise MoveException("The empty slot is in the top", "UP")
    
    cp = self.__table.copy()
    topIdx = self.__pos - 4

    cp[topIdx], cp[self.__pos] = cp[self.__pos], cp[topIdx]

    return Table(cp)

  def toBottom(self):
    i = self.__pos // 4

    if i >= 3:
      raise MoveException("The empty slot is in the bottom", "DOWN")

    cp = self.__table.copy()
    bottomIdx = self.__pos + 4

    cp[bottomIdx], cp[self.__pos] = cp[self.__pos], cp[bottomIdx]
    return Table(cp)
  
  def isSolution(self) -> bool:
    return self.prediction() == 0

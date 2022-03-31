class Table:
  def __init__(self, table: list) -> None:
    self.__table = []
    cnt = 0

    for i in table:
      for j in i:
        self.__table.append(j)
        
        if j == 16:
          self.__pos = cnt
        
        cnt += 1
  
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
      if i + 1 != self.__table[i]:
        score += 1
    
    return score
  
  def toLeft(self):
    j = self.__pos % 4

    if j == 0:
      raise Exception("The empty slot is in the leftmost")

    cp = self.__table.copy()
    cp[self.__pos-1], cp[self.__pos] = cp[self.__pos], cp[self.__pos-1]

    return Table(cp)

  def toRight(self):
    j = self.__pos % 4

    if j == 3:
      raise Exception("The empty slot is in the rightmost")

    cp = self.__table.copy()
    cp[self.__pos+1], cp[self.__pos] = cp[self.__pos], cp[self.__pos+1]

    return Table(cp)
  
  def toTop(self):
    i = self.__pos // 4

    if i == 0:
      raise Exception("The empty slot is in the top")
    
    cp = self.__table.copy()
    topIdx = self.__pos - 4

    cp[topIdx], cp[self.__pos] = cp[self.__pos], cp[topIdx]

    return Table(cp)

  def toBottom(self):
    i = self.__pos // 4

    if i >= 3:
      raise Exception("The empty slot is in the bottom")

    cp = self.__table.copy()
    bottomIdx = self.__pos + 4

    cp[bottomIdx], cp[self.__pos] = cp[self.__pos], cp[bottomIdx]
    return Table(cp)
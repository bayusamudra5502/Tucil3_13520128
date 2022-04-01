from lib.Table import Table

class StateSave:
  def __init__(self) -> None:
    self.__list = []
  
  def addState(self, table: Table):
    self.__list.append(table)
  
    for i in range(len(self.__list), 0, -1):
      if self.__list[i] < self.__list[i-1]:
        self.__list[i], self.__list[i-1] = self.__list[i-1], self.__list[i]
      else:
        break
  
  def isStateExist(self, table: Table):
    l = 0
    r = len(self.__list)

    while(l < r):
      mid = (l+r) // 2
      
      if self.__list[mid] == table:
        return True
      elif self.__list[mid] > table:
        r = mid
      else:
        l = mid + 1

    return False
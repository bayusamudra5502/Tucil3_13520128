from lib.Node import Node

class PrioQueue:
  def __init__(self) -> None:
    self.__queue = []
  
  def push(self, a: Node):
    self.__queue.append(a)

    for i in range(len(self.__queue), 0, -1):
      if self.__queue[i] < self.__queue[i-1]:
        self.__queue[i], self.__queue[i-1] = self.__queue[i-1], self.__queue[i]
      else:
        break
  
  def pop(self):
    res = self.__queue[0]
    self.__queue = self.__queue[1:]
    return res

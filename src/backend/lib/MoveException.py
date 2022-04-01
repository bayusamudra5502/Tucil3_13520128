class MoveException(Exception):
  def __init__(self, message: str, move: str) -> None:
      super().__init__(message)
      self.__move = move

  def getMove(self) -> str:
    return self.__move

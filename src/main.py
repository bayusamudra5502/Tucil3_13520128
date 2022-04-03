from lib.Node import Node
from lib.Solver import Solver
from lib.Table import Table
from lib.UnsolveableException import UnsolveableException

from datetime import datetime, timedelta

import sys

def main(filePath):
  file = open(filePath)

  contents = file.read()
  input = []

  for i in contents.split():
    if i == "-":
      input.append(16)
    else:
      input.append(int(i))

  print()

  table = Table(input)
  solver = Solver(table)
  start = datetime.now()
  try:
    print("\x1B[35mMatriks Input:\x1B[0m")
    printTable(table)
    print()

    solver.solve()

    print("\x1B[35mLangkah Penyelesaian:\x1B[0m\n")
    penjelajah = Node(table)
    cnt = 1
    for i in solver.getSolutions()[0].getMove():
      print("\x1B[36mLangkah\x1B[0m \x1B[33m%d\x1B[0m: \x1B[34m%s\x1B[0m" % (cnt, i))
      penjelajah = penjelajah.move(i)
      printTable(penjelajah.getTable())
      print()
      cnt += 1
    
    end = datetime.now()
    time = end - start
    printTime(time)
    print("Jumlah Langkah : \x1B[33m%d\x1B[0m langkah" % solver.getMinimalCost())
    print("Jumlah Node: \x1B[33m%d\x1B[0m node" % solver.getNodeNumber())
    print()
    
  except UnsolveableException:
    print("Hasil Proses:")
    print("\x1B[31mSolusi tidak ditemukan\x1B[0m")
    print()

    end = datetime.now()
    time = end - start
    printTime(time)
  finally:
    print("\x1B[35mData Instans:\x1B[0m")
    print("Jumlah Kurang(i) = \x1B[33m%d\x1B[0m" % table.fungsiKurang())
    print("Jumlah Kurang(i) + paritas = \x1B[33m%d\x1B[0m" % table.solvePoint())
  

def printTable(table: Table):
  num = 0

  for i in table.getTable():
    if((num + 1) % 4 != 0):
      if i < 10:
        print(" %d" % i, end=" ")
      else:
        print("%d" % i, end=" ")
    else:
      if i < 10:
        print(" %d" % i)
      else:
        print("%d" % i)
    
    num += 1

def printTime(ns: timedelta):
  if ns.microseconds < 1000:
    print("⌛ Time : \x1B[33m%d\x1B[0m us" % (ns.microseconds))
  elif ns.microseconds < 1_000_000:
    print("⌛ Time : \x1B[33m%d\x1B[0m ms" % (ns.microseconds / 1000))
  else:
    print("⌛ Time : \x1B[33m%d\x1B[0m s" % (ns.seconds))

  print()

if __name__ == "__main__":
  print("""\x1B[32m
 __ _____       _____               _      
/_ | ____|     |  __ \\             | |     
 | | |__ ______| |__) |   _ _______| | ___ 
 | |___ \\______|  ___/ | | |_  /_  / |/ _ \\
 | |___) |     | |   | |_| |/ / / /| |  __/
 |_|____/      |_|    \\__,_/___/___|_|\___|
                                           
\x1B[36mVersi 1.0.0\x1B[0m                                            
  """)
  if len(sys.argv) > 1:
    filePath = sys.argv[1]
    print("Membaca file \x1B[33m%s\x1B[0m" % filePath)
  else:
    filePath = input("Silahkan masukan file path : ")

  main(filePath)
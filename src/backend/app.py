#!/bin/python3

import sys
import uvicorn

from typing import List
from lib.Solver import Solver
from fastapi import FastAPI, UploadFile
from pydantic import BaseModel
from datetime import datetime

from lib.Table import Table
from lib.UnsolveableException import UnsolveableException

class InputTemplate(BaseModel):
  input: List[int]

app = FastAPI()

@app.get("/")
def homepage():
  return {"status": "success"}

@app.post("/solve/upload")
async def solve(file: UploadFile):
  contents = await file.read()
  input = []

  for i in contents.split():
    if i == b"-":
      input.append(16)
    else:
      input.append(int(i))

  try:
    result, length, node, ns = solve(input)
    
    return {
      "status": "success",
      "input": input,
      "length": length,
      "node": node,
      "time": ns,
      "result": result 
    }
  except UnsolveableException:
    return {
      "status": "success",
      "input": input,
      "length": 0,
      "result": [],
      "node": 0,
      "time": 0
    }


@app.post("/solve")
async def solve_manual(input: InputTemplate):
  try:
    result, length, node, ns = solve(input.input)
    
    return {
      "status": "success",
      "input": input.input,
      "length": length,
      "result": result,
      "node": node,
      "time": ns
    }
  except UnsolveableException:
    return {
      "status": "success",
      "input": input.input,
      "length": 0,
      "result": [],
      "node": 0,
      "time": 0
    }

def solve(input):
  table = Table(input)
  solver = Solver(table)

  start = datetime.now()
  solver.solve()
  end = datetime.now()
  result = []

  for i in solver.getSolutions():
    result.append({
      "moves": i.getMove(),
      "moveTables": i.getTable().getTable()
    })
  
  delta = end - start
  return result, len(result), solver.getNodeNumber(), delta.microseconds

if __name__ == "__main__":
  if len(sys.argv) > 1:
    uvicorn.run(app, host="0.0.0.0", port=int(sys.argv[1]))
  else:
    uvicorn.run(app, host="0.0.0.0", port=80)

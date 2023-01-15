from typing import Union

from fastapi import FastAPI
import uvicorn

import database
import operations

app = FastAPI()

@app.get("/read/All")
async def readAll():
    return operations.readAll()
@app.get("/read")
async def read(id):
    return operations.read(id)

@app.post("/create")
async def create(name:str,price:float,description:Union[str,None]=None):

    return operations.create(name,description,price)

@app.put("/update")
async def update(id,name:Union[str,None]=None,description:Union[str,None]=None,price:Union[float,None]=None):
    return operations.update(id,name,description,price)

@app.delete("/delete")
async def delete(id):
    return operations.delete(id)



# @app.get("/selectId")
# async def roo(id):
#     return database.start(id)
#
# @app.get("/")
# async def root():
#          return database.getAll()
#
# @app.delete("/delete")
# async def root(id):
#     return database.delete(id)
#
#
# @app.put("/update")
# async def root(id,isbn,name,author,section):
#     return database.update(id,isbn,name,author,section)
#
# @app.post("/create")
# async def root(id,isbn,name,author,section):
#     return database.create(id,isbn,name,author,section)

if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1',port=8010)
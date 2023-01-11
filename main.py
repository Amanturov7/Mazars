from fastapi import FastAPI
import uvicorn

import database


app = FastAPI()

@app.get("/selectId")
async def roo(id):
    return database.start(id)

@app.get("/")
async def root():
         return database.getAll()

@app.delete("/delete")
async def root(id):
    return database.delete(id)


@app.put("/update")
async def root(id,isbn,name,author,section):
    return database.update(id,isbn,name,author,section)

@app.post("/create")
async def root(id,isbn,name,author,section):
    return database.create(id,isbn,name,author,section)




# @app.get("/read")
# async def read():
#     return operations.read()
#
# @app.get("/write")
# async def write(id,name,description,price):
#     return operations.write(id,name,description,price)
#
# @app.get("/update")
# async def update(id,name,description,price):
#     return operations.update(id,name,description,price)
#
# @app.get("/delete")
# async def delete(id):
#     return operations.delete(id)
#


if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1',port=8010)
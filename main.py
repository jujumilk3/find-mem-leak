import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel, Field


class SimpleModel(BaseModel):
    name: str = Field(..., title="Name", description="Name of the item")
    description: str = Field(
        ..., title="Description", description="Description of the item"
    )


app = FastAPI()


@app.get("/async")
async def async_read_root():
    return {"Hello": "World"}


@app.get("/sync")
async def sync_read_root():
    return {"Hello": "World"}


@app.post("/async/pydantic")
async def create_item(item: SimpleModel):
    return item


test_stack = []


@app.get("/intended_mem_leak")
async def intended_mem_leak():
    global test_stack
    test_stack.append(str(len(test_stack)) * 10000)
    return {"Hello": "World", "len": len(test_stack)}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)

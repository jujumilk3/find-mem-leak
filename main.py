import gc

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


@app.get("/sync/check-object-count")
def sync_check_object_count():
    return {"object_count": len(gc.get_objects())}


@app.post("/async/pydantic")
async def create_item(item: SimpleModel):
    return item


@app.post("/sync/pydantic")
def create_item(item: SimpleModel):
    return {"item": item.model_dump(), "object_count": len(gc.get_objects())}


test_stack = []


@app.get("/intended_mem_leak")
async def intended_mem_leak():
    global test_stack
    # test_stack.append(str(len(test_stack)) * 10000)
    # if i use this, object count does not increase.
    # but it causes memory leak

    test_stack.append(["a"] * 10000)
    # if i use this, object count increases
    # very clear that it is a memory leak

    return {
        "Hello": "World",
        "len": len(test_stack),
        "object_count": len(gc.get_objects()),
    }


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)

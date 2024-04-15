from fastapi import FastAPI

app = FastAPI()


@app.get("/async")
async def async_read_root():
    return {"Hello": "World"}


@app.get("/sync")
async def sync_read_root():
    return {"Hello": "World"}

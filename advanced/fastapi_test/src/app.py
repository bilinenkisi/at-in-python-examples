from fastapi import FastAPI

app = FastAPI()

@app.get("/data")
def read_data():
    return {"items": ["a", "b", "c"]}



@app.get("/data/error")
def read_data():
    raise Exception("this is a test exception")
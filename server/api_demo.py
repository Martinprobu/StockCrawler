from pydantic import *
from fastapi import FastAPI

app = FastAPI()

class Item(BaseModel):
    a: int = None
    b: int = None

@app.post('/test_post')
def calculate(request_data: Item):
    a = request_data.a
    b = request_data.b
    c = a + b
    res = {"res":c}
    return res

@app.get('/test_get')
def calculate():
    res = {"res":123}
    return res

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app=app,
                host="0.0.0.0",
                port=8080,
                workers=1)


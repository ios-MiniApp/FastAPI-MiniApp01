from fastapi import FastAPI

# FastAPIのインスタンス化
app = FastAPI()
numbers = []

# asyncはなくてもOK、あれば非同期
@app.get("/")
async def index():
    return {'numbers': f'{numbers}'}

@app.post("/")
async def update_queri(number: int):
    numbers.append(number)
    return {'numbers': f'{numbers}'}

@app.post("/test/{number}")
async def update_path(number: int):
    numbers.append(number)
    return {'numbers': f'{numbers}'}

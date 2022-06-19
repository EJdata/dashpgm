from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def welcome():
    x = {"message: HELLO WORLD!!! Welcome to fastAPI!!! Free tacos"}
    return x

@app.get("/taco")
def welcome():
    x = {"message: tacotuesday, salsa, guac, tomatoes"}
    return x

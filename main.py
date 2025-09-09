from fastapi import FastAPI
from random import randint,choice
import json
app = FastAPI()

#1-kod
@app.get('/')
async def say_hello():
    return {
            "Salom FastAPI!"
        }
    
#2-kod
@app.get("/fikr")
async def fikr():
    return {
        "FastAPI juda zo‘r framework!"
    }
    
#3-kod
@app.get("/ism")
async def ism():
    return {
        "Mening ismim Shohjahon"
        }
    
#4-kod
@app.get("/yosh")
async def yosh():
    return {
        f"Mening yoshim 19 da"
    }
    
#5-kod
@app.get("/fanlar")
async def fanlar():
    return ["Matematika", "Fizika", "Ingliz tili"]

#6-kod
@app.get("/talaba")
async def talaba():
    return {
  "ism": "Ali",
  "yosh": 20
}

#7-misol
@app.get("/tasodifiy-son")
async def random_son():
    
    num = randint(1,100)
    
    return {
        "son": num
        }

#8-misol   
@app.get("/tasodifiy-fan")
async def random_fan():
    fanlar = ["Matematika", "Fizika", "Ingliz tili", "Tarix", "Biologiya"]
    tas_fan = choice(fanlar)
    
    return {"fan": tas_fan}

#9-misol
@app.get("/tasodifiy-talaba")
async def talaba():
    
    ismlar = ["Ali", "Vali", "Dilshod", "Aziza", "Malika", "Javlon"]
    ism = choice(ismlar)
    yosh = randint(18, 50)
    return {"ism": ism, "yosh": yosh}
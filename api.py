import os
from fastapi import FastAPI
from calc import Calc

app = FastAPI()
calc = Calc()

@app.get("/")
def read_root():
    return {"container_id": os.environ.get('HOSTNAME') or "Running in cloud"}

@app.get("/health")
def read_root():
    return {"status": "DevOps Days - Mi Primer Container Cloud"}

@app.get("/sumar")
def read_sumar(num1: int = 0, num2: int = 0):
    return  {
        "total": calc.sumar(num1, num2)
    }

@app.get("/restar")
def read_sumar(num1: int = 0, num2: int = 0):
    return  {
        "total": calc.restar(num1, num2)
    }    

@app.get("/multiplicar")
def read_sumar(num1: int = 0, num2: int = 0):
    return  {
        "total": calc.multiplicar(num1, num2)
    }   

@app.get("/dividir")
def read_sumar(num1: int = 0, num2: int = 0):
    return  {
        "total": calc.dividir(num1, num2)
    }           

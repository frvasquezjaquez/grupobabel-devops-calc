# Calculadora API

## Funcionalidades
    * Suma de 2 numeros
    * Resta de 2 Numeros
    * Multiplicacion de Numeros
    * Division de 2 numneros
 
# Requirements
- Docker
- Python3


# Tests

## Run unittest + Coverage
```
coverage run my-unittest.py
coverage report -m --fail-under=80 #Falla sino llegamos al 80% de coverage
```


## Run Integration Tests
```
behave tests/Integracion
```


# Run App
```
    uvicorn --host 0.0.0.0 --port 8000 api:app
```
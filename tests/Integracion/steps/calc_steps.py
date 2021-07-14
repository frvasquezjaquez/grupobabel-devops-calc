from behave import *
import api
from fastapi.testclient import TestClient

@given("que quiero realizar operaciones aritméticas")
def step_implementation(context):
    context.app = TestClient(api.app)

@when('desee {operacion} {num1} y {num2}')
def step_implementation(context, operacion, num1, num2,):
    context.api_response = context.app.get(f'/{operacion}?num1={num1}&num2={num2}')
    assert 200 == context.api_response.status_code

@then('El resultado debe ser {result}')
def step_implementation(context, result):
    assert str(result) == str(context.api_response.json().get('total'))   
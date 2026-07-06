from pytest_bdd import given, when, then
from order import calculate_total

@given('que o pedido possui os itens 10, 20, 30', target_fixture="pedido_itens")
def pedido_itens():
    return [10, 20, 30]

@when("o sistema calcula o valor total", target_fixture="total")
def calculate(pedido_itens):
    return calculate_total(pedido_itens)

@then("o resultado deve ser 60")
def check_total(total):
    assert total == 60
from pytest_bdd import scenarios, given, when, then
from order import calculate_total

scenarios('features')

@given('que o pedido possui os itens 10, 20, 30', target_fixture="order_items")
def pedido_itens():
    return [10, 20, 30]

@when("o sistema calcula o valor total", target_fixture="total")
def calculate(order_items): 
    return calculate_total(order_items)

@then("o resultado deve ser 60")
def check_total(total):
    assert total == 60
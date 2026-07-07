from pytest_bdd import given, when, then
from order import calculate_total
from pytest_bdd import scenarios

scenarios("features/order_total.feature")


@given('que o pedido possui os itens 10, 20 e 30', target_fixture="order_items")
def pedido_itens():
    return [10, 20, 30]

@when("o sistema calcula o valor total", target_fixture="total")
def calculate(order_items): 
    return calculate_total(order_items)

@then("o resultado deve ser 60")
def check_total(total):
    assert total == 60



@given('que o pedido possui apenas o item 45', target_fixture="order_items")
def pedido_um_item():
    return [45]


@then("o resultado deve ser 45")
def check_total_um_item(total):
    assert total == 45


@given('que o valor total do pedido é 100', target_fixture="order_total_base")
def total_base():
    return 100

@when('é aplicado um desconto de 10 por cento', target_fixture="total_com_desconto")
def aplicar_desconto(order_total_base):
    return calculate_total(order_total_base, discount=10)

@then('o valor final deve ser 90')
def check_valor_final(total_com_desconto):
    assert total_com_desconto == 90
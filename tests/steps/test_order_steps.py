from pytest_bdd import given, when, then
from order import calculate_total, apply_discount

# --- CENÁRIO 1: Somar os valores dos itens ---

@given("que o pedido possui os itens 10, 20 e 30", target_fixture="order_items")
def order_items():
    return [10, 20, 30]

@when("o sistema calcula o valor total", target_fixture="total")
def calculate(order_items):
    return calculate_total(order_items)

@then("o resultado deve ser 60")
def check_total(total):
    assert total == 60


# --- CENÁRIO 2: Pedido com apenas um item ---

@given("que o pedido possui apenas o item 45", target_fixture="single_order_item")
def single_order_item():
    return [45]

@when("o sistema calcula o valor total de um pedido com um item", target_fixture="single_total")
def calculate_single(single_order_item):
    return calculate_total(single_order_item)

@then("o resultado deve ser 45")
def check_single_total(single_total):
    assert single_total == 45


# --- CENÁRIO 3: Aplicar desconto de 10 por cento ---

@given("que o valor total do pedido é 100", target_fixture="discount_total")
def discount_total():
    return 100

@when("o sistema aplica um desconto de 10 por cento", target_fixture="discounted_value")
def apply_discount_step(discount_total):
    return apply_discount(discount_total, 10)

@then("o valor final deve ser 90")
def check_discount(discounted_value):
    assert discounted_value == 90
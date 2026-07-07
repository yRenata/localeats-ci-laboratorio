def calculate_total(items: list[float]) -> float:
    """
    Calcula e retorna o valor total de uma lista de itens.

    Args:
        items: Lista de valores dos itens do pedido.

    Returns:
        A soma de todos os valores da lista.

    Raises:
        TypeError: Se algum item não for numérico.
        ValueError: Se algum item for negativo.
    """
    for item in items:
        if not isinstance(item, (int, float)):
            raise TypeError("Todos os itens devem ser numéricos")
        if item < 0:
            raise ValueError("Os valores dos itens não podem ser negativos")

    return sum(items)


def apply_discount(total: float, discount_percent: float) -> float:
    """
    Aplica um desconto percentual ao valor total.

    Args:
        total: Valor total do pedido.
        discount_percent: Percentual de desconto.

    Returns:
        Valor final com desconto aplicado.
    """
    return total - (total * discount_percent / 100)
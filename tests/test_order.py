import pytest
from order import calculate_total, apply_discount


def test_calculate_total():
    assert calculate_total([10, 20, 30]) == 60


def test_calculate_total_lista_vazia():
    assert calculate_total([]) == 0


def test_apply_discount():
    assert apply_discount(100, 10) == 90


def test_calculate_total_nao_deve_aceitar_valores_negativos():
    with pytest.raises(ValueError, match="Os valores dos itens não podem ser negativos"):
        calculate_total([-10, 20, 30])


def test_calculate_total_nao_deve_aceitar_strings():
    with pytest.raises(TypeError, match="Todos os itens devem ser numéricos"):
        calculate_total(["abc", 20, 30])
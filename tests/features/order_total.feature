Feature: Calculo do total do pedido
  Como cliente do LocalEats,
  desejo que o sistema calcule o total do meu pedido,
  para que eu saiba o valor final da compra.

  Scenario: Somar os valores dos itens
    Given que o pedido possui os itens 10, 20 e 30
    When o sistema calcula o valor total
    Then o resultado deve ser 60

  Scenario: Pedido com apenas um item
    Given que o pedido possui apenas o item 45
    When o sistema calcula o valor total de um pedido com um item
    Then o resultado deve ser 45

  Scenario: Aplicar desconto de 10 por cento
    Given que o valor total do pedido é 100
    When o sistema aplica um desconto de 10 por cento
    Then o valor final deve ser 90
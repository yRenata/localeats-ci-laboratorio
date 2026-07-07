from pytest_bdd import scenarios
# Importa de forma limpa todas as funções de step que você criou no outro arquivo
from tests.steps.test_order_steps import *

# Vincula e roda os cenários do arquivo .feature
scenarios('features')
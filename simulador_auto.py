from simulador_auto_v1 import parcela48
from simulador_auto_v2 import parcela60
from simulador_auto_v3 import parcela70

valor_produto = float(input('Valor do produto: '))
valor_credito = float(input('Valor do crédito sugerido: '))
quantidade_parcelas = int(input('Em quantas parcelas: '))

lance = valor_credito - valor_produto
porcentagem = float((lance*100)/valor_credito)
porcentagem_produto = valor_produto * (porcentagem/100)
credito = valor_produto + porcentagem_produto

if quantidade_parcelas == 48:
    parcela48(quantidade_parcelas,valor_credito, porcentagem, porcentagem_produto,lance)
elif quantidade_parcelas == 60:
    parcela60(quantidade_parcelas,valor_credito, porcentagem, porcentagem_produto,lance)
elif quantidade_parcelas == 70:
    parcela70(quantidade_parcelas,valor_credito, porcentagem, porcentagem_produto,lance)
else: 
    print('Parcelas incorretas!')

print('O valor do credito será de : R$ {:.2f}'. format(valor_credito))
print('O tempo de pagamento será de {} meses, ou {} anos'.format(quantidade_parcelas, quantidade_parcelas/12))
print('O valor total pago do cliente {:.2f}'.format(credito))

def parcela60(quantidade_parcelas,valor_credito, porcentagem, porcentagem_produto,lance):
    if 10.0 <= porcentagem <= 50.0: 
        if valor_credito == 25000 and quantidade_parcelas == 60:
            entrada = float(1918.37)
            abatimento = float(498.36) * (porcentagem/100)
            valor_parcela = float(498.36 - abatimento)
            print('A entrada ficará de R$ {:.2f}'.format(entrada))
            print('A parcela ficará de R$ {:.2f}'.format(valor_parcela))    
        elif valor_credito == 30000 and quantidade_parcelas == 60:
            entrada = float(2302.03)
            abatimento = float(598.03) * (porcentagem/100)
            valor_parcela = float(598.03) - abatimento
            print('A entrada ficará no valor de R$ {}'.format(entrada))
            print('A parcela ficará de R$ {:.2f}'.format(valor_parcela))
        elif valor_credito == 35000 and quantidade_parcelas == 60:
            entrada = float(2685.71)
            abatimento = float(697.70) * (porcentagem/100)
            valor_parcela = float(697.70) - abatimento
            print('A entrada ficará no valor de R$ {}'.format(entrada))
            print('A parcela ficará de R$ {:.2f}'.format(valor_parcela))
        elif valor_credito == 40000 and quantidade_parcelas == 60:
            entrada = float(3069.37)
            abatimento = float(797.37) * (porcentagem/100)
            valor_parcela = float(797.37) - abatimento
            print('A entrada ficará no valor de R$ {}'.format(entrada))
            print('A parcela ficará de R$ {:.2f}'.format(valor_parcela))
        elif valor_credito == 45000 and quantidade_parcelas == 60:
            entrada = float(3453.05)
            abatimento = float(897.04) * (porcentagem/100)
            valor_parcela = float(897.04) - abatimento
            print('A entrada ficará no valor de R$ {}'.format(entrada))
            print('A parcela ficará de R$ {:.2f}'.format(valor_parcela))
        elif valor_credito == 50000 and quantidade_parcelas == 60:
            entrada = float(3836.71)
            abatimento = float(996.71) * (porcentagem/100)
            valor_parcela = float(996.71) - abatimento
            print('A entrada ficará no valor de R$ {}'.format(entrada))
            print('A parcela ficará de R$ {:.2f}'.format(valor_parcela))
        elif valor_credito == 55000 and quantidade_parcelas == 60:
            entrada = float(4220.40)
            abatimento = float(1096.39) * (porcentagem/100)
            valor_parcela = float(1096.39) - abatimento
            print('A entrada ficará no valor de R$ {}'.format(entrada))
            print('A parcela ficará de R$ {:.2f}'.format(valor_parcela))
        elif valor_credito == 60000 and quantidade_parcelas == 60:
            entrada = float(4604.05)
            abatimento = float(1196.05) * (porcentagem/100)
            valor_parcela = float(1196.05) - abatimento
            print('A entrada ficará no valor de R$ {}'.format(entrada))
            print('A parcela ficará de R$ {:.2f}'.format(valor_parcela))
        print('O lance será no valor de R$ {:.2f}, que corresponde a {:.0f}% da carta.'.format(lance, porcentagem))    
    else:
        print('O valor do lance ultrapassa os 50%, reveja a condição de crédito.')
        porcentagem_sugerida = float(input('Porcentagem sugerida: '))
        lance = valor_credito * (porcentagem_sugerida/100)
        credito_cliente = valor_credito - lance
        if valor_credito == 25000 and quantidade_parcelas == 60:
            entrada = float(1918.37)
            abatimento = float(498.36) * (porcentagem_sugerida/100)
            valor_parcela = float(498.36 - abatimento)
            print('A entrada ficará de R$ {:.2f}'.format(entrada))
            print('A parcela ficará de R$ {:.2f}'.format(valor_parcela))    
        elif valor_credito == 30000 and quantidade_parcelas == 60:
            entrada = float(2302.03)
            abatimento = float(598.03) * (porcentagem_sugerida/100)
            valor_parcela = float(598.03) - abatimento
            print('A entrada ficará no valor de R$ {}'.format(entrada))
            print('A parcela ficará de R$ {:.2f}'.format(valor_parcela))
        elif valor_credito == 35000 and quantidade_parcelas == 60:
            entrada = float(2685.71)
            abatimento = float(697.70) * (porcentagem_sugerida/100)
            valor_parcela = float(697.70) - abatimento
            print('A entrada ficará no valor de R$ {}'.format(entrada))
            print('A parcela ficará de R$ {:.2f}'.format(valor_parcela))
        elif valor_credito == 40000 and quantidade_parcelas == 60:
            entrada = float( 3069.37)
            abatimento = float(797.37) * (porcentagem_sugerida/100)
            valor_parcela = float(797.37) - abatimento
            print('A entrada ficará no valor de R$ {}'.format(entrada))
            print('A parcela ficará de R$ {:.2f}'.format(valor_parcela))
        elif valor_credito == 45000 and quantidade_parcelas == 60:
            entrada = float(3453.05)
            abatimento = float(897.04) * (porcentagem_sugerida/100)
            valor_parcela = float(897.04) - abatimento
            print('A entrada ficará no valor de R$ {}'.format(entrada))
            print('A parcela ficará de R$ {:.2f}'.format(valor_parcela))
        elif valor_credito == 50000 and quantidade_parcelas == 60:
            entrada = float(3836.71)
            abatimento = float(996.71) * (porcentagem_sugerida/100)
            valor_parcela = float(996.71) - abatimento
            print('A entrada ficará no valor de R$ {}'.format(entrada))
            print('A parcela ficará de R$ {:.2f}'.format(valor_parcela))
        elif valor_credito == 55000 and quantidade_parcelas == 60:
            entrada = float(4220.40)
            abatimento = float(1096.39) * (porcentagem_sugerida/100)
            valor_parcela = float(1096.39 ) - abatimento
            print('A entrada ficará no valor de R$ {}'.format(entrada))
            print('A parcela ficará de R$ {:.2f}'.format(valor_parcela))
        elif valor_credito == 60000 and quantidade_parcelas == 60:
            entrada = float(4604.05)
            abatimento = float(1196.05) * (porcentagem_sugerida/100)
            valor_parcela = float(1196.05) - abatimento
            print('A entrada ficará no valor de R$ {}'.format(entrada))
            print('A parcela ficará de R$ {:.2f}'.format(valor_parcela))
        print('O lance será no valor de R$ {:.2f}, que corresponde a {:.0f}% da carta.'. format(lance, porcentagem_sugerida))
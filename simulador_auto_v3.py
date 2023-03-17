def parcela70(quantidade_parcelas,valor_credito, porcentagem, porcentagem_produto,lance):
    if 10.0 <= porcentagem <= 50.0: 
        if valor_credito == 25000 and quantidade_parcelas == 70:
            entrada = float(1879.74)
            abatimento = float(430.49) * (porcentagem/100)
            valor_parcela = float(430.49 - abatimento)
            print('A entrada ficará de R$ {:.2f}'.format(entrada))
            print('A parcela ficará de R$ {:.2f}'.format(valor_parcela))    
        elif valor_credito == 30000 and quantidade_parcelas == 70:
            entrada = float(2255.68)
            abatimento = float(516.58) * (porcentagem/100)
            valor_parcela = float(516.58) - abatimento
            print('A entrada ficará no valor de R$ {}'.format(entrada))
            print('A parcela ficará de R$ {:.2f}'.format(valor_parcela))
        elif valor_credito == 35000 and quantidade_parcelas == 70:
            entrada = float(2631.63)
            abatimento = float(602.68) * (porcentagem/100)
            valor_parcela = float(602.68) - abatimento
            print('A entrada ficará no valor de R$ {}'.format(entrada))
            print('A parcela ficará de R$ {:.2f}'.format(valor_parcela))
        elif valor_credito == 40000 and quantidade_parcelas == 70:
            entrada = float(3007.57)
            abatimento = float(688.77) * (porcentagem/100)
            valor_parcela = float(688.77) - abatimento
            print('A entrada ficará no valor de R$ {}'.format(entrada))
            print('A parcela ficará de R$ {:.2f}'.format(valor_parcela))
        elif valor_credito == 45000 and quantidade_parcelas == 70:
            entrada = float(3383.52)
            abatimento = float(774.87) * (porcentagem/100)
            valor_parcela = float(774.87) - abatimento
            print('A entrada ficará no valor de R$ {}'.format(entrada))
            print('A parcela ficará de R$ {:.2f}'.format(valor_parcela))
        elif valor_credito == 50000 and quantidade_parcelas == 70:
            entrada = float(3759.46)
            abatimento = float(860.96) * (porcentagem/100)
            valor_parcela = float(860.96) - abatimento
            print('A entrada ficará no valor de R$ {}'.format(entrada))
            print('A parcela ficará de R$ {:.2f}'.format(valor_parcela))
        elif valor_credito == 55000 and quantidade_parcelas == 70:
            entrada = float(4135.42)
            abatimento = float(947.07) * (porcentagem/100)
            valor_parcela = float(947.07) - abatimento
            print('A entrada ficará no valor de R$ {}'.format(entrada))
            print('A parcela ficará de R$ {:.2f}'.format(valor_parcela))
        elif valor_credito == 60000 and quantidade_parcelas == 70:
            entrada = float(4511.35)
            abatimento = float(1033.15) * (porcentagem/100)
            valor_parcela = float(1033.15) - abatimento
            print('A entrada ficará no valor de R$ {}'.format(entrada))
            print('A parcela ficará de R$ {:.2f}'.format(valor_parcela))
        print('O lance será no valor de R$ {:.2f}, que corresponde a {:.0f}% da carta.'.format(lance, porcentagem))    
    else:
        print('O valor do lance ultrapassa os 50%, reveja a condição de crédito.')
        porcentagem_sugerida = float(input('Porcentagem sugerida: '))
        lance = valor_credito * (porcentagem_sugerida/100)
        credito_cliente = valor_credito - lance
        if valor_credito == 25000 and quantidade_parcelas == 70:
            entrada = float(1879.74)
            abatimento = float(430.49) * (porcentagem_sugerida/100)
            valor_parcela = float(430.49 - abatimento)
            print('A entrada ficará de R$ {:.2f}'.format(entrada))
            print('A parcela ficará de R$ {:.2f}'.format(valor_parcela))    
        elif valor_credito == 30000 and quantidade_parcelas == 70:
            entrada = float(2255.68)
            abatimento = float(516.58) * (porcentagem_sugerida/100)
            valor_parcela = float(516.58) - abatimento
            print('A entrada ficará no valor de R$ {}'.format(entrada))
            print('A parcela ficará de R$ {:.2f}'.format(valor_parcela))
        elif valor_credito == 35000 and quantidade_parcelas == 70:
            entrada = float(2631.63)
            abatimento = float(602.68) * (porcentagem_sugerida/100)
            valor_parcela = float(602.68) - abatimento
            print('A entrada ficará no valor de R$ {}'.format(entrada))
            print('A parcela ficará de R$ {:.2f}'.format(valor_parcela))
        elif valor_credito == 40000 and quantidade_parcelas == 70:
            entrada = float(3007.57)
            abatimento = float(688.77) * (porcentagem_sugerida/100)
            valor_parcela = float(688.77) - abatimento
            print('A entrada ficará no valor de R$ {}'.format(entrada))
            print('A parcela ficará de R$ {:.2f}'.format(valor_parcela))
        elif valor_credito == 45000 and quantidade_parcelas == 70:
            entrada = float(3383.52)
            abatimento = float(774.87) * (porcentagem_sugerida/100)
            valor_parcela = float(774.87) - abatimento
            print('A entrada ficará no valor de R$ {}'.format(entrada))
            print('A parcela ficará de R$ {:.2f}'.format(valor_parcela))
        elif valor_credito == 50000 and quantidade_parcelas == 70:
            entrada = float(3759.46)
            abatimento = float(860.96) * (porcentagem_sugerida/100)
            valor_parcela = float(860.96) - abatimento
            print('A entrada ficará no valor de R$ {}'.format(entrada))
            print('A parcela ficará de R$ {:.2f}'.format(valor_parcela))
        elif valor_credito == 55000 and quantidade_parcelas == 70:
            entrada = float(4135.42)
            abatimento = float(947.07) * (porcentagem_sugerida/100)
            valor_parcela = float(947.07) - abatimento
            print('A entrada ficará no valor de R$ {}'.format(entrada))
            print('A parcela ficará de R$ {:.2f}'.format(valor_parcela))
        elif valor_credito == 60000 and quantidade_parcelas == 70:
            entrada = float(4511.35)
            abatimento = float(1033.15) * (porcentagem_sugerida/100)
            valor_parcela = float(1033.15) - abatimento
            print('A entrada ficará no valor de R$ {}'.format(entrada))
            print('A parcela ficará de R$ {:.2f}'.format(valor_parcela))
        print('O lance será no valor de R$ {:.2f}, que corresponde a {:.0f}% da carta.'. format(lance, porcentagem_sugerida))
def parcela48(quantidade_parcelas,valor_credito, porcentagem, porcentagem_produto,lance):

    if 10.0 <= porcentagem <= 50.0: 
        if valor_credito == 25000 and quantidade_parcelas == 48:
            entrada = float(1956.36)
            abatimento = float(618.08) * (porcentagem/100)
            valor_parcela = float(618.08 - abatimento)
            print('A entrada ficará de R$ {:.2f}'.format(entrada))
            print('A parcela ficará de R$ {:.2f}'.format(valor_parcela))    
        elif valor_credito == 30000 and quantidade_parcelas == 48:
            entrada = float(2347.63)
            abatimento = float(741.70) * (porcentagem/100)
            valor_parcela = float(741.70) - abatimento
            print('A entrada ficará no valor de R$ {}'.format(entrada))
            print('A parcela ficará de R$ {:.2f}'.format(valor_parcela))
        elif valor_credito == 35000 and quantidade_parcelas == 48:
            entrada = float(2738.90)
            abatimento = float(865.31) * (porcentagem/100)
            valor_parcela = float(865.31) - abatimento
            print('A entrada ficará no valor de R$ {}'.format(entrada))
            print('A parcela ficará de R$ {:.2f}'.format(valor_parcela))
        elif valor_credito == 40000 and quantidade_parcelas == 48:
            entrada = float(3130.17)
            abatimento = float(988.93) * (porcentagem/100)
            valor_parcela = float(988.93) - abatimento
            print('A entrada ficará no valor de R$ {}'.format(entrada))
            print('A parcela ficará de R$ {:.2f}'.format(valor_parcela))
        elif valor_credito == 45000 and quantidade_parcelas == 48:
            entrada = float(3521.44)
            abatimento = float(1112.54) * (porcentagem/100)
            valor_parcela = float(1112.54) - abatimento
            print('A entrada ficará no valor de R$ {}'.format(entrada))
            print('A parcela ficará de R$ {:.2f}'.format(valor_parcela))
        elif valor_credito == 50000 and quantidade_parcelas == 48:
            entrada = float(3912.71)
            abatimento = float(1236.16) * (porcentagem/100)
            valor_parcela = float(1236.16) - abatimento
            print('A entrada ficará no valor de R$ {}'.format(entrada))
            print('A parcela ficará de R$ {:.2f}'.format(valor_parcela))
        elif valor_credito == 55000 and quantidade_parcelas == 48:
            entrada = float(4303.99)
            abatimento = float(1359.78) * (porcentagem/100)
            valor_parcela = float(1359.78) - abatimento
            print('A entrada ficará no valor de R$ {}'.format(entrada))
            print('A parcela ficará de R$ {:.2f}'.format(valor_parcela))
        elif valor_credito == 60000 and quantidade_parcelas == 48:
            entrada = float(4695.25)
            abatimento = float(1483.39) * (porcentagem/100)
            valor_parcela = float(1483.39) - abatimento
            print('A entrada ficará no valor de R$ {}'.format(entrada))
            print('A parcela ficará de R$ {:.2f}'.format(valor_parcela))
        print('O lance será no valor de R$ {:.2f}, que corresponde a {:.0f}% da carta.'.format(lance, porcentagem))    
    else:
        print('O valor do lance ultrapassa os 50%, reveja a condição de crédito.')
        porcentagem_sugerida = float(input('Porcentagem sugerida: '))
        lance = valor_credito * (porcentagem_sugerida/100)
        credito_cliente = valor_credito - lance
        if valor_credito == 25000 and quantidade_parcelas == 48:
            entrada = float(1956.36)
            abatimento = float(618.08) * (porcentagem_sugerida/100)
            valor_parcela = float(618.08 - abatimento)
            print('A entrada ficará de R$ {:.2f}'.format(entrada))
            print('A parcela ficará de R$ {:.2f}'.format(valor_parcela))    
        elif valor_credito == 30000 and quantidade_parcelas == 48:
            entrada = float(2347.63)
            abatimento = float(741.70) * (porcentagem_sugerida/100)
            valor_parcela = float(741.70) - abatimento
            print('A entrada ficará no valor de R$ {}'.format(entrada))
            print('A parcela ficará de R$ {:.2f}'.format(valor_parcela))
        elif valor_credito == 35000 and quantidade_parcelas == 48:
            entrada = float(2738.90)
            abatimento = float(865.31) * (porcentagem_sugerida/100)
            valor_parcela = float(865.31) - abatimento
            print('A entrada ficará no valor de R$ {}'.format(entrada))
            print('A parcela ficará de R$ {:.2f}'.format(valor_parcela))
        elif valor_credito == 40000 and quantidade_parcelas == 48:
            entrada = float(3130.17)
            abatimento = float(988.93) * (porcentagem_sugerida/100)
            valor_parcela = float(988.93) - abatimento
            print('A entrada ficará no valor de R$ {}'.format(entrada))
            print('A parcela ficará de R$ {:.2f}'.format(valor_parcela))
        elif valor_credito == 45000 and quantidade_parcelas == 48:
            entrada = float(3521.44)
            abatimento = float(1112.54) * (porcentagem_sugerida/100)
            valor_parcela = float(1112.54) - abatimento
            print('A entrada ficará no valor de R$ {}'.format(entrada))
            print('A parcela ficará de R$ {:.2f}'.format(valor_parcela))
        elif valor_credito == 50000 and quantidade_parcelas == 48:
            entrada = float(3912.71)
            abatimento = float(1236.16) * (porcentagem_sugerida/100)
            valor_parcela = float(1236.16) - abatimento
            print('A entrada ficará no valor de R$ {}'.format(entrada))
            print('A parcela ficará de R$ {:.2f}'.format(valor_parcela))
        elif valor_credito == 55000 and quantidade_parcelas == 48:
            entrada = float(4303.99)
            abatimento = float(1359.78) * (porcentagem_sugerida/100)
            valor_parcela = float(1359.78) - abatimento
            print('A entrada ficará no valor de R$ {}'.format(entrada))
            print('A parcela ficará de R$ {:.2f}'.format(valor_parcela))
        elif valor_credito == 60000 and quantidade_parcelas == 48:
            entrada = float(4695.25)
            abatimento = float(1483.39) * (porcentagem_sugerida/100)
            valor_parcela = float(1483.39) - abatimento
            print('A entrada ficará no valor de R$ {}'.format(entrada))
            print('A parcela ficará de R$ {:.2f}'.format(valor_parcela))
        print('O lance será no valor de R$ {:.2f}, que corresponde a {:.0f}% da carta.'. format(lance, porcentagem_sugerida))

        
divida_total = int(input())
pagamento_mensal = int(input())

numero_de_parcelas = divida_total // pagamento_mensal
resto = divida_total % pagamento_mensal

for i in range(numero_de_parcelas):
    print('pagamento:', i + 1)
    print('antes =', divida_total - pagamento_mensal * i)
    print('depois =', divida_total - pagamento_mensal * (i + 1))
    print('-----')

    if resto != 0:
        print('pagamento:', numero_de_parcelas + 1)
        print('antes = ', divida_total - pagamento_mensal * numero_de_parcelas)
        print('depois = ', divida_total - pagamento_mensal * numero_de_parcelas - resto)
        print('-----')
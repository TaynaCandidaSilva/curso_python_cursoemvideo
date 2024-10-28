print ('--------------------------Loja DEV-------------------------------------')
preco = float(input('Valor das compras: R$ '))
print ('''FORMA DE PAGAMENTO
[ 1 ] à vista dinheiro / cheque
[ 2 ] à vista cartão
[ 3 ] 2X no cartão
[ 4 ] 3X ou mais no cartão''')
op = int(input('Qual a opção de pagamento? '))
if op == 1:
    print (f'O valor total da compra é de {preco:.2f}')
    total = preco*0.90
    print (f'Valor total a ser pago com 10% de desconto R$ {total:.2f}')
elif op == 2:
    print (f'O valor total da compra é de {preco:.2f}')
    total = preco*0.95
    print (f'Valor total a ser pago com 5% de desconto R$ {total:.2f}')
elif op == 3:
    print (f'O total da sua compra é de R$ {preco:.2f}')
    parcela = preco/2
    print (f'Sua compra será parcelada em 2X de R$ {parcela} SEM JUROS!')
elif op == 4:
    print (f'O total da sua compra é de R$ {preco:.2f}')
    vezes = int (input('Quantas parcelas: '))
    parcela = (preco*1.20)/vezes
    print (f'Sua compra será parcelada em {vezes}X de {parcela} COM JUROS!')
    print (f'Sua compra de {preco} vai custar {preco*1.20:.2f} no final')
else:
    print ('Opção de pagamento inválida, tente novamente!')
    

    

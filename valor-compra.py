#Orientação ao usuario.
valor_compra = float(input( "Digite o valor da compra R$"))
#Calculo de desconto de acordo com o valor da compra
if valor_compra < 200:
    desconto = valor_compra * 0.05
elif valor_compra >= 200 and valor_compra < 300:
    desconto = valor_compra * 0.10
elif valor_compra >= 300:
    desconto = valor_compra * 0.15
    #Resultados do desconto e do valor total da compra.
valor_final= valor_compra - desconto
print("O valor de desconto da compra foi de R$", desconto)
print("O valor da compra foi de R$", valor_final)








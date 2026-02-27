nome_do_cliente =str(input("qual e o seu nome?"))
valor_compra =float(input("qual o valor da compra?"))
entrega =int(input("qual a distancia em km?"))
cupom =input("qual e cupom? (S/N): ")
frete = 40.00



if valor_compra >= 1.000 and cupom == 's':
    desconto = valor_compra * 0.20
    valor_total = valor_compra - desconto

elif valor_compra > 500.00 < 1.000 and cupom == 's':
    desconto = valor_compra * 0.10

    valor_total = valor_compra - desconto


if valor_total >= 200.00 and entrega <= 50.00:
    frete = 0.00
    valor_final = valor_total + frete
else:
    valor_final = valor_total + frete

print ('seu nome e' , nome_do_cliente)
print ('o valor da compra e' , valor_compra)
print ('valor total' , valor_total)
print ('valor final e ' , valor_final)




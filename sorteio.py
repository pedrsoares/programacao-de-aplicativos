id =int(input("qual o id do usuario?"))
valor =float(input("qual o valor da compra?"))
if id % 2 == 0 and valor > 500:
    print(f"Parabéns, usuário {id}! Você ganhou um cupom para sua compra de R$ {valor}.")
else:
    print(f"Obrigado pela compra, usuário {id}. Continue acompanhando nossas promoções!")

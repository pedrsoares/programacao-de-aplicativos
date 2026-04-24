def sofrer_dano(valor_dano):
    global vida
    vida -= valor_dano
vida = 100
print("__ INICIO DA BATALHA __")
while vida > 0:
    dano = float(input(f"vida atual: {vida}, quando de dano ele sofreu"))
    sofrer_dano(dano)
print ("vida 0, game over")
def analisa_vendas(nome, lista, meta_mensal):
    media = sum(lista_vendas) / len(lista_vendas)
    bateu_meta = media >= meta_mensal
    status = "bateu" if bateu_meta else "nao bateu"

    return f"o vendedor {nome} teve media de {media} e {status} a meta"

nome_vendedor = "carlos"
vendas = [1200, 1500, 11000, 1900]
meta = 1400

print(analisa_vendas(nome_vendedor, vendas, meta))

def converter_km_para_ms(velocidade_km):
    return velocidade_km / 3.6

vel = float(input("digite a velocidade em km/h"))

if vel > 80:
    ms = converter_km_para_ms(vel)
else:
    print("velocidade dentro do limite")
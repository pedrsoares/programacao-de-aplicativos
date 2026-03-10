id_funcionario = int(input("Digite o ID do funcionário: "))
temperatura = float(input("Digite a temperatura da máquina (°C): "))
tempo_uso = float(input("Digite o tempo de uso da máquina (horas): "))
if (id_funcionario % 3 == 0) and (temperatura > 40 or tempo_uso > 8):
    print(f"Funcionário {id_funcionario}, você foi escalado para a manutenção preventiva hoje.")
else:
    print(f"Funcionário {id_funcionario}, sua máquina opera dentro dos padrões normais.")
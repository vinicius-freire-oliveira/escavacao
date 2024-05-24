"""
Empolamento - material solto, acréscimo no volume do material original após a escavação, expresso em % do volume original.

O fator de conversão é exatamente a noção inversa do empolamento. Ele representa a relação entre o volume no corte e o volume solto.
"""

def calcular_volume_transportado(volume_escavado, empolamento):
    # Convertendo o empolamento para uma fração
    taxa_empolamento = empolamento / 100
    
    # Calculando o volume a ser transportado
    volume_transportado = volume_escavado * (1 + taxa_empolamento)
    
    return volume_transportado

def calcular_quantidade_caminhoes(volume_transportado, capacidade_caminhao):
    # Calculando a quantidade de caminhões necessários
    quantidade_caminhoes = volume_transportado / capacidade_caminhao
    return quantidade_caminhoes

# Definindo o volume escavado e o empolamento
volume_escavado = 150  # m³
empolamento = 40       # %

# Definindo a capacidade de carga de um caminhão
capacidade_caminhao = 8  # m³

# Chamando a função para calcular o volume transportado
volume_transportado = calcular_volume_transportado(volume_escavado, empolamento)

# Chamando a função para calcular a quantidade de caminhões necessários
quantidade_caminhoes = calcular_quantidade_caminhoes(volume_transportado, capacidade_caminhao)

# Exibir apresentação
print("\n===== Cálculo do volume a ser transportado e quantidade de viagens para caminhões de 8 m³ =====")
# Exibindo o resultado
print("Volume a ser transportado:", volume_transportado, "m³")
print("Quantidade de caminhões necessários:", round(quantidade_caminhoes))


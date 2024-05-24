"""
Empolamento - material solto, acréscimo no volume do material original após a escavação, expresso em % do volume original.

O fator de conversão é exatamente a noção inversa do empolamento. Ele representa a relação entre o volume no corte e o volume solto.
"""

def calcular_volumes_aterro(volume_compactado, reducao_volumetrica, empolamento):
    # Calculando o volume de terra necessário na jazida (corte)
    volume_corte = volume_compactado / (1 - reducao_volumetrica)
    
    # Calculando o volume transportado (solto)
    volume_transportado = volume_corte * (1 + empolamento)
    
    return volume_corte, volume_transportado

# Dados do problema
volume_compactado = 1  # m³
reducao_volumetrica = 0.10  # 10%
empolamento = 0.30  # 30%

# Chamando a função para calcular os volumes
volume_corte, volume_transportado = calcular_volumes_aterro(volume_compactado, reducao_volumetrica, empolamento)

# Exibir apresentação
print("\n----- Cálculo Volume de corte e produtividade escvadeira -----")
# Exibindo os resultados
print("Volume de terra necessário na jazida (corte):", round(volume_corte, 2), "m³")
print("Volume transportado (solto):", round(volume_transportado, 2), "m³")

"""
Empolamento - material solto, acréscimo no volume do material original após a escavação, expresso em % do volume original.

O fator de conversão é exatamente a noção inversa do empolamento. Ele representa a relação entre o volume no corte e o volume solto.
"""

class Escavacao:
    def __init__(self, quantidade_viagens, volume_caminhao, empolamento, horas_escavadeira):
        # Inicializa os atributos da classe com os valores fornecidos
        self.quantidade_viagens = quantidade_viagens
        self.volume_caminhao = volume_caminhao
        self.empolamento = empolamento
        self.horas_escavadeira = horas_escavadeira

    def calcular_volume_solto_transportado(self):
        # Calcula o volume solto transportado multiplicando a quantidade de viagens pelo volume do caminhão
        volume_solto_transportado = self.quantidade_viagens * self.volume_caminhao
        return volume_solto_transportado

    def calcular_volume_corte(self, volume_solto_transportado):
        # Calcula o fator de conversão para converter o volume solto para volume de corte
        fator_conversao = 1 / (1 + self.empolamento)
        # Calcula o volume de corte multiplicando o volume solto transportado pelo fator de conversão
        volume_corte = volume_solto_transportado * fator_conversao
        return volume_corte

    def calcular_produtividade_escavadeira(self, volume_corte):
        # Calcula a produtividade da escavadeira dividindo o volume de corte pelas horas de operação da escavadeira
        produtividade = volume_corte / self.horas_escavadeira
        return produtividade

# Dados fornecidos
quantidade_viagens = 160
volume_caminhao = 8  # Volume do caminhão em m³
empolamento = 0.25  # Empolamento de 25%
horas_escavadeira = 8  # Horas de operação da escavadeira

# Cria uma instância da classe Escavacao com os dados fornecidos
escavacao = Escavacao(quantidade_viagens, volume_caminhao, empolamento, horas_escavadeira)

# Realiza os cálculos
volume_solto_transportado = escavacao.calcular_volume_solto_transportado()
volume_corte = escavacao.calcular_volume_corte(volume_solto_transportado)
produtividade_escavadeira = escavacao.calcular_produtividade_escavadeira(volume_corte)

# Exibir apresentação
print("\n----- Cálculo Volume solto, Volume corte e produtividade da escavadeira -----")
# Exibe os resultados
print(f"Volume solto transportado: {volume_solto_transportado:.2f} m³")
print(f"Volume de corte: {volume_corte:.2f} m³")
print(f"Produtividade da escavadeira: {produtividade_escavadeira:.2f} m³/hora")


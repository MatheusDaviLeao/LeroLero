"""Gerador de Lero-lero

Gera frases de efeito sem significado real"""

import random

# listas de possibilidades para cada uma das partes.

parte1 = [
  "O sistema em desenvolvimento",
  "O novo protocolo de comunicação",
  "O algoritmo atualizado"
]

parte2 = [
  "possui excelente desempenho",
  "oferece garantias de precisão acima da média",
  "preenche uma lacuna significativa"
]

parte3 = [
  "as aplicações a que se destinam",
  "em relação às opções disponíveis no mercado",
  "provendo ampla vantagem competitiva a seu usuário"
]

print(random.choice(parte1), random.choice(parte2), random.choice(parte3))

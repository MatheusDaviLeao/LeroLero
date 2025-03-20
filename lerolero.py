"""Gerador de Lero-lero

Gera frases de efeito sem significado real"""

import random

<<<<<<< HEAD
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

lingua = int(input("Escolha a lingua 1- portugês; 2 - Inglês\n"))
if lingua == 2:
	parte1 = []
	parte2 = []
	parte3 = []

print(random.choice(parte1), random.choice(parte2), random.choice(parte3))



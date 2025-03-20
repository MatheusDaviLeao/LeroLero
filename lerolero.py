"""Gerador de Lero-lero

Gera frases de efeito sem significado real"""

import random

parte1 = []
parte2 = []
parte3 = []

lingua = int(input("Escolha a lingua 1- portugês; 2 - Inglês\n"))
if lingua == 2:
	parte1 = []
	parte2 = []
	parte3 = []
  print(random.choice(parte1), random.choice(parte2), random.choice(parte3))

"""
Esercizio 3 - Calcolare l'età media di 4 persone

Descrizione: Data in input l'età di 4 persone calcolare e restituire la media.
Autore: LEONARDO ESSAM DEI ROSSI (github.com/leonardodeirossi)
"""

# Definizione delle variabili
eta1 = 0
eta2 = 0
eta3 = 0
eta4 = 0
media = 0.0

# Fase di input
eta1 = int(input("Inserisci l'età della 1a persona: "))
eta2 = int(input("Inserisci l'età della 2a persona: "))
eta3 = int(input("Inserisci l'età della 3a persona: "))
eta4 = int(input("Inserisci l'età della 4a persona: "))

# Fase di elaborazione
media = (eta1 + eta2 + eta3 + eta4) / 4

# Fase di output
print("L'età media è: ", media)
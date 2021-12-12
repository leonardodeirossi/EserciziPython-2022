"""
Esercizio 4 - Trovare il maggiore tra due numeri

Descrizione: Dati in input due numeri restituire il maggiore.
Autore: LEONARDO ESSAM DEI ROSSI (github.com/leonardodeirossi)
"""

# Definizione delle variabili
numero1 = 0.0
numero2 = 0.0
maggiore = 0.0

# Fase di input
numero1 = float(input("Inserisci il primo numero: "))
numero2 = float(input("Inserisci il secondo numero: "))

# Fase di elaborazione
if(numero1 > numero2):
    maggiore = numero1
else:
    maggiore = numero2

# Fase di output
print("Il numero maggiore è: ", maggiore)

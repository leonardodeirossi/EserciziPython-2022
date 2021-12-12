"""
Esercizio 15 - Numero prezzi maggiori di 100

Descrizione: Dati in input N prezzi, calcolare quanti sono maggiori di 100 e quanti sono minori.
Autore: LEONARDO ESSAM DEI ROSSI (github.com/leonardodeirossi)
"""

# Definizione delle variabili
prezzo = 0.0
totPrezzi = 0
prezziMaggiori = 0
prezziMinori = 0
i = 0

# Fase di input
totPrezzi = int(input("Inserisci il numero di prezzi: "))

# Fase di elaborazione
while (i < totPrezzi):
    prezzo = float(input("Inserisci il numero di prezzi: "))

    if (prezzo > 100):
        prezziMaggiori = prezziMaggiori + 1
    else:
        prezziMinori = prezziMinori + 1

    i = i + 1

# Fase di output
print("Il numero di prezzi maggiori di 100 è: ", prezziMaggiori)
print("Il numero di prezzi minori di 100 è: ", prezziMinori)
"""
Esercizio 13 - Numero pari o dispari

Descrizione: Dato in input un numero, determina se pari o dispari.
Autore: LEONARDO ESSAM DEI ROSSI (github.com/leonardodeirossi)
"""

# Definizione delle variabili
numero = 0.0
esitoControllo = ""

# Fase di input
numero = float(input("Inserisci il numero: "))

# Fase di elaborazione
if (numero % 2 == 0):
    esitoControllo = "PARI"
else:
    esitoControllo = "DISPARI"

# Fase di output
print("Il numero inserito è: ", esitoControllo)
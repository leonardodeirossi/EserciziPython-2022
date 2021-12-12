"""
Esercizio 11 - Somma di N numeri

Descrizione: Dati in input N numeri calcolare e restituire la somma.
Autore: LEONARDO ESSAM DEI ROSSI (github.com/leonardodeirossi)
"""

# Definizione delle variabili
totNumeri = 0
numero = 0.0
somma = 0.0
i = 0

# Fase di input
totNumeri = int(input("Inserisci il numero di numeri da inserire: "))

# Fase di elaborazione
while (i < totNumeri):
    numero = float(input("Inserisci il numero: "))
    somma = somma + numero
    i = i + 1

# Fase di output
print("La somma dei numeri inseriti è: ", somma)
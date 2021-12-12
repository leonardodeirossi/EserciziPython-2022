"""
Esercizio 10 - Somma di 10 numeri

Descrizione: Dati in input 10 numeri calcolare e restituire la somma.
Autore: LEONARDO ESSAM DEI ROSSI (github.com/leonardodeirossi)
"""

# Definizione delle variabili
numero = 0.0
somma = 0.0
i = 0

# Fase di elaborazione
while (i < 10):
    numero = float(input("Inserisci un numero: "))
    somma = somma + numero
    i = i + 1

# Fase di output
print("La somma dei numeri inseriti è: ", somma)
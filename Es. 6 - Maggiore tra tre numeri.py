"""
Esercizio 5 - Confronto con operazioni

Descrizione: Dati in input tre numeri, trovare e restitutire il maggiore e il minore e calcolarne la differenza.
Autore: LEONARDO ESSAM DEI ROSSI (github.com/leonardodeirossi)
"""

# Definizione delle variabili
numero1 = 0.0
numero2 = 0.0
numero3 = 0.0
maggiore = 0.0
minore = 0.0
differenza = 0.0

# Fase di input
numero1 = float(input("Inserisci il primo numero: "))
numero2 = float(input("Inserisci il secondo numero: "))
numero3 = float(input("Inserisci il terzo numero: "))

# Fase di elaborazione
if (numero1 > numero2) and (numero1 > numero3):
    maggiore = numero1
else:
    if (numero2 > numero1) and (numero2 > numero3):
        maggiore = numero2
    else:
        maggiore = numero3

if (numero1 < numero2 and numero1 < numero3):
    minore = numero1

if (numero2 < numero1 and numero2 < numero3):
    minore = numero2

if (numero3 < numero1 and numero3 < numero2):
    minore = numero3

differenza = maggiore - minore

# Fase di output
print("Il numero maggiore è: ", maggiore)
print("Il numero minore è: ", minore)
print("La differenza tra i due è: ", differenza)

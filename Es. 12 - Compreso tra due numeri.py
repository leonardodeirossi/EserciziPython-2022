"""
Esercizio 12 - Compreso tra due numeri

Descrizione: Dati in input un massimo e un minimo, indicare se il terzo numero è nell'intervallo tra i due.
Autore: LEONARDO ESSAM DEI ROSSI (github.com/leonardodeirossi)
"""

# Definizione delle variabili
numeroMassimo = 0.0
numeroMinimo = 0.0
numeroIntermedio = 0.0
esitoControllo = ""

# Fase di input
numeroMassimo = float(input("Inserisci il numero massimo: "))
numeroMinimo = float(input("Inserisci il numero minimo: "))
numeroIntermedio = float(input("Inserisci il numero da controllare: "))

# Fase di elaborazione
if(numeroMinimo < numeroIntermedio and numeroIntermedio < numeroMassimo):
    esitoControllo = "COMPRESO TRA I DUE"
else:
    esitoControllo = "NON COMPRESO"

# Fase di output
print("Il numero inserito è: ", esitoControllo)

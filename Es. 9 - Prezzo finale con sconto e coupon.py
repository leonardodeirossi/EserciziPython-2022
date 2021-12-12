"""
Esercizio 9 - Prezzo finale con sconto e coupon

Descrizione: Dato in input un prezzo, uno sconto e/o un coupon calcolare il prezzo finale.
Autore: LEONARDO ESSAM DEI ROSSI (github.com/leonardodeirossi)
"""

# Definizione delle variabili
prezzo = 0.0
scontoPercentuale = 0.0
valoreCoupon = 0.0
prezzoIntermedio = 0.0  # Variabile di lavoro (elaborazione)
prezzoFinale = 0.0

# Fase di input
prezzo = float(input("Inserisci il prezzo: "))
scontoPercentuale = float(input("Inserisci il valore dello sconto: "))
valoreCoupon = float(input("Inserisci il valore del coupon: "))

# Fase di elaborazione
if (valoreCoupon == 0):
    prezzoFinale = prezzo - ((prezzo + scontoPercentuale) / 100)  # Formula per lo sconto %

if (scontoPercentuale == 0):
    prezzoFinale = prezzo - valoreCoupon # Valore coupon => TOT € da togliere al prezzo

if(valoreCoupon != 0 and scontoPercentuale != 0):
    prezzoIntermedio = prezzo - ((prezzo + scontoPercentuale) / 100)  # Formula per lo sconto %
    prezzoFinale = prezzoIntermedio - valoreCoupon # Applico il coupon al prezzo scontato

# Fase di output
print("Il prezzo con lo sconto e coupon applicati è: ", prezzoFinale)
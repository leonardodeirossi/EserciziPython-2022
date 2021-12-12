"""
Esercizio 14 - Massimo e minimo di N numeri

Descrizione: Dati in input N numeri, determina il maggiore e il minore.
Autore: LEONARDO ESSAM DEI ROSSI (github.com/leonardodeirossi)
"""

# Definizione delle variabili
numero = 0.0
totNumeri = 0.0
numeroMassimo = 0.0
numeroMinimo = 0.0
i = 0

# Fase di input
totNumeri = int(input("Inserisci il numero di numeri: "))

# Fase di elaborazione
while i < totNumeri:
    numero = int(input("Inserisci un numero: "))

    if (numero > numeroMassimo):
        numeroMassimo = numero
    
    if (numeroMinimo == 0.0):
        numeroMinimo = numero
    else:
        if (numero < numeroMinimo):
            numeroMinimo = numero
    
    i = i + 1

# Fase di output
print("Il numero massimo è: ", numeroMassimo)
print("Il numero minimo è: ", numeroMinimo)

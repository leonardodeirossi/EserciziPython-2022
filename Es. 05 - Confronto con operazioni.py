"""
Esercizio 5 - Confronto con operazioni

Descrizione: Dati in input due numeri, svolgere le seguenti operazioni:
                - Se il primo è maggiore del secondo => sottrazione tra i due
                - Se il secondo è maggiore del primo => addizione tra i due
                - Se i due numeri sono uguali => stampare "SONO UGUALI"

Autore: LEONARDO ESSAM DEI ROSSI (github.com/leonardodeirossi)
"""

# Definizione delle variabili
numero1 = 0.0
numero2 = 0.0
risultato = 0.0

# Fase di input
numero1 = float(input("Inserisci il primo numero: "))
numero2 = float(input("Inserisci il secondo numero: "))

# Fase di elaborazione
if(numero1 > numero2):
    risultato = numero1 - numero2
else:
    risultato = numero1 + numero2

# Fase di output
print("Il risultato è: ", risultato)
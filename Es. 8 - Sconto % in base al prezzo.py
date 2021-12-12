"""
Esercizio 8 - Sconto % in base al prezzo

Descrizione: Dato in input un prezzo, in base al suo valore applicare il seguente sconto:
                - Se il prezzo è minore di 100 € => 5% di sconto
                - Se il prezzo è maggiore o uguale di 100 € e minore di 300 € => 10% di sconto
                - Se il prezzo è maggiore o uguale a 300 € => 20% di sconto

Autore: LEONARDO ESSAM DEI ROSSI (github.com/leonardodeirossi)
"""

# Definizione delle variabili
prezzo = 0.0
prezzo_finale = 0.0

# Fase di input
prezzo = float(input("Inserisci il prezzo: "))

# Fase di elaborazione
if(prezzo < 100):
    prezzo_finale = prezzo - ((prezzo * 5) / 100)
else:
    if (prezzo >= 100 and prezzo < 300):
        prezzo_finale = prezzo - ((prezzo * 10) / 100)
    else:
        if (prezzo >= 300):
            prezzo_finale = prezzo - ((prezzo * 20) / 100)

# Fase di output
print("Il prezzo con lo sconto applicato è: ", prezzo_finale)
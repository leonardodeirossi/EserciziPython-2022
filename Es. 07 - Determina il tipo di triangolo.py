"""
Esercizio 7 - Determina il tipo di triangolo

Descrizione: Date in input le misure dei tre lati determinare il tipo di triangolo.
Autore: LEONARDO ESSAM DEI ROSSI (github.com/leonardodeirossi)
"""

# Definizione delle variabili
lato1 = 0.0
lato2 = 0.0
lato3 = 0.0
tipoTriangolo = ""

# Fase di input
lato1 = float(input("Inserisci il primo lato: "))
lato2 = float(input("Inserisci il secondo lato: "))
lato3 = float(input("Inserisci il terzo lato: "))

# Fase di elaborazione
if (lato1 == lato2 and lato2 == lato3):
    tipoTriangolo = "EQUILATERO"
else:
    if (lato1 == lato2 or lato1 == lato3 or lato2 == lato3):
        tipoTriangolo = "ISOSCELE"
    else:
        tipoTriangolo = "SCALENO"

# Fase di output
print("Il triangolo è: ", tipoTriangolo)
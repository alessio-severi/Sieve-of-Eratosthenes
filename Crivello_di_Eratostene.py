
"""
Crivello di Eratostene

Descrizione:
    Implementazione ricorsiva del crivello di Eratostene con decoratori.
    Il decoratore `setup_crivello` gestisce la validazione dell'input
    (da tastiera o da codice), calcola la lista dei numeri tramite
    la funzione `crivello_core`, e gestisce il limite di ricorsione
    e la visualizzazione grafica dei risultati tramite la funzione
    opzionale `visualizza`.

    Visualizzazione:
        - Numeri primi in sfondo blu con testo bianco.
        - Numeri non primi in sfondo bianco con testo nero.
        - Stampa tabellare 10 x N.



Autore: Alessio Severi
Licenza: MIT License

MIT License

Copyright (c) 2025 Alessio Severi

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

"""


from typing import List
from functools import wraps
import sys


def setup_crivello(n0, visual= None):

    def decorator(funzione):

        @wraps(funzione)
        def wrapper(n: str | int) -> List[int]:

            # Validazione del valore n

            # Validazione da input
            if isinstance(n, str):
                if not n.isdecimal():

                    raise ValueError("Errore di input: inserire un valore intero")
                
                n = int(n)

            # In caso di immissione del valore direttamente da codice
            # Conversione automatica per float
            elif isinstance(n, float):
                n = int(n)

            # Tipi non numerici
            elif not isinstance(n, int):
                raise ValueError("Errore di valore: scrivere un valore intero")

            # Controllo del valore minimo consentito
            if n <= n0:
                raise ValueError(f"Errore: il valore deve essere maggiore di {n0}")

           
            # Limite ricorsivo
            max_ri = sys.getrecursionlimit() - 1

            if (n - n0 + 1) > max_ri:
                raise RecursionError(f"n troppo grande per questa versione ricorsiva "
                                    f"(max ≈ {n0 + max_ri - 1})")


            # Creazione del setaccio
            setaccio = list(range(n0, n + 1))
            lista_primi = []
            
            # Esecuzione del decoratore: calcola e opzionalmente visualizza i risultati
            risultato= funzione(setaccio, lista_primi)
            return visual(n, risultato) if visual is not None else risultato
        
        return wrapper
    
    return decorator



# -----------------------------------------------
# Funzione principale del Crivello di Eratostene
# -----------------------------------------------
def crivello_core(setaccio: List[int], lista_primi: List[int]) -> List[int]:
    """
    Implementazione ricorsiva del crivello di Eratostene.
    Riceve il setaccio e la lista dei numeri primi trovati.
    Rimuove i multipli del primo elemento del setaccio e prosegue
    fino a svuotare il setaccio.
    """

    # Caso base: se il setaccio è vuoto → restituisce la lista dei primi
    if not setaccio:
        return lista_primi

    # Primo numero del setaccio (nuovo divisore)
    arg = setaccio[0]


    # Funzione interna per filtrare i multipli dell'argomento corrente
    def calcola(seta: List[int]) -> List[int]:

        # Rotazione del setaccio: sposta l’ultimo elemento in testa
        seta.insert(0, seta.pop())

        # Se il ciclo ha completato una rotazione, restituisce il setaccio
        if seta[0] == arg:
            return seta


         # Se il primo elemento è multiplo di arg, lo elimina
        if seta[0] % arg == 0:
            del seta[0]

        # Ricorsione sulla nuova configurazione del setaccio
        return calcola(seta)

    # Applica la funzione di filtraggio e aggiorna la lista dei numeri primi
    setaccio = calcola(setaccio)
    lista_primi.append(setaccio[0])

    # Chiamata ricorsiva sul nuovo setaccio
    del setaccio[0]

    return crivello_core(setaccio, lista_primi)


# -------------------------------
# Funzione di visualizzazione
# -------------------------------
def visualizza(n: int, lista_primi: list[int]):
    """
    Visualizzazione tabellare dei numeri da 2 a n.
    Evidenzia i numeri primi in blu e i composti in bianco.
    """

    print("\n")
    print(f"\033[47m\033[30m      \033[0m", end="")


    # Conversione in set per ottimizzare la ricerca (lookup O(1))
    primi = set(lista_primi)

    # Scansione dei numeri da 2 a n
    for numero in range(2, n + 1):

        
        # Numeri primi → blu (sfondo) con testo bianco
        if numero in primi:

            print(f"\033[44m {numero:4d} \033[0m", end="")

        # Numeri non primi → sfondo bianco con testo nero
        else:

            print(f"\033[47m\033[30m {numero:4d} \033[0m", end="")

        # A capo ogni 10 numeri
        if numero % 10 == 0:
            
            print()

    # Riempimento per completare la tabella (10xN)
    if resto:= n % 10:
        for _ in "_" * (10 - resto):

            print(f"\033[47m\033[30m      \033[0m", end="")

    
    print("\n\n")

    # Ritorno della lista di numeri primi per ulteriore implementazione
    return lista_primi
    


# ---------------------------------------------------
# Funzione di alto livello del Crivello di Eratostene
# ---------------------------------------------------
@setup_crivello(2, visualizza)
def crivello(setaccio: List[int], lista_primi: List[int]) -> List[int]:
    return crivello_core(setaccio, lista_primi)
    


# Titolo
print("\n\033[1;34m{:^60}\n".format("CRIVELLO DI ERATOSTENE"))

# Test
crivello(input("Inserire il valore di n: "))

# Test con input da codice
# Commenta la riga di codice precedente e decommenta la seguente
# per testare con input da codice
# crivello(100)

# Colorazione di default
print("\033[0m")


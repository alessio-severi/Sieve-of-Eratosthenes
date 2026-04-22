# Sieve of Eratosthenes

Recursive implementation of the Sieve of Eratosthenes to find all prime numbers up to a given limit, developed in Python.

For a full description of the algorithm and its design choices, read the article on chorax.it: [Programmare in Python: 1. Crivello di Eratostene](https://chorax.it/codice-e-creativita/programmare-in-python-1-crivello-di-eratostene/)

▶ [Run on Replit](https://replit.com/@alessioseveri27/Crivello-di-Eratostene)

## How it works

The algorithm is implemented using two nested recursions to highlight the inductive nature of the sieve: at each step, a prime number is selected and its multiples are eliminated, repeating the process until the sieve is exhausted. This approach prioritizes conceptual clarity over performance, making the progression of the algorithm directly observable in its structure.

The output is displayed as a formatted table that adapts its layout based on the value of `n`. Prime numbers are highlighted with a blue background and white text, non-prime numbers with a white background and black text.

## Usage

Set the upper limit `n` in the source file or pass it as input. The parameter `n` defines the interval [2, n] within which the program computes and displays the prime numbers. The value of `n` can be adjusted based on display size or desired execution speed.

Run the program:

```
python3 Crivello_di_Eratostene.py
```

Note that due to the recursive implementation, the value of `n` is subject to Python's recursion limit. Values that exceed it are handled by the program with an explicit error message.

## License

© 2025 Alessio Severi — released under the [MIT License](LICENSE).

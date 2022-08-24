import random

# jakýkoliv modul, která si vytvoříme můžeme vložit do našeho scriptu tim, že ho naimportujeme
# řeknemě, že máme modul, kde máme vypsané Pi (3.14) jednoduse ho ulozime, importujeme a vložíme do kodu a testneme jako print("jméno podulu.pi")

# takhle dostaneme random integer výber čísla mezi 1 - 10
random_integer = random.randint(1, 10)

# random float číslo, vždy dostaneme číslo od 0 - 1
random_float = random.random()

# abychom dostali více než rozmezí 0 - 1 napíšeme následovně
random_float_1 = random.random() * 5


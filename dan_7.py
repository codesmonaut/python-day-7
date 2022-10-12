# Regular Expression
import re

# reg_tablica = input("Unesite oznake reg. tablice: ")

# sablon = r'^[A-Z]{2}\-[0-9]{3,5}\-[A-Z]{2}$'
# rezultat_provere = re.search(sablon, reg_tablica)

# if rezultat_provere:
#     print("Ovo je ispravna tablica.")
# else:
#     print("Ovo je neispravna tablica.")

# broj = input("Unesite broj: ")

# validan_broj = r'^\-?[0-9]+(\.[0-9]*)?$' # + = {1,} (jedan ili vise brojeva) * = {0,} (0 ili vise brojeva)
# provera = re.search(validan_broj, broj)

# if provera:
#     print("Ovo je ispravan broj.")
# else:
#     print("Ovo je neispravan broj.")

# tekst = "Ovo su podaci: BG123, NI123, i takodje TO456, ali i NS123 i to je to."

# patern = r'[A-Z]{2}[0-9]{3}'
# rezultati = re.findall(patern, tekst)

# print(rezultati)

# tekst = "Vrednosti su: -100, 50.5, 2.5, -123, -1.0, 10 i 102.75 kraj."

# rezultati = re.findall(r'\-?[0-9]+(?:\.[0-9]+)?', tekst)
# # ?: - celina postaje non-matching, tj. nece biti posebno izdvojena.

# print(rezultati)

# ime_fajla = "studentske-adrese.txt"

# with open(ime_fajla, "r") as ulaz:
#     text = ulaz.read()

#     sablon = r'([a-z]+)\.([a-z]+)\.[0-9]{2,3}@singimail\.rs'
#     mails = re.findall(sablon, text)

#     for mail in mails:
#         print(mail)
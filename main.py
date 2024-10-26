import math


print(
    "Tervetuloa käyttämään arvosanalaskuria! Laskuri laskee arvosanasi perustuen \
1-5 asteikkoon ja lineaariseen pisteytysmalliin"
)

maksimipisteet = float(input("Anna pistemäärä arvosanalle 5: "))
minimipisteet = float(input("Anna pistemäärä arvosaanalle 1: "))

kayttajapisteet = float(input("Anna saamasi pistemäärä: "))

# if user points are less than minimum points, user gets 0 grade
if kayttajapisteet < minimipisteet:
    print("Arvosanasi on 0, et päässyt läpi.")
# if user points are larger than maximum points, user gets 5 grade
elif kayttajapisteet >= maksimipisteet:
    print("Arvosanasi on 5")
# if user points are smaller than maximum points linear calculation
elif kayttajapisteet < maksimipisteet:
    arvosana = 1 + 4 * (kayttajapisteet - minimipisteet) / (
        maksimipisteet - minimipisteet
    )
    print("Arvosanasi on", math.floor(arvosana))

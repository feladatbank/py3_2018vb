'''
A megoldás során vegye figyelembe a következőket:
 * A program megírásakor a fájlban lévő adatok helyes szerkezetét nem kell ellenőriznie, feltételezheti, hogy a rendelkezésre álló adatok a leírtnak megfelelnek.
 * Megoldását úgy készítse el, hogy az azonos szerkezetű, de tetszőleges inputadatok mellet is helyes eredményt adjon!

A "vb2018.txt" UTF-8 kódolású állomány soraiban a VB helyszíneinek (stadionjainak) adatait tároltuk a következő sorrendbe: a város neve, a stadion neve(nev1), a stadion alternatív neve(nev2) és a stadion férőhelye.

1. feladat:
Készítsen programot a következő feladatok megoldására, amelynek a forráskódját/projektjét vb2018 néven mentse el!

2. feladat:
Olvassa be a "vb2018.txt" állományban lévő adatokat és tárolja el egy összetett adatszerlezetben úgy, hogy a további feladtok megoldására alkalmas legyen! Az állományban maximum 50 adatsor lehet.

3. feladat:
Jelenítse meg a képernyőn, hogy hány stadionban játszották a VB mérkőzéseit

4. feladat:
Határozza meg, és írja ki a képernyőre a legkevesebb férőhellyel rendelkező stadion adatait

5. feladat:
Határozza meg, és írja a képernyőre a stadionok férőhelyszámának átlagát, az eredményt egy tizedesjegyre kerekítve jelenítse meg!

Minta:
3. feladat: Stadionok száma: 12
4. feladat: A legkevesebb férőhely: 
        Város: Jekatyerinburg
        Stadion neve: Központi stadion
        Férőhely: 33061
5. feladat: Átlagos férőhelyszám: 46532.8
'''

# Lehetséges megoldás

class Vb:
  def __init__(self, sor):
    varos, nev1, nev2, ferohely = sor.strip().split(";")
    self.varos = varos
    self.nev1 = nev1
    self.nev2 = nev2
    self.ferohely = int(ferohely)

lista = []
with open("vb2018.txt", "r", encoding="latin2") as f:
  f.readline()
  for sor in f:
    lista.append(Vb(sor))

#3. feladat:
print(f"3. feladat: Stadionok száma: {len(lista)}")

#4. feladat:
'''
ferohely = min(lista, key=lambda x:x.ferohely)
print(f"4. feladat: A legkevesebb férőhely: \n        Város: {ferohely.varos}\n        Stadion neve: {ferohely.nev1}\n        Férőhely: {ferohely.ferohely}")
'''
# Vagy

ferohely = lista[0].ferohely
for sor in lista:
  if sor.ferohely < ferohely:
    ferohely = sor.ferohely
    varos = sor.varos
    nev = sor.nev1
print(f"4. feladat: A legkevesebb férőhely: \n        Város: {varos}\n        Stadion neve: {nev}\n        Férőhely: {ferohely}")

#5. feladat:
szam = 0

for sor in lista:
  szam += sor.ferohely

print(f"5. feladat: Átlagos férőhelyszám: {round(szam / len(lista), 1)}")
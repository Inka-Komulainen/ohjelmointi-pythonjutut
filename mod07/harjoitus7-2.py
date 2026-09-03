# harjoitus 2 -- ohjelma kysyy montako tahkoa nopassa on. Tätä noppaa heitetään, kunnes saadaan nopan maksimiluku

import random

def heita_noppaa(a):
    i = random.randint(1,a)
    return i

tahkot = int(input("Montako tahkoa nopassa on: "))
luku = 0

while luku != tahkot:
    luku = heita_noppaa(tahkot)
    print(luku)
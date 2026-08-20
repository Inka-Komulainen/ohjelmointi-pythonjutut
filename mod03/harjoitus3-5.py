#harjoitus 5 - ohjelma kysyy monta leiviskät, naulat ja luodit, ja muuntaa ne kiloiksi ja grammoiksi

# Yksi leiviskä on 20 naulaa.
# Yksi naula on 32 luotia.
# Yksi luoti on 13,3 grammaa.

leiv = float(input("Kerro monta leiviskää: "))
naul = float(input("Kerro monta naulaa: "))
luod = float(input("Kerro monta luotia: "))

#eri yksikköjen muunto grammoihin (leiv grammoina) + (naul grammoina) + (luodit grammoina)
massa = (leiv * 20 * 32 * 13.3) + (naul * 32 * 13.3) + (luod *13.3) 

kilo = massa // 1000
gramma = massa % 1000

print(f"Massa nykymittojen mukaan: {kilo:.0f} kilogrammaa ja {gramma:.2f} grammaa.")

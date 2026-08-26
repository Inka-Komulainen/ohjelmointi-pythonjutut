## kertoo mihin linnanmäen laitteisiin käyttäjä saa mennä iän mukaan

iPituus = int(input("Miten pitkä olet?: "))
iIka = int(input("Miten vanha olet? "))

if  iPituus <= 195 and iIka >= 8:
   print("Saat mennä kaikkiin laitteisiin.")
elif iPituus <= 195 and iIka < 8:
    print("Saat mennä kaikkiin laitteisiin paitsi tulirekeen.")
elif iPituus >= 140 and iIka >= 8:
    print("Saat mennä kaikkiin laitteisiin paitsi kirnuun.")
elif iPituus >= 140 and iIka < 8:
    print("Saat mennä kaikkiin laitteisiin paitsi kirnuun ja tulirekeen.")
elif iPituus >= 100:
    print("Saat mennä lasten laitteisiin.")
else:
    print("Et pääse vielä mihinkään laitteeseen.")




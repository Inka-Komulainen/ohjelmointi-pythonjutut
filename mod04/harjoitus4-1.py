# harjoitus 1 -- ohjelma kysyy kuhan pituuden. Jos se on alle 37 cm, se kertoo paljonko puuttuu.

fKuha = float(input("Kuinka pitkä kuha on : "))

if fKuha < 37:
    fPuuttuu = 37 - fKuha
    print("Kuha on liian lyhyt. Laskethan sen takaisin järveen.")
    print(f"Jos se olisi ollut {fPuuttuu} cm pidempi, voisit pitää sen.")

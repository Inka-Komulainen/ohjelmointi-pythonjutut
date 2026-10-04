# Ensimmäinen pelini

Inka Komulainen



## projektitehtävä 1

Peli kysyy pelaaja nimen ja iän, ja tulostaa ne.

## projektitehtävä 2

Päävalikko on seuraavassa formaatissa:

- Profiili    (esittää pelaajan nimen ja iän, mahdollisesti antaa muuttaa niitä)
- Etene       (pelaaja siirtyy seuraavaan huoneeseen/alueeseen pelissä)
- Etsi        (pelaaja etsii nykyisestä alueesta esineitä/muuta kiinnostavaa)
- Löydöt      (inventaario, näyttää kaikki mitä pelaaja on löytänyt)
- Lopeta      (lopettaa pelin)

## projektitehtävä 3 

Lähes kaikilla päävalikon toiminnoilla on oma funktio. "Profiili" toiminto ei enää pelkästään esitä pelaajan nimeä ja ikää, mutta antaa myös pelaajan muuttamaan niitä. Inventaario tulostetaan "löydöt" toiminnolla, mikä myös kertoo, montako esinettä inventaariossa on. Päävalikon toiminto "etene" on vielä kesken.

(Haluan "etene" toiminolla pelaajan etenevän pelin seuraavalle alueelle, jonka on tarkoitus tulevaisuudessa sekoittaa se, mitä voidaan löytää "etsi" toiminnolla.)

## projektitehtävä 4

1. Olen jakanut koodin eri moduuleihin. Luokat pelaaja ja alue ovat molemmat omissa moduuleissaan. Etsi-toiminto, joka toimii eri tavalla riippuen millä pelin alueella pelaaja sijaitsee, on omassa moduulissaan sen verrattaisen suuruuden vuoksi. Pelissä on pieniä 'ASCII-taide' teoksia tuomaan vähän visuaalisuutta peliin, jotka sijaitsevat omassa tiedostossaan. En kokenut paketin luomsita tarpeelliseksi peliäni varten.

2. Pelissäni on kaksi luokkaa: Pelaaja ja Alue. Pelaajalla on ominaisuudet: nimi, ikä, sijainti ja inventaariona toimiva lista. Alueella on ominaisuudet: nimi, kuvaus, lähtöehto (millä perusteella alueesta pääsee pois). Alueella on myös kaksi luokkamuuttujaa: toinen on lista alue-objektien nimistä joita pelaaja ei ole suorittanut, ja toinen on luku joka kertoo montako aluetta pelaaja on suorittanut. Pelissäni ei ole Esine luokkaa, koska pelin esineillä ei ole ominaisuuksia tai erityisiä toimintoja.
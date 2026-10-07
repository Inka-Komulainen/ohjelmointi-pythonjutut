# Ensimmäinen pelini

Inka Komulainen


## Pelin idea ja rakenne

Olet valtakunnan ritari! Valtakunnassasi on neljä aluetta (metsä, vuoret, niitty, pellot), jotka kaikki ovat
joutuneet pulaan. Jokaisella alueella sinun tulee auttaa alueen asukkaita löytämällä joku esine tai esineitä,
ja antamalla ne asukkaille. Voit valita missä järjestyksessä pelaat alueet, mutta sinun tulee pelata valitsemasi alue loppuun ennen, kun voit edetä seuraavalle alueelle. Voitat, kun kaikki alueet ovat turvassa. 

## Pelin toiminnot

Päävalikon etsi-toiminnolla voit löytää esineitä eri tavoin riippuen alueesta, jossa olet. Yhdellä alueella löydät eri esineitä eri suunnista, toisella alueella eri suunnilla on eri mahdollisuudet löytää esineitä, kolmannella alueella voit parantaa tai huonontaa mahdollisuuksiasi löytää esineitä ripppuen mitä teet, neljännellä alueella kerätään esineitä, jotka tulee muuttaa toiseksi esineeksi etenemistä varten.

Kun olet löytänyt tarpeeksi esineitä voit edetä seuraavalle alueelle etene-toiminnolla. Voit kutsua tietosi profiili-toiminnolla ja inventaariosi löydöt-toiminnolla, ja lopettaa pelin lopeta-toiminnolla. Pelitilanteesi tallentuu lopettaessasi pelin. Pelin tallenne poistetaan, kun voitat pelin.

## Kestävän kehityksen periaatteet pelissäni

Jokainen pelin alue edustaa jotakin kestävän kehityksen tavoitetta. Metsä edustaa "ei nälkää" tavoitetta, koska alueen asukkaat ovat uhassa nälkiintyä ja metsän vallannut rölli tarvitsee ruokaa asukkaiden vapauttamiseksi. Vuoret edustavat "puhdas vesi" tavoitetta, koska vuorten asukkaat ovat vaarassa jäädä ilman vettä. Niitty edustaa "maanpäällinen elämä" tavoitteita, koska niityllä vieraslaji on uhka alueen monimuotoisuudelle ja estää uhanalaisen kasvin kasvamista. Pellot alue edustaa "terveyttä ja hyvinvointia" tavoitetta, koska autat alueen sairaita asukkaita löytämällä parannuskeinon.

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

## projektitehtävä 5

1. Pelin aloittaessa tulostetaan intro teksti, jossa on myös ohjeet pelaamiseen. Näiden lisäksi jokaiselle alueeelle on oma kuvaus, joka tulostuu sen jälkeen kun alue valitaan. Kaikki tekstitiedostot ovat tallennettu kuvaukset kansioon.

2. Peli luo tallennuksen, jos sen lopettaa ennen kun pelaaja on voittanut pelin. Seuraavan kerran pelin käynnistäessä jatketaan siitä mihin jäätiin. Pelin tallennus poistetaan, kun peli voitetaan.
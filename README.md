# Napovedovanje cen električne energije

V tem zvezku raziskujemo različne modele za napovedovanje cen električne energije v Sloveniji z uporabo časovnih vrst. Testiramo več pristopov, vključno z linearnimi modeli, harmoniki in mešanimi modeli, ter ocenjujemo njihovo uspešnost z uporabo povprečne kvadratne napake (MSE).

## Opis podatkov

Podatki o cenah električne energije so pridobljeni na **urni ravni** iz [Ember Climate](https://ember-climate.org/data-catalogue/european-wholesale-electricity-price-data/). Vsebujejo cene električne energije (v EUR/MWh) za Slovenijo.

## Navodila za uporabo

1. Prenesite datoteko `Slovenia.csv` in jo shranite v mapo `european_wholesale_electricity_price_data_hourly/`.
2. Poskrbite, da je modul `tester` na voljo v okolju.
3. Nekateri ključni parametri za trening modelov so:
   - `t.lokacija_originalnih_podatkov`: pot do datoteke s podatki
   - `t.zacetni_cas`: določa število zadnjih cen, ki jih uporabimo za 1. napoved (od tod naprej pa testiramo vse cene)
   - 't.test(*ime_funkcije*) : zažene test in vrne srednjo kvadratno napako napovedi

## Implementirani modeli

Osnovne modele najdemo v zacetni_modeli.ipynb. Te so vecinoma osnovani na predoločenih sistemih. Nekaj boljših modelov:

### 1. Linearni prediktor
Napoved tvori z linearno kombinacijo predhodnih cen.

### 2. Ciklični prediktor s harmoniki
Ta model uporablja kotne funkcije z različnimi periodami in njihove višje harmonike harmonike (sinus in kosinus) za zajem cikličnih trendov v cenah električne energije. Pri tem lahko uporabljamo različne ferkvence (npr. dnevni, tedenski in letni cikeli).

### 3. Mešan model
Mešan model združuje linearne komponente in ciklične harmonike. Harmoniki se izračunajo na podlagi različnih cikličnih frekvenc (`k`), linearni del pa deluje podobno kot pri linearnem prediktorju.

## Evaluacija

Vsak model testiramo s pomočjo modula `tester`, pri čemer uspešnost merimo z **povprečno kvadratno napako (MSE)**. Različne konfiguracije modelov preizkušamo, da določimo najuspešnejšega.

### Primeri uspešnosti modelov

- **Predhodna cena**
Datoteka vsebuje tudi nekaj osnovnejših modelov Primer cena prejšne ure:

```python
def zadnja_cena(cene):
    return cene[-1]
```

- **zadnja_cena**:
  - MSE: 242.53
  - Čas izvajanja: 0.03 sekunde


- **Linearni model s kombinacijo 512-ih predhodnih cen**: 
  - MSE: 131.91
  - Čas izvajanja: 7.11 sekund

- **Ciklični model s dnevnimi, tedenskimi in letnimi cikli**: 
  - MSE: 165.84
  - Čas izvajanja: 4.85 sekunde

- **Mešan model (najboljši do sedaj)**: 
  - MSE: 128.68
  - Čas izvajanja: 9.45 sekund


## Vizualizacija

Zvezek vključuje vizualizacije povprečnih cen električne energije po urah dneva, dnevih v tednu in mesecih. Te vizualizacije pomagajo bolje razumeti ciklične trende v podatkih:

- **Povprečja po urah**
- **Povprečja po dnevih v tednu**
- **Povprečja po mesecih**

## Projekt je še v nastjanju

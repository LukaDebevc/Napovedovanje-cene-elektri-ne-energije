import time
import os
zacetni_cas = 1000
lokacija_originalnih_podatkov = r"european_wholesale_electricity_price_data_hourly/Slovenia.csv"

ze_obstaja = r"logs/slo_price"
if os.path.exists(ze_obstaja):
    with open(ze_obstaja, "r") as file:
        for i in file:
            t0 = time.time()
            # cene = eval(i)
            cene = [float(x) for x in i.split(",")]
else:
    cene = []
    with open(lokacija_originalnih_podatkov, "r") as podatki:
        for vrstica in podatki: break
        for vrstica in podatki:
            cene.append(float(vrstica.split(",")[-1]))

    os.makedirs("logs", exist_ok=True)
    with open(ze_obstaja, "w") as file:
        print(",".join(str(cena) for cena in cene), file=file, end="")


def funkcija_napake(predvidana_cena, prava_cena):
    return (predvidana_cena - prava_cena)**2

class FreezableList(list):
    def __init__(self, *args, freeze=False, **kwargs):
        self.freeze = freeze
        super().__init__(*args, **kwargs)

    def _check_mutability(self):
        if self.freeze:
            raise ValueError("Ne spreminjaj podatkov. Če želist to početi prosim uporabi eno od naslednjih:\r"
                             "1) podaki[:] seveda lahko uporabljas tudi [start:stop:step] fore ipd...\r"
                             "2) podaki.copy()\r"
                             "3) [element for element in podaki]\r")

    def append(self, item):
        self._check_mutability()
        super().append(item)

    def extend(self, iterable):
        self._check_mutability()
        super().extend(iterable)

    def insert(self, index, item):
        self._check_mutability()
        super().insert(index, item)

    def __setitem__(self, index, value):
        self._check_mutability()
        super().__setitem__(index, value)
    
    def DO_NOT_USE_this_backdoor_append(self, item): # tu zaradi hitrejsega posodabljana
        super().append(item)


def test(funckija_napovedi):
    t0 = time.time()
    pretekli_podatki = FreezableList(cene[:zacetni_cas], freeze=True)
    sesteta_napaka = 0
    for cas in range(zacetni_cas, len(cene)):
        sesteta_napaka += funkcija_napake(funckija_napovedi(pretekli_podatki), cene[cas])
        pretekli_podatki.DO_NOT_USE_this_backdoor_append(cene[cas])
    print(f"test {funckija_napovedi.__name__}: povprecna kvadratna napaka:", sesteta_napaka / (len(cene) - zacetni_cas), f"porabljen cas: {time.time() - t0}")



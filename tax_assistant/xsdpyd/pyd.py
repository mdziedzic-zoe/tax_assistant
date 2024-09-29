cfrom decimal import Decimal
from enum import Enum
from typing import Optional

from pydantic import BaseModel, ConfigDict
from xsdata.models.datatype import XmlDate
from xsdata_pydantic.fields import field


class PozycjeSzczegoloweP20(Enum):
    """
    :cvar VALUE_1: umowa
    :cvar VALUE_2: zmiana umowy
    :cvar VALUE_3: orzeczenie sądu lub ugoda
    :cvar VALUE_4: inne
    """

    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3
    VALUE_4 = 4


class PozycjeSzczegoloweP42(Enum):
    VALUE_19 = 19


class PozycjeSzczegoloweP48(Enum):
    """
    :cvar VALUE_1: zawarcia umowy spółki
    :cvar VALUE_2: zwiększenia majątku spółki albo podwyższenia kapitału
        zakładowego
    :cvar VALUE_3: dopłaty
    :cvar VALUE_4: pożyczki udzielonej spółce osobowej przez wspólnika
    :cvar VALUE_5: oddania spółce rzeczy lub praw majątkowych do
        nieodpłatnego używania
    :cvar VALUE_6: przekształcenia spółek
    :cvar VALUE_7: łączenia spółek
    :cvar VALUE_8: przeniesienia na terytorium Rzeczypospolitej Polskiej
        rzeczywistego ośrodka zarządzania spółki kapitałowej lub jej
        siedziby
    """

    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3
    VALUE_4 = 4
    VALUE_5 = 5
    VALUE_6 = 6
    VALUE_7 = 7
    VALUE_8 = 8


class PozycjeSzczegoloweP7(Enum):
    """
    :cvar VALUE_1: Podmiot zobowiązany solidarnie do zapłaty podatku
    :cvar VALUE_2: Strona umowy zamiany
    :cvar VALUE_3: Wspólnik spółki cywilnej
    :cvar VALUE_4: Podmiot, o którym mowa w art. 9 pkt 10 lit. b ustawy
        (pożyczkobiorca)
    :cvar VALUE_5: Inny podmiot - różny od: podmiotu zobowiązanego
        solidarnie do zapłaty podatku, strony umowy zamiany, wspólnika
        spółki cywilnej
    """

    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3
    VALUE_4 = 4
    VALUE_5 = 5


class TadresPolskiKodKraju(Enum):
    """
    :cvar PL: POLSKA
    """

    PL = "PL"


class TidentyfikatorOsobyFizycznej4(BaseModel):
    """
    Podstawowy zestaw danych identyfikacyjnych o osobie fizycznej z identyfikatorem
    NIP albo PESEL.

    :ivar nip: Identyfikator podatkowy NIP
    :ivar pesel: Identyfikator podatkowy numer PESEL
    :ivar imie_pierwsze: Pierwsze imię
    :ivar nazwisko: Nazwisko
    :ivar data_urodzenia: Data urodzenia
    """

    class Meta:
        name = "TIdentyfikatorOsobyFizycznej"
        target_namespace = "http://crd.gov.pl/wzor/2023/12/13/13064/"

    model_config = ConfigDict(defer_build=True)
    nip: Optional[str] = field(
        default=None,
        metadata={
            "name": "NIP",
            "type": "Element",
            "namespace": "http://crd.gov.pl/wzor/2023/12/13/13064/",
            "pattern": r"[1-9]((\d[1-9])|([1-9]\d))\d{7}",
        },
    )
    pesel: Optional[str] = field(
        default=None,
        metadata={
            "name": "PESEL",
            "type": "Element",
            "namespace": "http://crd.gov.pl/wzor/2023/12/13/13064/",
            "pattern": r"\d{11}",
        },
    )
    imie_pierwsze: str = field(
        metadata={
            "name": "ImiePierwsze",
            "type": "Element",
            "namespace": "http://crd.gov.pl/wzor/2023/12/13/13064/",
            "required": True,
            "min_length": 1,
            "max_length": 30,
        }
    )
    nazwisko: str = field(
        metadata={
            "name": "Nazwisko",
            "type": "Element",
            "namespace": "http://crd.gov.pl/wzor/2023/12/13/13064/",
            "required": True,
            "min_length": 1,
            "max_length": 81,
        }
    )
    data_urodzenia: str = field(
        metadata={
            "name": "DataUrodzenia",
            "type": "Element",
            "namespace": "http://crd.gov.pl/wzor/2023/12/13/13064/",
            "required": True,
            "min_inclusive": "1900-01-01",
            "max_inclusive": "2050-12-31",
            "pattern": r"((\d{4})-(\d{2})-(\d{2}))",
        }
    )


class TidentyfikatorOsobyNiefizycznej3(BaseModel):
    """
    Skrócony zestaw danych identyfikacyjnych o osobie niefizycznej.

    :ivar nip: Identyfikator podatkowy NIP
    :ivar pelna_nazwa: Nazwa pełna
    :ivar skrocona_nazwa: Nazwa skrócona
    """

    class Meta:
        name = "TIdentyfikatorOsobyNiefizycznej"
        target_namespace = "http://crd.gov.pl/wzor/2023/12/13/13064/"

    model_config = ConfigDict(defer_build=True)
    nip: str = field(
        metadata={
            "name": "NIP",
            "type": "Element",
            "namespace": "http://crd.gov.pl/wzor/2023/12/13/13064/",
            "required": True,
            "pattern": r"[1-9]((\d[1-9])|([1-9]\d))\d{7}",
        }
    )
    pelna_nazwa: str = field(
        metadata={
            "name": "PelnaNazwa",
            "type": "Element",
            "namespace": "http://crd.gov.pl/wzor/2023/12/13/13064/",
            "required": True,
            "min_length": 1,
            "max_length": 240,
        }
    )
    skrocona_nazwa: str = field(
        metadata={
            "name": "SkroconaNazwa",
            "type": "Element",
            "namespace": "http://crd.gov.pl/wzor/2023/12/13/13064/",
            "required": True,
            "min_length": 1,
            "max_length": 70,
        }
    )


class TkodFormularza(Enum):
    """
    Symbol wzoru formularza.
    """

    PCC_3 = "PCC-3"


class TnaglowekWariantFormularza(Enum):
    VALUE_6 = 6


class TkodUs(Enum):
    """
     "URZAD_SKARBOWY_W_BOLESLAWCU": 0202
     "URZAD_SKARBOWY_W_BYSTRZYCY_KLODZKIEJ": 0203
     "URZAD_SKARBOWY_W_DZIERZONIOWIE": 0204
     "URZAD_SKARBOWY_W_GLOGOWIE": 0205
     "URZAD_SKARBOWY_W_JAWORZE": 0206
     "URZAD_SKARBOWY_W_JELENIEJ_GORZE": 0207
     "URZAD_SKARBOWY_W_KAMIENNEJ_GORZE": 0208
     "URZAD_SKARBOWY_W_KLODZKU": 0209
     "URZAD_SKARBOWY_W_LEGNICY": 0210
     "URZAD_SKARBOWY_W_LUBANIU": 0211
     "URZAD_SKARBOWY_W_LUBINIE": 0212
     "URZAD_SKARBOWY_W_LWOWKU_SLASKIM": 0213
     "URZAD_SKARBOWY_W_MILICZU": 0214
     "URZAD_SKARBOWY_W_NOWEJ_RUDZIE": 0215
     "URZAD_SKARBOWY_W_OLESNICY": 0216
     "URZAD_SKARBOWY_W_OLAWIE": 0217
     "URZAD_SKARBOWY_W_STRZELINIE": 0218
     "URZAD_SKARBOWY_W_SRODZIE_SLASKIEJ": 0219
     "URZAD_SKARBOWY_W_SWIDNICY": 0220
     "URZAD_SKARBOWY_W_TRZEBNICY": 0221
     "URZAD_SKARBOWY_W_WALBRZYCHU": 0222
     "URZAD_SKARBOWY_W_WOLOWIE": 0223
     "URZAD_SKARBOWY_WROCLAW_FABRYCZNA": 0224
     "URZAD_SKARBOWY_WROCLAW_KRZYKI": 0225
     "URZAD_SKARBOWY_WROCLAW_PSIE_POLE": 0226
     "URZAD_SKARBOWY_WROCLAW_STARE_MIASTO": 0227
     "URZAD_SKARBOWY_WROCLAW_SRODMIESCIE": 0228
     "PIERWSZY_URZAD_SKARBOWY_WE_WROCLAWIU": 0229
     "URZAD_SKARBOWY_W_ZABKOWICACH_SLASKICH": 0230
     "URZAD_SKARBOWY_W_ZGORZELCU": 0231
     "URZAD_SKARBOWY_W_ZLOTORYI": 0232
     "URZAD_SKARBOWY_W_GORZE": 0233
     "URZAD_SKARBOWY_W_POLKOWICACH": 0234
     "DOLNOSLASKI_URZAD_SKARBOWY_WE_WROCLAWIU": 0271
     "URZAD_SKARBOWY_W_ALEKSANDROWIE_KUJAWSKIM": 0402
     "URZAD_SKARBOWY_W_BRODNICY": 0403
     "PIERWSZY_URZAD_SKARBOWY_W_BYDGOSZCZY": 0404
     "DRUGI_URZAD_SKARBOWY_W_BYDGOSZCZY": 0405
     "TRZECI_URZAD_SKARBOWY_W_BYDGOSZCZY": 0406
     "URZAD_SKARBOWY_W_CHELMNIE": 0407
     "URZAD_SKARBOWY_W_GRUDZIADZU": 0408
     "URZAD_SKARBOWY_W_INOWROCLAWIU": 0409
     "URZAD_SKARBOWY_W_LIPNIE": 0410
     "URZAD_SKARBOWY_W_MOGILNIE": 0411
     "URZAD_SKARBOWY_W_NAKLE_NAD_NOTECIA": 0412
     "URZAD_SKARBOWY_W_RADZIEJOWIE": 0413
     "URZAD_SKARBOWY_W_RYPINIE": 0414
     "URZAD_SKARBOWY_W_SWIECIU": 0415
     "PIERWSZY_URZAD_SKARBOWY_W_TORUNIU": 0416
     "DRUGI_URZAD_SKARBOWY_W_TORUNIU": 0417
     "URZAD_SKARBOWY_W_TUCHOLI": 0418
     "URZAD_SKARBOWY_W_WABRZEZNIE": 0419
     "URZAD_SKARBOWY_WE_WLOCLAWKU": 0420
     "URZAD_SKARBOWY_W_ZNINIE": 0421
     "URZAD_SKARBOWY_W_GOLUBIU_DOBRZYNIU": 0422
     "URZAD_SKARBOWY_W_SEPOLNIE_KRAJENSKIM": 0423
     "KUJAWSKO_POMORSKI_URZAD_SKARBOWY_W_BYDGOSZCZY": 0471
     "URZAD_SKARBOWY_W_BIALEJ_PODLASKIEJ": 0602
     "URZAD_SKARBOWY_W_BILGORAJU": 0603
     "URZAD_SKARBOWY_W_CHELMIE": 0604
     "URZAD_SKARBOWY_W_HRUBIESZOWIE": 0605
     "URZAD_SKARBOWY_W_JANOWIE_LUBELSKIM": 0606
     "URZAD_SKARBOWY_W_KRASNYMSTAWIE": 0607
     "URZAD_SKARBOWY_W_KRASNIKU": 0608
     "URZAD_SKARBOWY_W_LUBARTOWIE": 0609
     "PIERWSZY_URZAD_SKARBOWY_W_LUBLINIE": 0610
     "DRUGI_URZAD_SKARBOWY_W_LUBLINIE": 0611
     "TRZECI_URZAD_SKARBOWY_W_LUBLINIE": 0612
     "URZAD_SKARBOWY_W_LUKOWIE": 0613
     "URZAD_SKARBOWY_W_OPOLU_LUBELSKIM": 0614
     "URZAD_SKARBOWY_W_PARCZEWIE": 0615
     "URZAD_SKARBOWY_W_PULAWACH": 0616
     "URZAD_SKARBOWY_W_RADZYNIU_PODLASKIM": 0617
     "URZAD_SKARBOWY_W_TOMASZOWIE_LUBELSKIM": 0618
     "URZAD_SKARBOWY_WE_WLODAWIE": 0619
     "URZAD_SKARBOWY_W_ZAMOSCIU": 0620
     "URZAD_SKARBOWY_W_LECZNEJ": 0621
     "URZAD_SKARBOWY_W_RYKACH": 0622
     "LUBELSKI_URZAD_SKARBOWY_W_LUBLINIE": 0671
     "URZAD_SKARBOWY_W_GORZOWIE_WIELKOPOLSKIM": 0802
     "URZAD_SKARBOWY_W_KROSNIE_ODRZANSKIM": 0803
     "URZAD_SKARBOWY_W_MIEDZYRZECZU": 0804
     "URZAD_SKARBOWY_W_NOWEJ_SOLI": 0805
     "URZAD_SKARBOWY_W_SLUBICACH": 0806
     "URZAD_SKARBOWY_W_SWIEBODZINIE": 0807
     "PIERWSZY_URZAD_SKARBOWY_W_ZIELONEJ_GORZE": 0808
     "DRUGI_URZAD_SKARBOWY_W_ZIELONEJ_GORZE": 0809
     "URZAD_SKARBOWY_W_ZAGANIU": 0810
     "URZAD_SKARBOWY_W_ZARACH": 0811
     "URZAD_SKARBOWY_W_DREZDENKU": 0812
     "URZAD_SKARBOWY_W_SULECINIE": 0813
     "URZAD_SKARBOWY_WE_WSCHOWIE": 0814
     "LUBUSKI_URZAD_SKARBOWY_W_ZIELONEJ_GORZE": 0871
     "URZAD_SKARBOWY_W_BELCHATOWIE": 1002
     "URZAD_SKARBOWY_W_BRZEZINACH": 1003
     "URZAD_SKARBOWY_W_GLOWNIE": 1004
     "URZAD_SKARBOWY_W_KUTNIE": 1005
     "URZAD_SKARBOWY_W_LASKU": 1006
     "URZAD_SKARBOWY_W_LOWICZU": 1007
     "PIERWSZY_URZAD_SKARBOWY_LODZ_BALUTY": 1008
     "DRUGI_URZAD_SKARBOWY_LODZ_BALUTY": 1009
     "PIERWSZY_URZAD_SKARBOWY_LODZ_GORNA": 1010
     "DRUGI_URZAD_SKARBOWY_LODZ_GORNA": 1011
     "URZAD_SKARBOWY_LODZ_POLESIE": 1012
     "URZAD_SKARBOWY_LODZ_SRODMIESCIE": 1013
     "URZAD_SKARBOWY_LODZ_WIDZEW": 1014
     "URZAD_SKARBOWY_W_OPOCZNIE": 1015
     "URZAD_SKARBOWY_W_PABIANICACH": 1016
     "URZAD_SKARBOWY_W_PIOTRKOWIE_TRYBUNALSKIM": 1017
     "URZAD_SKARBOWY_W_PODDEBICACH": 1018
     "URZAD_SKARBOWY_W_RADOMSKU": 1019
     "URZAD_SKARBOWY_W_RAWIE_MAZOWIECKIEJ": 1020
     "URZAD_SKARBOWY_W_SIERADZU": 1021
     "URZAD_SKARBOWY_W_SKIERNIEWICACH": 1022
     "URZAD_SKARBOWY_W_TOMASZOWIE_MAZOWIECKIM": 1023
     "URZAD_SKARBOWY_W_WIELUNIU": 1024
     "URZAD_SKARBOWY_W_ZDUNSKIEJ_WOLI": 1025
     "URZAD_SKARBOWY_W_ZGIERZU": 1026
     "URZAD_SKARBOWY_W_WIERUSZOWIE": 1027
     "URZAD_SKARBOWY_W_LECZYCY": 1028
     "URZAD_SKARBOWY_W_PAJECZNIE": 1029
     "LODZKI_URZAD_SKARBOWY_W_LODZI": 1071
     "URZAD_SKARBOWY_W_BOCHNI": 1202
     "URZAD_SKARBOWY_W_BRZESKU": 1203
     "URZAD_SKARBOWY_W_CHRZANOWIE": 1204
     "URZAD_SKARBOWY_W_DABROWIE_TARNOWSKIEJ": 1205
     "URZAD_SKARBOWY_W_GORLICACH": 1206
     "PIERWSZY_URZAD_SKARBOWY_KRAKOW": 1207
     "URZAD_SKARBOWY_KRAKOW_KROWODRZA": 1208
     "URZAD_SKARBOWY_KRAKOW_NOWA_HUTA": 1209
     "URZAD_SKARBOWY_KRAKOW_PODGORZE": 1210
     "URZAD_SKARBOWY_KRAKOW_PRADNIK": 1211
     "URZAD_SKARBOWY_KRAKOW_STARE_MIASTO": 1212
     "URZAD_SKARBOWY_KRAKOW_SRODMIESCIE": 1213
     "URZAD_SKARBOWY_W_LIMANOWEJ": 1214
     "URZAD_SKARBOWY_W_MIECHOWIE": 1215
     "URZAD_SKARBOWY_W_MYSLENICACH": 1216
     "URZAD_SKARBOWY_W_NOWYM_SACZU": 1217
     "URZAD_SKARBOWY_W_NOWYM_TARGU": 1218
     "URZAD_SKARBOWY_W_OLKUSZU": 1219
     "URZAD_SKARBOWY_W_OSWIECIMIU": 1220
     "URZAD_SKARBOWY_W_PROSZOWICACH": 1221
     "URZAD_SKARBOWY_W_SUCHEJ_BESKIDZKIEJ": 1222
     "PIERWSZY_URZAD_SKARBOWY_W_TARNOWIE": 1223
     "DRUGI_URZAD_SKARBOWY_W_TARNOWIE": 1224
     "URZAD_SKARBOWY_W_WADOWICACH": 1225
     "URZAD_SKARBOWY_W_WIELICZCE": 1226
     "URZAD_SKARBOWY_W_ZAKOPANEM": 1227
     "DRUGI_URZAD_SKARBOWY_KRAKOW": 1228
     "MALOPOLSKI_URZAD_SKARBOWY_W_KRAKOWIE": 1271
     "URZAD_SKARBOWY_W_BIALOBRZEGACH": 1402
     "URZAD_SKARBOWY_W_CIECHANOWIE": 1403
     "URZAD_SKARBOWY_W_GARWOLINIE": 1404
     "URZAD_SKARBOWY_W_GOSTYNINIE": 1405
     "URZAD_SKARBOWY_W_GRODZISKU_MAZOWIECKIM": 1406
     "URZAD_SKARBOWY_W_GROJCU": 1407
     "URZAD_SKARBOWY_W_KOZIENICACH": 1408
     "URZAD_SKARBOWY_W_LEGIONOWIE": 1409
     "URZAD_SKARBOWY_W_LOSICACH": 1410
     "URZAD_SKARBOWY_W_MAKOWIE_MAZOWIECKIM": 1411
     "URZAD_SKARBOWY_W_MINSKU_MAZOWIECKIM": 1412
     "URZAD_SKARBOWY_W_MLAWIE": 1413
     "URZAD_SKARBOWY_W_NOWYM_DWORZE_MAZOWIECKIM": 1414
     "URZAD_SKARBOWY_W_OSTROLECE": 1415
     "URZAD_SKARBOWY_W_OSTROWI_MAZOWIECKIEJ": 1416
     "URZAD_SKARBOWY_W_OTWOCKU": 1417
     "URZAD_SKARBOWY_W_PIASECZNIE": 1418
     "URZAD_SKARBOWY_W_PLOCKU": 1419
     "URZAD_SKARBOWY_W_PLONSKU": 1420
     "URZAD_SKARBOWY_W_PRUSZKOWIE": 1421
     "URZAD_SKARBOWY_W_PRZASNYSZU": 1422
     "URZAD_SKARBOWY_W_PULTUSKU": 1423
     "PIERWSZY_URZAD_SKARBOWY_W_RADOMIU": 1424
     "DRUGI_URZAD_SKARBOWY_W_RADOMIU": 1425
     "URZAD_SKARBOWY_W_SIEDLCACH": 1426
     "URZAD_SKARBOWY_W_SIERPCU": 1427
     "URZAD_SKARBOWY_W_SOCHACZEWIE": 1428
     "URZAD_SKARBOWY_W_SOKOLOWIE_PODLASKIM": 1429
     "URZAD_SKARBOWY_W_SZYDLOWCU": 1430
     "URZAD_SKARBOWY_WARSZAWA_BEMOWO": 1431
     "URZAD_SKARBOWY_WARSZAWA_BIELANY": 1432
     "URZAD_SKARBOWY_WARSZAWA_MOKOTOW": 1433
     "URZAD_SKARBOWY_WARSZAWA_PRAGA": 1434
     "PIERWSZY_URZAD_SKARBOWY_WARSZAWA_SRODMIESCIE": 1435
     "DRUGI_URZAD_SKARBOWY_WARSZAWA_SRODMIESCIE": 1436
     "URZAD_SKARBOWY_WARSZAWA_TARGOWEK": 1437
     "URZAD_SKARBOWY_WARSZAWA_URSYNOW": 1438
     "URZAD_SKARBOWY_WARSZAWA_WAWER": 1439
     "URZAD_SKARBOWY_WARSZAWA_WOLA": 1440
     "URZAD_SKARBOWY_W_WEGROWIE": 1441
     "URZAD_SKARBOWY_W_WOLOMINIE": 1442
     "URZAD_SKARBOWY_W_WYSZKOWIE": 1443
     "URZAD_SKARBOWY_W_ZWOLENIU": 1444
     "URZAD_SKARBOWY_W_ZUROMINIE": 1445
     "URZAD_SKARBOWY_W_ZYRARDOWIE": 1446
     "URZAD_SKARBOWY_W_LIPSKU": 1447
     "URZAD_SKARBOWY_W_PRZYSUSZE": 1448
     "TRZECI_URZAD_SKARBOWY_WARSZAWA_SRODMIESCIE": 1449
     "PIERWSZY_MAZOWIECKI_URZAD_SKARBOWY_W_WARSZAWIE": 1471
     "DRUGI_MAZOWIECKI_URZAD_SKARBOWY_W_WARSZAWIE": 1472
     "TRZECI_MAZOWIECKI_URZAD_SKARBOWY_W_RADOMIU": 1473
     "URZAD_SKARBOWY_W_BRZEGU": 1602
     "URZAD_SKARBOWY_W_GLUBCZYCACH": 1603
     "URZAD_SKARBOWY_W_KEDZIERZYNIE_KOZLU": 1604
     "URZAD_SKARBOWY_W_KLUCZBORKU": 1605
     "URZAD_SKARBOWY_W_NAMYSLOWIE": 1606
     "URZAD_SKARBOWY_W_NYSIE": 1607
     "URZAD_SKARBOWY_W_OLESNIE": 1608
     "PIERWSZY_URZAD_SKARBOWY_W_OPOLU": 1609
     "DRUGI_URZAD_SKARBOWY_W_OPOLU": 1610
     "URZAD_SKARBOWY_W_PRUDNIKU": 1611
     "URZAD_SKARBOWY_W_STRZELCACH_OPOLSKICH": 1612
     "URZAD_SKARBOWY_W_KRAPKOWICACH": 1613
     "OPOLSKI_URZAD_SKARBOWY_W_OPOLU": 1671
     "URZAD_SKARBOWY_W_BRZOZOWIE": 1802
     "URZAD_SKARBOWY_W_DEBICY": 1803
     "URZAD_SKARBOWY_W_JAROSLAWIU": 1804
     "URZAD_SKARBOWY_W_JASLE": 1805
     "URZAD_SKARBOWY_W_KOLBUSZOWEJ": 1806
     "URZAD_SKARBOWY_W_KROSNIE": 1807
     "URZAD_SKARBOWY_W_LESKU": 1808
     "URZAD_SKARBOWY_W_LEZAJSKU": 1809
     "URZAD_SKARBOWY_W_LUBACZOWIE": 1810
     "URZAD_SKARBOWY_W_LANCUCIE": 1811
     "URZAD_SKARBOWY_W_MIELCU": 1812
     "URZAD_SKARBOWY_W_PRZEMYSLU": 1813
     "URZAD_SKARBOWY_W_PRZEWORSKU": 1814
     "URZAD_SKARBOWY_W_ROPCZYCACH": 1815
     "PIERWSZY_URZAD_SKARBOWY_W_RZESZOWIE": 1816
     "URZAD_SKARBOWY_W_SANOKU": 1817
     "URZAD_SKARBOWY_W_STALOWEJ_WOLI": 1818
     "URZAD_SKARBOWY_W_STRZYZOWIE": 1819
     "URZAD_SKARBOWY_W_TARNOBRZEGU": 1820
     "URZAD_SKARBOWY_W_USTRZYKACH_DOLNYCH": 1821
     "DRUGI_URZAD_SKARBOWY_W_RZESZOWIE": 1822
     "URZAD_SKARBOWY_W_NISKU": 1823
     "PODKARPACKI_URZAD_SKARBOWY_W_RZESZOWIE": 1871
     "URZAD_SKARBOWY_W_AUGUSTOWIE": 2002
     "PIERWSZY_URZAD_SKARBOWY_W_BIALYMSTOKU": 2003
     "DRUGI_URZAD_SKARBOWY_W_BIALYMSTOKU": 2004
     "URZAD_SKARBOWY_W_BIELSKU_PODLASKIM": 2005
     "URZAD_SKARBOWY_W_GRAJEWIE": 2006
     "URZAD_SKARBOWY_W_KOLNIE": 2007
     "URZAD_SKARBOWY_W_LOMZY": 2008
     "URZAD_SKARBOWY_W_MONKACH": 2009
     "URZAD_SKARBOWY_W_SIEMIATYCZACH": 2010
     "URZAD_SKARBOWY_W_SOKOLCE": 2011
     "URZAD_SKARBOWY_W_SUWALKACH": 2012
     "URZAD_SKARBOWY_W_WYSOKIEM_MAZOWIECKIEM": 2013
     "URZAD_SKARBOWY_W_ZAMBROWIE": 2014
     "URZAD_SKARBOWY_W_HAJNOWCE": 2015
     "PODLASKI_URZAD_SKARBOWY_W_BIALYMSTOKU": 2071
     "URZAD_SKARBOWY_W_BYTOWIE": 2202
     "URZAD_SKARBOWY_W_CHOJNICACH": 2203
     "URZAD_SKARBOWY_W_CZLUCHOWIE": 2204
     "PIERWSZY_URZAD_SKARBOWY_W_GDANSKU": 2205
     "DRUGI_URZAD_SKARBOWY_W_GDANSKU": 2206
     "TRZECI_URZAD_SKARBOWY_W_GDANSKU": 2207
     "PIERWSZY_URZAD_SKARBOWY_W_GDYNI": 2208
     "DRUGI_URZAD_SKARBOWY_W_GDYNI": 2209
     "URZAD_SKARBOWY_W_KARTUZACH": 2210
     "URZAD_SKARBOWY_W_KOSCIERZYNIE": 2211
     "URZAD_SKARBOWY_W_KWIDZYNIE": 2212
     "URZAD_SKARBOWY_W_LEBORKU": 2213
     "URZAD_SKARBOWY_W_MALBORKU": 2214
     "URZAD_SKARBOWY_W_PUCKU": 2215
     "URZAD_SKARBOWY_W_SLUPSKU": 2216
     "URZAD_SKARBOWY_W_SOPOCIE": 2217
     "URZAD_SKARBOWY_W_STAROGARDZIE_GDANSKIM": 2218
     "URZAD_SKARBOWY_W_TCZEWIE": 2219
     "URZAD_SKARBOWY_W_WEJHEROWIE": 2220
     "URZAD_SKARBOWY_W_PRUSZCZU_GDANSKIM": 2221
     "POMORSKI_URZAD_SKARBOWY_W_GDANSKU": 2271
     "URZAD_SKARBOWY_W_BEDZINIE": 2402
     "PIERWSZY_URZAD_SKARBOWY_W_BIELSKU_BIALEJ": 2403
     "DRUGI_URZAD_SKARBOWY_W_BIELSKU_BIALEJ": 2404
     "URZAD_SKARBOWY_W_BYTOMIU": 2405
     "URZAD_SKARBOWY_W_CHORZOWIE": 2406
     "URZAD_SKARBOWY_W_CIESZYNIE": 2407
     "URZAD_SKARBOWY_W_CZECHOWICACH_DZIEDZICACH": 2408
     "PIERWSZY_URZAD_SKARBOWY_W_CZESTOCHOWIE": 2409
     "DRUGI_URZAD_SKARBOWY_W_CZESTOCHOWIE": 2410
     "URZAD_SKARBOWY_W_DABROWIE_GORNICZEJ": 2411
     "PIERWSZY_URZAD_SKARBOWY_W_GLIWICACH": 2412
     "DRUGI_URZAD_SKARBOWY_W_GLIWICACH": 2413
     "URZAD_SKARBOWY_W_JASTRZEBIU_ZDROJU": 2414
     "URZAD_SKARBOWY_W_JAWORZNIE": 2415
     "PIERWSZY_URZAD_SKARBOWY_W_KATOWICACH": 2416
     "DRUGI_URZAD_SKARBOWY_W_KATOWICACH": 2417
     "URZAD_SKARBOWY_W_KLOBUCKU": 2418
     "URZAD_SKARBOWY_W_LUBLINCU": 2419
     "URZAD_SKARBOWY_W_MIKOLOWIE": 2420
     "URZAD_SKARBOWY_W_MYSLOWICACH": 2421
     "URZAD_SKARBOWY_W_MYSZKOWIE": 2422
     "URZAD_SKARBOWY_W_PIEKARACH_SLASKICH": 2423
     "URZAD_SKARBOWY_W_PSZCZYNIE": 2424
     "URZAD_SKARBOWY_W_RACIBORZU": 2425
     "URZAD_SKARBOWY_W_RUDZIE_SLASKIEJ": 2426
     "URZAD_SKARBOWY_W_RYBNIKU": 2427
     "URZAD_SKARBOWY_W_SIEMIANOWICACH_SLASKICH": 2428
     "URZAD_SKARBOWY_W_SOSNOWCU": 2429
     "URZAD_SKARBOWY_W_TARNOWSKICH_GORACH": 2430
     "URZAD_SKARBOWY_W_TYCHACH": 2431
     "URZAD_SKARBOWY_W_WODZISLAWIU_SLASKIM": 2432
     "URZAD_SKARBOWY_W_ZABRZU": 2433
     "URZAD_SKARBOWY_W_ZAWIERCIU": 2434
     "URZAD_SKARBOWY_W_ZORACH": 2435
     "URZAD_SKARBOWY_W_ZYWCU": 2436
     "PIERWSZY_SLASKI_URZAD_SKARBOWY_W_SOSNOWCU": 2471
     "DRUGI_SLASKI_URZAD_SKARBOWY_W_BIELSKU_BIALEJ": 2472
     "URZAD_SKARBOWY_W_BUSKU_ZDROJU": 2602
     "URZAD_SKARBOWY_W_JEDRZEJOWIE": 2603
     "PIERWSZY_URZAD_SKARBOWY_W_KIELCACH": 2604
     "DRUGI_URZAD_SKARBOWY_W_KIELCACH": 2605
     "URZAD_SKARBOWY_W_KONSKICH": 2606
     "URZAD_SKARBOWY_W_OPATOWIE": 2607
     "URZAD_SKARBOWY_W_OSTROWCU_SWIETOKRZYSKIM": 2608
     "URZAD_SKARBOWY_W_PINCZOWIE": 2609
     "URZAD_SKARBOWY_W_SANDOMIERZU": 2610
     "URZAD_SKARBOWY_W_SKARZYSKU_KAMIENNEJ": 2611
     "URZAD_SKARBOWY_W_STARACHOWICACH": 2612
     "URZAD_SKARBOWY_W_STASZOWIE": 2613
     "URZAD_SKARBOWY_W_KAZIMIERZY_WIELKIEJ": 2614
     "URZAD_SKARBOWY_WE_WLOSZCZOWIE": 2615
     "SWIETOKRZYSKI_URZAD_SKARBOWY_W_KIELCACH": 2671
     "URZAD_SKARBOWY_W_BARTOSZYCACH": 2802
     "URZAD_SKARBOWY_W_BRANIEWIE": 2803
     "URZAD_SKARBOWY_W_DZIALDOWIE": 2804
     "URZAD_SKARBOWY_W_ELBLAGU": 2805
     "URZAD_SKARBOWY_W_ELKU": 2806
     "URZAD_SKARBOWY_W_GIZYCKU": 2807
     "URZAD_SKARBOWY_W_ILAWIE": 2808
     "URZAD_SKARBOWY_W_KETRZYNIE": 2809
     "URZAD_SKARBOWY_W_NIDZICY": 2810
     "URZAD_SKARBOWY_W_NOWYM_MIESCIE_LUBAWSKIM": 2811
     "URZAD_SKARBOWY_W_OLECKU": 2812
     "URZAD_SKARBOWY_W_OLSZTYNIE": 2813
     "URZAD_SKARBOWY_W_OSTRODZIE": 2814
     "URZAD_SKARBOWY_W_PISZU": 2815
     "URZAD_SKARBOWY_W_SZCZYTNIE": 2816
     "WARMINSKO_MAZURSKI_URZAD_SKARBOWY_W_OLSZTYNIE": 2871
     "URZAD_SKARBOWY_W_CZARNKOWIE": 3002
     "URZAD_SKARBOWY_W_GNIEZNIE": 3003
     "URZAD_SKARBOWY_W_GOSTYNIU": 3004
     "URZAD_SKARBOWY_W_GRODZISKU_WIELKOPOLSKIM": 3005
     "URZAD_SKARBOWY_W_JAROCINIE": 3006
     "PIERWSZY_URZAD_SKARBOWY_W_KALISZU": 3007
     "DRUGI_URZAD_SKARBOWY_W_KALISZU": 3008
     "URZAD_SKARBOWY_W_KEPNIE": 3009
     "URZAD_SKARBOWY_W_KOLE": 3010
     "URZAD_SKARBOWY_W_KONINIE": 3011
     "URZAD_SKARBOWY_W_KOSCIANIE": 3012
     "URZAD_SKARBOWY_W_KROTOSZYNIE": 3013
     "URZAD_SKARBOWY_W_LESZNIE": 3014
     "URZAD_SKARBOWY_W_MIEDZYCHODZIE": 3015
     "URZAD_SKARBOWY_W_NOWYM_TOMYSLU": 3016
     "URZAD_SKARBOWY_W_OSTROWIE_WIELKOPOLSKIM": 3017
     "URZAD_SKARBOWY_W_OSTRZESZOWIE": 3018
     "URZAD_SKARBOWY_W_PILE": 3019
     "URZAD_SKARBOWY_POZNAN_GRUNWALD": 3020
     "URZAD_SKARBOWY_POZNAN_JEZYCE": 3021
     "URZAD_SKARBOWY_POZNAN_NOWE_MIASTO": 3022
     "PIERWSZY_URZAD_SKARBOWY_W_POZNANIU": 3023
     "URZAD_SKARBOWY_POZNAN_WINOGRADY": 3025
     "URZAD_SKARBOWY_POZNAN_WILDA": 3026
     "URZAD_SKARBOWY_W_RAWICZU": 3027
     "URZAD_SKARBOWY_W_SLUPCY": 3028
     "URZAD_SKARBOWY_W_SZAMOTULACH": 3029
     "URZAD_SKARBOWY_W_SREMIE": 3030
     "URZAD_SKARBOWY_W_SRODZIE_WIELKOPOLSKIEJ": 3031
     "URZAD_SKARBOWY_W_TURKU": 3032
     "URZAD_SKARBOWY_W_WAGROWCU": 3033
     "URZAD_SKARBOWY_W_WOLSZTYNIE": 3034
     "URZAD_SKARBOWY_WE_WRZESNI": 3035
     "URZAD_SKARBOWY_W_ZLOTOWIE": 3036
     "URZAD_SKARBOWY_W_CHODZIEZY": 3037
     "URZAD_SKARBOWY_W_OBORNIKACH": 3038
     "URZAD_SKARBOWY_W_PLESZEWIE": 3039
     "PIERWSZY_WIELKOPOLSKI_URZAD_SKARBOWY_W_POZNANIU": 3071
     "DRUGI_WIELKOPOLSKI_URZAD_SKARBOWY_W_KALISZU": 3072
     "URZAD_SKARBOWY_W_BIALOGARDZIE": 3202
     "URZAD_SKARBOWY_W_CHOSZCZNIE": 3203
     "URZAD_SKARBOWY_W_DRAWSKU_POMORSKIM": 3204
     "URZAD_SKARBOWY_W_GOLENIOWIE": 3205
     "URZAD_SKARBOWY_W_GRYFICACH": 3206
     "URZAD_SKARBOWY_W_GRYFINIE": 3207
     "URZAD_SKARBOWY_W_KAMIENIU_POMORSKIM": 3208
     "URZAD_SKARBOWY_W_KOLOBRZEGU": 3209
     "PIERWSZY_URZAD_SKARBOWY_W_KOSZALINIE": 3210
     "DRUGI_URZAD_SKARBOWY_W_KOSZALINIE": 3211
     "URZAD_SKARBOWY_W_MYSLIBORZU": 3212
     "URZAD_SKARBOWY_W_PYRZYCACH": 3213
     "URZAD_SKARBOWY_W_STARGARDZIE": 3214
     "PIERWSZY_URZAD_SKARBOWY_W_SZCZECINIE": 3215
     "DRUGI_URZAD_SKARBOWY_W_SZCZECINIE": 3216
     "TRZECI_URZAD_SKARBOWY_W_SZCZECINIE": 3217
     "URZAD_SKARBOWY_W_SZCZECINKU": 3218
     "URZAD_SKARBOWY_W_SWINOUJSCIU": 3219
     "URZAD_SKARBOWY_W_WALCZU": 3220
     "ZACHODNIOPOMORSKI_URZAD_SKARBOWY_W_SZCZECINIE": 3271
    """

    VALUE_0202 = "0202"
    VALUE_0203 = "0203"
    VALUE_0204 = "0204"
    VALUE_0205 = "0205"
    VALUE_0206 = "0206"
    VALUE_0207 = "0207"
    VALUE_0208 = "0208"
    VALUE_0209 = "0209"
    VALUE_0210 = "0210"
    VALUE_0211 = "0211"
    VALUE_0212 = "0212"
    VALUE_0213 = "0213"
    VALUE_0214 = "0214"
    VALUE_0215 = "0215"
    VALUE_0216 = "0216"
    VALUE_0217 = "0217"
    VALUE_0218 = "0218"
    VALUE_0219 = "0219"
    VALUE_0220 = "0220"
    VALUE_0221 = "0221"
    VALUE_0222 = "0222"
    VALUE_0223 = "0223"
    VALUE_0224 = "0224"
    VALUE_0225 = "0225"
    VALUE_0226 = "0226"
    VALUE_0227 = "0227"
    VALUE_0228 = "0228"
    VALUE_0229 = "0229"
    VALUE_0230 = "0230"
    VALUE_0231 = "0231"
    VALUE_0232 = "0232"
    VALUE_0233 = "0233"
    VALUE_0234 = "0234"
    VALUE_0271 = "0271"
    VALUE_0402 = "0402"
    VALUE_0403 = "0403"
    VALUE_0404 = "0404"
    VALUE_0405 = "0405"
    VALUE_0406 = "0406"
    VALUE_0407 = "0407"
    VALUE_0408 = "0408"
    VALUE_0409 = "0409"
    VALUE_0410 = "0410"
    VALUE_0411 = "0411"
    VALUE_0412 = "0412"
    VALUE_0413 = "0413"
    VALUE_0414 = "0414"
    VALUE_0415 = "0415"
    VALUE_0416 = "0416"
    VALUE_0417 = "0417"
    VALUE_0418 = "0418"
    VALUE_0419 = "0419"
    VALUE_0420 = "0420"
    VALUE_0421 = "0421"
    VALUE_0422 = "0422"
    VALUE_0423 = "0423"
    VALUE_0471 = "0471"
    VALUE_0602 = "0602"
    VALUE_0603 = "0603"
    VALUE_0604 = "0604"
    VALUE_0605 = "0605"
    VALUE_0606 = "0606"
    VALUE_0607 = "0607"
    VALUE_0608 = "0608"
    VALUE_0609 = "0609"
    VALUE_0610 = "0610"
    VALUE_0611 = "0611"
    VALUE_0612 = "0612"
    VALUE_0613 = "0613"
    VALUE_0614 = "0614"
    VALUE_0615 = "0615"
    VALUE_0616 = "0616"
    VALUE_0617 = "0617"
    VALUE_0618 = "0618"
    VALUE_0619 = "0619"
    VALUE_0620 = "0620"
    VALUE_0621 = "0621"
    VALUE_0622 = "0622"
    VALUE_0671 = "0671"
    VALUE_0802 = "0802"
    VALUE_0803 = "0803"
    VALUE_0804 = "0804"
    VALUE_0805 = "0805"
    VALUE_0806 = "0806"
    VALUE_0807 = "0807"
    VALUE_0808 = "0808"
    VALUE_0809 = "0809"
    VALUE_0810 = "0810"
    VALUE_0811 = "0811"
    VALUE_0812 = "0812"
    VALUE_0813 = "0813"
    VALUE_0814 = "0814"
    VALUE_0871 = "0871"
    VALUE_1002 = "1002"
    VALUE_1003 = "1003"
    VALUE_1004 = "1004"
    VALUE_1005 = "1005"
    VALUE_1006 = "1006"
    VALUE_1007 = "1007"
    VALUE_1008 = "1008"
    VALUE_1009 = "1009"
    VALUE_1010 = "1010"
    VALUE_1011 = "1011"
    VALUE_1012 = "1012"
    VALUE_1013 = "1013"
    VALUE_1014 = "1014"
    VALUE_1015 = "1015"
    VALUE_1016 = "1016"
    VALUE_1017 = "1017"
    VALUE_1018 = "1018"
    VALUE_1019 = "1019"
    VALUE_1020 = "1020"
    VALUE_1021 = "1021"
    VALUE_1022 = "1022"
    VALUE_1023 = "1023"
    VALUE_1024 = "1024"
    VALUE_1025 = "1025"
    VALUE_1026 = "1026"
    VALUE_1027 = "1027"
    VALUE_1028 = "1028"
    VALUE_1029 = "1029"
    VALUE_1071 = "1071"
    VALUE_1202 = "1202"
    VALUE_1203 = "1203"
    VALUE_1204 = "1204"
    VALUE_1205 = "1205"
    VALUE_1206 = "1206"
    VALUE_1207 = "1207"
    VALUE_1208 = "1208"
    VALUE_1209 = "1209"
    VALUE_1210 = "1210"
    VALUE_1211 = "1211"
    VALUE_1212 = "1212"
    VALUE_1213 = "1213"
    VALUE_1214 = "1214"
    VALUE_1215 = "1215"
    VALUE_1216 = "1216"
    VALUE_1217 = "1217"
    VALUE_1218 = "1218"
    VALUE_1219 = "1219"
    VALUE_1220 = "1220"
    VALUE_1221 = "1221"
    VALUE_1222 = "1222"
    VALUE_1223 = "1223"
    VALUE_1224 = "1224"
    VALUE_1225 = "1225"
    VALUE_1226 = "1226"
    VALUE_1227 = "1227"
    VALUE_1228 = "1228"
    VALUE_1271 = "1271"
    VALUE_1402 = "1402"
    VALUE_1403 = "1403"
    VALUE_1404 = "1404"
    VALUE_1405 = "1405"
    VALUE_1406 = "1406"
    VALUE_1407 = "1407"
    VALUE_1408 = "1408"
    VALUE_1409 = "1409"
    VALUE_1410 = "1410"
    VALUE_1411 = "1411"
    VALUE_1412 = "1412"
    VALUE_1413 = "1413"
    VALUE_1414 = "1414"
    VALUE_1415 = "1415"
    VALUE_1416 = "1416"
    VALUE_1417 = "1417"
    VALUE_1418 = "1418"
    VALUE_1419 = "1419"
    VALUE_1420 = "1420"
    VALUE_1421 = "1421"
    VALUE_1422 = "1422"
    VALUE_1423 = "1423"
    VALUE_1424 = "1424"
    VALUE_1425 = "1425"
    VALUE_1426 = "1426"
    VALUE_1427 = "1427"
    VALUE_1428 = "1428"
    VALUE_1429 = "1429"
    VALUE_1430 = "1430"
    VALUE_1431 = "1431"
    VALUE_1432 = "1432"
    VALUE_1433 = "1433"
    VALUE_1434 = "1434"
    VALUE_1435 = "1435"
    VALUE_1436 = "1436"
    VALUE_1437 = "1437"
    VALUE_1438 = "1438"
    VALUE_1439 = "1439"
    VALUE_1440 = "1440"
    VALUE_1441 = "1441"
    VALUE_1442 = "1442"
    VALUE_1443 = "1443"
    VALUE_1444 = "1444"
    VALUE_1445 = "1445"
    VALUE_1446 = "1446"
    VALUE_1447 = "1447"
    VALUE_1448 = "1448"
    VALUE_1449 = "1449"
    VALUE_1471 = "1471"
    VALUE_1472 = "1472"
    VALUE_1473 = "1473"
    VALUE_1602 = "1602"
    VALUE_1603 = "1603"
    VALUE_1604 = "1604"
    VALUE_1605 = "1605"
    VALUE_1606 = "1606"
    VALUE_1607 = "1607"
    VALUE_1608 = "1608"
    VALUE_1609 = "1609"
    VALUE_1610 = "1610"
    VALUE_1611 = "1611"
    VALUE_1612 = "1612"
    VALUE_1613 = "1613"
    VALUE_1671 = "1671"
    VALUE_1802 = "1802"
    VALUE_1803 = "1803"
    VALUE_1804 = "1804"
    VALUE_1805 = "1805"
    VALUE_1806 = "1806"
    VALUE_1807 = "1807"
    VALUE_1808 = "1808"
    VALUE_1809 = "1809"
    VALUE_1810 = "1810"
    VALUE_1811 = "1811"
    VALUE_1812 = "1812"
    VALUE_1813 = "1813"
    VALUE_1814 = "1814"
    VALUE_1815 = "1815"
    VALUE_1816 = "1816"
    VALUE_1817 = "1817"
    VALUE_1818 = "1818"
    VALUE_1819 = "1819"
    VALUE_1820 = "1820"
    VALUE_1821 = "1821"
    VALUE_1822 = "1822"
    VALUE_1823 = "1823"
    VALUE_1871 = "1871"
    VALUE_2002 = "2002"
    VALUE_2003 = "2003"
    VALUE_2004 = "2004"
    VALUE_2005 = "2005"
    VALUE_2006 = "2006"
    VALUE_2007 = "2007"
    VALUE_2008 = "2008"
    VALUE_2009 = "2009"
    VALUE_2010 = "2010"
    VALUE_2011 = "2011"
    VALUE_2012 = "2012"
    VALUE_2013 = "2013"
    VALUE_2014 = "2014"
    VALUE_2015 = "2015"
    VALUE_2071 = "2071"
    VALUE_2202 = "2202"
    VALUE_2203 = "2203"
    VALUE_2204 = "2204"
    VALUE_2205 = "2205"
    VALUE_2206 = "2206"
    VALUE_2207 = "2207"
    VALUE_2208 = "2208"
    VALUE_2209 = "2209"
    VALUE_2210 = "2210"
    VALUE_2211 = "2211"
    VALUE_2212 = "2212"
    VALUE_2213 = "2213"
    VALUE_2214 = "2214"
    VALUE_2215 = "2215"
    VALUE_2216 = "2216"
    VALUE_2217 = "2217"
    VALUE_2218 = "2218"
    VALUE_2219 = "2219"
    VALUE_2220 = "2220"
    VALUE_2221 = "2221"
    VALUE_2271 = "2271"
    VALUE_2402 = "2402"
    VALUE_2403 = "2403"
    VALUE_2404 = "2404"
    VALUE_2405 = "2405"
    VALUE_2406 = "2406"
    VALUE_2407 = "2407"
    VALUE_2408 = "2408"
    VALUE_2409 = "2409"
    VALUE_2410 = "2410"
    VALUE_2411 = "2411"
    VALUE_2412 = "2412"
    VALUE_2413 = "2413"
    VALUE_2414 = "2414"
    VALUE_2415 = "2415"
    VALUE_2416 = "2416"
    VALUE_2417 = "2417"
    VALUE_2418 = "2418"
    VALUE_2419 = "2419"
    VALUE_2420 = "2420"
    VALUE_2421 = "2421"
    VALUE_2422 = "2422"
    VALUE_2423 = "2423"
    VALUE_2424 = "2424"
    VALUE_2425 = "2425"
    VALUE_2426 = "2426"
    VALUE_2427 = "2427"
    VALUE_2428 = "2428"
    VALUE_2429 = "2429"
    VALUE_2430 = "2430"
    VALUE_2431 = "2431"
    VALUE_2432 = "2432"
    VALUE_2433 = "2433"
    VALUE_2434 = "2434"
    VALUE_2435 = "2435"
    VALUE_2436 = "2436"
    VALUE_2471 = "2471"
    VALUE_2472 = "2472"
    VALUE_2602 = "2602"
    VALUE_2603 = "2603"
    VALUE_2604 = "2604"
    VALUE_2605 = "2605"
    VALUE_2606 = "2606"
    VALUE_2607 = "2607"
    VALUE_2608 = "2608"
    VALUE_2609 = "2609"
    VALUE_2610 = "2610"
    VALUE_2611 = "2611"
    VALUE_2612 = "2612"
    VALUE_2613 = "2613"
    VALUE_2614 = "2614"
    VALUE_2615 = "2615"
    VALUE_2671 = "2671"
    VALUE_2802 = "2802"
    VALUE_2803 = "2803"
    VALUE_2804 = "2804"
    VALUE_2805 = "2805"
    VALUE_2806 = "2806"
    VALUE_2807 = "2807"
    VALUE_2808 = "2808"
    VALUE_2809 = "2809"
    VALUE_2810 = "2810"
    VALUE_2811 = "2811"
    VALUE_2812 = "2812"
    VALUE_2813 = "2813"
    VALUE_2814 = "2814"
    VALUE_2815 = "2815"
    VALUE_2816 = "2816"
    VALUE_2871 = "2871"
    VALUE_3002 = "3002"
    VALUE_3003 = "3003"
    VALUE_3004 = "3004"
    VALUE_3005 = "3005"
    VALUE_3006 = "3006"
    VALUE_3007 = "3007"
    VALUE_3008 = "3008"
    VALUE_3009 = "3009"
    VALUE_3010 = "3010"
    VALUE_3011 = "3011"
    VALUE_3012 = "3012"
    VALUE_3013 = "3013"
    VALUE_3014 = "3014"
    VALUE_3015 = "3015"
    VALUE_3016 = "3016"
    VALUE_3017 = "3017"
    VALUE_3018 = "3018"
    VALUE_3019 = "3019"
    VALUE_3020 = "3020"
    VALUE_3021 = "3021"
    VALUE_3022 = "3022"
    VALUE_3023 = "3023"
    VALUE_3025 = "3025"
    VALUE_3026 = "3026"
    VALUE_3027 = "3027"
    VALUE_3028 = "3028"
    VALUE_3029 = "3029"
    VALUE_3030 = "3030"
    VALUE_3031 = "3031"
    VALUE_3032 = "3032"
    VALUE_3033 = "3033"
    VALUE_3034 = "3034"
    VALUE_3035 = "3035"
    VALUE_3036 = "3036"
    VALUE_3037 = "3037"
    VALUE_3038 = "3038"
    VALUE_3039 = "3039"
    VALUE_3071 = "3071"
    VALUE_3072 = "3072"
    VALUE_3202 = "3202"
    VALUE_3203 = "3203"
    VALUE_3204 = "3204"
    VALUE_3205 = "3205"
    VALUE_3206 = "3206"
    VALUE_3207 = "3207"
    VALUE_3208 = "3208"
    VALUE_3209 = "3209"
    VALUE_3210 = "3210"
    VALUE_3211 = "3211"
    VALUE_3212 = "3212"
    VALUE_3213 = "3213"
    VALUE_3214 = "3214"
    VALUE_3215 = "3215"
    VALUE_3216 = "3216"
    VALUE_3217 = "3217"
    VALUE_3218 = "3218"
    VALUE_3219 = "3219"
    VALUE_3220 = "3220"
    VALUE_3271 = "3271"


class TcelZlozenia(Enum):
    """
    Określa, czy to jest złożenie, czy korekta dokumentu.

    :cvar VALUE_1: złożenie po raz pierwszy deklaracji za dany okres
    :cvar VALUE_2: korekta deklaracji za dany okres
    """

    VALUE_1 = 1
    VALUE_2 = 2


class TidentyfikatorOsobyFizycznej1(BaseModel):
    """
    Podstawowy zestaw danych identyfikacyjnych o osobie fizycznej z identyfikatorem
    NIP albo PESEL.

    :ivar nip: Identyfikator podatkowy NIP
    :ivar pesel: Identyfikator podatkowy numer PESEL
    :ivar imie_pierwsze: Pierwsze imię
    :ivar nazwisko: Nazwisko
    :ivar data_urodzenia: Data urodzenia
    """

    class Meta:
        name = "TIdentyfikatorOsobyFizycznej1"
        target_namespace = "http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2022/09/13/eD/DefinicjeTypy/"

    model_config = ConfigDict(defer_build=True)
    nip: Optional[str] = field(
        default=None,
        metadata={
            "name": "NIP",
            "type": "Element",
            "namespace": "http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2022/09/13/eD/DefinicjeTypy/",
            "pattern": r"[1-9]((\d[1-9])|([1-9]\d))\d{7}",
        },
    )
    pesel: Optional[str] = field(
        default=None,
        metadata={
            "name": "PESEL",
            "type": "Element",
            "namespace": "http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2022/09/13/eD/DefinicjeTypy/",
            "pattern": r"\d{11}",
        },
    )
    imie_pierwsze: str = field(
        metadata={
            "name": "ImiePierwsze",
            "type": "Element",
            "namespace": "http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2022/09/13/eD/DefinicjeTypy/",
            "required": True,
            "min_length": 1,
            "max_length": 30,
        }
    )
    nazwisko: str = field(
        metadata={
            "name": "Nazwisko",
            "type": "Element",
            "namespace": "http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2022/09/13/eD/DefinicjeTypy/",
            "required": True,
            "min_length": 1,
            "max_length": 81,
        }
    )
    data_urodzenia: str = field(
        metadata={
            "name": "DataUrodzenia",
            "type": "Element",
            "namespace": "http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2022/09/13/eD/DefinicjeTypy/",
            "required": True,
            "min_inclusive": "1900-01-01",
            "max_inclusive": "2050-12-31",
            "pattern": r"((\d{4})-(\d{2})-(\d{2}))",
        }
    )


class TidentyfikatorOsobyFizycznej2(BaseModel):
    """
    Podstawowy zestaw danych identyfikacyjnych o osobie fizycznej z identyfikatorem
    NIP.

    :ivar nip: Identyfikator podatkowy NIP
    :ivar imie_pierwsze: Pierwsze imię
    :ivar nazwisko: Nazwisko
    :ivar data_urodzenia: Data urodzenia
    """

    class Meta:
        name = "TIdentyfikatorOsobyFizycznej2"
        target_namespace = "http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2022/09/13/eD/DefinicjeTypy/"

    model_config = ConfigDict(defer_build=True)
    nip: str = field(
        metadata={
            "name": "NIP",
            "type": "Element",
            "namespace": "http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2022/09/13/eD/DefinicjeTypy/",
            "required": True,
            "pattern": r"[1-9]((\d[1-9])|([1-9]\d))\d{7}",
        }
    )
    imie_pierwsze: str = field(
        metadata={
            "name": "ImiePierwsze",
            "type": "Element",
            "namespace": "http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2022/09/13/eD/DefinicjeTypy/",
            "required": True,
            "min_length": 1,
            "max_length": 30,
        }
    )
    nazwisko: str = field(
        metadata={
            "name": "Nazwisko",
            "type": "Element",
            "namespace": "http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2022/09/13/eD/DefinicjeTypy/",
            "required": True,
            "min_length": 1,
            "max_length": 81,
        }
    )
    data_urodzenia: str = field(
        metadata={
            "name": "DataUrodzenia",
            "type": "Element",
            "namespace": "http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2022/09/13/eD/DefinicjeTypy/",
            "required": True,
            "min_inclusive": "1900-01-01",
            "max_inclusive": "2050-12-31",
            "pattern": r"((\d{4})-(\d{2})-(\d{2}))",
        }
    )


class TidentyfikatorOsobyFizycznejPelny(BaseModel):
    """
    Pełny zestaw danych identyfikacyjnych o osobie fizycznej.

    :ivar nip: Identyfikator podatkowy NIP
    :ivar imie_pierwsze: Pierwsze imię
    :ivar nazwisko: Nazwisko
    :ivar data_urodzenia: Data urodzenia
    :ivar imie_ojca: Imię ojca
    :ivar imie_matki: Imię matki
    :ivar pesel: Identyfikator podatkowy numer PESEL
    """

    class Meta:
        name = "TIdentyfikatorOsobyFizycznejPelny"
        target_namespace = "http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2022/09/13/eD/DefinicjeTypy/"

    model_config = ConfigDict(defer_build=True)
    nip: Optional[str] = field(
        default=None,
        metadata={
            "name": "NIP",
            "type": "Element",
            "namespace": "http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2022/09/13/eD/DefinicjeTypy/",
            "pattern": r"[1-9]((\d[1-9])|([1-9]\d))\d{7}",
        },
    )
    imie_pierwsze: str = field(
        metadata={
            "name": "ImiePierwsze",
            "type": "Element",
            "namespace": "http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2022/09/13/eD/DefinicjeTypy/",
            "required": True,
            "min_length": 1,
            "max_length": 30,
        }
    )
    nazwisko: str = field(
        metadata={
            "name": "Nazwisko",
            "type": "Element",
            "namespace": "http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2022/09/13/eD/DefinicjeTypy/",
            "required": True,
            "min_length": 1,
            "max_length": 81,
        }
    )
    data_urodzenia: str = field(
        metadata={
            "name": "DataUrodzenia",
            "type": "Element",
            "namespace": "http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2022/09/13/eD/DefinicjeTypy/",
            "required": True,
            "min_inclusive": "1900-01-01",
            "max_inclusive": "2050-12-31",
            "pattern": r"((\d{4})-(\d{2})-(\d{2}))",
        }
    )
    imie_ojca: str = field(
        metadata={
            "name": "ImieOjca",
            "type": "Element",
            "namespace": "http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2022/09/13/eD/DefinicjeTypy/",
            "required": True,
            "min_length": 1,
            "max_length": 30,
        }
    )
    imie_matki: str = field(
        metadata={
            "name": "ImieMatki",
            "type": "Element",
            "namespace": "http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2022/09/13/eD/DefinicjeTypy/",
            "required": True,
            "min_length": 1,
            "max_length": 30,
        }
    )
    pesel: str = field(
        metadata={
            "name": "PESEL",
            "type": "Element",
            "namespace": "http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2022/09/13/eD/DefinicjeTypy/",
            "required": True,
            "pattern": r"\d{11}",
        }
    )


class TidentyfikatorOsobyFizycznejZagranicznej(BaseModel):
    """
    Zestaw danych identyfikacyjnych dla osoby fizycznej zagranicznej.

    :ivar imie_pierwsze: Imię pierwsze [First name]
    :ivar nazwisko: Nazwisko [Family name]
    :ivar data_urodzenia: Data urodzenia [Date of Birth]
    :ivar miejsce_urodzenia: Miejsce urodzenia [Place of Birth]
    :ivar imie_ojca: Imię ojca [Father’s name]
    :ivar imie_matki: Imię matki [Mother’s name]
    :ivar nip: Identyfikator podatkowy NIP [Tax Identification Number
        (NIP)]
    """

    class Meta:
        name = "TIdentyfikatorOsobyFizycznejZagranicznej"
        target_namespace = "http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2022/09/13/eD/DefinicjeTypy/"

    model_config = ConfigDict(defer_build=True)
    imie_pierwsze: str = field(
        metadata={
            "name": "ImiePierwsze",
            "type": "Element",
            "namespace": "http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2022/09/13/eD/DefinicjeTypy/",
            "required": True,
            "min_length": 1,
            "max_length": 30,
        }
    )
    nazwisko: str = field(
        metadata={
            "name": "Nazwisko",
            "type": "Element",
            "namespace": "http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2022/09/13/eD/DefinicjeTypy/",
            "required": True,
            "min_length": 1,
            "max_length": 81,
        }
    )
    data_urodzenia: str = field(
        metadata={
            "name": "DataUrodzenia",
            "type": "Element",
            "namespace": "http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2022/09/13/eD/DefinicjeTypy/",
            "required": True,
            "min_inclusive": "1900-01-01",
            "max_inclusive": "2050-12-31",
            "pattern": r"((\d{4})-(\d{2})-(\d{2}))",
        }
    )
    miejsce_urodzenia: str = field(
        metadata={
            "name": "MiejsceUrodzenia",
            "type": "Element",
            "namespace": "http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2022/09/13/eD/DefinicjeTypy/",
            "required": True,
            "min_length": 1,
            "max_length": 56,
        }
    )
    imie_ojca: Optional[str] = field(
        default=None,
        metadata={
            "name": "ImieOjca",
            "type": "Element",
            "namespace": "http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2022/09/13/eD/DefinicjeTypy/",
            "min_length": 1,
            "max_length": 30,
        },
    )
    imie_matki: Optional[str] = field(
        default=None,
        metadata={
            "name": "ImieMatki",
            "type": "Element",
            "namespace": "http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2022/09/13/eD/DefinicjeTypy/",
            "min_length": 1,
            "max_length": 30,
        },
    )
    nip: Optional[str] = field(
        default=None,
        metadata={
            "name": "NIP",
            "type": "Element",
            "namespace": "http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2022/09/13/eD/DefinicjeTypy/",
            "pattern": r"[1-9]((\d[1-9])|([1-9]\d))\d{7}",
        },
    )


class TidentyfikatorOsobyFizycznej3(BaseModel):
    """
    Podstawowy zestaw danych identyfikacyjnych o osobie fizycznej.

    :ivar nip: Identyfikator podatkowy NIP
    :ivar imie_pierwsze: Pierwsze imię
    :ivar nazwisko: Nazwisko
    :ivar data_urodzenia: Data urodzenia
    :ivar pesel: Identyfikator podatkowy numer PESEL
    """

    class Meta:
        name = "TIdentyfikatorOsobyFizycznej"
        target_namespace = "http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2022/09/13/eD/DefinicjeTypy/"

    model_config = ConfigDict(defer_build=True)
    nip: str = field(
        metadata={
            "name": "NIP",
            "type": "Element",
            "namespace": "http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2022/09/13/eD/DefinicjeTypy/",
            "required": True,
            "pattern": r"[1-9]((\d[1-9])|([1-9]\d))\d{7}",
        }
    )
    imie_pierwsze: str = field(
        metadata={
            "name": "ImiePierwsze",
            "type": "Element",
            "namespace": "http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2022/09/13/eD/DefinicjeTypy/",
            "required": True,
            "min_length": 1,
            "max_length": 30,
        }
    )
    nazwisko: str = field(
        metadata={
            "name": "Nazwisko",
            "type": "Element",
            "namespace": "http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2022/09/13/eD/DefinicjeTypy/",
            "required": True,
            "min_length": 1,
            "max_length": 81,
        }
    )
    data_urodzenia: str = field(
        metadata={
            "name": "DataUrodzenia",
            "type": "Element",
            "namespace": "http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2022/09/13/eD/DefinicjeTypy/",
            "required": True,
            "min_inclusive": "1900-01-01",
            "max_inclusive": "2050-12-31",
            "pattern": r"((\d{4})-(\d{2})-(\d{2}))",
        }
    )
    pesel: Optional[str] = field(
        default=None,
        metadata={
            "name": "PESEL",
            "type": "Element",
            "namespace": "http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2022/09/13/eD/DefinicjeTypy/",
            "pattern": r"\d{11}",
        },
    )


class TidentyfikatorOsobyNiefizycznej1(BaseModel):
    """Podstawowy zestaw danych identyfikacyjnych o osobie niefizycznej  - bez elementu Numer REGON

    :ivar nip: Identyfikator podatkowy NIP
    :ivar pelna_nazwa: Pełna nazwa
    """

    class Meta:
        name = "TIdentyfikatorOsobyNiefizycznej1"
        target_namespace = "http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2022/09/13/eD/DefinicjeTypy/"

    model_config = ConfigDict(defer_build=True)
    nip: str = field(
        metadata={
            "name": "NIP",
            "type": "Element",
            "namespace": "http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2022/09/13/eD/DefinicjeTypy/",
            "required": True,
            "pattern": r"[1-9]((\d[1-9])|([1-9]\d))\d{7}",
        }
    )
    pelna_nazwa: str = field(
        metadata={
            "name": "PelnaNazwa",
            "type": "Element",
            "namespace": "http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2022/09/13/eD/DefinicjeTypy/",
            "required": True,
            "min_length": 1,
            "max_length": 240,
        }
    )


class TidentyfikatorOsobyNiefizycznejPelny(BaseModel):
    """
    Pełny zestaw danych identyfikacyjnych o osobie niefizycznej.

    :ivar nip: Identyfikator podatkowy NIP
    :ivar pelna_nazwa: Pełna nazwa
    :ivar skrocona_nazwa: Skrócona nazwa
    :ivar regon: Numer REGON
    """

    class Meta:
        name = "TIdentyfikatorOsobyNiefizycznejPelny"
        target_namespace = "http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2022/09/13/eD/DefinicjeTypy/"

    model_config = ConfigDict(defer_build=True)
    nip: Optional[str] = field(
        default=None,
        metadata={
            "name": "NIP",
            "type": "Element",
            "namespace": "http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2022/09/13/eD/DefinicjeTypy/",
            "pattern": r"[1-9]((\d[1-9])|([1-9]\d))\d{7}",
        },
    )
    pelna_nazwa: str = field(
        metadata={
            "name": "PelnaNazwa",
            "type": "Element",
            "namespace": "http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2022/09/13/eD/DefinicjeTypy/",
            "required": True,
            "min_length": 1,
            "max_length": 240,
        }
    )
    skrocona_nazwa: str = field(
        metadata={
            "name": "SkroconaNazwa",
            "type": "Element",
            "namespace": "http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2022/09/13/eD/DefinicjeTypy/",
            "required": True,
            "min_length": 1,
            "max_length": 70,
        }
    )
    regon: str = field(
        metadata={
            "name": "REGON",
            "type": "Element",
            "namespace": "http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2022/09/13/eD/DefinicjeTypy/",
            "required": True,
            "pattern": r"\d{14}",
        }
    )


class TidentyfikatorOsobyNiefizycznejZagranicznej(BaseModel):
    """
    Zestaw danych identyfikacyjnych dla osoby niefizycznej zagranicznej.

    :ivar pelna_nazwa: Pełna nazwa [Name]
    :ivar skrocona_nazwa: Nazwa skrócona [Short Name]
    :ivar nip: Identyfikator podatkowy NIP [Tax Identification Number
        (NIP)]
    """

    class Meta:
        name = "TIdentyfikatorOsobyNiefizycznejZagranicznej"
        target_namespace = "http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2022/09/13/eD/DefinicjeTypy/"

    model_config = ConfigDict(defer_build=True)
    pelna_nazwa: str = field(
        metadata={
            "name": "PelnaNazwa",
            "type": "Element",
            "namespace": "http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2022/09/13/eD/DefinicjeTypy/",
            "required": True,
            "min_length": 1,
            "max_length": 240,
        }
    )
    skrocona_nazwa: Optional[str] = field(
        default=None,
        metadata={
            "name": "SkroconaNazwa",
            "type": "Element",
            "namespace": "http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2022/09/13/eD/DefinicjeTypy/",
            "min_length": 1,
            "max_length": 70,
        },
    )
    nip: Optional[str] = field(
        default=None,
        metadata={
            "name": "NIP",
            "type": "Element",
            "namespace": "http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2022/09/13/eD/DefinicjeTypy/",
            "pattern": r"[1-9]((\d[1-9])|([1-9]\d))\d{7}",
        },
    )


class TidentyfikatorOsobyNiefizycznej2(BaseModel):
    """
    Podstawowy zestaw danych identyfikacyjnych o osobie niefizycznej.

    :ivar nip: Identyfikator podatkowy NIP
    :ivar pelna_nazwa: Pełna nazwa
    :ivar regon: Numer REGON
    """

    class Meta:
        name = "TIdentyfikatorOsobyNiefizycznej"
        target_namespace = "http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2022/09/13/eD/DefinicjeTypy/"

    model_config = ConfigDict(defer_build=True)
    nip: str = field(
        metadata={
            "name": "NIP",
            "type": "Element",
            "namespace": "http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2022/09/13/eD/DefinicjeTypy/",
            "required": True,
            "pattern": r"[1-9]((\d[1-9])|([1-9]\d))\d{7}",
        }
    )
    pelna_nazwa: str = field(
        metadata={
            "name": "PelnaNazwa",
            "type": "Element",
            "namespace": "http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2022/09/13/eD/DefinicjeTypy/",
            "required": True,
            "min_length": 1,
            "max_length": 240,
        }
    )
    regon: Optional[str] = field(
        default=None,
        metadata={
            "name": "REGON",
            "type": "Element",
            "namespace": "http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2022/09/13/eD/DefinicjeTypy/",
            "pattern": r"\d{14}",
        },
    )


class Twybor12(Enum):
    """
    Podwójne pole wyboru.
    """

    VALUE_1 = 1
    VALUE_2 = 2


class TkodFormularzaZu(Enum):
    """
    Symbol wzoru formularza.
    """

    ORD_ZU = "ORD-ZU"


class TnaglowekOrdZuWariantFormularza(Enum):
    VALUE_3 = 3


class TkodKraju(Enum):
    """
    Słownik kodów krajów.

    :cvar AF: AFGANISTAN
    :cvar AX: ALAND ISLANDS
    :cvar AL: ALBANIA
    :cvar DZ: ALGIERIA
    :cvar AD: ANDORA
    :cvar AO: ANGOLA
    :cvar AI: ANGUILLA
    :cvar AQ: ANTARKTYDA
    :cvar AG: ANTIGUA I BARBUDA
    :cvar AN: ANTYLE HOLENDERSKIE
    :cvar SA: ARABIA SAUDYJSKA
    :cvar AR: ARGENTYNA
    :cvar AM: ARMENIA
    :cvar AW: ARUBA
    :cvar AU: AUSTRALIA
    :cvar AT: AUSTRIA
    :cvar AZ: AZERBEJDŻAN
    :cvar BS: BAHAMY
    :cvar BH: BAHRAJN
    :cvar BD: BANGLADESZ
    :cvar BB: BARBADOS
    :cvar BE: BELGIA
    :cvar BZ: BELIZE
    :cvar BJ: BENIN
    :cvar BM: BERMUDY
    :cvar BT: BHUTAN
    :cvar BY: BIAŁORUŚ
    :cvar BO: BOLIWIA
    :cvar BQ: BONAIRE, SINT EUSTATIUS I SABA
    :cvar BA: BOŚNIA I HERCEGOWINA
    :cvar BW: BOTSWANA
    :cvar BR: BRAZYLIA
    :cvar BN: BRUNEI DARUSSALAM
    :cvar IO: BRYTYJSKIE TERYTORIUM OCEANU INDYJSKIEGO
    :cvar BG: BUŁGARIA
    :cvar BF: BURKINA FASO
    :cvar BI: BURUNDI
    :cvar XC: CEUTA
    :cvar CL: CHILE
    :cvar CN: CHINY
    :cvar HR: CHORWACJA
    :cvar CW: CURAÇAO
    :cvar CY: CYPR
    :cvar TD: CZAD
    :cvar ME: CZARNOGÓRA
    :cvar DK: DANIA
    :cvar DM: DOMINIKA
    :cvar DO: DOMINIKANA
    :cvar DJ: DŻIBUTI
    :cvar EG: EGIPT
    :cvar EC: EKWADOR
    :cvar ER: ERYTREA
    :cvar EE: ESTONIA
    :cvar ET: ETIOPIA
    :cvar FK: FALKLANDY
    :cvar FJ: FIDŻI REPUBLIKA
    :cvar PH: FILIPINY
    :cvar FI: FINLANDIA
    :cvar FR: FRANCJA
    :cvar TF: FRANCUSKIE TERYTORIUM POŁUDNIOWE
    :cvar GA: GABON
    :cvar GM: GAMBIA
    :cvar GH: GHANA
    :cvar GI: GIBRALTAR
    :cvar GR: GRECJA
    :cvar GD: GRENADA
    :cvar GL: GRENLANDIA
    :cvar GE: GRUZJA
    :cvar GU: GUAM
    :cvar GG: GUERNSEY
    :cvar GY: GUJANA
    :cvar GF: GUJANA FRANCUSKA
    :cvar GP: GWADELUPA
    :cvar GT: GWATEMALA
    :cvar GN: GWINEA
    :cvar GQ: GWINEA RÓWNIKOWA
    :cvar GW: GWINEA-BISSAU
    :cvar HT: HAITI
    :cvar ES: HISZPANIA
    :cvar HN: HONDURAS
    :cvar HK: HONGKONG
    :cvar IN: INDIE
    :cvar ID: INDONEZJA
    :cvar IQ: IRAK
    :cvar IR: IRAN
    :cvar IE: IRLANDIA
    :cvar IS: ISLANDIA
    :cvar IL: IZRAEL
    :cvar JM: JAMAJKA
    :cvar JP: JAPONIA
    :cvar YE: JEMEN
    :cvar JE: JERSEY
    :cvar JO: JORDANIA
    :cvar KY: KAJMANY
    :cvar KH: KAMBODŻA
    :cvar CM: KAMERUN
    :cvar CA: KANADA
    :cvar QA: KATAR
    :cvar KZ: KAZACHSTAN
    :cvar KE: KENIA
    :cvar KG: KIRGISTAN
    :cvar KI: KIRIBATI
    :cvar CO: KOLUMBIA
    :cvar KM: KOMORY
    :cvar CG: KONGO
    :cvar CD: KONGO, REPUBLIKA DEMOKRATYCZNA
    :cvar KP: KOREAŃSKA REPUBLIKA LUDOWO-DEMOKRATYCZNA
    :cvar XK: KOSOWO
    :cvar CR: KOSTARYKA
    :cvar CU: KUBA
    :cvar KW: KUWEJT
    :cvar LA: LAOS
    :cvar LS: LESOTHO
    :cvar LB: LIBAN
    :cvar LR: LIBERIA
    :cvar LY: LIBIA
    :cvar LI: LIECHTENSTEIN
    :cvar LT: LITWA
    :cvar LV: ŁOTWA
    :cvar LU: LUKSEMBURG
    :cvar MK: MACEDONIA
    :cvar MG: MADAGASKAR
    :cvar YT: MAJOTTA
    :cvar MO: MAKAU
    :cvar MW: MALAWI
    :cvar MV: MALEDIWY
    :cvar MY: MALEZJA
    :cvar ML: MALI
    :cvar MT: MALTA
    :cvar MP: MARIANY PÓŁNOCNE
    :cvar MA: MAROKO
    :cvar MQ: MARTYNIKA
    :cvar MR: MAURETANIA
    :cvar MU: MAURITIUS
    :cvar MX: MEKSYK
    :cvar XL: MELILLA
    :cvar FM: MIKRONEZJA
    :cvar UM: MINOR
    :cvar MD: MOŁDOWA
    :cvar MC: MONAKO
    :cvar MN: MONGOLIA
    :cvar MS: MONTSERRAT
    :cvar MZ: MOZAMBIK
    :cvar MM: MYANMAR (BURMA)
    :cvar NA: NAMIBIA
    :cvar NR: NAURU
    :cvar NP: NEPAL
    :cvar NL: NIDERLANDY (HOLANDIA)
    :cvar DE: NIEMCY
    :cvar NE: NIGER
    :cvar NG: NIGERIA
    :cvar NI: NIKARAGUA
    :cvar NU: NIUE
    :cvar NF: NORFOLK
    :cvar NO: NORWEGIA
    :cvar NC: NOWA KALEDONIA
    :cvar NZ: NOWA ZELANDIA
    :cvar PS: OKUPOWANE TERYTORIUM PALESTYNY
    :cvar OM: OMAN
    :cvar PK: PAKISTAN
    :cvar PW: PALAU
    :cvar PA: PANAMA
    :cvar PG: PAPUA NOWA GWINEA
    :cvar PY: PARAGWAJ
    :cvar PE: PERU
    :cvar PN: PITCAIRN
    :cvar PF: POLINEZJA FRANCUSKA
    :cvar PL: POLSKA
    :cvar GS: POŁUDNIOWA GEORGIA I POŁUD.WYSPY SANDWICH
    :cvar PT: PORTUGALIA
    :cvar PR: PORTORYKO
    :cvar CF: REP.ŚRODKOWOAFRYKAŃSKA
    :cvar CZ: REPUBLIKA CZESKA
    :cvar KR: REPUBLIKA KOREI
    :cvar ZA: REPUBLIKA POŁUDNIOWEJ AFRYKI
    :cvar RE: REUNION
    :cvar RU: ROSJA
    :cvar RO: RUMUNIA
    :cvar RW: RWANDA
    :cvar EH: SAHARA ZACHODNIA
    :cvar BL: SAINT BARTHELEMY
    :cvar KN: SAINT KITTS I NEVIS
    :cvar LC: SAINT LUCIA
    :cvar MF: SAINT MARTIN
    :cvar VC: SAINT VINCENT I GRENADYNY
    :cvar SV: SALWADOR
    :cvar WS: SAMOA
    :cvar AS: SAMOA AMERYKAŃSKIE
    :cvar SM: SAN MARINO
    :cvar SN: SENEGAL
    :cvar RS: SERBIA
    :cvar SC: SESZELE
    :cvar SL: SIERRA LEONE
    :cvar SG: SINGAPUR
    :cvar SK: SŁOWACJA
    :cvar SI: SŁOWENIA
    :cvar SO: SOMALIA
    :cvar LK: SRI LANKA
    :cvar PM: SAINT PIERRE I MIQUELON
    :cvar US: STANY ZJEDNOCZONE AMERYKI
    :cvar SZ: SUAZI
    :cvar SD: SUDAN
    :cvar SS: SUDAN POŁUDNIOWY
    :cvar SR: SURINAM
    :cvar SJ: SVALBARD I JAN MAYEN
    :cvar SH: ŚWIĘTA HELENA
    :cvar SY: SYRIA
    :cvar CH: SZWAJCARIA
    :cvar SE: SZWECJA
    :cvar TJ: TADŻYKISTAN
    :cvar TH: TAJLANDIA
    :cvar TW: TAJWAN
    :cvar TZ: TANZANIA
    :cvar TG: TOGO
    :cvar TK: TOKELAU
    :cvar TO: TONGA
    :cvar TT: TRYNIDAD I TOBAGO
    :cvar TN: TUNEZJA
    :cvar TR: TURCJA
    :cvar TM: TURKMENISTAN
    :cvar TV: TUVALU
    :cvar UG: UGANDA
    :cvar UA: UKRAINA
    :cvar UY: URUGWAJ
    :cvar UZ: UZBEKISTAN
    :cvar VU: VANUATU
    :cvar WF: WALLIS I FUTUNA
    :cvar VA: WATYKAN
    :cvar HU: WĘGRY
    :cvar VE: WENEZUELA
    :cvar GB: WIELKA BRYTANIA
    :cvar VN: WIETNAM
    :cvar IT: WŁOCHY
    :cvar TL: WSCHODNI TIMOR
    :cvar CI: WYBRZEŻE KOŚCI SŁONIOWEJ
    :cvar BV: WYSPA BOUVETA
    :cvar CX: WYSPA BOŻEGO NARODZENIA
    :cvar IM: WYSPA MAN
    :cvar SX: WYSPA SINT MAARTEN (CZĘŚĆ HOLENDERSKA WYSPY)
    :cvar CK: WYSPY COOKA
    :cvar VI: WYSPY DZIEWICZE-USA
    :cvar VG: WYSPY DZIEWICZE-W.B.
    :cvar HM: WYSPY HEARD I MCDONALD
    :cvar CC: WYSPY KOKOSOWE (KEELINGA)
    :cvar MH: WYSPY MARSHALLA
    :cvar FO: WYSPY OWCZE
    :cvar SB: WYSPY SALOMONA
    :cvar ST: WYSPY ŚWIĘTEGO TOMASZA I KSIĄŻĘCA
    :cvar TC: WYSPY TURKS I CAICOS
    :cvar ZM: ZAMBIA
    :cvar CV: ZIELONY PRZYLĄDEK
    :cvar ZW: ZIMBABWE
    :cvar AE: ZJEDNOCZONE EMIRATY ARABSKIE
    :cvar XI: ZJEDNOCZONE KRÓLESTWO (IRLANDIA PÓŁNOCNA)
    :cvar XU: ZJEDNOCZONE KRÓLESTWO (WYŁĄCZAJĄC IRLANDIĘ PÓŁNOCNĄ)
    """

    AF = "AF"
    AX = "AX"
    AL = "AL"
    DZ = "DZ"
    AD = "AD"
    AO = "AO"
    AI = "AI"
    AQ = "AQ"
    AG = "AG"
    AN = "AN"
    SA = "SA"
    AR = "AR"
    AM = "AM"
    AW = "AW"
    AU = "AU"
    AT = "AT"
    AZ = "AZ"
    BS = "BS"
    BH = "BH"
    BD = "BD"
    BB = "BB"
    BE = "BE"
    BZ = "BZ"
    BJ = "BJ"
    BM = "BM"
    BT = "BT"
    BY = "BY"
    BO = "BO"
    BQ = "BQ"
    BA = "BA"
    BW = "BW"
    BR = "BR"
    BN = "BN"
    IO = "IO"
    BG = "BG"
    BF = "BF"
    BI = "BI"
    XC = "XC"
    CL = "CL"
    CN = "CN"
    HR = "HR"
    CW = "CW"
    CY = "CY"
    TD = "TD"
    ME = "ME"
    DK = "DK"
    DM = "DM"
    DO = "DO"
    DJ = "DJ"
    EG = "EG"
    EC = "EC"
    ER = "ER"
    EE = "EE"
    ET = "ET"
    FK = "FK"
    FJ = "FJ"
    PH = "PH"
    FI = "FI"
    FR = "FR"
    TF = "TF"
    GA = "GA"
    GM = "GM"
    GH = "GH"
    GI = "GI"
    GR = "GR"
    GD = "GD"
    GL = "GL"
    GE = "GE"
    GU = "GU"
    GG = "GG"
    GY = "GY"
    GF = "GF"
    GP = "GP"
    GT = "GT"
    GN = "GN"
    GQ = "GQ"
    GW = "GW"
    HT = "HT"
    ES = "ES"
    HN = "HN"
    HK = "HK"
    IN = "IN"
    ID = "ID"
    IQ = "IQ"
    IR = "IR"
    IE = "IE"
    IS = "IS"
    IL = "IL"
    JM = "JM"
    JP = "JP"
    YE = "YE"
    JE = "JE"
    JO = "JO"
    KY = "KY"
    KH = "KH"
    CM = "CM"
    CA = "CA"
    QA = "QA"
    KZ = "KZ"
    KE = "KE"
    KG = "KG"
    KI = "KI"
    CO = "CO"
    KM = "KM"
    CG = "CG"
    CD = "CD"
    KP = "KP"
    XK = "XK"
    CR = "CR"
    CU = "CU"
    KW = "KW"
    LA = "LA"
    LS = "LS"
    LB = "LB"
    LR = "LR"
    LY = "LY"
    LI = "LI"
    LT = "LT"
    LV = "LV"
    LU = "LU"
    MK = "MK"
    MG = "MG"
    YT = "YT"
    MO = "MO"
    MW = "MW"
    MV = "MV"
    MY = "MY"
    ML = "ML"
    MT = "MT"
    MP = "MP"
    MA = "MA"
    MQ = "MQ"
    MR = "MR"
    MU = "MU"
    MX = "MX"
    XL = "XL"
    FM = "FM"
    UM = "UM"
    MD = "MD"
    MC = "MC"
    MN = "MN"
    MS = "MS"
    MZ = "MZ"
    MM = "MM"
    NA = "NA"
    NR = "NR"
    NP = "NP"
    NL = "NL"
    DE = "DE"
    NE = "NE"
    NG = "NG"
    NI = "NI"
    NU = "NU"
    NF = "NF"
    NO = "NO"
    NC = "NC"
    NZ = "NZ"
    PS = "PS"
    OM = "OM"
    PK = "PK"
    PW = "PW"
    PA = "PA"
    PG = "PG"
    PY = "PY"
    PE = "PE"
    PN = "PN"
    PF = "PF"
    PL = "PL"
    GS = "GS"
    PT = "PT"
    PR = "PR"
    CF = "CF"
    CZ = "CZ"
    KR = "KR"
    ZA = "ZA"
    RE = "RE"
    RU = "RU"
    RO = "RO"
    RW = "RW"
    EH = "EH"
    BL = "BL"
    KN = "KN"
    LC = "LC"
    MF = "MF"
    VC = "VC"
    SV = "SV"
    WS = "WS"
    AS = "AS"
    SM = "SM"
    SN = "SN"
    RS = "RS"
    SC = "SC"
    SL = "SL"
    SG = "SG"
    SK = "SK"
    SI = "SI"
    SO = "SO"
    LK = "LK"
    PM = "PM"
    US = "US"
    SZ = "SZ"
    SD = "SD"
    SS = "SS"
    SR = "SR"
    SJ = "SJ"
    SH = "SH"
    SY = "SY"
    CH = "CH"
    SE = "SE"
    TJ = "TJ"
    TH = "TH"
    TW = "TW"
    TZ = "TZ"
    TG = "TG"
    TK = "TK"
    TO = "TO"
    TT = "TT"
    TN = "TN"
    TR = "TR"
    TM = "TM"
    TV = "TV"
    UG = "UG"
    UA = "UA"
    UY = "UY"
    UZ = "UZ"
    VU = "VU"
    WF = "WF"
    VA = "VA"
    HU = "HU"
    VE = "VE"
    GB = "GB"
    VN = "VN"
    IT = "IT"
    TL = "TL"
    CI = "CI"
    BV = "BV"
    CX = "CX"
    IM = "IM"
    SX = "SX"
    CK = "CK"
    VI = "VI"
    VG = "VG"
    HM = "HM"
    CC = "CC"
    MH = "MH"
    FO = "FO"
    SB = "SB"
    ST = "ST"
    TC = "TC"
    ZM = "ZM"
    CV = "CV"
    ZW = "ZW"
    AE = "AE"
    XI = "XI"
    XU = "XU"


class TadresPolski(BaseModel):
    """
    Informacje opisujące adres polski.

    :ivar kod_kraju: Kraj
    :ivar wojewodztwo: Województwo
    :ivar powiat: Powiat
    :ivar gmina: Gmina
    :ivar ulica: Ulica
    :ivar nr_domu: Nr domu
    :ivar nr_lokalu: Nr lokalu
    :ivar miejscowosc: Miejscowość
    :ivar kod_pocztowy: Kod pocztowy
    """

    class Meta:
        name = "TAdresPolski"
        target_namespace = "http://crd.gov.pl/wzor/2023/12/13/13064/"

    model_config = ConfigDict(defer_build=True)
    kod_kraju: TadresPolskiKodKraju = field(
        metadata={
            "name": "KodKraju",
            "type": "Element",
            "namespace": "http://crd.gov.pl/wzor/2023/12/13/13064/",
            "required": True,
        }
    )
    wojewodztwo: str = field(
        metadata={
            "name": "Wojewodztwo",
            "type": "Element",
            "namespace": "http://crd.gov.pl/wzor/2023/12/13/13064/",
            "required": True,
            "min_length": 1,
            "max_length": 36,
        }
    )
    powiat: str = field(
        metadata={
            "name": "Powiat",
            "type": "Element",
            "namespace": "http://crd.gov.pl/wzor/2023/12/13/13064/",
            "required": True,
            "min_length": 1,
            "max_length": 36,
        }
    )
    gmina: str = field(
        metadata={
            "name": "Gmina",
            "type": "Element",
            "namespace": "http://crd.gov.pl/wzor/2023/12/13/13064/",
            "required": True,
            "min_length": 1,
            "max_length": 36,
        }
    )
    ulica: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ulica",
            "type": "Element",
            "namespace": "http://crd.gov.pl/wzor/2023/12/13/13064/",
            "min_length": 1,
            "max_length": 65,
        },
    )
    nr_domu: str = field(
        metadata={
            "name": "NrDomu",
            "type": "Element",
            "namespace": "http://crd.gov.pl/wzor/2023/12/13/13064/",
            "required": True,
            "min_length": 1,
            "max_length": 9,
        }
    )
    nr_lokalu: Optional[str] = field(
        default=None,
        metadata={
            "name": "NrLokalu",
            "type": "Element",
            "namespace": "http://crd.gov.pl/wzor/2023/12/13/13064/",
            "min_length": 1,
            "max_length": 10,
        },
    )
    miejscowosc: str = field(
        metadata={
            "name": "Miejscowosc",
            "type": "Element",
            "namespace": "http://crd.gov.pl/wzor/2023/12/13/13064/",
            "required": True,
            "min_length": 1,
            "max_length": 56,
        }
    )
    kod_pocztowy: str = field(
        metadata={
            "name": "KodPocztowy",
            "type": "Element",
            "namespace": "http://crd.gov.pl/wzor/2023/12/13/13064/",
            "required": True,
            "min_length": 1,
            "max_length": 8,
        }
    )


class TadresZagraniczny(BaseModel):
    """
    Informacje opisujące adres zagraniczny.

    :ivar kod_kraju: Kraj
    :ivar kod_pocztowy: Kod pocztowy
    :ivar miejscowosc: Miejscowość
    :ivar ulica: Ulica
    :ivar nr_domu: Nr domu
    :ivar nr_lokalu: Nr lokalu
    """

    class Meta:
        name = "TAdresZagraniczny"
        target_namespace = "http://crd.gov.pl/wzor/2023/12/13/13064/"

    model_config = ConfigDict(defer_build=True)
    kod_kraju: TkodKraju = field(
        metadata={
            "name": "KodKraju",
            "type": "Element",
            "namespace": "http://crd.gov.pl/wzor/2023/12/13/13064/",
            "required": True,
            "pattern": r"P[A-KM-Z]|[A-OQ-Z][A-Z]",
        }
    )
    kod_pocztowy: Optional[str] = field(
        default=None,
        metadata={
            "name": "KodPocztowy",
            "type": "Element",
            "namespace": "http://crd.gov.pl/wzor/2023/12/13/13064/",
            "min_length": 1,
            "max_length": 8,
        },
    )
    miejscowosc: str = field(
        metadata={
            "name": "Miejscowosc",
            "type": "Element",
            "namespace": "http://crd.gov.pl/wzor/2023/12/13/13064/",
            "required": True,
            "min_length": 1,
            "max_length": 56,
        }
    )
    ulica: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ulica",
            "type": "Element",
            "namespace": "http://crd.gov.pl/wzor/2023/12/13/13064/",
            "min_length": 1,
            "max_length": 65,
        },
    )
    nr_domu: Optional[str] = field(
        default=None,
        metadata={
            "name": "NrDomu",
            "type": "Element",
            "namespace": "http://crd.gov.pl/wzor/2023/12/13/13064/",
            "min_length": 1,
            "max_length": 9,
        },
    )
    nr_lokalu: Optional[str] = field(
        default=None,
        metadata={
            "name": "NrLokalu",
            "type": "Element",
            "namespace": "http://crd.gov.pl/wzor/2023/12/13/13064/",
            "min_length": 1,
            "max_length": 10,
        },
    )


class Tnaglowek(BaseModel):
    """
    Nagłówek deklaracji.

    :ivar kod_formularza:
    :ivar wariant_formularza:
    :ivar cel_zlozenia:
    :ivar data: Data dokonania czynności
    :ivar kod_urzedu:
    """

    class Meta:
        name = "TNaglowek"
        target_namespace = "http://crd.gov.pl/wzor/2023/12/13/13064/"

    model_config = ConfigDict(defer_build=True)
    kod_formularza: "Tnaglowek.KodFormularza" = field(
        metadata={
            "name": "KodFormularza",
            "type": "Element",
            "namespace": "http://crd.gov.pl/wzor/2023/12/13/13064/",
            "required": True,
        }
    )
    wariant_formularza: TnaglowekWariantFormularza = field(
        metadata={
            "name": "WariantFormularza",
            "type": "Element",
            "namespace": "http://crd.gov.pl/wzor/2023/12/13/13064/",
            "required": True,
        }
    )
    cel_zlozenia: "Tnaglowek.CelZlozenia" = field(
        metadata={
            "name": "CelZlozenia",
            "type": "Element",
            "namespace": "http://crd.gov.pl/wzor/2023/12/13/13064/",
            "required": True,
        }
    )
    data: "Tnaglowek.Data" = field(
        metadata={
            "name": "Data",
            "type": "Element",
            "namespace": "http://crd.gov.pl/wzor/2023/12/13/13064/",
            "required": True,
        }
    )
    kod_urzedu: TkodUs = field(
        metadata={
            "name": "KodUrzedu",
            "type": "Element",
            "namespace": "http://crd.gov.pl/wzor/2023/12/13/13064/",
            "required": True,
        }
    )

    class KodFormularza(BaseModel):
        model_config = ConfigDict(defer_build=True)
        value: TkodFormularza = field(
            metadata={
                "required": True,
            }
        )
        kod_systemowy: str = field(
            const=True,
            default="PCC-3 (6)",
            metadata={
                "name": "kodSystemowy",
                "type": "Attribute",
                "required": True,
            },
        )
        kod_podatku: str = field(
            const=True,
            default="PCC",
            metadata={
                "name": "kodPodatku",
                "type": "Attribute",
                "required": True,
            },
        )
        rodzaj_zobowiazania: str = field(
            const=True,
            default="Z",
            metadata={
                "name": "rodzajZobowiazania",
                "type": "Attribute",
                "required": True,
            },
        )
        wersja_schemy: str = field(
            const=True,
            default="1-0E",
            metadata={
                "name": "wersjaSchemy",
                "type": "Attribute",
                "required": True,
            },
        )

    class CelZlozenia(BaseModel):
        model_config = ConfigDict(defer_build=True)
        value: TcelZlozenia = field(
            metadata={
                "required": True,
            }
        )
        poz: str = field(
            const=True,
            default="P_6",
            metadata={
                "type": "Attribute",
                "required": True,
            },
        )

    class Data(BaseModel):
        model_config = ConfigDict(defer_build=True)
        value: XmlDate = field(
            metadata={
                "required": True,
                "min_inclusive": XmlDate(2024, 1, 1),
            }
        )
        poz: str = field(
            const=True,
            default="P_4",
            metadata={
                "type": "Attribute",
                "required": True,
            },
        )


class TpodmiotDowolnyBezAdresu(BaseModel):
    """
    Skrócony zestaw danych o osobie fizycznej lub niefizycznej.
    """

    class Meta:
        name = "TPodmiotDowolnyBezAdresu"
        target_namespace = "http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2022/09/13/eD/DefinicjeTypy/"

    model_config = ConfigDict(defer_build=True)
    osoba_fizyczna: Optional[TidentyfikatorOsobyFizycznej3] = field(
        default=None,
        metadata={
            "name": "OsobaFizyczna",
            "type": "Element",
            "namespace": "http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2022/09/13/eD/DefinicjeTypy/",
        },
    )
    osoba_niefizyczna: Optional[TidentyfikatorOsobyNiefizycznej2] = field(
        default=None,
        metadata={
            "name": "OsobaNiefizyczna",
            "type": "Element",
            "namespace": "http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2022/09/13/eD/DefinicjeTypy/",
        },
    )


class TpodmiotDowolnyBezAdresu1(BaseModel):
    """
    Skrócony zestaw danych o osobie fizycznej lub niefizycznej z identyfikatorem
    NIP albo PESEL.
    """

    class Meta:
        name = "TPodmiotDowolnyBezAdresu1"
        target_namespace = "http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2022/09/13/eD/DefinicjeTypy/"

    model_config = ConfigDict(defer_build=True)
    osoba_fizyczna: Optional[TidentyfikatorOsobyFizycznej1] = field(
        default=None,
        metadata={
            "name": "OsobaFizyczna",
            "type": "Element",
            "namespace": "http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2022/09/13/eD/DefinicjeTypy/",
        },
    )
    osoba_niefizyczna: Optional[TidentyfikatorOsobyNiefizycznej2] = field(
        default=None,
        metadata={
            "name": "OsobaNiefizyczna",
            "type": "Element",
            "namespace": "http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2022/09/13/eD/DefinicjeTypy/",
        },
    )


class TpodmiotDowolnyBezAdresu2(BaseModel):
    """
    Skrócony zestaw danych o osobie fizycznej lub niefizycznej z identyfikatorem
    NIP.
    """

    class Meta:
        name = "TPodmiotDowolnyBezAdresu2"
        target_namespace = "http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2022/09/13/eD/DefinicjeTypy/"

    model_config = ConfigDict(defer_build=True)
    osoba_fizyczna: Optional[TidentyfikatorOsobyFizycznej2] = field(
        default=None,
        metadata={
            "name": "OsobaFizyczna",
            "type": "Element",
            "namespace": "http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2022/09/13/eD/DefinicjeTypy/",
        },
    )
    osoba_niefizyczna: Optional[TidentyfikatorOsobyNiefizycznej2] = field(
        default=None,
        metadata={
            "name": "OsobaNiefizyczna",
            "type": "Element",
            "namespace": "http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2022/09/13/eD/DefinicjeTypy/",
        },
    )


class TpodmiotDowolnyBezAdresu3(BaseModel):
    """Skrócony zestaw danych o osobie fizycznej lub niefizycznej z identyfikatorem NIP - bez elementu numer REGON dla osoby niefizycznej"""

    class Meta:
        name = "TPodmiotDowolnyBezAdresu3"
        target_namespace = "http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2022/09/13/eD/DefinicjeTypy/"

    model_config = ConfigDict(defer_build=True)
    osoba_fizyczna: Optional[TidentyfikatorOsobyFizycznej2] = field(
        default=None,
        metadata={
            "name": "OsobaFizyczna",
            "type": "Element",
            "namespace": "http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2022/09/13/eD/DefinicjeTypy/",
        },
    )
    osoba_niefizyczna: Optional[TidentyfikatorOsobyNiefizycznej1] = field(
        default=None,
        metadata={
            "name": "OsobaNiefizyczna",
            "type": "Element",
            "namespace": "http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2022/09/13/eD/DefinicjeTypy/",
        },
    )


class TnaglowekOrdZu(BaseModel):
    """
    Nagłówek deklaracji.
    """

    class Meta:
        name = "TNaglowek_ORD-ZU"
        target_namespace = "http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2022/09/13/eD/ORDZU/"

    model_config = ConfigDict(defer_build=True)
    kod_formularza: "TnaglowekOrdZu.KodFormularza" = field(
        metadata={
            "name": "KodFormularza",
            "type": "Element",
            "namespace": "http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2022/09/13/eD/ORDZU/",
            "required": True,
        }
    )
    wariant_formularza: TnaglowekOrdZuWariantFormularza = field(
        metadata={
            "name": "WariantFormularza",
            "type": "Element",
            "namespace": "http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2022/09/13/eD/ORDZU/",
            "required": True,
        }
    )

    class KodFormularza(BaseModel):
        model_config = ConfigDict(defer_build=True)
        value: TkodFormularzaZu = field(
            metadata={
                "required": True,
            }
        )
        kod_systemowy: str = field(
            const=True,
            default="ORD-ZU (3)",
            metadata={
                "name": "kodSystemowy",
                "type": "Attribute",
                "required": True,
            },
        )
        wersja_schemy: str = field(
            const=True,
            default="10-0E",
            metadata={
                "name": "wersjaSchemy",
                "type": "Attribute",
                "required": True,
            },
        )


class Tadres(BaseModel):
    """
    Dane określające adres.
    """

    class Meta:
        name = "TAdres"
        target_namespace = "http://crd.gov.pl/wzor/2023/12/13/13064/"

    model_config = ConfigDict(defer_build=True)
    adres_pol: Optional[TadresPolski] = field(
        default=None,
        metadata={
            "name": "AdresPol",
            "type": "Element",
            "namespace": "http://crd.gov.pl/wzor/2023/12/13/13064/",
        },
    )
    adres_zagr: Optional[TadresZagraniczny] = field(
        default=None,
        metadata={
            "name": "AdresZagr",
            "type": "Element",
            "namespace": "http://crd.gov.pl/wzor/2023/12/13/13064/",
        },
    )


class ZalacznikOrdZu(BaseModel):
    """
    UZASADNIENIE PRZYCZYN KOREKTY DEKLARACJI.
    """

    class Meta:
        name = "Zalacznik_ORD-ZU"
        namespace = "http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2022/09/13/eD/ORDZU/"

    model_config = ConfigDict(defer_build=True)
    naglowek: TnaglowekOrdZu = field(
        metadata={
            "name": "Naglowek",
            "type": "Element",
            "required": True,
        }
    )
    pozycje_szczegolowe: "ZalacznikOrdZu.PozycjeSzczegolowe" = field(
        metadata={
            "name": "PozycjeSzczegolowe",
            "type": "Element",
            "required": True,
        }
    )

    class PozycjeSzczegolowe(BaseModel):
        """
        :ivar p_13: Treść uzasadnienia
        """

        model_config = ConfigDict(defer_build=True)
        p_13: str = field(
            metadata={
                "name": "P_13",
                "type": "Element",
                "required": True,
                "min_length": 1,
                "max_length": 2000,
            }
        )


class Deklaracja(BaseModel):
    """
    DEKLARACJA W SPRAWIE PODATKU OD CZYNNOŚCI CYWILNOPRAWNYCH.

    :ivar naglowek: Nagłówek deklaracji
    :ivar podmiot1: Dane podatnika dokonującego zapłaty lub zwolnionego
        z podatku na podstawie art. 9 pkt 10 lit. b ustawy
    :ivar pozycje_szczegolowe: Przedmiot opodatkowania i treść czynności
        cywilnoprawnej, obliczenie należnego podatku od czynności
        cywilnoprawnych, z wyjątkiem umowy spółki lub jej zmiany,
        obliczenie należnego podatku od umowy spółki / zmiany umowy
        spółki, podatek do zapłaty, informacje dodatkowe
    :ivar pouczenia: Wartość 1 oznacza potwierdzenie zapoznania się z
        treścią i akceptację poniższych pouczeń: Za podanie nieprawdy
        lub zatajenie prawdy i przez to narażenie podatku na
        uszczuplenie grozi odpowiedzialność przewidziana w Kodeksie
        karnym skarbowym. W przypadku niezapłacenia w obowiązującym
        terminie kwoty podatku od czynności cywilnoprawnych z poz. 53
        lub wpłacenia jej w niepełnej wysokości, niniejsza deklaracja
        stanowi podstawę do wystawienia tytułu wykonawczego, zgodnie z
        przepisami ustawy z dnia 17 czerwca 1966 r. o postępowaniu
        egzekucyjnym w administracji (Dz. U. z 2023 r. poz. 2505).
    :ivar zalaczniki:
    """

    class Meta:
        namespace = "http://crd.gov.pl/wzor/2023/12/13/13064/"

    model_config = ConfigDict(defer_build=True)
    naglowek: Tnaglowek = field(
        metadata={
            "name": "Naglowek",
            "type": "Element",
            "required": True,
        }
    )
    podmiot1: "Deklaracja.Podmiot1" = field(
        metadata={
            "name": "Podmiot1",
            "type": "Element",
            "required": True,
        }
    )
    pozycje_szczegolowe: "Deklaracja.PozycjeSzczegolowe" = field(
        metadata={
            "name": "PozycjeSzczegolowe",
            "type": "Element",
            "required": True,
        }
    )
    pouczenia: Decimal = field(
        metadata={
            "name": "Pouczenia",
            "type": "Element",
            "required": True,
            "min_exclusive": Decimal("0"),
            "min_inclusive": Decimal("0"),
            "max_exclusive": Decimal("2"),
            "total_digits": 16,
            "fraction_digits": 0,
            "white_space": "collapse",
        }
    )
    zalaczniki: Optional["Deklaracja.Zalaczniki"] = field(
        default=None,
        metadata={
            "name": "Zalaczniki",
            "type": "Element",
        },
    )

    class Podmiot1(BaseModel):
        """
        :ivar osoba_fizyczna:
        :ivar osoba_niefizyczna:
        :ivar adres_zamieszkania_siedziby: Adres siedziby / Aktualny
            adres zamieszkania
        :ivar rola:
        """

        model_config = ConfigDict(defer_build=True)
        osoba_fizyczna: Optional["Deklaracja.Podmiot1.OsobaFizyczna"] = field(
            default=None,
            metadata={
                "name": "OsobaFizyczna",
                "type": "Element",
            },
        )
        osoba_niefizyczna: Optional[TidentyfikatorOsobyNiefizycznej3] = field(
            default=None,
            metadata={
                "name": "OsobaNiefizyczna",
                "type": "Element",
            },
        )
        adres_zamieszkania_siedziby: "Deklaracja.Podmiot1.AdresZamieszkaniaSiedziby" = field(
            metadata={
                "name": "AdresZamieszkaniaSiedziby",
                "type": "Element",
                "required": True,
            }
        )
        rola: str = field(
            const=True,
            default="Podatnik",
            metadata={
                "type": "Attribute",
                "required": True,
            },
        )

        class AdresZamieszkaniaSiedziby(Tadres):
            model_config = ConfigDict(defer_build=True)
            rodzaj_adresu: str = field(
                const=True,
                default="RAD",
                metadata={
                    "name": "rodzajAdresu",
                    "type": "Attribute",
                    "required": True,
                },
            )

        class OsobaFizyczna(TidentyfikatorOsobyFizycznej4):
            """
            :ivar imie_ojca: Imię ojca
            :ivar imie_matki: Imię matki
            """

            model_config = ConfigDict(defer_build=True)
            imie_ojca: Optional[str] = field(
                default=None,
                metadata={
                    "name": "ImieOjca",
                    "type": "Element",
                    "min_length": 1,
                    "max_length": 30,
                },
            )
            imie_matki: Optional[str] = field(
                default=None,
                metadata={
                    "name": "ImieMatki",
                    "type": "Element",
                    "min_length": 1,
                    "max_length": 30,
                },
            )

    class PozycjeSzczegolowe(BaseModel):
        """
        :ivar p_7: Podmiot składający deklarację
        :ivar p_20: Przedmiot opodatkowania : 1 - umowa, 2 - zmiana
            umowy, 3 - orzeczenie sądu lub ugoda, 4 - inne
        :ivar p_21: Miejsce położenia rzeczy lub miejsce wykonywania
            prawa majątkowego: 1 - terytorium RP, 2 - poza terytorium RP
        :ivar p_22: Miejsce dokonania czynności cywilnoprawnej: 1 -
            terytorium RP, 2 - poza terytorium RP
        :ivar p_23: Zwięzłe określenie treści i przedmiotu czynności
            cywilnoprawnej
        :ivar p_24: Podstawa opodatkowania określona zgodnie z art. 6
            ustawy (po zaokrągleniu do pełnych złotych)
        :ivar p_25: Obliczony należny podatek od czynności
            cywilnoprawnej (po zaokrągleniu do pełnych złotych)
        :ivar p_26: Podstawa opodatkowania określona zgodnie z art. 6
            ustawy (po zaokrągleniu do pełnych złotych)
        :ivar p_27: Obliczony należny podatek od czynności
            cywilnoprawnej (po zaokrągleniu do pełnych złotych)
        :ivar p_28: Podstawa opodatkowania określona zgodnie z art. 6
            ustawy (po zaokrągleniu do pełnych złotych)
        :ivar p_29: Stawka podatku określona zgodnie z art. 7 ustawy
        :ivar p_30: Obliczony należny podatek od czynności
            cywilnoprawnej (po zaokrągleniu do pełnych złotych)
        :ivar p_31: Podstawa opodatkowania określona zgodnie z art. 6
            ustawy (po zaokrągleniu do pełnych złotych)
        :ivar p_32: Stawka podatku określona zgodnie z art. 7 ustawy
        :ivar p_33: Obliczony należny podatek od czynności
            cywilnoprawnej (po zaokrągleniu do pełnych złotych)
        :ivar p_34: Podstawa opodatkowania określona zgodnie z art. 6
            ustawy (po zaokrągleniu do pełnych złotych)
        :ivar p_35: Stawka podatku określona zgodnie z art. 7 ustawy
        :ivar p_36: Obliczony należny podatek od czynności
            cywilnoprawnej (po zaokrągleniu do pełnych złotych)
        :ivar p_37: Podstawa opodatkowania określona zgodnie z art. 6
            ustawy (po zaokrągleniu do pełnych złotych)
        :ivar p_38: Stawka podatku określona zgodnie z art. 7 ustawy
        :ivar p_39: Obliczony należny podatek od czynności
            cywilnoprawnej (po zaokrągleniu do pełnych złotych)
        :ivar p_40: Podstawa opodatkowania określona zgodnie z art. 6
            ustawy (po zaokrągleniu do pełnych złotych) - opodatkowana
            wg stawki podatku 0,1 %
        :ivar p_41: Obliczony należny podatek od czynności
            cywilnoprawnej (po zaokrągleniu do pełnych złotych)
        :ivar p_42: Obliczony należny podatek od czynności
            cywilnoprawnej (po zaokrągleniu do pełnych złotych) - dot.
            ustanowienia hipoteki na zabezpieczenie wierzytelności o
            wysokości nieustalonej
        :ivar p_43_a: Rodzaj czynności cywilnoprawnej (w tym zmiana
            umowy, orzeczenie sądu lub ugoda)
        :ivar p_43: Podstawa opodatkowania określona zgodnie z art. 6
            ustawy (po zaokrągleniu do pełnych złotych)
        :ivar p_44: Stawka podatku określona zgodnie z art. 7 ustawy
        :ivar p_45: Obliczony należny podatek od czynności
            cywilnoprawnej (po zaokrągleniu do pełnych złotych)
        :ivar p_46: Kwota należnego podatku
        :ivar p_47: Typ spółki: 1 - spółka osobowa, 2 - spółka
            kapitałowa
        :ivar p_48: Podstawa opodatkowania dotyczy: 1 - zawarcia umowy
            spółki, 2 - zwiększenia majątku spółki albo podwyższenia
            kapitału zakładowego, 3 - dopłaty, 4 - pożyczki udzielonej
            spółce osobowej przez wspólnika, 5 - oddania spółce rzeczy
            lub praw majątkowych do nieodpłatnego używania, 6 -
            przekształcenia spółek, 7 - łączenia spółek, 8 -
            przeniesienia na terytorium Rzeczypospolitej Polskiej
            rzeczywistego ośrodka zarządzania spółki kapitałowej lub jej
            siedziby
        :ivar p_49: Podstawa opodatkowania - określona zgodnie z art. 6
            ust. 1 pkt 8 ustawy (po zaokrągleniu do pełnych złotych)
        :ivar p_50: Opłaty i koszty związane z zawarciem umowy spółki
            lub jej zmiany - na podstawie art. 6 ust. 9 ustawy
        :ivar p_51: Podstawa obliczenia podatku
        :ivar p_52: Kwota należnego podatku (po zaokrągleniu do pełnych
            złotych)
        :ivar p_53: Kwota podatku do zapłaty
        :ivar p_54: Województwo
        :ivar p_55: Powiat
        :ivar p_56: Gmina
        :ivar p_57: Ulica
        :ivar p_58: Nr domu
        :ivar p_59: Nr lokalu
        :ivar p_60: Miejscowość
        :ivar p_61: Kod pocztowy
        :ivar p_62: Informacja o załącznikach - Liczba dołączonych
            załączników PCC-3/A
        """

        model_config = ConfigDict(defer_build=True)
        p_7: PozycjeSzczegoloweP7 = field(
            metadata={
                "name": "P_7",
                "type": "Element",
                "required": True,
            }
        )
        p_20: PozycjeSzczegoloweP20 = field(
            metadata={
                "name": "P_20",
                "type": "Element",
                "required": True,
            }
        )
        p_21: Optional[Twybor12] = field(
            default=None,
            metadata={
                "name": "P_21",
                "type": "Element",
            },
        )
        p_22: Optional[Twybor12] = field(
            default=None,
            metadata={
                "name": "P_22",
                "type": "Element",
            },
        )
        p_23: str = field(
            metadata={
                "name": "P_23",
                "type": "Element",
                "required": True,
                "min_length": 1,
                "max_length": 3500,
            }
        )
        p_24: Optional[int] = field(
            default=None,
            metadata={
                "name": "P_24",
                "type": "Element",
                "min_inclusive": 0,
                "total_digits": 14,
            },
        )
        p_25: Optional[int] = field(
            default=None,
            metadata={
                "name": "P_25",
                "type": "Element",
                "min_inclusive": 0,
                "total_digits": 14,
            },
        )
        p_26: Optional[int] = field(
            default=None,
            metadata={
                "name": "P_26",
                "type": "Element",
                "min_inclusive": 0,
                "total_digits": 14,
            },
        )
        p_27: Optional[int] = field(
            default=None,
            metadata={
                "name": "P_27",
                "type": "Element",
                "min_inclusive": 0,
                "total_digits": 14,
            },
        )
        p_28: Optional[int] = field(
            default=None,
            metadata={
                "name": "P_28",
                "type": "Element",
                "min_inclusive": 0,
                "total_digits": 14,
            },
        )
        p_29: Optional[Decimal] = field(
            default=None,
            metadata={
                "name": "P_29",
                "type": "Element",
                "min_inclusive": Decimal("0"),
                "max_inclusive": Decimal("100"),
                "total_digits": 5,
                "fraction_digits": 0,
                "white_space": "collapse",
            },
        )
        p_30: Optional[int] = field(
            default=None,
            metadata={
                "name": "P_30",
                "type": "Element",
                "min_inclusive": 0,
                "total_digits": 14,
            },
        )
        p_31: Optional[int] = field(
            default=None,
            metadata={
                "name": "P_31",
                "type": "Element",
                "min_inclusive": 0,
                "total_digits": 14,
            },
        )
        p_32: Optional[Decimal] = field(
            default=None,
            metadata={
                "name": "P_32",
                "type": "Element",
                "min_inclusive": Decimal("0"),
                "max_inclusive": Decimal("100"),
                "total_digits": 5,
                "fraction_digits": 1,
                "white_space": "collapse",
            },
        )
        p_33: Optional[int] = field(
            default=None,
            metadata={
                "name": "P_33",
                "type": "Element",
                "min_inclusive": 0,
                "total_digits": 14,
            },
        )
        p_34: Optional[int] = field(
            default=None,
            metadata={
                "name": "P_34",
                "type": "Element",
                "min_inclusive": 0,
                "total_digits": 14,
            },
        )
        p_35: Optional[Decimal] = field(
            default=None,
            metadata={
                "name": "P_35",
                "type": "Element",
                "min_inclusive": Decimal("0"),
                "max_inclusive": Decimal("100"),
                "total_digits": 5,
                "fraction_digits": 0,
                "white_space": "collapse",
            },
        )
        p_36: Optional[int] = field(
            default=None,
            metadata={
                "name": "P_36",
                "type": "Element",
                "min_inclusive": 0,
                "total_digits": 14,
            },
        )
        p_37: Optional[int] = field(
            default=None,
            metadata={
                "name": "P_37",
                "type": "Element",
                "min_inclusive": 0,
                "total_digits": 14,
            },
        )
        p_38: Optional[Decimal] = field(
            default=None,
            metadata={
                "name": "P_38",
                "type": "Element",
                "min_inclusive": Decimal("0"),
                "max_inclusive": Decimal("100"),
                "total_digits": 5,
                "fraction_digits": 0,
                "white_space": "collapse",
            },
        )
        p_39: Optional[int] = field(
            default=None,
            metadata={
                "name": "P_39",
                "type": "Element",
                "min_inclusive": 0,
                "total_digits": 14,
            },
        )
        p_40: Optional[int] = field(
            default=None,
            metadata={
                "name": "P_40",
                "type": "Element",
                "min_inclusive": 0,
                "total_digits": 14,
            },
        )
        p_41: Optional[int] = field(
            default=None,
            metadata={
                "name": "P_41",
                "type": "Element",
                "min_inclusive": 0,
                "total_digits": 14,
            },
        )
        p_42: Optional[PozycjeSzczegoloweP42] = field(
            default=None,
            metadata={
                "name": "P_42",
                "type": "Element",
            },
        )
        p_43_a: Optional[str] = field(
            default=None,
            metadata={
                "name": "P_43A",
                "type": "Element",
                "min_length": 1,
                "max_length": 240,
            },
        )
        p_43: Optional[int] = field(
            default=None,
            metadata={
                "name": "P_43",
                "type": "Element",
                "min_inclusive": 0,
                "total_digits": 14,
            },
        )
        p_44: Optional[Decimal] = field(
            default=None,
            metadata={
                "name": "P_44",
                "type": "Element",
                "min_inclusive": Decimal("0"),
                "max_inclusive": Decimal("100"),
                "total_digits": 5,
                "fraction_digits": 0,
                "white_space": "collapse",
            },
        )
        p_45: Optional[int] = field(
            default=None,
            metadata={
                "name": "P_45",
                "type": "Element",
                "min_inclusive": 0,
                "total_digits": 14,
            },
        )
        p_46: Optional[int] = field(
            default=None,
            metadata={
                "name": "P_46",
                "type": "Element",
                "min_inclusive": 0,
                "total_digits": 14,
            },
        )
        p_47: Optional[Twybor12] = field(
            default=None,
            metadata={
                "name": "P_47",
                "type": "Element",
            },
        )
        p_48: Optional[PozycjeSzczegoloweP48] = field(
            default=None,
            metadata={
                "name": "P_48",
                "type": "Element",
            },
        )
        p_49: Optional[int] = field(
            default=None,
            metadata={
                "name": "P_49",
                "type": "Element",
                "min_inclusive": 0,
                "total_digits": 14,
            },
        )
        p_50: Optional[Decimal] = field(
            default=None,
            metadata={
                "name": "P_50",
                "type": "Element",
                "min_inclusive": Decimal("0"),
                "total_digits": 16,
                "fraction_digits": 2,
                "white_space": "collapse",
            },
        )
        p_51: Optional[Decimal] = field(
            default=None,
            metadata={
                "name": "P_51",
                "type": "Element",
                "min_inclusive": Decimal("0"),
                "total_digits": 16,
                "fraction_digits": 2,
                "white_space": "collapse",
            },
        )
        p_52: Optional[int] = field(
            default=None,
            metadata={
                "name": "P_52",
                "type": "Element",
                "min_inclusive": 0,
                "total_digits": 14,
            },
        )
        p_53: int = field(
            metadata={
                "name": "P_53",
                "type": "Element",
                "required": True,
                "min_inclusive": 0,
                "total_digits": 14,
            }
        )
        p_54: Optional[str] = field(
            default=None,
            metadata={
                "name": "P_54",
                "type": "Element",
                "min_length": 1,
                "max_length": 36,
            },
        )
        p_55: Optional[str] = field(
            default=None,
            metadata={
                "name": "P_55",
                "type": "Element",
                "min_length": 1,
                "max_length": 36,
            },
        )
        p_56: Optional[str] = field(
            default=None,
            metadata={
                "name": "P_56",
                "type": "Element",
                "min_length": 1,
                "max_length": 36,
            },
        )
        p_57: Optional[str] = field(
            default=None,
            metadata={
                "name": "P_57",
                "type": "Element",
                "min_length": 1,
                "max_length": 65,
            },
        )
        p_58: Optional[str] = field(
            default=None,
            metadata={
                "name": "P_58",
                "type": "Element",
                "min_length": 1,
                "max_length": 9,
            },
        )
        p_59: Optional[str] = field(
            default=None,
            metadata={
                "name": "P_59",
                "type": "Element",
                "min_length": 1,
                "max_length": 10,
            },
        )
        p_60: Optional[str] = field(
            default=None,
            metadata={
                "name": "P_60",
                "type": "Element",
                "min_length": 1,
                "max_length": 56,
            },
        )
        p_61: Optional[str] = field(
            default=None,
            metadata={
                "name": "P_61",
                "type": "Element",
                "min_length": 1,
                "max_length": 8,
            },
        )
        p_62: Optional[int] = field(
            default=None,
            metadata={
                "name": "P_62",
                "type": "Element",
                "min_inclusive": 0,
                "total_digits": 14,
                "white_space": "collapse",
            },
        )

    class Zalaczniki(BaseModel):
        model_config = ConfigDict(defer_build=True)
        zalacznik_ord_zu: ZalacznikOrdZu = field(
            metadata={
                "name": "Zalacznik_ORD-ZU",
                "type": "Element",
                "namespace": "http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2022/09/13/eD/ORDZU/",
                "required": True,
            }
        )

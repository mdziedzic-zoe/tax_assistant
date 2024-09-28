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
    :cvar VALUE_0202: URZĄD SKARBOWY W BOLESŁAWCU
    :cvar VALUE_0203: URZĄD SKARBOWY W BYSTRZYCY KŁODZKIEJ
    :cvar VALUE_0204: URZĄD SKARBOWY W DZIERŻONIOWIE
    :cvar VALUE_0205: URZĄD SKARBOWY W GŁOGOWIE
    :cvar VALUE_0206: URZĄD SKARBOWY W JAWORZE
    :cvar VALUE_0207: URZĄD SKARBOWY W JELENIEJ GÓRZE
    :cvar VALUE_0208: URZĄD SKARBOWY W KAMIENNEJ GÓRZE
    :cvar VALUE_0209: URZĄD SKARBOWY W KŁODZKU
    :cvar VALUE_0210: URZĄD SKARBOWY W LEGNICY
    :cvar VALUE_0211: URZĄD SKARBOWY W LUBANIU
    :cvar VALUE_0212: URZĄD SKARBOWY W LUBINIE
    :cvar VALUE_0213: URZĄD SKARBOWY W LWÓWKU ŚLĄSKIM
    :cvar VALUE_0214: URZĄD SKARBOWY W MILICZU
    :cvar VALUE_0215: URZĄD SKARBOWY W NOWEJ RUDZIE
    :cvar VALUE_0216: URZĄD SKARBOWY W OLEŚNICY
    :cvar VALUE_0217: URZĄD SKARBOWY W OŁAWIE
    :cvar VALUE_0218: URZĄD SKARBOWY W STRZELINIE
    :cvar VALUE_0219: URZĄD SKARBOWY W ŚRODZIE ŚLĄSKIEJ
    :cvar VALUE_0220: URZĄD SKARBOWY W ŚWIDNICY
    :cvar VALUE_0221: URZĄD SKARBOWY W TRZEBNICY
    :cvar VALUE_0222: URZĄD SKARBOWY W WAŁBRZYCHU
    :cvar VALUE_0223: URZĄD SKARBOWY W WOŁOWIE
    :cvar VALUE_0224: URZĄD SKARBOWY WROCŁAW-FABRYCZNA
    :cvar VALUE_0225: URZĄD SKARBOWY WROCŁAW-KRZYKI
    :cvar VALUE_0226: URZĄD SKARBOWY WROCŁAW-PSIE POLE
    :cvar VALUE_0227: URZĄD SKARBOWY WROCŁAW-STARE MIASTO
    :cvar VALUE_0228: URZĄD SKARBOWY WROCŁAW-ŚRÓDMIEŚCIE
    :cvar VALUE_0229: PIERWSZY URZĄD SKARBOWY WE WROCŁAWIU
    :cvar VALUE_0230: URZĄD SKARBOWY W ZĄBKOWICACH ŚLĄSKICH
    :cvar VALUE_0231: URZĄD SKARBOWY W ZGORZELCU
    :cvar VALUE_0232: URZĄD SKARBOWY W ZŁOTORYI
    :cvar VALUE_0233: URZĄD SKARBOWY W GÓRZE
    :cvar VALUE_0234: URZĄD SKARBOWY W POLKOWICACH
    :cvar VALUE_0271: DOLNOŚLĄSKI URZĄD SKARBOWY WE WROCŁAWIU
    :cvar VALUE_0402: URZĄD SKARBOWY W ALEKSANDROWIE KUJAWSKIM
    :cvar VALUE_0403: URZĄD SKARBOWY W BRODNICY
    :cvar VALUE_0404: PIERWSZY URZĄD SKARBOWY W BYDGOSZCZY
    :cvar VALUE_0405: DRUGI URZĄD SKARBOWY W BYDGOSZCZY
    :cvar VALUE_0406: TRZECI URZĄD SKARBOWY W BYDGOSZCZY
    :cvar VALUE_0407: URZĄD SKARBOWY W CHEŁMNIE
    :cvar VALUE_0408: URZĄD SKARBOWY W GRUDZIĄDZU
    :cvar VALUE_0409: URZĄD SKARBOWY W INOWROCŁAWIU
    :cvar VALUE_0410: URZĄD SKARBOWY W LIPNIE
    :cvar VALUE_0411: URZĄD SKARBOWY W MOGILNIE
    :cvar VALUE_0412: URZĄD SKARBOWY W NAKLE NAD NOTECIĄ
    :cvar VALUE_0413: URZĄD SKARBOWY W RADZIEJOWIE
    :cvar VALUE_0414: URZĄD SKARBOWY W RYPINIE
    :cvar VALUE_0415: URZĄD SKARBOWY W ŚWIECIU
    :cvar VALUE_0416: PIERWSZY URZĄD SKARBOWY W TORUNIU
    :cvar VALUE_0417: DRUGI URZĄD SKARBOWY W TORUNIU
    :cvar VALUE_0418: URZĄD SKARBOWY W TUCHOLI
    :cvar VALUE_0419: URZĄD SKARBOWY W WĄBRZEŹNIE
    :cvar VALUE_0420: URZĄD SKARBOWY WE WŁOCŁAWKU
    :cvar VALUE_0421: URZĄD SKARBOWY W ŻNINIE
    :cvar VALUE_0422: URZĄD SKARBOWY W GOLUBIU-DOBRZYNIU
    :cvar VALUE_0423: URZĄD SKARBOWY W SĘPÓLNIE KRAJEŃSKIM
    :cvar VALUE_0471: KUJAWSKO-POMORSKI URZĄD SKARBOWY W BYDGOSZCZY
    :cvar VALUE_0602: URZĄD SKARBOWY W BIAŁEJ PODLASKIEJ
    :cvar VALUE_0603: URZĄD SKARBOWY W BIŁGORAJU
    :cvar VALUE_0604: URZĄD SKARBOWY W CHEŁMIE
    :cvar VALUE_0605: URZĄD SKARBOWY W HRUBIESZOWIE
    :cvar VALUE_0606: URZĄD SKARBOWY W JANOWIE LUBELSKIM
    :cvar VALUE_0607: URZĄD SKARBOWY W KRASNYMSTAWIE
    :cvar VALUE_0608: URZĄD SKARBOWY W KRAŚNIKU
    :cvar VALUE_0609: URZĄD SKARBOWY W LUBARTOWIE
    :cvar VALUE_0610: PIERWSZY URZĄD SKARBOWY W LUBLINIE
    :cvar VALUE_0611: DRUGI URZĄD SKARBOWY W LUBLINIE
    :cvar VALUE_0612: TRZECI URZĄD SKARBOWY W LUBLINIE
    :cvar VALUE_0613: URZĄD SKARBOWY W ŁUKOWIE
    :cvar VALUE_0614: URZĄD SKARBOWY W OPOLU LUBELSKIM
    :cvar VALUE_0615: URZĄD SKARBOWY W PARCZEWIE
    :cvar VALUE_0616: URZĄD SKARBOWY W PUŁAWACH
    :cvar VALUE_0617: URZĄD SKARBOWY W RADZYNIU PODLASKIM
    :cvar VALUE_0618: URZĄD SKARBOWY W TOMASZOWIE LUBELSKIM
    :cvar VALUE_0619: URZĄD SKARBOWY WE WŁODAWIE
    :cvar VALUE_0620: URZĄD SKARBOWY W ZAMOŚCIU
    :cvar VALUE_0621: URZĄD SKARBOWY W ŁĘCZNEJ
    :cvar VALUE_0622: URZĄD SKARBOWY W RYKACH
    :cvar VALUE_0671: LUBELSKI URZĄD SKARBOWY W LUBLINIE
    :cvar VALUE_0802: URZĄD SKARBOWY W GORZOWIE WIELKOPOLSKIM
    :cvar VALUE_0803: URZĄD SKARBOWY W KROŚNIE ODRZAŃSKIM
    :cvar VALUE_0804: URZĄD SKARBOWY W MIĘDZYRZECZU
    :cvar VALUE_0805: URZĄD SKARBOWY W NOWEJ SOLI
    :cvar VALUE_0806: URZĄD SKARBOWY W SŁUBICACH
    :cvar VALUE_0807: URZĄD SKARBOWY W ŚWIEBODZINIE
    :cvar VALUE_0808: PIERWSZY URZĄD SKARBOWY W ZIELONEJ GÓRZE
    :cvar VALUE_0809: DRUGI URZĄD SKARBOWY W ZIELONEJ GÓRZE
    :cvar VALUE_0810: URZĄD SKARBOWY W ŻAGANIU
    :cvar VALUE_0811: URZĄD SKARBOWY W ŻARACH
    :cvar VALUE_0812: URZĄD SKARBOWY W DREZDENKU
    :cvar VALUE_0813: URZĄD SKARBOWY W SULĘCINIE
    :cvar VALUE_0814: URZĄD SKARBOWY WE WSCHOWIE
    :cvar VALUE_0871: LUBUSKI URZĄD SKARBOWY W ZIELONEJ GÓRZE
    :cvar VALUE_1002: URZĄD SKARBOWY W BEŁCHATOWIE
    :cvar VALUE_1003: URZĄD SKARBOWY W BRZEZINACH
    :cvar VALUE_1004: URZĄD SKARBOWY W GŁOWNIE
    :cvar VALUE_1005: URZĄD SKARBOWY W KUTNIE
    :cvar VALUE_1006: URZĄD SKARBOWY W ŁASKU
    :cvar VALUE_1007: URZĄD SKARBOWY W ŁOWICZU
    :cvar VALUE_1008: PIERWSZY URZĄD SKARBOWY ŁÓDŹ-BAŁUTY
    :cvar VALUE_1009: DRUGI URZĄD SKARBOWY ŁÓDŹ-BAŁUTY
    :cvar VALUE_1010: PIERWSZY URZĄD SKARBOWY ŁÓDŹ-GÓRNA
    :cvar VALUE_1011: DRUGI URZĄD SKARBOWY ŁÓDŹ-GÓRNA
    :cvar VALUE_1012: URZĄD SKARBOWY ŁÓDŹ-POLESIE
    :cvar VALUE_1013: URZĄD SKARBOWY ŁÓDŹ-ŚRÓDMIEŚCIE
    :cvar VALUE_1014: URZĄD SKARBOWY ŁÓDŹ-WIDZEW
    :cvar VALUE_1015: URZĄD SKARBOWY W OPOCZNIE
    :cvar VALUE_1016: URZĄD SKARBOWY W PABIANICACH
    :cvar VALUE_1017: URZĄD SKARBOWY W PIOTRKOWIE TRYBUNALSKIM
    :cvar VALUE_1018: URZĄD SKARBOWY W PODDĘBICACH
    :cvar VALUE_1019: URZĄD SKARBOWY W RADOMSKU
    :cvar VALUE_1020: URZĄD SKARBOWY W RAWIE MAZOWIECKIEJ
    :cvar VALUE_1021: URZĄD SKARBOWY W SIERADZU
    :cvar VALUE_1022: URZĄD SKARBOWY W SKIERNIEWICACH
    :cvar VALUE_1023: URZĄD SKARBOWY W TOMASZOWIE MAZOWIECKIM
    :cvar VALUE_1024: URZĄD SKARBOWY W WIELUNIU
    :cvar VALUE_1025: URZĄD SKARBOWY W ZDUŃSKIEJ WOLI
    :cvar VALUE_1026: URZĄD SKARBOWY W ZGIERZU
    :cvar VALUE_1027: URZĄD SKARBOWY W WIERUSZOWIE
    :cvar VALUE_1028: URZĄD SKARBOWY W ŁĘCZYCY
    :cvar VALUE_1029: URZĄD SKARBOWY W PAJĘCZNIE
    :cvar VALUE_1071: ŁÓDZKI URZĄD SKARBOWY W ŁODZI
    :cvar VALUE_1202: URZĄD SKARBOWY W BOCHNI
    :cvar VALUE_1203: URZĄD SKARBOWY W BRZESKU
    :cvar VALUE_1204: URZĄD SKARBOWY W CHRZANOWIE
    :cvar VALUE_1205: URZĄD SKARBOWY W DĄBROWIE TARNOWSKIEJ
    :cvar VALUE_1206: URZĄD SKARBOWY W GORLICACH
    :cvar VALUE_1207: PIERWSZY URZĄD SKARBOWY KRAKÓW
    :cvar VALUE_1208: URZĄD SKARBOWY KRAKÓW-KROWODRZA
    :cvar VALUE_1209: URZĄD SKARBOWY KRAKÓW-NOWA HUTA
    :cvar VALUE_1210: URZĄD SKARBOWY KRAKÓW-PODGÓRZE
    :cvar VALUE_1211: URZĄD SKARBOWY KRAKÓW-PRĄDNIK
    :cvar VALUE_1212: URZĄD SKARBOWY KRAKÓW-STARE MIASTO
    :cvar VALUE_1213: URZĄD SKARBOWY KRAKÓW-ŚRÓDMIEŚCIE
    :cvar VALUE_1214: URZĄD SKARBOWY W LIMANOWEJ
    :cvar VALUE_1215: URZĄD SKARBOWY W MIECHOWIE
    :cvar VALUE_1216: URZĄD SKARBOWY W MYŚLENICACH
    :cvar VALUE_1217: URZĄD SKARBOWY W NOWYM SĄCZU
    :cvar VALUE_1218: URZĄD SKARBOWY W NOWYM TARGU
    :cvar VALUE_1219: URZĄD SKARBOWY W OLKUSZU
    :cvar VALUE_1220: URZĄD SKARBOWY W OŚWIĘCIMIU
    :cvar VALUE_1221: URZĄD SKARBOWY W PROSZOWICACH
    :cvar VALUE_1222: URZĄD SKARBOWY W SUCHEJ BESKIDZKIEJ
    :cvar VALUE_1223: PIERWSZY URZĄD SKARBOWY W TARNOWIE
    :cvar VALUE_1224: DRUGI URZĄD SKARBOWY W TARNOWIE
    :cvar VALUE_1225: URZĄD SKARBOWY W WADOWICACH
    :cvar VALUE_1226: URZĄD SKARBOWY W WIELICZCE
    :cvar VALUE_1227: URZĄD SKARBOWY W ZAKOPANEM
    :cvar VALUE_1228: DRUGI URZĄD SKARBOWY KRAKÓW
    :cvar VALUE_1271: MAŁOPOLSKI URZĄD SKARBOWY W KRAKOWIE
    :cvar VALUE_1402: URZĄD SKARBOWY W BIAŁOBRZEGACH
    :cvar VALUE_1403: URZĄD SKARBOWY W CIECHANOWIE
    :cvar VALUE_1404: URZĄD SKARBOWY W GARWOLINIE
    :cvar VALUE_1405: URZĄD SKARBOWY W GOSTYNINIE
    :cvar VALUE_1406: URZĄD SKARBOWY W GRODZISKU MAZOWIECKIM
    :cvar VALUE_1407: URZĄD SKARBOWY W GRÓJCU
    :cvar VALUE_1408: URZĄD SKARBOWY W KOZIENICACH
    :cvar VALUE_1409: URZĄD SKARBOWY W LEGIONOWIE
    :cvar VALUE_1410: URZĄD SKARBOWY W ŁOSICACH
    :cvar VALUE_1411: URZĄD SKARBOWY W MAKOWIE MAZOWIECKIM
    :cvar VALUE_1412: URZĄD SKARBOWY W MIŃSKU MAZOWIECKIM
    :cvar VALUE_1413: URZĄD SKARBOWY W MŁAWIE
    :cvar VALUE_1414: URZĄD SKARBOWY W NOWYM DWORZE MAZOWIECKIM
    :cvar VALUE_1415: URZĄD SKARBOWY W OSTROŁĘCE
    :cvar VALUE_1416: URZĄD SKARBOWY W OSTROWI MAZOWIECKIEJ
    :cvar VALUE_1417: URZĄD SKARBOWY W OTWOCKU
    :cvar VALUE_1418: URZĄD SKARBOWY W PIASECZNIE
    :cvar VALUE_1419: URZĄD SKARBOWY W PŁOCKU
    :cvar VALUE_1420: URZĄD SKARBOWY W PŁOŃSKU
    :cvar VALUE_1421: URZĄD SKARBOWY W PRUSZKOWIE
    :cvar VALUE_1422: URZĄD SKARBOWY W PRZASNYSZU
    :cvar VALUE_1423: URZĄD SKARBOWY W PUŁTUSKU
    :cvar VALUE_1424: PIERWSZY URZĄD SKARBOWY W RADOMIU
    :cvar VALUE_1425: DRUGI URZĄD SKARBOWY W RADOMIU
    :cvar VALUE_1426: URZĄD SKARBOWY W SIEDLCACH
    :cvar VALUE_1427: URZĄD SKARBOWY W SIERPCU
    :cvar VALUE_1428: URZĄD SKARBOWY W SOCHACZEWIE
    :cvar VALUE_1429: URZĄD SKARBOWY W SOKOŁOWIE PODLASKIM
    :cvar VALUE_1430: URZĄD SKARBOWY W SZYDŁOWCU
    :cvar VALUE_1431: URZĄD SKARBOWY WARSZAWA-BEMOWO
    :cvar VALUE_1432: URZĄD SKARBOWY WARSZAWA-BIELANY
    :cvar VALUE_1433: URZĄD SKARBOWY WARSZAWA-MOKOTÓW
    :cvar VALUE_1434: URZĄD SKARBOWY WARSZAWA-PRAGA
    :cvar VALUE_1435: PIERWSZY URZĄD SKARBOWY WARSZAWA-ŚRÓDMIEŚCIE
    :cvar VALUE_1436: DRUGI URZĄD SKARBOWY WARSZAWA-ŚRÓDMIEŚCIE
    :cvar VALUE_1437: URZĄD SKARBOWY WARSZAWA-TARGÓWEK
    :cvar VALUE_1438: URZĄD SKARBOWY WARSZAWA-URSYNÓW
    :cvar VALUE_1439: URZĄD SKARBOWY WARSZAWA-WAWER
    :cvar VALUE_1440: URZĄD SKARBOWY WARSZAWA-WOLA
    :cvar VALUE_1441: URZĄD SKARBOWY W WĘGROWIE
    :cvar VALUE_1442: URZĄD SKARBOWY W WOŁOMINIE
    :cvar VALUE_1443: URZĄD SKARBOWY W WYSZKOWIE
    :cvar VALUE_1444: URZĄD SKARBOWY W ZWOLENIU
    :cvar VALUE_1445: URZĄD SKARBOWY W ŻUROMINIE
    :cvar VALUE_1446: URZĄD SKARBOWY W ŻYRARDOWIE
    :cvar VALUE_1447: URZĄD SKARBOWY W LIPSKU
    :cvar VALUE_1448: URZĄD SKARBOWY W PRZYSUSZE
    :cvar VALUE_1449: TRZECI URZĄD SKARBOWY WARSZAWA-ŚRÓDMIEŚCIE
    :cvar VALUE_1471: PIERWSZY MAZOWIECKI URZĄD SKARBOWY W WARSZAWIE
    :cvar VALUE_1472: DRUGI MAZOWIECKI URZĄD SKARBOWY W WARSZAWIE
    :cvar VALUE_1473: TRZECI MAZOWIECKI URZĄD SKARBOWY W RADOMIU
    :cvar VALUE_1602: URZĄD SKARBOWY W BRZEGU
    :cvar VALUE_1603: URZĄD SKARBOWY W GŁUBCZYCACH
    :cvar VALUE_1604: URZĄD SKARBOWY W KĘDZIERZYNIE-KOŹLU
    :cvar VALUE_1605: URZĄD SKARBOWY W KLUCZBORKU
    :cvar VALUE_1606: URZĄD SKARBOWY W NAMYSŁOWIE
    :cvar VALUE_1607: URZĄD SKARBOWY W NYSIE
    :cvar VALUE_1608: URZĄD SKARBOWY W OLEŚNIE
    :cvar VALUE_1609: PIERWSZY URZĄD SKARBOWY W OPOLU
    :cvar VALUE_1610: DRUGI URZĄD SKARBOWY W OPOLU
    :cvar VALUE_1611: URZĄD SKARBOWY W PRUDNIKU
    :cvar VALUE_1612: URZĄD SKARBOWY W STRZELCACH OPOLSKICH
    :cvar VALUE_1613: URZĄD SKARBOWY W KRAPKOWICACH
    :cvar VALUE_1671: OPOLSKI URZĄD SKARBOWY W OPOLU
    :cvar VALUE_1802: URZĄD SKARBOWY W BRZOZOWIE
    :cvar VALUE_1803: URZĄD SKARBOWY W DĘBICY
    :cvar VALUE_1804: URZĄD SKARBOWY W JAROSŁAWIU
    :cvar VALUE_1805: URZĄD SKARBOWY W JAŚLE
    :cvar VALUE_1806: URZĄD SKARBOWY W KOLBUSZOWEJ
    :cvar VALUE_1807: URZĄD SKARBOWY W KROŚNIE
    :cvar VALUE_1808: URZĄD SKARBOWY W LESKU
    :cvar VALUE_1809: URZĄD SKARBOWY W LEŻAJSKU
    :cvar VALUE_1810: URZĄD SKARBOWY W LUBACZOWIE
    :cvar VALUE_1811: URZĄD SKARBOWY W ŁAŃCUCIE
    :cvar VALUE_1812: URZĄD SKARBOWY W MIELCU
    :cvar VALUE_1813: URZĄD SKARBOWY W PRZEMYŚLU
    :cvar VALUE_1814: URZĄD SKARBOWY W PRZEWORSKU
    :cvar VALUE_1815: URZĄD SKARBOWY W ROPCZYCACH
    :cvar VALUE_1816: PIERWSZY URZĄD SKARBOWY W RZESZOWIE
    :cvar VALUE_1817: URZĄD SKARBOWY W SANOKU
    :cvar VALUE_1818: URZĄD SKARBOWY W STALOWEJ WOLI
    :cvar VALUE_1819: URZĄD SKARBOWY W STRZYŻOWIE
    :cvar VALUE_1820: URZĄD SKARBOWY W TARNOBRZEGU
    :cvar VALUE_1821: URZĄD SKARBOWY W USTRZYKACH DOLNYCH
    :cvar VALUE_1822: DRUGI URZĄD SKARBOWY W RZESZOWIE
    :cvar VALUE_1823: URZĄD SKARBOWY W NISKU
    :cvar VALUE_1871: PODKARPACKI URZĄD SKARBOWY W RZESZOWIE
    :cvar VALUE_2002: URZĄD SKARBOWY W AUGUSTOWIE
    :cvar VALUE_2003: PIERWSZY URZĄD SKARBOWY W BIAŁYMSTOKU
    :cvar VALUE_2004: DRUGI URZĄD SKARBOWY W BIAŁYMSTOKU
    :cvar VALUE_2005: URZĄD SKARBOWY W BIELSKU PODLASKIM
    :cvar VALUE_2006: URZĄD SKARBOWY W GRAJEWIE
    :cvar VALUE_2007: URZĄD SKARBOWY W KOLNIE
    :cvar VALUE_2008: URZĄD SKARBOWY W ŁOMŻY
    :cvar VALUE_2009: URZĄD SKARBOWY W MOŃKACH
    :cvar VALUE_2010: URZĄD SKARBOWY W SIEMIATYCZACH
    :cvar VALUE_2011: URZĄD SKARBOWY W SOKÓŁCE
    :cvar VALUE_2012: URZĄD SKARBOWY W SUWAŁKACH
    :cvar VALUE_2013: URZĄD SKARBOWY W WYSOKIEM MAZOWIECKIEM
    :cvar VALUE_2014: URZĄD SKARBOWY W ZAMBROWIE
    :cvar VALUE_2015: URZĄD SKARBOWY W HAJNÓWCE
    :cvar VALUE_2071: PODLASKI URZĄD SKARBOWY W BIAŁYMSTOKU
    :cvar VALUE_2202: URZĄD SKARBOWY W BYTOWIE
    :cvar VALUE_2203: URZĄD SKARBOWY W CHOJNICACH
    :cvar VALUE_2204: URZĄD SKARBOWY W CZŁUCHOWIE
    :cvar VALUE_2205: PIERWSZY URZĄD SKARBOWY W GDAŃSKU
    :cvar VALUE_2206: DRUGI URZĄD SKARBOWY W GDAŃSKU
    :cvar VALUE_2207: TRZECI URZĄD SKARBOWY W GDAŃSKU
    :cvar VALUE_2208: PIERWSZY URZĄD SKARBOWY W GDYNI
    :cvar VALUE_2209: DRUGI URZĄD SKARBOWY W GDYNI
    :cvar VALUE_2210: URZĄD SKARBOWY W KARTUZACH
    :cvar VALUE_2211: URZĄD SKARBOWY W KOŚCIERZYNIE
    :cvar VALUE_2212: URZĄD SKARBOWY W KWIDZYNIE
    :cvar VALUE_2213: URZĄD SKARBOWY W LĘBORKU
    :cvar VALUE_2214: URZĄD SKARBOWY W MALBORKU
    :cvar VALUE_2215: URZĄD SKARBOWY W PUCKU
    :cvar VALUE_2216: URZĄD SKARBOWY W SŁUPSKU
    :cvar VALUE_2217: URZĄD SKARBOWY W SOPOCIE
    :cvar VALUE_2218: URZĄD SKARBOWY W STAROGARDZIE GDAŃSKIM
    :cvar VALUE_2219: URZĄD SKARBOWY W TCZEWIE
    :cvar VALUE_2220: URZĄD SKARBOWY W WEJHEROWIE
    :cvar VALUE_2221: URZĄD SKARBOWY W PRUSZCZU GDAŃSKIM
    :cvar VALUE_2271: POMORSKI URZĄD SKARBOWY W GDAŃSKU
    :cvar VALUE_2402: URZĄD SKARBOWY W BĘDZINIE
    :cvar VALUE_2403: PIERWSZY URZĄD SKARBOWY W BIELSKU-BIAŁEJ
    :cvar VALUE_2404: DRUGI URZĄD SKARBOWY W BIELSKU-BIAŁEJ
    :cvar VALUE_2405: URZĄD SKARBOWY W BYTOMIU
    :cvar VALUE_2406: URZĄD SKARBOWY W CHORZOWIE
    :cvar VALUE_2407: URZĄD SKARBOWY W CIESZYNIE
    :cvar VALUE_2408: URZĄD SKARBOWY W CZECHOWICACH-DZIEDZICACH
    :cvar VALUE_2409: PIERWSZY URZĄD SKARBOWY W CZĘSTOCHOWIE
    :cvar VALUE_2410: DRUGI URZĄD SKARBOWY W CZĘSTOCHOWIE
    :cvar VALUE_2411: URZĄD SKARBOWY W DĄBROWIE GÓRNICZEJ
    :cvar VALUE_2412: PIERWSZY URZĄD SKARBOWY W GLIWICACH
    :cvar VALUE_2413: DRUGI URZĄD SKARBOWY W GLIWICACH
    :cvar VALUE_2414: URZĄD SKARBOWY W JASTRZĘBIU-ZDROJU
    :cvar VALUE_2415: URZĄD SKARBOWY W JAWORZNIE
    :cvar VALUE_2416: PIERWSZY URZĄD SKARBOWY W KATOWICACH
    :cvar VALUE_2417: DRUGI URZĄD SKARBOWY W KATOWICACH
    :cvar VALUE_2418: URZĄD SKARBOWY W KŁOBUCKU
    :cvar VALUE_2419: URZĄD SKARBOWY W LUBLIŃCU
    :cvar VALUE_2420: URZĄD SKARBOWY W MIKOŁOWIE
    :cvar VALUE_2421: URZĄD SKARBOWY W MYSŁOWICACH
    :cvar VALUE_2422: URZĄD SKARBOWY W MYSZKOWIE
    :cvar VALUE_2423: URZĄD SKARBOWY W PIEKARACH ŚLĄSKICH
    :cvar VALUE_2424: URZĄD SKARBOWY W PSZCZYNIE
    :cvar VALUE_2425: URZĄD SKARBOWY W RACIBORZU
    :cvar VALUE_2426: URZĄD SKARBOWY W RUDZIE ŚLĄSKIEJ
    :cvar VALUE_2427: URZĄD SKARBOWY W RYBNIKU
    :cvar VALUE_2428: URZĄD SKARBOWY W SIEMIANOWICACH ŚLĄSKICH
    :cvar VALUE_2429: URZĄD SKARBOWY W SOSNOWCU
    :cvar VALUE_2430: URZĄD SKARBOWY W TARNOWSKICH GÓRACH
    :cvar VALUE_2431: URZĄD SKARBOWY W TYCHACH
    :cvar VALUE_2432: URZĄD SKARBOWY W WODZISŁAWIU ŚLĄSKIM
    :cvar VALUE_2433: URZĄD SKARBOWY W ZABRZU
    :cvar VALUE_2434: URZĄD SKARBOWY W ZAWIERCIU
    :cvar VALUE_2435: URZĄD SKARBOWY W ŻORACH
    :cvar VALUE_2436: URZĄD SKARBOWY W ŻYWCU
    :cvar VALUE_2471: PIERWSZY ŚLĄSKI URZĄD SKARBOWY W SOSNOWCU
    :cvar VALUE_2472: DRUGI ŚLĄSKI URZĄD SKARBOWY W BIELSKU-BIAŁEJ
    :cvar VALUE_2602: URZĄD SKARBOWY W BUSKU-ZDROJU
    :cvar VALUE_2603: URZĄD SKARBOWY W JĘDRZEJOWIE
    :cvar VALUE_2604: PIERWSZY URZĄD SKARBOWY W KIELCACH
    :cvar VALUE_2605: DRUGI URZĄD SKARBOWY W KIELCACH
    :cvar VALUE_2606: URZĄD SKARBOWY W KOŃSKICH
    :cvar VALUE_2607: URZĄD SKARBOWY W OPATOWIE
    :cvar VALUE_2608: URZĄD SKARBOWY W OSTROWCU ŚWIĘTOKRZYSKIM
    :cvar VALUE_2609: URZĄD SKARBOWY W PIŃCZOWIE
    :cvar VALUE_2610: URZĄD SKARBOWY W SANDOMIERZU
    :cvar VALUE_2611: URZĄD SKARBOWY W SKARŻYSKU-KAMIENNEJ
    :cvar VALUE_2612: URZĄD SKARBOWY W STARACHOWICACH
    :cvar VALUE_2613: URZĄD SKARBOWY W STASZOWIE
    :cvar VALUE_2614: URZĄD SKARBOWY W KAZIMIERZY WIELKIEJ
    :cvar VALUE_2615: URZĄD SKARBOWY WE WŁOSZCZOWIE
    :cvar VALUE_2671: ŚWIĘTOKRZYSKI URZĄD SKARBOWY W KIELCACH
    :cvar VALUE_2802: URZĄD SKARBOWY W BARTOSZYCACH
    :cvar VALUE_2803: URZĄD SKARBOWY W BRANIEWIE
    :cvar VALUE_2804: URZĄD SKARBOWY W DZIAŁDOWIE
    :cvar VALUE_2805: URZĄD SKARBOWY W ELBLĄGU
    :cvar VALUE_2806: URZĄD SKARBOWY W EŁKU
    :cvar VALUE_2807: URZĄD SKARBOWY W GIŻYCKU
    :cvar VALUE_2808: URZĄD SKARBOWY W IŁAWIE
    :cvar VALUE_2809: URZĄD SKARBOWY W KĘTRZYNIE
    :cvar VALUE_2810: URZĄD SKARBOWY W NIDZICY
    :cvar VALUE_2811: URZĄD SKARBOWY W NOWYM MIEŚCIE LUBAWSKIM
    :cvar VALUE_2812: URZĄD SKARBOWY W OLECKU
    :cvar VALUE_2813: URZĄD SKARBOWY W OLSZTYNIE
    :cvar VALUE_2814: URZĄD SKARBOWY W OSTRÓDZIE
    :cvar VALUE_2815: URZĄD SKARBOWY W PISZU
    :cvar VALUE_2816: URZĄD SKARBOWY W SZCZYTNIE
    :cvar VALUE_2871: WARMIŃSKO-MAZURSKI URZĄD SKARBOWY W OLSZTYNIE
    :cvar VALUE_3002: URZĄD SKARBOWY W CZARNKOWIE
    :cvar VALUE_3003: URZĄD SKARBOWY W GNIEŹNIE
    :cvar VALUE_3004: URZĄD SKARBOWY W GOSTYNIU
    :cvar VALUE_3005: URZĄD SKARBOWY W GRODZISKU WIELKOPOLSKIM
    :cvar VALUE_3006: URZĄD SKARBOWY W JAROCINIE
    :cvar VALUE_3007: PIERWSZY URZĄD SKARBOWY W KALISZU
    :cvar VALUE_3008: DRUGI URZĄD SKARBOWY W KALISZU
    :cvar VALUE_3009: URZĄD SKARBOWY W KĘPNIE
    :cvar VALUE_3010: URZĄD SKARBOWY W KOLE
    :cvar VALUE_3011: URZĄD SKARBOWY W KONINIE
    :cvar VALUE_3012: URZĄD SKARBOWY W KOŚCIANIE
    :cvar VALUE_3013: URZĄD SKARBOWY W KROTOSZYNIE
    :cvar VALUE_3014: URZĄD SKARBOWY W LESZNIE
    :cvar VALUE_3015: URZĄD SKARBOWY W MIĘDZYCHODZIE
    :cvar VALUE_3016: URZĄD SKARBOWY W NOWYM TOMYŚLU
    :cvar VALUE_3017: URZĄD SKARBOWY W OSTROWIE WIELKOPOLSKIM
    :cvar VALUE_3018: URZĄD SKARBOWY W OSTRZESZOWIE
    :cvar VALUE_3019: URZĄD SKARBOWY W PILE
    :cvar VALUE_3020: URZĄD SKARBOWY POZNAŃ-GRUNWALD
    :cvar VALUE_3021: URZĄD SKARBOWY POZNAŃ-JEŻYCE
    :cvar VALUE_3022: URZĄD SKARBOWY POZNAŃ-NOWE MIASTO
    :cvar VALUE_3023: PIERWSZY URZĄD SKARBOWY W POZNANIU
    :cvar VALUE_3025: URZĄD SKARBOWY POZNAŃ-WINOGRADY
    :cvar VALUE_3026: URZĄD SKARBOWY POZNAŃ-WILDA
    :cvar VALUE_3027: URZĄD SKARBOWY W RAWICZU
    :cvar VALUE_3028: URZĄD SKARBOWY W SŁUPCY
    :cvar VALUE_3029: URZĄD SKARBOWY W SZAMOTUŁACH
    :cvar VALUE_3030: URZĄD SKARBOWY W ŚREMIE
    :cvar VALUE_3031: URZĄD SKARBOWY W ŚRODZIE WIELKOPOLSKIEJ
    :cvar VALUE_3032: URZĄD SKARBOWY W TURKU
    :cvar VALUE_3033: URZĄD SKARBOWY W WĄGROWCU
    :cvar VALUE_3034: URZĄD SKARBOWY W WOLSZTYNIE
    :cvar VALUE_3035: URZĄD SKARBOWY WE WRZEŚNI
    :cvar VALUE_3036: URZĄD SKARBOWY W ZŁOTOWIE
    :cvar VALUE_3037: URZĄD SKARBOWY W CHODZIEŻY
    :cvar VALUE_3038: URZĄD SKARBOWY W OBORNIKACH
    :cvar VALUE_3039: URZĄD SKARBOWY W PLESZEWIE
    :cvar VALUE_3071: PIERWSZY WIELKOPOLSKI URZĄD SKARBOWY W POZNANIU
    :cvar VALUE_3072: DRUGI WIELKOPOLSKI URZĄD SKARBOWY W KALISZU
    :cvar VALUE_3202: URZĄD SKARBOWY W BIAŁOGARDZIE
    :cvar VALUE_3203: URZĄD SKARBOWY W CHOSZCZNIE
    :cvar VALUE_3204: URZĄD SKARBOWY W DRAWSKU POMORSKIM
    :cvar VALUE_3205: URZĄD SKARBOWY W GOLENIOWIE
    :cvar VALUE_3206: URZĄD SKARBOWY W GRYFICACH
    :cvar VALUE_3207: URZĄD SKARBOWY W GRYFINIE
    :cvar VALUE_3208: URZĄD SKARBOWY W KAMIENIU POMORSKIM
    :cvar VALUE_3209: URZĄD SKARBOWY W KOŁOBRZEGU
    :cvar VALUE_3210: PIERWSZY URZĄD SKARBOWY W KOSZALINIE
    :cvar VALUE_3211: DRUGI URZĄD SKARBOWY W KOSZALINIE
    :cvar VALUE_3212: URZĄD SKARBOWY W MYŚLIBORZU
    :cvar VALUE_3213: URZĄD SKARBOWY W PYRZYCACH
    :cvar VALUE_3214: URZĄD SKARBOWY W STARGARDZIE
    :cvar VALUE_3215: PIERWSZY URZĄD SKARBOWY W SZCZECINIE
    :cvar VALUE_3216: DRUGI URZĄD SKARBOWY W SZCZECINIE
    :cvar VALUE_3217: TRZECI URZĄD SKARBOWY W SZCZECINIE
    :cvar VALUE_3218: URZĄD SKARBOWY W SZCZECINKU
    :cvar VALUE_3219: URZĄD SKARBOWY W ŚWINOUJŚCIU
    :cvar VALUE_3220: URZĄD SKARBOWY W WAŁCZU
    :cvar VALUE_3271: ZACHODNIOPOMORSKI URZĄD SKARBOWY W SZCZECINIE
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

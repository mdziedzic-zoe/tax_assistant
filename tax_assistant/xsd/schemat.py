from dataclasses import dataclass, field
from decimal import Decimal
from enum import Enum
from typing import Optional

from xsdata.models.datatype import XmlDate

from pkg_2022.pkg_01.pkg_05.e_d.kody_urzedow_skarbowych.kody_urzedow_skarbowych_v8_0_e import (
    TkodUs,
)
from pkg_2022.pkg_09.pkg_13.e_d.definicje_typy.struktury_danych_v12_0_e import (
    TcelZlozenia,
    Twybor12,
)
from pkg_2022.pkg_09.pkg_13.e_d.ordzu.ord_zu_3_v10_0_e import (
    ZalacznikOrdZu,
)
from pkg_2023.pkg_09.pkg_06.e_d.kody_krajow.kody_krajow_v13_0_e import (
    TkodKraju,
)

__NAMESPACE__ = "http://crd.gov.pl/wzor/2023/12/13/13064/"


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


@dataclass
class TidentyfikatorOsobyFizycznej:
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
    imie_pierwsze: Optional[str] = field(
        default=None,
        metadata={
            "name": "ImiePierwsze",
            "type": "Element",
            "namespace": "http://crd.gov.pl/wzor/2023/12/13/13064/",
            "required": True,
            "min_length": 1,
            "max_length": 30,
        },
    )
    nazwisko: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nazwisko",
            "type": "Element",
            "namespace": "http://crd.gov.pl/wzor/2023/12/13/13064/",
            "required": True,
            "min_length": 1,
            "max_length": 81,
        },
    )
    data_urodzenia: Optional[str] = field(
        default=None,
        metadata={
            "name": "DataUrodzenia",
            "type": "Element",
            "namespace": "http://crd.gov.pl/wzor/2023/12/13/13064/",
            "required": True,
            "min_inclusive": "1900-01-01",
            "max_inclusive": "2050-12-31",
            "pattern": r"((\d{4})-(\d{2})-(\d{2}))",
        },
    )


@dataclass
class TidentyfikatorOsobyNiefizycznej:
    """
    Skrócony zestaw danych identyfikacyjnych o osobie niefizycznej.

    :ivar nip: Identyfikator podatkowy NIP
    :ivar pelna_nazwa: Nazwa pełna
    :ivar skrocona_nazwa: Nazwa skrócona
    """

    class Meta:
        name = "TIdentyfikatorOsobyNiefizycznej"

    nip: Optional[str] = field(
        default=None,
        metadata={
            "name": "NIP",
            "type": "Element",
            "namespace": "http://crd.gov.pl/wzor/2023/12/13/13064/",
            "required": True,
            "pattern": r"[1-9]((\d[1-9])|([1-9]\d))\d{7}",
        },
    )
    pelna_nazwa: Optional[str] = field(
        default=None,
        metadata={
            "name": "PelnaNazwa",
            "type": "Element",
            "namespace": "http://crd.gov.pl/wzor/2023/12/13/13064/",
            "required": True,
            "min_length": 1,
            "max_length": 240,
        },
    )
    skrocona_nazwa: Optional[str] = field(
        default=None,
        metadata={
            "name": "SkroconaNazwa",
            "type": "Element",
            "namespace": "http://crd.gov.pl/wzor/2023/12/13/13064/",
            "required": True,
            "min_length": 1,
            "max_length": 70,
        },
    )


class TkodFormularza(Enum):
    """
    Symbol wzoru formularza.
    """

    PCC_3 = "PCC-3"


class TnaglowekWariantFormularza(Enum):
    VALUE_6 = 6


@dataclass
class TadresPolski:
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

    kod_kraju: Optional[TadresPolskiKodKraju] = field(
        default=None,
        metadata={
            "name": "KodKraju",
            "type": "Element",
            "namespace": "http://crd.gov.pl/wzor/2023/12/13/13064/",
            "required": True,
        },
    )
    wojewodztwo: Optional[str] = field(
        default=None,
        metadata={
            "name": "Wojewodztwo",
            "type": "Element",
            "namespace": "http://crd.gov.pl/wzor/2023/12/13/13064/",
            "required": True,
            "min_length": 1,
            "max_length": 36,
        },
    )
    powiat: Optional[str] = field(
        default=None,
        metadata={
            "name": "Powiat",
            "type": "Element",
            "namespace": "http://crd.gov.pl/wzor/2023/12/13/13064/",
            "required": True,
            "min_length": 1,
            "max_length": 36,
        },
    )
    gmina: Optional[str] = field(
        default=None,
        metadata={
            "name": "Gmina",
            "type": "Element",
            "namespace": "http://crd.gov.pl/wzor/2023/12/13/13064/",
            "required": True,
            "min_length": 1,
            "max_length": 36,
        },
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
            "required": True,
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
    miejscowosc: Optional[str] = field(
        default=None,
        metadata={
            "name": "Miejscowosc",
            "type": "Element",
            "namespace": "http://crd.gov.pl/wzor/2023/12/13/13064/",
            "required": True,
            "min_length": 1,
            "max_length": 56,
        },
    )
    kod_pocztowy: Optional[str] = field(
        default=None,
        metadata={
            "name": "KodPocztowy",
            "type": "Element",
            "namespace": "http://crd.gov.pl/wzor/2023/12/13/13064/",
            "required": True,
            "min_length": 1,
            "max_length": 8,
        },
    )


@dataclass
class TadresZagraniczny:
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

    kod_kraju: Optional[TkodKraju] = field(
        default=None,
        metadata={
            "name": "KodKraju",
            "type": "Element",
            "namespace": "http://crd.gov.pl/wzor/2023/12/13/13064/",
            "required": True,
            "pattern": r"P[A-KM-Z]|[A-OQ-Z][A-Z]",
        },
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
    miejscowosc: Optional[str] = field(
        default=None,
        metadata={
            "name": "Miejscowosc",
            "type": "Element",
            "namespace": "http://crd.gov.pl/wzor/2023/12/13/13064/",
            "required": True,
            "min_length": 1,
            "max_length": 56,
        },
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


@dataclass
class Tnaglowek:
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

    kod_formularza: Optional["Tnaglowek.KodFormularza"] = field(
        default=None,
        metadata={
            "name": "KodFormularza",
            "type": "Element",
            "namespace": "http://crd.gov.pl/wzor/2023/12/13/13064/",
            "required": True,
        },
    )
    wariant_formularza: Optional[TnaglowekWariantFormularza] = field(
        default=None,
        metadata={
            "name": "WariantFormularza",
            "type": "Element",
            "namespace": "http://crd.gov.pl/wzor/2023/12/13/13064/",
            "required": True,
        },
    )
    cel_zlozenia: Optional["Tnaglowek.CelZlozenia"] = field(
        default=None,
        metadata={
            "name": "CelZlozenia",
            "type": "Element",
            "namespace": "http://crd.gov.pl/wzor/2023/12/13/13064/",
            "required": True,
        },
    )
    data: Optional["Tnaglowek.Data"] = field(
        default=None,
        metadata={
            "name": "Data",
            "type": "Element",
            "namespace": "http://crd.gov.pl/wzor/2023/12/13/13064/",
            "required": True,
        },
    )
    kod_urzedu: Optional[TkodUs] = field(
        default=None,
        metadata={
            "name": "KodUrzedu",
            "type": "Element",
            "namespace": "http://crd.gov.pl/wzor/2023/12/13/13064/",
            "required": True,
        },
    )

    @dataclass
    class KodFormularza:
        value: Optional[TkodFormularza] = field(
            default=None,
            metadata={
                "required": True,
            },
        )
        kod_systemowy: str = field(
            init=False,
            default="PCC-3 (6)",
            metadata={
                "name": "kodSystemowy",
                "type": "Attribute",
                "required": True,
            },
        )
        kod_podatku: str = field(
            init=False,
            default="PCC",
            metadata={
                "name": "kodPodatku",
                "type": "Attribute",
                "required": True,
            },
        )
        rodzaj_zobowiazania: str = field(
            init=False,
            default="Z",
            metadata={
                "name": "rodzajZobowiazania",
                "type": "Attribute",
                "required": True,
            },
        )
        wersja_schemy: str = field(
            init=False,
            default="1-0E",
            metadata={
                "name": "wersjaSchemy",
                "type": "Attribute",
                "required": True,
            },
        )

    @dataclass
    class CelZlozenia:
        value: Optional[TcelZlozenia] = field(
            default=None,
            metadata={
                "required": True,
            },
        )
        poz: str = field(
            init=False,
            default="P_6",
            metadata={
                "type": "Attribute",
                "required": True,
            },
        )

    @dataclass
    class Data:
        value: Optional[XmlDate] = field(
            default=None,
            metadata={
                "required": True,
                "min_inclusive": XmlDate(2024, 1, 1),
            },
        )
        poz: str = field(
            init=False,
            default="P_4",
            metadata={
                "type": "Attribute",
                "required": True,
            },
        )


@dataclass
class Tadres:
    """
    Dane określające adres.
    """

    class Meta:
        name = "TAdres"

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


@dataclass
class Deklaracja:
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

    naglowek: Optional[Tnaglowek] = field(
        default=None,
        metadata={
            "name": "Naglowek",
            "type": "Element",
            "required": True,
        },
    )
    podmiot1: Optional["Deklaracja.Podmiot1"] = field(
        default=None,
        metadata={
            "name": "Podmiot1",
            "type": "Element",
            "required": True,
        },
    )
    pozycje_szczegolowe: Optional["Deklaracja.PozycjeSzczegolowe"] = field(
        default=None,
        metadata={
            "name": "PozycjeSzczegolowe",
            "type": "Element",
            "required": True,
        },
    )
    pouczenia: Optional[Decimal] = field(
        default=None,
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
        },
    )
    zalaczniki: Optional["Deklaracja.Zalaczniki"] = field(
        default=None,
        metadata={
            "name": "Zalaczniki",
            "type": "Element",
        },
    )

    @dataclass
    class Podmiot1:
        """
        :ivar osoba_fizyczna:
        :ivar osoba_niefizyczna:
        :ivar adres_zamieszkania_siedziby: Adres siedziby / Aktualny
            adres zamieszkania
        :ivar rola:
        """

        osoba_fizyczna: Optional["Deklaracja.Podmiot1.OsobaFizyczna"] = field(
            default=None,
            metadata={
                "name": "OsobaFizyczna",
                "type": "Element",
            },
        )
        osoba_niefizyczna: Optional[TidentyfikatorOsobyNiefizycznej] = field(
            default=None,
            metadata={
                "name": "OsobaNiefizyczna",
                "type": "Element",
            },
        )
        adres_zamieszkania_siedziby: Optional[
            "Deklaracja.Podmiot1.AdresZamieszkaniaSiedziby"
        ] = field(
            default=None,
            metadata={
                "name": "AdresZamieszkaniaSiedziby",
                "type": "Element",
                "required": True,
            },
        )
        rola: str = field(
            init=False,
            default="Podatnik",
            metadata={
                "type": "Attribute",
                "required": True,
            },
        )

        @dataclass
        class AdresZamieszkaniaSiedziby(Tadres):
            rodzaj_adresu: str = field(
                init=False,
                default="RAD",
                metadata={
                    "name": "rodzajAdresu",
                    "type": "Attribute",
                    "required": True,
                },
            )

        @dataclass
        class OsobaFizyczna(TidentyfikatorOsobyFizycznej):
            """
            :ivar imie_ojca: Imię ojca
            :ivar imie_matki: Imię matki
            """

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

    @dataclass
    class PozycjeSzczegolowe:
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

        p_7: Optional[PozycjeSzczegoloweP7] = field(
            default=None,
            metadata={
                "name": "P_7",
                "type": "Element",
                "required": True,
            },
        )
        p_20: Optional[PozycjeSzczegoloweP20] = field(
            default=None,
            metadata={
                "name": "P_20",
                "type": "Element",
                "required": True,
            },
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
        p_23: Optional[str] = field(
            default=None,
            metadata={
                "name": "P_23",
                "type": "Element",
                "required": True,
                "min_length": 1,
                "max_length": 3500,
            },
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
        p_53: Optional[int] = field(
            default=None,
            metadata={
                "name": "P_53",
                "type": "Element",
                "required": True,
                "min_inclusive": 0,
                "total_digits": 14,
            },
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

    @dataclass
    class Zalaczniki:
        zalacznik_ord_zu: Optional[ZalacznikOrdZu] = field(
            default=None,
            metadata={
                "name": "Zalacznik_ORD-ZU",
                "type": "Element",
                "namespace": "http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2022/09/13/eD/ORDZU/",
                "required": True,
            },
        )

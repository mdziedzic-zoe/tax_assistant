from dataclasses import dataclass, field
from enum import Enum
from typing import Optional

__NAMESPACE__ = "http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2022/09/13/eD/DefinicjeTypy/"


class TcelZlozenia(Enum):
    """
    Określa, czy to jest złożenie, czy korekta dokumentu.

    :cvar VALUE_1: złożenie po raz pierwszy deklaracji za dany okres
    :cvar VALUE_2: korekta deklaracji za dany okres
    """

    VALUE_1 = 1
    VALUE_2 = 2


@dataclass
class TidentyfikatorOsobyFizycznej:
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

    nip: Optional[str] = field(
        default=None,
        metadata={
            "name": "NIP",
            "type": "Element",
            "namespace": "http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2022/09/13/eD/DefinicjeTypy/",
            "required": True,
            "pattern": r"[1-9]((\d[1-9])|([1-9]\d))\d{7}",
        },
    )
    imie_pierwsze: Optional[str] = field(
        default=None,
        metadata={
            "name": "ImiePierwsze",
            "type": "Element",
            "namespace": "http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2022/09/13/eD/DefinicjeTypy/",
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
            "namespace": "http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2022/09/13/eD/DefinicjeTypy/",
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
            "namespace": "http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2022/09/13/eD/DefinicjeTypy/",
            "required": True,
            "min_inclusive": "1900-01-01",
            "max_inclusive": "2050-12-31",
            "pattern": r"((\d{4})-(\d{2})-(\d{2}))",
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


@dataclass
class TidentyfikatorOsobyFizycznej1:
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
    imie_pierwsze: Optional[str] = field(
        default=None,
        metadata={
            "name": "ImiePierwsze",
            "type": "Element",
            "namespace": "http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2022/09/13/eD/DefinicjeTypy/",
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
            "namespace": "http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2022/09/13/eD/DefinicjeTypy/",
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
            "namespace": "http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2022/09/13/eD/DefinicjeTypy/",
            "required": True,
            "min_inclusive": "1900-01-01",
            "max_inclusive": "2050-12-31",
            "pattern": r"((\d{4})-(\d{2})-(\d{2}))",
        },
    )


@dataclass
class TidentyfikatorOsobyFizycznej2:
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

    nip: Optional[str] = field(
        default=None,
        metadata={
            "name": "NIP",
            "type": "Element",
            "namespace": "http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2022/09/13/eD/DefinicjeTypy/",
            "required": True,
            "pattern": r"[1-9]((\d[1-9])|([1-9]\d))\d{7}",
        },
    )
    imie_pierwsze: Optional[str] = field(
        default=None,
        metadata={
            "name": "ImiePierwsze",
            "type": "Element",
            "namespace": "http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2022/09/13/eD/DefinicjeTypy/",
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
            "namespace": "http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2022/09/13/eD/DefinicjeTypy/",
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
            "namespace": "http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2022/09/13/eD/DefinicjeTypy/",
            "required": True,
            "min_inclusive": "1900-01-01",
            "max_inclusive": "2050-12-31",
            "pattern": r"((\d{4})-(\d{2})-(\d{2}))",
        },
    )


@dataclass
class TidentyfikatorOsobyFizycznejPelny:
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

    nip: Optional[str] = field(
        default=None,
        metadata={
            "name": "NIP",
            "type": "Element",
            "namespace": "http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2022/09/13/eD/DefinicjeTypy/",
            "pattern": r"[1-9]((\d[1-9])|([1-9]\d))\d{7}",
        },
    )
    imie_pierwsze: Optional[str] = field(
        default=None,
        metadata={
            "name": "ImiePierwsze",
            "type": "Element",
            "namespace": "http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2022/09/13/eD/DefinicjeTypy/",
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
            "namespace": "http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2022/09/13/eD/DefinicjeTypy/",
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
            "namespace": "http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2022/09/13/eD/DefinicjeTypy/",
            "required": True,
            "min_inclusive": "1900-01-01",
            "max_inclusive": "2050-12-31",
            "pattern": r"((\d{4})-(\d{2})-(\d{2}))",
        },
    )
    imie_ojca: Optional[str] = field(
        default=None,
        metadata={
            "name": "ImieOjca",
            "type": "Element",
            "namespace": "http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2022/09/13/eD/DefinicjeTypy/",
            "required": True,
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
            "required": True,
            "min_length": 1,
            "max_length": 30,
        },
    )
    pesel: Optional[str] = field(
        default=None,
        metadata={
            "name": "PESEL",
            "type": "Element",
            "namespace": "http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2022/09/13/eD/DefinicjeTypy/",
            "required": True,
            "pattern": r"\d{11}",
        },
    )


@dataclass
class TidentyfikatorOsobyFizycznejZagranicznej:
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

    imie_pierwsze: Optional[str] = field(
        default=None,
        metadata={
            "name": "ImiePierwsze",
            "type": "Element",
            "namespace": "http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2022/09/13/eD/DefinicjeTypy/",
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
            "namespace": "http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2022/09/13/eD/DefinicjeTypy/",
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
            "namespace": "http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2022/09/13/eD/DefinicjeTypy/",
            "required": True,
            "min_inclusive": "1900-01-01",
            "max_inclusive": "2050-12-31",
            "pattern": r"((\d{4})-(\d{2})-(\d{2}))",
        },
    )
    miejsce_urodzenia: Optional[str] = field(
        default=None,
        metadata={
            "name": "MiejsceUrodzenia",
            "type": "Element",
            "namespace": "http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2022/09/13/eD/DefinicjeTypy/",
            "required": True,
            "min_length": 1,
            "max_length": 56,
        },
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


@dataclass
class TidentyfikatorOsobyNiefizycznej:
    """
    Podstawowy zestaw danych identyfikacyjnych o osobie niefizycznej.

    :ivar nip: Identyfikator podatkowy NIP
    :ivar pelna_nazwa: Pełna nazwa
    :ivar regon: Numer REGON
    """

    class Meta:
        name = "TIdentyfikatorOsobyNiefizycznej"

    nip: Optional[str] = field(
        default=None,
        metadata={
            "name": "NIP",
            "type": "Element",
            "namespace": "http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2022/09/13/eD/DefinicjeTypy/",
            "required": True,
            "pattern": r"[1-9]((\d[1-9])|([1-9]\d))\d{7}",
        },
    )
    pelna_nazwa: Optional[str] = field(
        default=None,
        metadata={
            "name": "PelnaNazwa",
            "type": "Element",
            "namespace": "http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2022/09/13/eD/DefinicjeTypy/",
            "required": True,
            "min_length": 1,
            "max_length": 240,
        },
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


@dataclass
class TidentyfikatorOsobyNiefizycznej1:
    """Podstawowy zestaw danych identyfikacyjnych o osobie niefizycznej  - bez elementu Numer REGON

    :ivar nip: Identyfikator podatkowy NIP
    :ivar pelna_nazwa: Pełna nazwa
    """

    class Meta:
        name = "TIdentyfikatorOsobyNiefizycznej1"

    nip: Optional[str] = field(
        default=None,
        metadata={
            "name": "NIP",
            "type": "Element",
            "namespace": "http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2022/09/13/eD/DefinicjeTypy/",
            "required": True,
            "pattern": r"[1-9]((\d[1-9])|([1-9]\d))\d{7}",
        },
    )
    pelna_nazwa: Optional[str] = field(
        default=None,
        metadata={
            "name": "PelnaNazwa",
            "type": "Element",
            "namespace": "http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2022/09/13/eD/DefinicjeTypy/",
            "required": True,
            "min_length": 1,
            "max_length": 240,
        },
    )


@dataclass
class TidentyfikatorOsobyNiefizycznejPelny:
    """
    Pełny zestaw danych identyfikacyjnych o osobie niefizycznej.

    :ivar nip: Identyfikator podatkowy NIP
    :ivar pelna_nazwa: Pełna nazwa
    :ivar skrocona_nazwa: Skrócona nazwa
    :ivar regon: Numer REGON
    """

    class Meta:
        name = "TIdentyfikatorOsobyNiefizycznejPelny"

    nip: Optional[str] = field(
        default=None,
        metadata={
            "name": "NIP",
            "type": "Element",
            "namespace": "http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2022/09/13/eD/DefinicjeTypy/",
            "pattern": r"[1-9]((\d[1-9])|([1-9]\d))\d{7}",
        },
    )
    pelna_nazwa: Optional[str] = field(
        default=None,
        metadata={
            "name": "PelnaNazwa",
            "type": "Element",
            "namespace": "http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2022/09/13/eD/DefinicjeTypy/",
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
            "namespace": "http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2022/09/13/eD/DefinicjeTypy/",
            "required": True,
            "min_length": 1,
            "max_length": 70,
        },
    )
    regon: Optional[str] = field(
        default=None,
        metadata={
            "name": "REGON",
            "type": "Element",
            "namespace": "http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2022/09/13/eD/DefinicjeTypy/",
            "required": True,
            "pattern": r"\d{14}",
        },
    )


@dataclass
class TidentyfikatorOsobyNiefizycznejZagranicznej:
    """
    Zestaw danych identyfikacyjnych dla osoby niefizycznej zagranicznej.

    :ivar pelna_nazwa: Pełna nazwa [Name]
    :ivar skrocona_nazwa: Nazwa skrócona [Short Name]
    :ivar nip: Identyfikator podatkowy NIP [Tax Identification Number
        (NIP)]
    """

    class Meta:
        name = "TIdentyfikatorOsobyNiefizycznejZagranicznej"

    pelna_nazwa: Optional[str] = field(
        default=None,
        metadata={
            "name": "PelnaNazwa",
            "type": "Element",
            "namespace": "http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2022/09/13/eD/DefinicjeTypy/",
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


class Twybor12(Enum):
    """
    Podwójne pole wyboru.
    """

    VALUE_1 = 1
    VALUE_2 = 2


@dataclass
class TpodmiotDowolnyBezAdresu:
    """
    Skrócony zestaw danych o osobie fizycznej lub niefizycznej.
    """

    class Meta:
        name = "TPodmiotDowolnyBezAdresu"

    osoba_fizyczna: Optional[TidentyfikatorOsobyFizycznej] = field(
        default=None,
        metadata={
            "name": "OsobaFizyczna",
            "type": "Element",
            "namespace": "http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2022/09/13/eD/DefinicjeTypy/",
        },
    )
    osoba_niefizyczna: Optional[TidentyfikatorOsobyNiefizycznej] = field(
        default=None,
        metadata={
            "name": "OsobaNiefizyczna",
            "type": "Element",
            "namespace": "http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2022/09/13/eD/DefinicjeTypy/",
        },
    )


@dataclass
class TpodmiotDowolnyBezAdresu1:
    """
    Skrócony zestaw danych o osobie fizycznej lub niefizycznej z identyfikatorem
    NIP albo PESEL.
    """

    class Meta:
        name = "TPodmiotDowolnyBezAdresu1"

    osoba_fizyczna: Optional[TidentyfikatorOsobyFizycznej1] = field(
        default=None,
        metadata={
            "name": "OsobaFizyczna",
            "type": "Element",
            "namespace": "http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2022/09/13/eD/DefinicjeTypy/",
        },
    )
    osoba_niefizyczna: Optional[TidentyfikatorOsobyNiefizycznej] = field(
        default=None,
        metadata={
            "name": "OsobaNiefizyczna",
            "type": "Element",
            "namespace": "http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2022/09/13/eD/DefinicjeTypy/",
        },
    )


@dataclass
class TpodmiotDowolnyBezAdresu2:
    """
    Skrócony zestaw danych o osobie fizycznej lub niefizycznej z identyfikatorem
    NIP.
    """

    class Meta:
        name = "TPodmiotDowolnyBezAdresu2"

    osoba_fizyczna: Optional[TidentyfikatorOsobyFizycznej2] = field(
        default=None,
        metadata={
            "name": "OsobaFizyczna",
            "type": "Element",
            "namespace": "http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2022/09/13/eD/DefinicjeTypy/",
        },
    )
    osoba_niefizyczna: Optional[TidentyfikatorOsobyNiefizycznej] = field(
        default=None,
        metadata={
            "name": "OsobaNiefizyczna",
            "type": "Element",
            "namespace": "http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2022/09/13/eD/DefinicjeTypy/",
        },
    )


@dataclass
class TpodmiotDowolnyBezAdresu3:
    """Skrócony zestaw danych o osobie fizycznej lub niefizycznej z identyfikatorem NIP - bez elementu numer REGON dla osoby niefizycznej"""

    class Meta:
        name = "TPodmiotDowolnyBezAdresu3"

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

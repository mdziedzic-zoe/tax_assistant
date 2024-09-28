from dataclasses import dataclass, field
from enum import Enum
from typing import Optional

__NAMESPACE__ = (
    "http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2022/09/13/eD/ORDZU/"
)


class TkodFormularzaZu(Enum):
    """
    Symbol wzoru formularza.
    """

    ORD_ZU = "ORD-ZU"


class TnaglowekOrdZuWariantFormularza(Enum):
    VALUE_3 = 3


@dataclass
class TnaglowekOrdZu:
    """
    Nagłówek deklaracji.
    """

    class Meta:
        name = "TNaglowek_ORD-ZU"

    kod_formularza: Optional["TnaglowekOrdZu.KodFormularza"] = field(
        default=None,
        metadata={
            "name": "KodFormularza",
            "type": "Element",
            "namespace": "http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2022/09/13/eD/ORDZU/",
            "required": True,
        },
    )
    wariant_formularza: Optional[TnaglowekOrdZuWariantFormularza] = field(
        default=None,
        metadata={
            "name": "WariantFormularza",
            "type": "Element",
            "namespace": "http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2022/09/13/eD/ORDZU/",
            "required": True,
        },
    )

    @dataclass
    class KodFormularza:
        value: Optional[TkodFormularzaZu] = field(
            default=None,
            metadata={
                "required": True,
            },
        )
        kod_systemowy: str = field(
            init=False,
            default="ORD-ZU (3)",
            metadata={
                "name": "kodSystemowy",
                "type": "Attribute",
                "required": True,
            },
        )
        wersja_schemy: str = field(
            init=False,
            default="10-0E",
            metadata={
                "name": "wersjaSchemy",
                "type": "Attribute",
                "required": True,
            },
        )


@dataclass
class ZalacznikOrdZu:
    """
    UZASADNIENIE PRZYCZYN KOREKTY DEKLARACJI.
    """

    class Meta:
        name = "Zalacznik_ORD-ZU"
        namespace = "http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2022/09/13/eD/ORDZU/"

    naglowek: Optional[TnaglowekOrdZu] = field(
        default=None,
        metadata={
            "name": "Naglowek",
            "type": "Element",
            "required": True,
        },
    )
    pozycje_szczegolowe: Optional["ZalacznikOrdZu.PozycjeSzczegolowe"] = field(
        default=None,
        metadata={
            "name": "PozycjeSzczegolowe",
            "type": "Element",
            "required": True,
        },
    )

    @dataclass
    class PozycjeSzczegolowe:
        """
        :ivar p_13: Treść uzasadnienia
        """

        p_13: Optional[str] = field(
            default=None,
            metadata={
                "name": "P_13",
                "type": "Element",
                "required": True,
                "min_length": 1,
                "max_length": 2000,
            },
        )

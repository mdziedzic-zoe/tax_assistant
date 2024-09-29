from types import UnionType

from pydantic import BaseModel, Field, constr, validator, ConfigDict
from typing import Optional, Any, Dict, Annotated, Literal, get_origin, get_args
from datetime import date
from enum import Enum
import re

from tax_assistant.models.gminy import Municipality, Voivodeship, County
from tax_assistant.models.partial_taxform import TaxOffice


class OptionalModel(BaseModel):
    model_config = ConfigDict(arbitrary_types_allowed=True)

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)

        for field_name, field in cls.model_fields.items():
            if field.annotation is not None:
                # Check if the field is already Optional
                if get_origin(field.annotation) is UnionType and type(None) in get_args(field.annotation):
                    continue

                # Make the field optional
                field.annotation = Annotated[field.annotation | None, field.annotation]
                field.default = None


def form_field(form_field_number: str):
    def decorator(field: Field):
        field.json_schema_extra = {"form_field_number": form_field_number}
        return field

    return decorator


class CelZlozenia(Enum):
    ZLOZENIE = "ZLOZENIE"
    KOREKTA = "KOREKTA"


class PodmiotSkladajacy(Enum):
    PODMIOT_ZOBOWIAZANY = "PODMIOT_ZOBOWIAZANY"
    STRONA_UMOWY_ZAMIANY = "STRONA_UMOWY_ZAMIANY"
    WSPOLNIK_SPOLKI_CYWILNEJ = "WSPOLNIK_SPOLKI_CYWILNEJ"
    POZYCZKOBIORCA = "POZYCZKOBIORCA"
    INNY_PODMIOT = "INNY_PODMIOT"


class PrzedmiotOpodatkowania(Enum):
    UMOWA = "UMOWA"
    ZMIANA_UMOWY = "ZMIANA_UMOWY"
    ORZECZENIE_SADU_LUB_UGODA = "ORZECZENIE_SADU_LUB_UGODA"
    INNE = "INNE"


class MiejscePolozenia(Enum):
    TERYTORIUM_RP = "TERYTORIUM_RP"
    POZA_TERYTORIUM_RP = "POZA_TERYTORIUM_RP"


class TypSpolki(Enum):
    OSOBOWA = "OSOBOWA"
    KAPITALOWA = "KAPITALOWA"


class PodstawaOpodatkowania(Enum):
    ZAWARCIE_UMOWY_SPOLKI = "ZAWARCIE_UMOWY_SPOLKI"
    ZWIEKSZENIE_MAJATKU_SPOLKI = "ZWIEKSZENIE_MAJATKU_SPOLKI"
    DOPLATA = "DOPLATA"
    POZYCZKA_UDZIELONA_SPOLCE = "POZYCZKA_UDZIELONA_SPOLCE"
    ODDANIE_RZECZY_DO_UZYWANIA = "ODDANIE_RZECZY_DO_UZYWANIA"
    PRZEKSZTALCENIE_SPOLEK = "PRZEKSZTALCENIE_SPOLEK"
    LACZENIE_SPOLEK = "LACZENIE_SPOLEK"
    PRZENIESIENIE_SIEDZIBY = "PRZENIESIENIE_SIEDZIBY"


class SectionA(OptionalModel):
    """Sekcja A: Nagłówek deklaracji"""
    kod_formularza: Literal["PCC-3"] = "PCC-3"
    wariant_formularza: Literal[6] = 6
    cel_zlozenia: Annotated[CelZlozenia, form_field("P_6")]
    data_dokonania_czynnosci: Annotated[date, form_field("P_4")]
    nazwa_urzedu: Annotated[TaxOffice, form_field("P_5")]
    is_complete: Optional[bool]

    @validator('data_dokonania_czynnosci')
    def validate_date(cls, v):
        if v < date(2024, 1, 1):
            raise ValueError('Data musi być nie wcześniejsza niż 1 stycznia 2024')
        return v


class Adres(OptionalModel):
    kod_kraju: Literal["POLSKA"] = "POLSKA"
    wojewodztwo: Annotated[Optional[Voivodeship], form_field("P_9")] = Field(None, min_length=1, max_length=36)
    powiat: Annotated[Optional[County], form_field("P_10")] = Field(None, min_length=1, max_length=36)
    gmina: Annotated[Optional[Municipality], form_field("P_11")] = Field(None, min_length=1, max_length=36)
    ulica: Annotated[Optional[str], form_field("P_12")] = Field(None, min_length=1, max_length=65)
    nr_domu: Annotated[str, form_field("P_13")] = Field(..., min_length=1, max_length=9)
    nr_lokalu: Annotated[Optional[str], form_field("P_14")] = Field(None, min_length=1, max_length=10)
    miejscowosc: Annotated[str, form_field("P_15")] = Field(..., min_length=1, max_length=56)
    kod_pocztowy: Annotated[Optional[str], form_field("P_16")] = None

    @validator('kod_pocztowy')
    def validate_kod_pocztowy(cls, v):
        if v is not None and not re.match(r'^\d{2}-\d{3}$', v):
            raise ValueError('Nieprawidłowy format kodu pocztowego')
        return v


class OsobaFizyczna(OptionalModel):
    nip: Annotated[Optional[str], form_field("P_17")] = None
    pesel: Annotated[Optional[str], form_field("P_18")] = None
    imie_pierwsze: Annotated[str, form_field("P_19")] = Field(..., min_length=1, max_length=30)
    nazwisko: Annotated[str, form_field("P_20")] = Field(..., min_length=1, max_length=81)
    data_urodzenia: Annotated[date, form_field("P_21")]
    imie_ojca: Annotated[Optional[str], form_field("P_22")] = Field(None, min_length=1, max_length=30)
    imie_matki: Annotated[Optional[str], form_field("P_23")] = Field(None, min_length=1, max_length=30)

    @validator('nip')
    def validate_nip(cls, v):
        if v is not None and not re.match(r'^\d{10}$', v):
            raise ValueError('Nieprawidłowy format NIP')
        return v

    @validator('pesel')
    def validate_pesel(cls, v):
        if v is not None and not re.match(r'^\d{11}$', v):
            raise ValueError('Nieprawidłowy format PESEL')
        return v


class OsobaNiefizyczna(OptionalModel):
    nip: Annotated[str, form_field("P_24")]
    pelna_nazwa: Annotated[str, form_field("P_25")] = Field(..., min_length=1, max_length=240)
    skrocona_nazwa: Annotated[str, form_field("P_26")] = Field(..., min_length=1, max_length=70)

    @validator('nip')
    def validate_nip(cls, v):
        if not re.match(r'^\d{10}$', v):
            raise ValueError('Nieprawidłowy format NIP')
        return v


class SectionB(OptionalModel):
    """Sekcja B: Dane podatnika"""
    osoba_fizyczna: Optional[OsobaFizyczna] = None
    osoba_niefizyczna: Optional[OsobaNiefizyczna] = None
    adres_zamieszkania_siedziby: Adres
    podmiot_skladajacy: Annotated[PodmiotSkladajacy, form_field("P_7")]
    is_complete: Optional[bool]


class SectionC(OptionalModel):
    """Sekcja C: Przedmiot opodatkowania i treść czynności cywilnoprawnej"""
    przedmiot_opodatkowania: Annotated[PrzedmiotOpodatkowania, form_field("P_20")]
    miejsce_polozenia: Annotated[Optional[MiejscePolozenia], form_field("P_21")] = None
    miejsce_dokonania_czynnosci: Annotated[Optional[MiejscePolozenia], form_field("P_22")] = None
    tresc_czynnosci: Annotated[constr(max_length=2000), form_field("P_23")]
    is_complete: Optional[bool]


class SectionD(OptionalModel):
    """Sekcja D: Obliczenie należnego podatku od czynności cywilnoprawnych, z wyjątkiem umowy spółki lub jej zmiany"""
    podstawa_opodatkowania: Annotated[Optional[int], form_field("P_26")] = Field(None, ge=0)
    kwota_podatku: Annotated[Optional[int], form_field("P_27")] = Field(None, ge=0)
    kwota_podatku_naleznego: Annotated[Optional[int], form_field("P_46")] = Field(None, ge=0)
    is_complete: Optional[bool]


class SectionE(OptionalModel):
    """Sekcja E: Obliczenie należnego podatku od umowy spółki / zmiany umowy spółki"""
    typ_spolki: Annotated[Optional[TypSpolki], form_field("P_47")] = None
    podstawa_opodatkowania: Annotated[Optional[PodstawaOpodatkowania], form_field("P_48")] = None
    kwota_podstawy_opodatkowania: Annotated[Optional[int], form_field("P_49")] = Field(None, ge=0)
    koszty: Annotated[Optional[float], form_field("P_50")] = Field(None, ge=0)
    podstawa_obliczenia_podatku: Annotated[Optional[float], form_field("P_51")] = Field(None, ge=0)
    kwota_podatku: Annotated[Optional[int], form_field("P_52")] = Field(None, ge=0)
    is_complete: Optional[bool]


class SectionF(OptionalModel):
    """Sekcja F: Podatek do zapłaty"""
    kwota_podatku_do_zaplaty: Annotated[int, form_field("P_53")] = Field(..., ge=0)
    is_complete: Optional[bool]


class SectionG(OptionalModel):
    """Sekcja G: Informacje dodatkowe"""
    wojewodztwo: Annotated[Optional[str], form_field("P_54")] = Field(None, min_length=1, max_length=36)
    powiat: Annotated[Optional[str], form_field("P_55")] = Field(None, min_length=1, max_length=36)
    gmina: Annotated[Optional[str], form_field("P_56")] = Field(None, min_length=1, max_length=36)
    ulica: Annotated[Optional[str], form_field("P_57")] = Field(None, min_length=1, max_length=65)
    nr_domu: Annotated[Optional[str], form_field("P_58")] = Field(None, min_length=1, max_length=9)
    nr_lokalu: Annotated[Optional[str], form_field("P_59")] = Field(None, min_length=1, max_length=10)
    miejscowosc: Annotated[Optional[str], form_field("P_60")] = Field(None, min_length=1, max_length=56)
    kod_pocztowy: Annotated[Optional[str], form_field("P_61")] = None
    is_complete: Optional[bool]

    @validator('kod_pocztowy')
    def validate_kod_pocztowy(cls, v):
        if v is not None and not re.match(r'^\d{2}-\d{3}$', v):
            raise ValueError('Nieprawidłowy format kodu pocztowego')
        return v


class SectionH(OptionalModel):
    """Sekcja H: Informacja o załącznikach"""
    liczba_zalacznikow: Annotated[Optional[int], form_field("P_62")] = Field(None, ge=0)
    is_complete: Optional[bool]


class Deklaracja(OptionalModel):
    sekcja_a: SectionA
    sekcja_b: SectionB
    sekcja_c: SectionC
    sekcja_d: SectionD
    sekcja_e: SectionE
    sekcja_f: SectionF
    sekcja_g: Optional[SectionG] = None
    sekcja_h: Optional[SectionH] = None
    pouczenia: int = Literal[1]


# Komentarz główny
"""
Ten model Pydantic reprezentuje strukturę deklaracji PCC-3 (Podatek od czynności cywilnoprawnych).
Model został podzielony na sekcje odpowiadające głównym częściom formularza:
A. Nagłówek deklaracji
B. Dane podatnika
C. Przedmiot opodatkowania i treść czynności cywilnoprawnej
D. Obliczenie należnego podatku od czynności cywilnoprawnych, z wyjątkiem umowy spółki lub jej zmiany
E. Obliczenie należnego podatku od umowy spółki / zmiany umowy spółki
F. Podatek do zapłaty
G. Informacje dodatkowe
H. Informacja o załącznikach

Każda sekcja jest reprezentowana przez osobną klasę, co ułatwia organizację i zrozumienie struktury formularza.
Dodatkowo, każde pole zawiera informację o numerze odpowiadającego mu pola w formularzu PCC-3.

Model zawiera również walidacje zgodne z regułami określonymi w schemacie XSD, 
w tym ograniczenia dotyczące długości pól tekstowych, formatów danych (np. NIP, PESEL, kod pocztowy) 
oraz zakresów wartości liczbowych.

Użyto dekoratora form_field do przechowywania numeru pola formularza dla każdego pola,
co jest zgodne z Pydantic v2 i pozwala na dodanie niestandardowych metadanych do pól.
"""

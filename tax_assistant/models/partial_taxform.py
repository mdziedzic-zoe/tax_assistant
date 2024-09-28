from types import UnionType

from pydantic import BaseModel, Field, constr, validator, ConfigDict
from typing import Optional, Any, Dict, Annotated, Literal, get_origin, get_args
from datetime import date
from enum import Enum
import re


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
    ZLOZENIE = 1
    KOREKTA = 2


class PodmiotSkladajacy(Enum):
    PODMIOT_ZOBOWIAZANY = 1
    STRONA_UMOWY_ZAMIANY = 2
    WSPOLNIK_SPOLKI_CYWILNEJ = 3
    POZYCZKOBIORCA = 4
    INNY_PODMIOT = 5


class PrzedmiotOpodatkowania(Enum):
    UMOWA = 1
    ZMIANA_UMOWY = 2
    ORZECZENIE_SADU_LUB_UGODA = 3
    INNE = 4


class MiejscePolozenia(Enum):
    TERYTORIUM_RP = 1
    POZA_TERYTORIUM_RP = 2


class TypSpolki(Enum):
    OSOBOWA = 1
    KAPITALOWA = 2


class PodstawaOpodatkowania(Enum):
    ZAWARCIE_UMOWY_SPOLKI = 1
    ZWIEKSZENIE_MAJATKU_SPOLKI = 2
    DOPLATA = 3
    POZYCZKA_UDZIELONA_SPOLCE = 4
    ODDANIE_RZECZY_DO_UZYWANIA = 5
    PRZEKSZTALCENIE_SPOLEK = 6
    LACZENIE_SPOLEK = 7
    PRZENIESIENIE_SIEDZIBY = 8


class PartialSectionA(OptionalModel):
    """Sekcja A: Nagłówek deklaracji"""
    kod_formularza: Optional[Literal["PCC-3"]] = "PCC-3"
    wariant_formularza: Optional[Literal[6]] = 6
    cel_zlozenia: Optional[Annotated[CelZlozenia, form_field("P_6")]] = None
    data_dokonania_czynnosci: Optional[Annotated[date, form_field("P_4")]] = None
    kod_urzedu: Optional[Annotated[str, form_field("P_5")]] = None

    @validator('data_dokonania_czynnosci')
    def validate_date(cls, v):
        if v and v < date(2024, 1, 1):
            raise ValueError('Data musi być nie wcześniejsza niż 1 stycznia 2024')
        return v


class PartialAdres(OptionalModel):
    kod_kraju: Optional[Annotated[str, form_field("P_8")]] = None
    wojewodztwo: Optional[Annotated[Optional[str], form_field("P_9")]] = Field(None, min_length=1, max_length=36)
    powiat: Optional[Annotated[Optional[str], form_field("P_10")]] = Field(None, min_length=1, max_length=36)
    gmina: Optional[Annotated[Optional[str], form_field("P_11")]] = Field(None, min_length=1, max_length=36)
    ulica: Optional[Annotated[Optional[str], form_field("P_12")]] = Field(None, min_length=1, max_length=65)
    nr_domu: Optional[Annotated[str, form_field("P_13")]] = Field(None, min_length=1, max_length=9)
    nr_lokalu: Optional[Annotated[Optional[str], form_field("P_14")]] = Field(None, min_length=1, max_length=10)
    miejscowosc: Optional[Annotated[str, form_field("P_15")]] = Field(None, min_length=1, max_length=56)
    kod_pocztowy: Optional[Annotated[Optional[str], form_field("P_16")]] = None

    @validator('kod_pocztowy')
    def validate_kod_pocztowy(cls, v):
        if v is not None and not re.match(r'^\d{2}-\d{3}$', v):
            raise ValueError('Nieprawidłowy format kodu pocztowego')
        return v


class PartialOsobaFizyczna(OptionalModel):
    nip: Optional[Annotated[Optional[str], form_field("P_17")]] = None
    pesel: Optional[Annotated[Optional[str], form_field("P_18")]] = None
    imie_pierwsze: Optional[Annotated[str, form_field("P_19")]] = Field(None, min_length=1, max_length=30)
    nazwisko: Optional[Annotated[str, form_field("P_20")]] = Field(None, min_length=1, max_length=81)
    data_urodzenia: Optional[Annotated[date, form_field("P_21")]] = None
    imie_ojca: Optional[Annotated[Optional[str], form_field("P_22")]] = Field(None, min_length=1, max_length=30)
    imie_matki: Optional[Annotated[Optional[str], form_field("P_23")]] = Field(None, min_length=1, max_length=30)

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


class PartialOsobaNiefizyczna(OptionalModel):
    nip: Optional[Annotated[str, form_field("P_24")]] = None
    pelna_nazwa: Optional[Annotated[str, form_field("P_25")]] = Field(None, min_length=1, max_length=240)
    skrocona_nazwa: Optional[Annotated[str, form_field("P_26")]] = Field(None, min_length=1, max_length=70)

    @validator('nip')
    def validate_nip(cls, v):
        if v is not None and not re.match(r'^\d{10}$', v):
            raise ValueError('Nieprawidłowy format NIP')
        return v


class PartialSectionB(OptionalModel):
    """Sekcja B: Dane podatnika"""
    osoba_fizyczna: Optional[PartialOsobaFizyczna] = None
    osoba_niefizyczna: Optional[PartialOsobaNiefizyczna] = None
    adres_zamieszkania_siedziby: Optional[PartialAdres] = None
    podmiot_skladajacy: Optional[Annotated[PodmiotSkladajacy, form_field("P_7")]] = None


class PartialSectionC(OptionalModel):
    """Sekcja C: Przedmiot opodatkowania i treść czynności cywilnoprawnej"""
    przedmiot_opodatkowania: Optional[Annotated[PrzedmiotOpodatkowania, form_field("P_20")]] = None
    miejsce_polozenia: Optional[Annotated[Optional[MiejscePolozenia], form_field("P_21")]] = None
    miejsce_dokonania_czynnosci: Optional[Annotated[Optional[MiejscePolozenia], form_field("P_22")]] = None
    tresc_czynnosci: Optional[Annotated[constr(max_length=2000), form_field("P_23")]] = None


class PartialSectionD(OptionalModel):
    """Sekcja D: Obliczenie należnego podatku od czynności cywilnoprawnych, z wyjątkiem umowy spółki lub jej zmiany"""
    podstawa_opodatkowania_1: Optional[Annotated[Optional[int], form_field("P_24")]] = Field(None, ge=0)
    kwota_podatku_1: Optional[Annotated[Optional[int], form_field("P_25")]] = Field(None, ge=0)
    podstawa_opodatkowania_2: Optional[Annotated[Optional[int], form_field("P_26")]] = Field(None, ge=0)
    kwota_podatku_2: Optional[Annotated[Optional[int], form_field("P_27")]] = Field(None, ge=0)
    podstawa_opodatkowania_zamiana: Optional[Annotated[Optional[int], form_field("P_28")]] = Field(None, ge=0)
    stawka_podatku_zamiana: Optional[Annotated[Optional[int], form_field("P_29")]] = Field(None, ge=0, le=100)
    kwota_podatku_zamiana: Optional[Annotated[Optional[int], form_field("P_30")]] = Field(None, ge=0)
    podstawa_opodatkowania_pozyczka: Optional[Annotated[Optional[int], form_field("P_31")]] = Field(None, ge=0)
    stawka_podatku_pozyczka: Optional[Annotated[Optional[float], form_field("P_32")]] = Field(None, ge=0, le=100)
    kwota_podatku_pozyczka: Optional[Annotated[Optional[int], form_field("P_33")]] = Field(None, ge=0)
    podstawa_opodatkowania_darowizna: Optional[Annotated[Optional[int], form_field("P_34")]] = Field(None, ge=0)
    stawka_podatku_darowizna: Optional[Annotated[Optional[int], form_field("P_35")]] = Field(None, ge=0, le=100)
    kwota_podatku_darowizna: Optional[Annotated[Optional[int], form_field("P_36")]] = Field(None, ge=0)
    podstawa_opodatkowania_uzytkowanie: Optional[Annotated[Optional[int], form_field("P_37")]] = Field(None, ge=0)
    stawka_podatku_uzytkowanie: Optional[Annotated[Optional[int], form_field("P_38")]] = Field(None, ge=0, le=100)
    kwota_podatku_uzytkowanie: Optional[Annotated[Optional[int], form_field("P_39")]] = Field(None, ge=0)
    podstawa_opodatkowania_hipoteka: Optional[Annotated[Optional[int], form_field("P_40")]] = Field(None, ge=0)
    kwota_podatku_hipoteka: Optional[Annotated[Optional[int], form_field("P_41")]] = Field(None, ge=0)
    kwota_podatku_hipoteka_nieustalona: Optional[Annotated[Optional[int], form_field("P_42")]] = Field(None, ge=0)
    rodzaj_czynnosci_innej: Optional[Annotated[Optional[str], form_field("P_43A")]] = None
    podstawa_opodatkowania_inna: Optional[Annotated[Optional[int], form_field("P_43")]] = Field(None, ge=0)
    stawka_podatku_inna: Optional[Annotated[Optional[int], form_field("P_44")]] = Field(None, ge=0, le=100)
    kwota_podatku_inna: Optional[Annotated[Optional[int], form_field("P_45")]] = Field(None, ge=0)
    kwota_podatku_naleznego: Optional[Annotated[Optional[int], form_field("P_46")]] = Field(None, ge=0)


class PartialSectionE(OptionalModel):
    """Sekcja E: Obliczenie należnego podatku od umowy spółki / zmiany umowy spółki"""
    typ_spolki: Optional[Annotated[Optional[TypSpolki], form_field("P_47")]] = None
    podstawa_opodatkowania: Optional[Annotated[Optional[PodstawaOpodatkowania], form_field("P_48")]] = None
    kwota_podstawy_opodatkowania: Optional[Annotated[Optional[int], form_field("P_49")]] = Field(None, ge=0)
    koszty: Optional[Annotated[Optional[float], form_field("P_50")]] = Field(None, ge=0)
    podstawa_obliczenia_podatku: Optional[Annotated[Optional[float], form_field("P_51")]] = Field(None, ge=0)
    kwota_podatku: Optional[Annotated[Optional[int], form_field("P_52")]] = Field(None, ge=0)


class PartialSectionF(OptionalModel):
    """Sekcja F: Podatek do zapłaty"""
    kwota_podatku_do_zaplaty: Optional[Annotated[int, form_field("P_53")]] = Field(None, ge=0)


class PartialSectionG(OptionalModel):
    """Sekcja G: Informacje dodatkowe"""
    wojewodztwo: Optional[Annotated[Optional[str], form_field("P_54")]] = Field(None, min_length=1, max_length=36)
    powiat: Optional[Annotated[Optional[str], form_field("P_55")]] = Field(None, min_length=1, max_length=36)
    gmina: Optional[Annotated[Optional[str], form_field("P_56")]] = Field(None, min_length=1, max_length=36)
    ulica: Optional[Annotated[Optional[str], form_field("P_57")]] = Field(None, min_length=1, max_length=65)
    nr_domu: Optional[Annotated[Optional[str], form_field("P_58")]] = Field(None, min_length=1, max_length=9)
    nr_lokalu: Optional[Annotated[Optional[str], form_field("P_59")]] = Field(None, min_length=1, max_length=10)
    miejscowosc: Optional[Annotated[Optional[str], form_field("P_60")]] = Field(None, min_length=1, max_length=56)
    kod_pocztowy: Optional[Annotated[Optional[str], form_field("P_61")]] = None

    @validator('kod_pocztowy')
    def validate_kod_pocztowy(cls, v):
        if v is not None and not re.match(r'^\d{2}-\d{3}$', v):
            raise ValueError('Nieprawidłowy format kodu pocztowego')
        return v


class PartialSectionH(OptionalModel):
    """Sekcja H: Informacja o załącznikach"""
    liczba_zalacznikow: Optional[Annotated[Optional[int], form_field("P_62")]] = Field(None, ge=0)


class PartialDeklaracja(OptionalModel):
    sekcja_a: Optional[PartialSectionA] = None
    sekcja_b: Optional[PartialSectionB] = None
    sekcja_c: Optional[PartialSectionC] = None
    sekcja_d: Optional[PartialSectionD] = None
    sekcja_e: Optional[PartialSectionE] = None
    sekcja_f: Optional[PartialSectionF] = None
    sekcja_g: Optional[PartialSectionG] = None
    sekcja_h: Optional[PartialSectionH] = None
    pouczenia: Optional[int] = None

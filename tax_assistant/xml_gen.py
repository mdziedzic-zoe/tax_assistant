from lxml import etree
from datetime import date
from typing import Optional

from tax_assistant.models.partial_taxform import TaxOffice
from tax_assistant.models.taxform import *


def generate_xml(deklaracja: Deklaracja) -> str:
    root = etree.Element("Deklaracja")

    # Naglowek
    naglowek = etree.SubElement(root, "Naglowek")
    etree.SubElement(naglowek, "KodFormularza").text = "PCC-3"
    etree.SubElement(naglowek, "WariantFormularza").text = "6"
    cel_zlozenia = etree.SubElement(naglowek, "CelZlozenia")
    cel_zlozenia.text = str(deklaracja.sekcja_a.cel_zlozenia.value)
    cel_zlozenia.set("poz", "P_6")
    data = etree.SubElement(naglowek, "Data")
    data.text = deklaracja.sekcja_a.data_dokonania_czynnosci.isoformat()
    data.set("poz", "P_4")
    etree.SubElement(naglowek, "KodUrzedu").text = deklaracja.sekcja_a.kod_urzedu.value

    # Podmiot1
    podmiot1 = etree.SubElement(root, "Podmiot1")
    podmiot1.set("rola", "Podatnik")

    if deklaracja.sekcja_b.osoba_fizyczna:
        osoba_fizyczna = etree.SubElement(podmiot1, "OsobaFizyczna")
        if deklaracja.sekcja_b.osoba_fizyczna.nip:
            etree.SubElement(osoba_fizyczna, "NIP").text = deklaracja.sekcja_b.osoba_fizyczna.nip
        if deklaracja.sekcja_b.osoba_fizyczna.pesel:
            etree.SubElement(osoba_fizyczna, "PESEL").text = deklaracja.sekcja_b.osoba_fizyczna.pesel
        etree.SubElement(osoba_fizyczna, "ImiePierwsze").text = deklaracja.sekcja_b.osoba_fizyczna.imie_pierwsze
        etree.SubElement(osoba_fizyczna, "Nazwisko").text = deklaracja.sekcja_b.osoba_fizyczna.nazwisko
        etree.SubElement(osoba_fizyczna,
                         "DataUrodzenia").text = deklaracja.sekcja_b.osoba_fizyczna.data_urodzenia.isoformat()
        if deklaracja.sekcja_b.osoba_fizyczna.imie_ojca:
            etree.SubElement(osoba_fizyczna, "ImieOjca").text = deklaracja.sekcja_b.osoba_fizyczna.imie_ojca
        if deklaracja.sekcja_b.osoba_fizyczna.imie_matki:
            etree.SubElement(osoba_fizyczna, "ImieMatki").text = deklaracja.sekcja_b.osoba_fizyczna.imie_matki
    elif deklaracja.sekcja_b.osoba_niefizyczna:
        osoba_niefizyczna = etree.SubElement(podmiot1, "OsobaNiefizyczna")
        etree.SubElement(osoba_niefizyczna, "NIP").text = deklaracja.sekcja_b.osoba_niefizyczna.nip
        etree.SubElement(osoba_niefizyczna, "PelnaNazwa").text = deklaracja.sekcja_b.osoba_niefizyczna.pelna_nazwa
        etree.SubElement(osoba_niefizyczna, "SkroconaNazwa").text = deklaracja.sekcja_b.osoba_niefizyczna.skrocona_nazwa

    adres = etree.SubElement(podmiot1, "AdresZamieszkaniaSiedziby")
    adres.set("rodzajAdresu", "RAD")
    if deklaracja.sekcja_b.adres_zamieszkania_siedziby.kod_kraju == "PL":
        adres_pol = etree.SubElement(adres, "AdresPol")
        etree.SubElement(adres_pol, "KodKraju").text = "PL"
        etree.SubElement(adres_pol, "Wojewodztwo").text = deklaracja.sekcja_b.adres_zamieszkania_siedziby.wojewodztwo
        etree.SubElement(adres_pol, "Powiat").text = deklaracja.sekcja_b.adres_zamieszkania_siedziby.powiat
        etree.SubElement(adres_pol, "Gmina").text = deklaracja.sekcja_b.adres_zamieszkania_siedziby.gmina
        if deklaracja.sekcja_b.adres_zamieszkania_siedziby.ulica:
            etree.SubElement(adres_pol, "Ulica").text = deklaracja.sekcja_b.adres_zamieszkania_siedziby.ulica
        etree.SubElement(adres_pol, "NrDomu").text = deklaracja.sekcja_b.adres_zamieszkania_siedziby.nr_domu
        if deklaracja.sekcja_b.adres_zamieszkania_siedziby.nr_lokalu:
            etree.SubElement(adres_pol, "NrLokalu").text = deklaracja.sekcja_b.adres_zamieszkania_siedziby.nr_lokalu
        etree.SubElement(adres_pol, "Miejscowosc").text = deklaracja.sekcja_b.adres_zamieszkania_siedziby.miejscowosc
        etree.SubElement(adres_pol, "KodPocztowy").text = deklaracja.sekcja_b.adres_zamieszkania_siedziby.kod_pocztowy
    else:
        adres_zagr = etree.SubElement(adres, "AdresZagr")
        etree.SubElement(adres_zagr, "KodKraju").text = deklaracja.sekcja_b.adres_zamieszkania_siedziby.kod_kraju
        if deklaracja.sekcja_b.adres_zamieszkania_siedziby.kod_pocztowy:
            etree.SubElement(adres_zagr,
                             "KodPocztowy").text = deklaracja.sekcja_b.adres_zamieszkania_siedziby.kod_pocztowy
        etree.SubElement(adres_zagr, "Miejscowosc").text = deklaracja.sekcja_b.adres_zamieszkania_siedziby.miejscowosc
        if deklaracja.sekcja_b.adres_zamieszkania_siedziby.ulica:
            etree.SubElement(adres_zagr, "Ulica").text = deklaracja.sekcja_b.adres_zamieszkania_siedziby.ulica
        if deklaracja.sekcja_b.adres_zamieszkania_siedziby.nr_domu:
            etree.SubElement(adres_zagr, "NrDomu").text = deklaracja.sekcja_b.adres_zamieszkania_siedziby.nr_domu
        if deklaracja.sekcja_b.adres_zamieszkania_siedziby.nr_lokalu:
            etree.SubElement(adres_zagr, "NrLokalu").text = deklaracja.sekcja_b.adres_zamieszkania_siedziby.nr_lokalu

    # PozycjeSzczegolowe
    pozycje_szczegolowe = etree.SubElement(root, "PozycjeSzczegolowe")
    etree.SubElement(pozycje_szczegolowe, "P_7").text = str(deklaracja.sekcja_b.podmiot_skladajacy.value)
    etree.SubElement(pozycje_szczegolowe, "P_20").text = str(deklaracja.sekcja_c.przedmiot_opodatkowania.value)
    if deklaracja.sekcja_c.miejsce_polozenia:
        etree.SubElement(pozycje_szczegolowe, "P_21").text = str(deklaracja.sekcja_c.miejsce_polozenia.value)
    if deklaracja.sekcja_c.miejsce_dokonania_czynnosci:
        etree.SubElement(pozycje_szczegolowe, "P_22").text = str(deklaracja.sekcja_c.miejsce_dokonania_czynnosci.value)
    etree.SubElement(pozycje_szczegolowe, "P_23").text = deklaracja.sekcja_c.tresc_czynnosci

    # Sekcja D
    if deklaracja.sekcja_d.podstawa_opodatkowania_1 is not None:
        etree.SubElement(pozycje_szczegolowe, "P_24").text = str(deklaracja.sekcja_d.podstawa_opodatkowania_1)
    if deklaracja.sekcja_d.kwota_podatku_1 is not None:
        etree.SubElement(pozycje_szczegolowe, "P_25").text = str(deklaracja.sekcja_d.kwota_podatku_1)
    if deklaracja.sekcja_d.podstawa_opodatkowania_2 is not None:
        etree.SubElement(pozycje_szczegolowe, "P_26").text = str(deklaracja.sekcja_d.podstawa_opodatkowania_2)
    if deklaracja.sekcja_d.kwota_podatku_2 is not None:
        etree.SubElement(pozycje_szczegolowe, "P_27").text = str(deklaracja.sekcja_d.kwota_podatku_2)
    if deklaracja.sekcja_d.kwota_podatku_naleznego is not None:
        etree.SubElement(pozycje_szczegolowe, "P_46").text = str(deklaracja.sekcja_d.kwota_podatku_naleznego)

    # Sekcja E
    if deklaracja.sekcja_e.typ_spolki:
        etree.SubElement(pozycje_szczegolowe, "P_47").text = str(deklaracja.sekcja_e.typ_spolki.value)
    if deklaracja.sekcja_e.podstawa_opodatkowania:
        etree.SubElement(pozycje_szczegolowe, "P_48").text = str(deklaracja.sekcja_e.podstawa_opodatkowania.value)
    if deklaracja.sekcja_e.kwota_podstawy_opodatkowania is not None:
        etree.SubElement(pozycje_szczegolowe, "P_49").text = str(deklaracja.sekcja_e.kwota_podstawy_opodatkowania)
    if deklaracja.sekcja_e.koszty is not None:
        etree.SubElement(pozycje_szczegolowe, "P_50").text = f"{deklaracja.sekcja_e.koszty:.2f}"
    if deklaracja.sekcja_e.podstawa_obliczenia_podatku is not None:
        etree.SubElement(pozycje_szczegolowe, "P_51").text = f"{deklaracja.sekcja_e.podstawa_obliczenia_podatku:.2f}"
    if deklaracja.sekcja_e.kwota_podatku is not None:
        etree.SubElement(pozycje_szczegolowe, "P_52").text = str(deklaracja.sekcja_e.kwota_podatku)

    # Sekcja F
    etree.SubElement(pozycje_szczegolowe, "P_53").text = str(deklaracja.sekcja_f.kwota_podatku_do_zaplaty)

    # Sekcja G
    if deklaracja.sekcja_g:
        if deklaracja.sekcja_g.wojewodztwo:
            etree.SubElement(pozycje_szczegolowe, "P_54").text = deklaracja.sekcja_g.wojewodztwo
        if deklaracja.sekcja_g.powiat:
            etree.SubElement(pozycje_szczegolowe, "P_55").text = deklaracja.sekcja_g.powiat
        if deklaracja.sekcja_g.gmina:
            etree.SubElement(pozycje_szczegolowe, "P_56").text = deklaracja.sekcja_g.gmina
        if deklaracja.sekcja_g.ulica:
            etree.SubElement(pozycje_szczegolowe, "P_57").text = deklaracja.sekcja_g.ulica
        if deklaracja.sekcja_g.nr_domu:
            etree.SubElement(pozycje_szczegolowe, "P_58").text = deklaracja.sekcja_g.nr_domu
        if deklaracja.sekcja_g.nr_lokalu:
            etree.SubElement(pozycje_szczegolowe, "P_59").text = deklaracja.sekcja_g.nr_lokalu
        if deklaracja.sekcja_g.miejscowosc:
            etree.SubElement(pozycje_szczegolowe, "P_60").text = deklaracja.sekcja_g.miejscowosc
        if deklaracja.sekcja_g.kod_pocztowy:
            etree.SubElement(pozycje_szczegolowe, "P_61").text = deklaracja.sekcja_g.kod_pocztowy

    # Sekcja H
    if deklaracja.sekcja_h and deklaracja.sekcja_h.liczba_zalacznikow is not None:
        etree.SubElement(pozycje_szczegolowe, "P_62").text = str(deklaracja.sekcja_h.liczba_zalacznikow)

    # Pouczenia
    etree.SubElement(root, "Pouczenia").text = "1"

    return etree.tostring(root, pretty_print=True, encoding="unicode")


# Create mock data
mock_deklaracja = Deklaracja(
    sekcja_a=SectionA(
        cel_zlozenia=CelZlozenia.ZLOZENIE,
        data_dokonania_czynnosci=date(2024, 3, 15),
        kod_urzedu=TaxOffice.URZĄD_SKARBOWY_W_LEGNICY
    ),
    sekcja_b=SectionB(
        osoba_fizyczna=OsobaFizyczna(
            nip="1234567890",
            imie_pierwsze="Jan",
            nazwisko="Kowalski",
            data_urodzenia=date(1980, 5, 15),
            imie_ojca="Adam",
            imie_matki="Ewa"
        ),
        adres_zamieszkania_siedziby=Adres(
            kod_kraju="PL",
            wojewodztwo="mazowieckie",
            powiat="Warszawa",
            gmina="Warszawa",
            ulica="Marszałkowska",
            nr_domu="1",
            nr_lokalu="10",
            miejscowosc="Warszawa",
            kod_pocztowy="00-001"
        ),
        podmiot_skladajacy=PodmiotSkladajacy.PODMIOT_ZOBOWIAZANY
    ),
    sekcja_c=SectionC(
        przedmiot_opodatkowania=PrzedmiotOpodatkowania.UMOWA,
        miejsce_polozenia=MiejscePolozenia.TERYTORIUM_RP,
        miejsce_dokonania_czynnosci=MiejscePolozenia.TERYTORIUM_RP,
        tresc_czynnosci="Zakup nieruchomości"
    ),
    sekcja_d=SectionD(
        podstawa_opodatkowania_1=500000,
        kwota_podatku_1=5000,
        kwota_podatku_naleznego=5000
    ),
    sekcja_e=SectionE(
        typ_spolki=TypSpolki.OSOBOWA,
        podstawa_opodatkowania=PodstawaOpodatkowania.ZAWARCIE_UMOWY_SPOLKI,
        kwota_podstawy_opodatkowania=100000,
        koszty=1000.50,
        podstawa_obliczenia_podatku=99000.50,
        kwota_podatku=990
    ),
    sekcja_f=SectionF(
        kwota_podatku_do_zaplaty=5990
    ),
    sekcja_g=SectionG(
        wojewodztwo="mazowieckie",
        powiat="Warszawa",
        gmina="Warszawa",
        ulica="Nowy Świat",
        nr_domu="1",
        nr_lokalu="1",
        miejscowosc="Warszawa",
        kod_pocztowy="00-001"
    ),
    sekcja_h=SectionH(
        liczba_zalacznikow=1
    ),
    pouczenia=1
)

print(generate_xml(mock_deklaracja))

#!/usr/bin/env python3
"""Angebot Odoo-Einführung für die biotec GmbH.

    python3 angebot_odoo.py <ziel.docx>

Struktur nach der Work-Breakdown-Structure 1–8 aus
01_Projektsteuerung/todo-angebot-begleitdokument.md, damit biotec den
aktivierungsfähigen Anteil sauber vom Aufwand trennen kann.
"""
import sys
from docx import Document
from docx.shared import Pt, Cm, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH

sys.path.insert(0, __file__.rsplit("/", 1)[0])
from docx_bausteine import (ACCENT, GREY, seite_einrichten, titel, heading,
                            table, bullets, note, set_base_style)

DOK = "ANG-2026-001"
STAND = "Version 1, Stand 01.09.2026"
STUNDENSATZ = 137.50
STD_JE_TAG = 8
PT_SATZ = STUNDENSATZ * STD_JE_TAG          # 1.100,00 € je Personentag

GELB = "FFF2A8"
BLAU = "DCE6F1"


def eur(x):
    return f"{x:,.2f} €".replace(",", "§").replace(".", ",").replace("§", ".")


def pt(x):
    return f"{x:,.1f}".replace(".", ",")


def absatz(doc, text, groesse=10, kursiv=False, abstand=6, fett=False):
    p = doc.add_paragraph()
    p.paragraph_format.space_after = Pt(abstand)
    for i, teil in enumerate(text.split("**")):
        if not teil:
            continue
        r = p.add_run(teil)
        r.font.size = Pt(groesse)
        r.font.italic = kursiv
        r.font.bold = fett or i % 2 == 1
    return p


# ---------------------------------------------------------------- Leistungen
# (Workstream, Einordnung, [(Position, Inhalt, PT)])
WORKSTREAMS = [
    ("1 · Analyse und Beratung", "Aufwand", [
        ("1.1", "Prozessaufnahme Labor: Auftrag, Probenahme, Bebrütung, Auszählung, "
                "Gutachtenübergabe, Rechnung", 3.0),
        ("1.2", "Prozessaufnahme Schulungsgeschäft und kaufmännische Abläufe", 2.0),
        ("1.3", "Soll-Konzept mit Abbildungsentscheidungen je Bereich, abgestimmt und "
                "freigegeben", 3.0),
        ("1.4", "Rollen- und Rechtekonzept, Grundlage für Lizenzzahl und Zugriffe", 2.0),
        ("1.5", "Projektleitung, Abstimmungen, Statusberichte über die Laufzeit", 12.0),
    ]),
    ("2 · Konfiguration der Odoo-Module", "aktivierungsbezogen", [
        ("2.1", "Grundeinrichtung: Unternehmen, drei Standorte, Nummernkreise, Benutzer, "
                "Zugriffsrechte, Sprachen", 3.0),
        ("2.2", "Kontakte und CRM: Kundenkategorien, Ansprechpartner, Werke und Gebäude als "
                "untergeordnete Kontakte, USt-IdNr.-Prüfung", 3.0),
        ("2.3", "Verkauf: Preislisten für Prüfleistungen, Kurse und Inhouse-Schulungen, "
                "Angebots- und Auftragsarten, Rahmenverträge", 4.0),
        ("2.4", "Leistungs- und Artikelstamm: Prüfleistungen, Kursarten, Verbrauchsmaterial, "
                "Kategorien mit Erlöskonten", 2.5),
        ("2.5", "Einkauf und Lager: Lagerorte, Verbrauchsmaterial, Nachbestellregeln für "
                "Gelatinefilter und Nährmedien", 3.0),
        ("2.6", "Buchhaltung: SKR04, Steuersätze 19 und 7 Prozent, Reverse Charge nach § 13b, "
                "Drittlandfälle, GoBD-Festschreibung, DATEV-Export, Bankabgleich, Mahnwesen", 10.0),
        ("2.7", "Analytische Buchhaltung: Ergebnis je Standort und je Geschäftsbereich "
                "(Hygieneinspektion, Analytik, Schulung)", 2.0),
        ("2.8", "**Anlagen und Turnussteuerung:** Wartungs-App mit Gerätekategorie RLT-Anlage, "
                "Zusatzfelder, Prüfintervalle je Anlagentyp, automatisch erzeugte "
                "Wartungsanfragen mit Fälligkeit", 9.0),
        ("2.9", "**Schulungsgeschäft:** Kursarten VDI 6022 und VDI 2047, Seminartermine mit "
                "Ort und Kapazität, Mindestteilnehmerzahl, Anmeldung, Bestätigungs- und "
                "Erinnerungsmails, Dozentenverwaltung", 8.0),
    ]),
    ("3 · Kundenspezifische Entwicklung", "aktivierungsbezogen", [
        ("3.1", "Belegformulare im biotec-Layout: Angebot, Auftragsbestätigung, Lieferschein, "
                "Rechnung, Mahnung – Layouttreue ist bindende Anforderung", 5.0),
        ("3.2", "Teilnahmebescheinigung und Zertifikatsvorlage für die VDI-Schulungen", 2.0),
        ("3.3", "Erweiterungsmodul für den Anlagenstamm: VDI-Luftwerte, drei Kennungen je "
                "Anlage, Standortfelder – als eigenes Modul mit Quellcode", 3.0),
        ("3.4", "Arbeitsvorrat und Fälligkeitsübersicht der Wiederholungsprüfungen, "
                "Übergang von der Wartungsanfrage zum Angebot", 3.0),
    ]),
    ("4 · Schnittstellen", "aktivierungsbezogen", [
        ("4.1", "**Stammdatenbrücke Odoo zum Gutachten-Altsystem:** Analyse der Feldbedeutung, "
                "Anbindung, Erstabgleich, Dienstbetrieb mit Protokoll, Neuanlagen, Anpassung "
                "der Odoo-Oberfläche, gemeinsamer Einstieg, Abnahme", 17.0),
    ]),
    ("5 · Datenmigration", "aktivierungsbezogen", [
        ("5.1", "Kunden, Ansprechpartner, Werke und Gebäude – Neuaufbau aus der vorhandenen "
                "Kontaktliste inklusive Bereinigung", 6.0),
        ("5.2", "Anlagenstamm mit 938 RLT-Anlagen: Übernahme, Bereinigung der Hersteller- und "
                "Wartungsfirmenschreibweisen, Umsetzung der Zahlenformate, Aussonderung der "
                "Testdatensätze", 5.0),
        ("5.3", "Lieferanten und Fremdlabore aus Kreditorenstamm und Eingangsrechnungen", 3.0),
        ("5.4", "Leistungen, Artikel, Verbrauchsmaterial und Kurskatalog", 2.0),
        ("5.5", "Kontenrahmen, offene Posten, Saldenvortrag zum Stichtag", 4.0),
        ("5.6", "Lagerbestand aus der Stichtagsinventur", 1.5),
        ("5.7", "Importmethodik mit externen Kennungen, Probeläufe, Abstimmung der Summen mit "
                "der Buchhaltung", 3.0),
    ]),
    ("6 · Integration und Test", "aktivierungsbezogen", [
        ("6.1", "Funktionstests je Modul, rund 60 Testfälle mit dokumentiertem Ergebnis", 9.0),
        ("6.2", "Durchgängige Prozesstests: Auftrag bis Rechnung, Kurs von der Anmeldung bis "
                "zur Bescheinigung, Einkauf bis Lieferantenrechnung", 6.0),
        ("6.3", "Betriebssimulation über einen Monat mit dem Fachbereich, mit echten Fällen", 4.0),
        ("6.4", "Fehlerbehebung und Abnahmeprotokolle je Workstream", 4.0),
    ]),
    ("7 · Schulung und Einführungsbegleitung", "Aufwand", [
        ("7.1", "Anwenderleitfäden je Rolle mit den tatsächlichen Abläufen bei biotec", 3.0),
        ("7.2", "**Vor-Ort-Schulung in Gütersloh, drei Tage:** zwei Tage für die vier "
                "Kernnutzer, ein Tag für die weiteren Rollen in Labor, Verwaltung und "
                "Buchhaltung", 3.0),
        ("7.3", "An- und Abreise", 1.0),
        ("7.4", "Nachschulung vier Wochen nach dem Start, aus der Ferne", 1.0),
    ]),
    ("8 · Umstellung und Betreuung", "Aufwand", [
        ("8.1", "Umstellungsplan, Begleitung der Stichtagsinventur, abschließende "
                "Datenübernahme", 4.0),
        ("8.2", "Begleitung am Umstellungstag und an den beiden Folgetagen", 2.0),
        ("8.3", "Enge Betreuung über vier Wochen nach dem Start", 5.0),
    ]),
]

OPTIONEN = [
    ("O1", "Übernahme des Interessentenbestands mit 10.387 Adressen in das CRM, "
           "inklusive Bereinigung und Zuordnung zu bestehenden Kunden", 3.0),
    ("O2", "**Datenlieferung an LucaNet:** Einrichtung, Abstimmung des Lieferformats mit der "
           "Certania-Gruppe, Testlieferung und Abnahme. Der laufende Aufwand je Periode liegt "
           "danach nahe null", 8.0),
    ("O3", "**IFRS-Überleitung:** zusätzliche Erfassungsfelder, Kontenzuordnung und Journal "
           "für die Berichterstattung an die Gruppe", 6.0),
    ("O4", "Übernahme der Prüfhistorie: bestehende Gutachten als Nachweis am Anlagensatz "
           "verknüpft, ohne inhaltliche Migration", 4.0),
]

MITWIRKUNG = [
    ["M1", "**Stichtagsinventur** des Verbrauchsmaterials unmittelbar vor der Umstellung – "
           "Gelatinefilter, Nährmedien, Röhrchen. Eine vollständige Lagerliste besteht heute "
           "nicht; der Bestand wird gezählt, nicht migriert", "biotec", "vor Go-live"],
    ["M2", "**Finale Unterlagen zum Stichtag:** offene Posten Debitoren und Kreditoren, "
           "Saldenvortrag, letzter Kontostand", "Buchhaltung", "Stichtag"],
    ["M3", "**Summen- und Saldenliste als Excel oder CSV.** Die vorliegende Fassung besteht "
           "aus Bildschirmfotos und ist maschinell nicht auswertbar", "Buchhaltung", "Projektstart"],
    ["M4", "Fehlende Quelldateien des Altsystems, vor allem die Briefköpfe und Vorlagen aus "
           "der Gutachten-Software", "Westbomke EDV", "vor Layoutarbeit"],
    ["M5", "Prüfintervalle je Anlagentyp: nach welcher Regel wird heute terminiert", "biotec",
     "vor Konfiguration"],
    ["M6", "Bestätigung des gültigen Kundenstands – im Altsystem liegen mehrere Fassungen "
           "nebeneinander", "biotec", "vor Migration"],
    ["M7", "Freigabe der Belegformulare durch die Geschäftsführung, bevor sie gebaut werden",
     "biotec", "Meilenstein 2"],
    ["M8", "Benennung der vier Personen für die Vor-Ort-Schulung", "biotec", "vor Meilenstein 4"],
    ["M9", "Verfügbarkeit der Fachbereiche für Abstimmung, Test und Betriebssimulation – "
           "erfahrungsgemäß ein halber Tag je Woche und Bereich", "biotec", "laufend"],
    ["M10", "Zugang zum produktiven Bestand des Altsystems und eine Sicherung zum Testen, "
            "dazu Zugriff auf das Vorlagenverzeichnis", "Westbomke EDV", "Projektstart"],
]

MEILENSTEINE = [
    ["1", "Soll-Konzept abgestimmt und freigegeben", "Konzeptdokument, Abnahmeprotokoll", "Woche 3"],
    ["2", "Grundsystem konfiguriert, Belegformulare freigegeben", "Testsystem, Layoutmuster", "Woche 8"],
    ["3", "Daten übernommen, Summen abgestimmt", "Migrationsprotokoll", "Woche 12"],
    ["4", "Abnahmetest bestanden", "Testprotokoll, Fehlerliste geschlossen", "Woche 16"],
    ["5", "Schulung durchgeführt", "Teilnehmerliste, Anwenderleitfäden", "Woche 18"],
    ["6", "**Betriebsbereitschaft** – Stichtag für die Aktivierung", "Abnahmeprotokoll "
          "Betriebsbereitschaft", "Woche 19"],
    ["7", "Betreuungsphase abgeschlossen", "Abschlussbericht, offene Punkte übergeben", "Woche 23"],
]


def summe(ws):
    return sum(p[2] for p in ws[2])


def build(ziel):
    doc = Document()
    set_base_style(doc)
    seite_einrichten(doc, "Angebot Odoo-Einführung  ·  Dok.-Nr. " + DOK + "  ·  " + STAND)
    titel(doc, "Angebot: Einführung von Odoo", "biotec GmbH  ·  " + STAND)

    # ---- Adressblock
    table(doc, ["", "Angaben"], [4.6, 12.4], [
        ["Angebot für", "biotec GmbH, Umwelt-Analytik-Beratung-Service\n"
                        "Elbrachtsweg 76, 33332 Gütersloh\n"
                        "z. Hd. Herrn Dr. Thomas Wilke, Geschäftsführer"],
        ["Ansprechpartner biotec", "Michael Brand, Projektleitung Hygieneinspektion "
                                   "(fachlich und technisch)\n"
                                   "Nicole Krupa (kaufmännisch und organisatorisch)"],
        ["Angebot von", "CertoClav Sterilizer GmbH\nPeintner Straße 10, 4060 Leonding, "
                        "Österreich\nMichael Simon (geb. Dirix), MSc., Geschäftsführer\n"
                        "michael.simon@certoclav.com"],
        ["Dokument", DOK + "  ·  " + STAND],
        ["Gültigkeit", "60 Tage ab Ausstellungsdatum"],
    ])
    doc.add_paragraph()

    # ---- 1 Ausgangslage
    heading(doc, "Ausgangslage", kicker="Worum es geht")
    absatz(doc, "biotec arbeitet an drei Standorten – Gütersloh mit Labor und Verwaltung, "
                "München mit den Hygienekontrollen und dem Technologiepark Mittweida für die "
                "Analytik von Boden und Wasser. Die kaufmännischen Abläufe laufen heute "
                "außerhalb eines Systems: Rechnungen, Buchhaltung, Artikel und Lager, "
                "Zeiterfassung und das gesamte Schulungsgeschäft werden von Hand geführt.")
    absatz(doc, "Die fachliche Arbeit trägt eine über Jahre gewachsene Eigenentwicklung. Wir "
                "haben Quellcode und Datenbestand ausgewertet: 255 Programmeinheiten, 430 "
                "Tabellen, die Gutachten entstehen über eine automatisierte Satzstrecke. Rund "
                "die Hälfte der Anwendung deckt Aufgaben ab, die Odoo mitbringt – Akquise, "
                "Kunden, Angebote. Die andere Hälfte ist Fachlogik ohne Entsprechung: "
                "Prüflisten nach VDI 6022, Labormasken, Maßnahmenkatalog und die "
                "Gutachtenerzeugung.")
    note(doc, "Daraus folgt der Zuschnitt dieses Angebots: Odoo übernimmt das Kaufmännische, "
              "die bewährte Gutachtenerstellung bleibt. Verbunden werden beide über eine "
              "Stammdatenbrücke. Was funktioniert, wird nicht ersetzt.")

    heading(doc, "Der Zuschnitt", kicker="Zwei Systeme, eine Datenbasis")
    table(doc, ["Bereich", "Künftig", "Anmerkung"], [5.4, 3.4, 8.2], [
        ["Akquise und Interessenten", "**Odoo**", "10.387 Adressen im CRM"],
        ["Kunden, Werke, Gebäude", "**Odoo**", "führender Stand für beide Systeme"],
        ["Anlagenstamm, Prüfintervalle", "**Odoo**", "938 RLT-Anlagen, Turnussteuerung neu"],
        ["Angebote und Aufträge", "**Odoo**", ""],
        ["Rechnungen und Buchhaltung", "**Odoo**", "heute außerhalb, SKR04"],
        ["Artikel, Lager, Einkauf", "**Odoo**", "heute mehrere Einzeldokumente"],
        ["Zeiterfassung", "**Odoo**", "heute außerhalb"],
        ["Schulungsgeschäft", "**Odoo**", "heute vollständig außerhalb"],
        ["Prüflisten nach VDI 6022", "bestehendes System", "bleibt unverändert"],
        ["Gutachten erstellen und bearbeiten", "bestehendes System", "Layout und Ablauf bleiben"],
        ["Labormasken, Messergebnisse", "bestehendes System", "bleibt unverändert"],
    ], zeilen_fuellung=lambda z: BLAU if "Odoo" in z[1] else None)
    absatz(doc, "Die Stammdatenbrücke sorgt dafür, dass die Gutachtenanwendung Kunden und "
                "Anlagen automatisch sieht, sobald sie in Odoo gepflegt werden. Die "
                "Erfassungsmasken für Kunden, Akquise und Angebote werden im Altsystem "
                "ausgeblendet, damit Stammdaten nur an einer Stelle entstehen.", abstand=12)

    doc.add_page_break()

    # ---- Leistungsumfang
    heading(doc, "Leistungsumfang", kicker="Acht Arbeitspakete")
    absatz(doc, "Die Gliederung folgt den acht Arbeitspaketen, die zwischen "
                "aktivierungsbezogenen und laufenden Leistungen unterscheiden. Damit lässt "
                "sich der Herstellungsanteil sauber abgrenzen; die bilanzielle Beurteilung "
                "trifft biotec mit dem Wirtschaftsprüfer.", kursiv=True, abstand=10)

    gesamt = 0.0
    for name, art, positionen in WORKSTREAMS:
        s = sum(p[2] for p in positionen)
        gesamt += s
        heading(doc, name, kicker=art)
        zeilen = [[nr, inhalt, pt(tage)] for nr, inhalt, tage in positionen]
        zeilen.append(["", "**Summe " + name.split(" · ")[0] + "**",
                       "**" + pt(s) + "**"])
        table(doc, ["Nr.", "Leistung", "PT"], [1.4, 13.6, 2.0], zeilen,
              zeilen_fuellung=lambda z: BLAU if z[0] == "" else None)
        doc.add_paragraph()

    # ---- Preisübersicht
    doc.add_page_break()
    heading(doc, "Preisübersicht", kicker="Grundpaket")
    zeilen = []
    for name, art, positionen in WORKSTREAMS:
        s = sum(p[2] for p in positionen)
        zeilen.append([name, art, pt(s), eur(s * PT_SATZ)])
    zeilen.append(["**Grundpaket gesamt**", "", "**" + pt(gesamt) + "**",
                   "**" + eur(gesamt * PT_SATZ) + "**"])
    table(doc, ["Arbeitspaket", "Einordnung", "PT", "Betrag"], [7.0, 4.0, 2.0, 4.0], zeilen,
          zeilen_fuellung=lambda z: GELB if z[1] == "" else None)
    absatz(doc, f"Stundensatz {STUNDENSATZ:.2f} €".replace(".", ",") +
                f", Personentag zu {STD_JE_TAG} Stunden entspricht {eur(PT_SATZ)}. "
                "Alle Beträge netto zuzüglich Umsatzsteuer.", groesse=9, kursiv=True, abstand=12)

    aktiv = sum(sum(p[2] for p in ws[2]) for ws in WORKSTREAMS if ws[1] == "aktivierungsbezogen")
    absatz(doc, "**Davon aktivierungsbezogen:** " + pt(aktiv) + " PT (" + eur(aktiv * PT_SATZ) +
                "). **Davon Aufwand:** " + pt(gesamt - aktiv) + " PT (" +
                eur((gesamt - aktiv) * PT_SATZ) + ").", abstand=12)

    heading(doc, "Optionen", kicker="Auf Abruf, nicht im Grundpaket")
    zeilen = [[nr, inhalt, pt(tage), eur(tage * PT_SATZ)] for nr, inhalt, tage in OPTIONEN]
    so = sum(o[2] for o in OPTIONEN)
    zeilen.append(["", "**Summe Optionen**", "**" + pt(so) + "**", "**" + eur(so * PT_SATZ) + "**"])
    table(doc, ["Nr.", "Leistung", "PT", "Betrag"], [1.4, 10.6, 2.0, 3.0], zeilen,
          zeilen_fuellung=lambda z: BLAU if z[0] == "" else None)
    absatz(doc, "Optionen werden erst nach schriftlicher Freigabe erbracht. Bei O2 ist die "
                "Abstimmung des Lieferformats mit der Certania-Gruppe Voraussetzung – liegt "
                "ein Format einer anderen Gruppengesellschaft vor, sinkt der Aufwand.",
           groesse=9, kursiv=True, abstand=12)

    # ---- Abrechnung
    heading(doc, "Abrechnung", kicker="Nach Leistung, nicht nach Stunden")
    bullets(doc, [
        "Abgerechnet wird nach erbrachter Leistung je Arbeitspaket, jeweils mit "
        "Leistungsnachweis und Abnahme. Die genannten Beträge sind die kalkulierte Grundlage, "
        "kein Festpreis.",
        "Rechnungsstellung monatlich nach Leistungsfortschritt, getrennt nach Arbeitspaket. "
        "Damit bleibt die Zuordnung zu aktivierungsbezogenen und laufenden Leistungen "
        "durchgängig nachvollziehbar.",
        "Abweichungen von mehr als zehn Prozent je Arbeitspaket werden vor der Ausführung "
        "angezeigt und schriftlich freigegeben.",
        "Der entstehende Quellcode – Erweiterungsmodule, Stammdatenbrücke, Auswertungen – wird "
        "an biotec übergeben und in einem Repository von biotec abgelegt.",
        "Reisekosten für die Vor-Ort-Schulung werden nach Aufwand abgerechnet und vorab "
        "abgestimmt.",
        "Nicht enthalten sind Odoo-Lizenzen, Hosting, Hardware und Leistungen Dritter.",
    ])

    # ---- Zeitplan
    doc.add_page_break()
    heading(doc, "Zeitplan und Meilensteine", kicker="Rund 23 Wochen")
    table(doc, ["Nr.", "Meilenstein", "Nachweis", "Zeitpunkt"], [1.2, 7.0, 6.0, 2.8],
          MEILENSTEINE,
          zeilen_fuellung=lambda z: GELB if z[0] == "6" else None)
    absatz(doc, "Der Meilenstein Betriebsbereitschaft ist der Stichtag, bis zu dem "
                "zurechenbare Herstellungskosten anfallen. Er wird mit einem eigenen "
                "Abnahmeprotokoll dokumentiert.", groesse=9, kursiv=True, abstand=12)

    # ---- Mitwirkung
    heading(doc, "Mitwirkung von biotec", kicker="Was biotec beisteuert")
    absatz(doc, "Eine Einführung gelingt nur gemeinsam. Die folgenden Punkte liegen bei "
                "biotec und sind terminkritisch – ohne sie verschiebt sich der Plan.")
    table(doc, ["Nr.", "Aufgabe", "Wer", "Wann"], [1.2, 11.0, 3.0, 1.8], MITWIRKUNG,
          zeilen_fuellung=lambda z: GELB if z[0] in ("M1", "M2") else None)

    # ---- Annahmen
    heading(doc, "Annahmen und Voraussetzungen", kicker="Woran die Kalkulation hängt")
    bullets(doc, [
        "Odoo wird in einer Fassung betrieben, die eigene Module zulässt. Bei einem reinen "
        "Mietbetrieb ohne eigene Module ändern sich Aufwand und die Frage der Aktivierung.",
        "Die drei Standorte werden als eine Gesellschaft mit analytischer Trennung abgebildet, "
        "nicht als getrennte Mandanten.",
        "Die Buchführung bleibt bei biotec; der Steuerberater erhält einen DATEV-Export.",
        "Das Gutachtenlayout bleibt unverändert und wird nicht in Odoo nachgebaut.",
        "Die Prüflisten nach VDI 6022 bleiben im bestehenden System; eine Abbildung in Odoo "
        "ist nicht Gegenstand dieses Angebots.",
        "Der Kundenstamm wird neu aufgebaut, nicht eins zu eins übernommen. Die vorliegende "
        "Liste ist eine Kontaktliste ohne Kundennummern und Konditionen.",
        "Lagerbestände werden zum Stichtag gezählt und nicht aus dem Altsystem übernommen.",
        "Zeitaufnahmen der heutigen Abläufe liegen nicht vor. Die Aufwände beruhen auf der "
        "Auswertung der gelieferten Daten und auf Erfahrungswerten aus vergleichbaren "
        "Einführungen.",
    ])

    # ---- Nicht enthalten
    heading(doc, "Nicht enthalten", kicker="Klarstellung")
    bullets(doc, [
        "Lizenz-, Hosting- und Betriebskosten für Odoo",
        "Änderungen an der bestehenden Gutachtenanwendung",
        "Abbildung der Prüflisten oder der Labormasken in Odoo",
        "Webshop und Online-Buchung der Seminare",
        "Fertigung und Stücklisten über die vorhandene geringe Eigenproduktion hinaus",
        "Steuerliche und bilanzielle Beratung, insbesondere zur Aktivierung",
        "Rechtsberatung, Prüfung der Vertrags- und Belegtexte",
    ])

    # ---- Schluss
    heading(doc, "Nächster Schritt", kicker="")
    absatz(doc, "Wir schlagen vor, dieses Angebot in einem Termin gemeinsam durchzugehen und "
                "die Punkte unter Mitwirkung zu terminieren. Nach Beauftragung beginnen wir "
                "mit der Prozessaufnahme; die erste Fassung des Soll-Konzepts liegt drei "
                "Wochen später vor.")
    absatz(doc, "Für Rückfragen stehe ich jederzeit zur Verfügung.", abstand=18)

    table(doc, ["biotec GmbH", "CertoClav Sterilizer GmbH"], [8.5, 8.5], [
        ["\n\nOrt, Datum\n\n\n\n\n________________________________\n"
         "Dr. Thomas Wilke\nGeschäftsführer",
         "\n\nOrt, Datum\n\n\n\n\n________________________________\n"
         "Michael Simon (geb. Dirix), MSc.\nGeschäftsführer"],
    ])

    doc.save(ziel)
    print("geschrieben:", ziel)
    print(f"Grundpaket: {pt(gesamt)} PT = {eur(gesamt*PT_SATZ)}")
    print(f"  davon aktivierungsbezogen: {pt(aktiv)} PT = {eur(aktiv*PT_SATZ)}")
    print(f"  davon Aufwand:             {pt(gesamt-aktiv)} PT = {eur((gesamt-aktiv)*PT_SATZ)}")
    print(f"Optionen:   {pt(so)} PT = {eur(so*PT_SATZ)}")
    print(f"Gesamt max: {pt(gesamt+so)} PT = {eur((gesamt+so)*PT_SATZ)}")


if __name__ == "__main__":
    build(sys.argv[1] if len(sys.argv) > 1 else "Angebot_Odoo_biotec.docx")

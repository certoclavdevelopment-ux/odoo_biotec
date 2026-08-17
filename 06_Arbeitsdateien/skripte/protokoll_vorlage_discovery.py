#!/usr/bin/env python3
"""Erzeugt die Word-Vorlage für das Discovery-Call-Protokoll (biotec GmbH).

Aufbau folgt 1:1 der Discovery-Call-Präsentation
(03_Praesentationen/2026-08-17_Discovery_Call/Discovery_Call_Biotec_CertoClav.pdf).

Aufruf:  python3 protokoll_vorlage_discovery.py <zieldatei.docx>
"""
import sys

from docx import Document
from docx.enum.section import WD_SECTION
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.shared import Cm, Pt, RGBColor

ACCENT = RGBColor(0x1F, 0x4E, 0x79)      # dunkelblau, Deck-Akzent
GREY = RGBColor(0x7F, 0x7F, 0x7F)
LINE = RGBColor(0xBF, 0xBF, 0xBF)

FOOTER = ("CertoClav Sterilizer GmbH  ·  Leonding, Österreich  ·  "
          "support@certoclav.com  ·  www.certoclav.com")


# --------------------------------------------------------------------------- Hilfsfunktionen
def set_base_style(doc):
    st = doc.styles["Normal"]
    st.font.name = "Calibri"
    st.font.size = Pt(10.5)
    st.paragraph_format.space_after = Pt(4)
    st.paragraph_format.line_spacing = 1.08


def shade(cell, hexcolor):
    el = OxmlElement("w:shd")
    el.set(qn("w:val"), "clear")
    el.set(qn("w:fill"), hexcolor)
    cell._tc.get_or_add_tcPr().append(el)


def bottom_border(par, color="BFBFBF", size=6):
    pPr = par._p.get_or_add_pPr()
    borders = OxmlElement("w:pBdr")
    bottom = OxmlElement("w:bottom")
    bottom.set(qn("w:val"), "single")
    bottom.set(qn("w:sz"), str(size))
    bottom.set(qn("w:space"), "2")
    bottom.set(qn("w:color"), color)
    borders.append(bottom)
    pPr.append(borders)


def answer_lines(doc, count=2):
    """Beschreibbare Zeilen mit dezenter Linie darunter."""
    for _ in range(count):
        p = doc.add_paragraph()
        p.paragraph_format.space_before = Pt(6)
        p.paragraph_format.space_after = Pt(6)
        p.paragraph_format.left_indent = Cm(0.4)
        bottom_border(p)


def heading(doc, text, kicker=None):
    if kicker:
        k = doc.add_paragraph()
        k.paragraph_format.space_before = Pt(14)
        k.paragraph_format.space_after = Pt(0)
        r = k.add_run(kicker.upper())
        r.font.size = Pt(7.5)
        r.font.bold = True
        r.font.color.rgb = GREY
        r.font.name = "Calibri"
    h = doc.add_paragraph()
    h.paragraph_format.space_before = Pt(2) if kicker else Pt(14)
    h.paragraph_format.space_after = Pt(6)
    bottom_border(h, color="1F4E79", size=8)
    r = h.add_run(text)
    r.font.size = Pt(13)
    r.font.bold = True
    r.font.color.rgb = ACCENT
    return h


def question(doc, text, hint=None, lines=2):
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(8)
    p.paragraph_format.space_after = Pt(0)
    r = p.add_run(text)
    r.font.bold = True
    if hint:
        h = p.add_run("  " + hint)
        h.font.italic = True
        h.font.color.rgb = GREY
        h.font.size = Pt(9)
    answer_lines(doc, lines)


def note(doc, text):
    p = doc.add_paragraph()
    p.paragraph_format.space_after = Pt(2)
    r = p.add_run(text)
    r.font.italic = True
    r.font.size = Pt(9)
    r.font.color.rgb = GREY


def table(doc, cols, widths, rows, header_fill="1F4E79"):
    t = doc.add_table(rows=1, cols=len(cols))
    t.style = "Table Grid"
    t.alignment = WD_TABLE_ALIGNMENT.LEFT
    for i, (name, w) in enumerate(zip(cols, widths)):
        c = t.rows[0].cells[i]
        c.width = Cm(w)
        shade(c, header_fill)
        p = c.paragraphs[0]
        p.paragraph_format.space_after = Pt(0)
        r = p.add_run(name)
        r.font.bold = True
        r.font.size = Pt(9.5)
        r.font.color.rgb = RGBColor(0xFF, 0xFF, 0xFF)
    for row in rows:
        cells = t.add_row().cells
        for i, val in enumerate(row):
            cells[i].width = Cm(widths[i])
            p = cells[i].paragraphs[0]
            p.paragraph_format.space_after = Pt(0)
            r = p.add_run(val)
            r.font.size = Pt(9.5)
    return t


def page_field(par):
    par.add_run("Seite ")
    for instr in ("PAGE", "NUMPAGES"):
        fld = OxmlElement("w:fldSimple")
        fld.set(qn("w:instr"), instr)
        run = OxmlElement("w:r")
        txt = OxmlElement("w:t")
        txt.text = "1"
        run.append(txt)
        fld.append(run)
        par._p.append(fld)
        if instr == "PAGE":
            par.add_run(" von ")


# --------------------------------------------------------------------------- Dokument
def build(path):
    doc = Document()
    set_base_style(doc)

    sec = doc.sections[0]
    sec.page_width, sec.page_height = Cm(21), Cm(29.7)
    sec.top_margin = Cm(2.2)
    sec.bottom_margin = Cm(1.8)
    sec.left_margin = sec.right_margin = Cm(2.0)

    # Kopfzeile
    hp = sec.header.paragraphs[0]
    hp.text = ""
    r = hp.add_run("CERTOCLAV CONSULTING")
    r.font.size = Pt(8)
    r.font.bold = True
    r.font.color.rgb = ACCENT
    tab = hp.add_run("\tProtokoll Discovery Call  ·  Dok.-Nr. DISC-2026-001")
    tab.font.size = Pt(8)
    tab.font.color.rgb = GREY
    hp.alignment = WD_ALIGN_PARAGRAPH.LEFT
    bottom_border(hp)

    # Fußzeile
    fp = sec.footer.paragraphs[0]
    fp.text = ""
    fr = fp.add_run(FOOTER + "   ·   ")
    fr.font.size = Pt(7.5)
    fr.font.color.rgb = GREY
    page_field(fp)
    for run in fp.runs:
        run.font.size = Pt(7.5)
        run.font.color.rgb = GREY
    fp.alignment = WD_ALIGN_PARAGRAPH.CENTER

    # Titel
    t = doc.add_paragraph()
    t.paragraph_format.space_after = Pt(0)
    r = t.add_run("Protokoll Discovery Call")
    r.font.size = Pt(22)
    r.font.bold = True
    r.font.color.rgb = ACCENT
    s = doc.add_paragraph()
    s.paragraph_format.space_after = Pt(14)
    r = s.add_run("Odoo für die biotec GmbH  ·  Verstehen, wo Sie stehen – "
                  "und prüfen, ob und wie Odoo Sie weiterbringt.")
    r.font.size = Pt(11)
    r.font.color.rgb = GREY

    # Metadaten
    table(doc,
          ["Feld", "Eintrag"], [4.5, 12.5],
          [["Datum / Uhrzeit", ""],
           ["Dauer (geplant 45–60 Min.)", ""],
           ["Ort / Tool", ""],
           ["Teilnehmer biotec", ""],
           ["Teilnehmer CertoClav", "Michael Simon (Consultant & SPOC)"],
           ["Weitere Teilnehmer (Certania)", ""],
           ["Protokoll", "Michael Simon"],
           ["Aufzeichnung", "☐ ja   ☐ nein   (Einverständnis eingeholt: ☐ ja  ☐ nein)"]])

    # 0 Kernaussagen
    heading(doc, "Kernaussagen des Gesprächs", kicker="Zusammenfassung – nach dem Termin ausfüllen")
    note(doc, "Drei bis fünf Sätze: Ausgangslage, wichtigste Erkenntnis, Einschätzung Machbarkeit.")
    answer_lines(doc, 5)

    # 1 CertoClav & Ansatz
    heading(doc, "1 · CertoClav & unser Ansatz", kicker="Agenda 01 – ca. 10 Min.")
    note(doc, "Vorgestellt: SPOC auf Beraterseite, Einrichtung + Datenimport durch CertoClav "
              "mit Claude, iterative Feedbackrunden, Train-the-Trainer.")
    question(doc, "Reaktionen, Rückfragen, Bedenken zum Arbeitsmodell",
             "(z. B. SPOC-Rolle, KI-Einsatz, Datenschutz, Verfügbarkeit)", lines=3)

    # 2 Firmenprofil
    heading(doc, "2 · Firmenprofil-Check", kicker="Deck-Folie „Was wir über biotec wissen“")
    note(doc, "Unsere Annahmen aus biotec-gmbh.com – Korrekturen und Ergänzungen festhalten.")
    table(doc,
          ["Annahme", "Bestätigt?", "Korrektur / Ergänzung"], [6.0, 2.6, 8.4],
          [["Bundesweites Hygieneinstitut, VDI-Schulungspartner (VDI 6022 / 2047)", "☐ ja ☐ nein", ""],
           ["Inspektionen vor Ort: RLT-Anlagen, Verdunstungskühlanlagen, Luftentkeimung", "☐ ja ☐ nein", ""],
           ["Beratung & Gefährdungsbeurteilungen (Trinkwasser-, Krankenhaushygiene)", "☐ ja ☐ nein", ""],
           ["Bundesweite VDI-Schulungen, Termine online buchbar", "☐ ja ☐ nein", ""],
           ["Labor & Forschung, Entwicklung neuer Analyseverfahren", "☐ ja ☐ nein", ""],
           ["Standort Gütersloh (Elbrachtsweg 76, 33332)", "☐ ja ☐ nein", ""]])
    question(doc, "Was haben wir übersehen? Was ist am wichtigsten – was läuft heute schon gut?", lines=3)

    # 3 Discovery 1/3
    heading(doc, "3 · Schmerzpunkte & Ziele", kicker="Discovery 1/3")
    for q, hint in [
        ("Warum sprechen wir gerade jetzt über ein ERP?", None),
        ("Was funktioniert heute nicht – oder nur mit viel Handarbeit?",
         "(Doppelerfassung, Zettelwirtschaft, Excel-Inseln)"),
        ("Wo geht im Alltag am meisten Zeit verloren?",
         "(Einsatzplanung, Berichte, Rechnungsstellung, Kursorganisation)"),
        ("Was ist der Auslöser, das jetzt anzugehen?",
         "(Wachstum, Personalwechsel, Kundenanforderungen, Altsystem)"),
        ("Woran würden Sie in 12 Monaten festmachen, dass sich das Projekt gelohnt hat?", None),
        ("Was soll auf keinen Fall schlechter werden als heute?", None),
    ]:
        question(doc, q, hint)

    # 4 Discovery 2/3
    heading(doc, "4 · Prozesse, Systeme & Daten", kicker="Discovery 2/3")
    note(doc, "Basis für Scoping, Phasierung und den Claude-gestützten Datenimport.")
    for q, hint in [
        ("Welche Software ist heute im Einsatz – und wofür?",
         "(Buchhaltung/DATEV, Planung, Labor, Kursbuchung, Office)"),
        ("Wie läuft ein Auftrag heute durch – von der Anfrage bis zur Rechnung?",
         "(Inspektion, Beratung, Schulung im Vergleich)"),
        ("Welche Daten liegen vor – und in welcher Qualität?",
         "(Kunden, Anlagen/Objekte, Prüfberichte, Vorlagen, Kurskatalog)"),
        ("Wie arbeiten die Prüfer vor Ort?",
         "(mobil/offline, Checklisten, Fotos, Unterschriften, Berichtserstellung)"),
        ("Welche Systeme müssen bleiben und angebunden werden – was darf Odoo ersetzen?", None),
    ]:
        question(doc, q, hint)

    doc.add_page_break()

    # 5 App-Hypothese
    heading(doc, "5 · App-Hypothese validieren", kicker="Deck-Folie „Odoo-Apps für biotec“")
    table(doc,
          ["Odoo-App", "Zweck (Hypothese)", "Relevant?", "Anmerkung"], [3.6, 5.4, 2.6, 5.4],
          [["CRM & Verkauf", "Anfragen, Angebote & Aufträge", "☐ ja ☐ nein ☐ offen", ""],
           ["Rechnungsstellung", "Rechnungen & Zahlungen", "☐ ja ☐ nein ☐ offen", ""],
           ["Einkauf & Lager", "Labor- & Prüfmaterial", "☐ ja ☐ nein ☐ offen", ""],
           ["Außendienst", "Einsatzplanung & Prüfberichte vor Ort", "☐ ja ☐ nein ☐ offen", ""],
           ["Projekte & Zeiterfassung", "Beratungsaufträge & Gutachten", "☐ ja ☐ nein ☐ offen", ""],
           ["Veranstaltungen & E-Learning", "VDI-Schulungen inkl. Online-Buchung", "☐ ja ☐ nein ☐ offen", ""],
           ["Abonnements", "Wiederkehrende Prüfintervalle & Verträge", "☐ ja ☐ nein ☐ offen", ""],
           ["Qualität & Dokumente", "Proben, Berichte & Nachweise", "☐ ja ☐ nein ☐ offen", ""],
           ["Buchhaltung", "Finanzbuchhaltung, DATEV-Anbindung", "☐ ja ☐ nein ☐ offen", ""],
           ["Produktion", "bewusst nicht eingeplant – klären", "☐ ja ☐ nein ☐ offen", ""],
           ["Website / E-Commerce", "bewusst nicht eingeplant – klären", "☐ ja ☐ nein ☐ offen", ""],
           ["Weitere:", "", "☐ ja ☐ nein ☐ offen", ""]])

    # 6 Certania-Anforderungen
    heading(doc, "6 · Anforderungen Finance / Certania-Gruppe", kicker="Ergänzung zum Deck")
    note(doc, "Aus dem Gruppen-Strang (Jeannette Bühler, Head of Group Accounting): "
              "vollintegriertes P2P/O2C und POC-/WIP-Bewertung. Klären, ob das zum Scope gehört.")
    for q, hint in [
        ("Gehören die Gruppenanforderungen (P2P/O2C, POC/WIP) zum biotec-Projekt – oder separat?", None),
        ("Welche Anforderungen bestehen an das Reporting Package der Gruppe?",
         "(Inhalte, Frequenz, Empfänger, Format)"),
        ("Laufen mehrjährige/mehrmonatige Projekte, die nach Fertigstellungsgrad bewertet werden?",
         "(Festpreis, Meilensteinabrechnung, Fremdlabor)"),
        ("Bilanzierung nach HGB, IFRS oder beidem? Wer ist Steuerberater / Wirtschaftsprüfer?", None),
    ]:
        question(doc, q, hint)

    # 7 Discovery 3/3
    heading(doc, "7 · Team, Zeitrahmen & Budget", kicker="Discovery 3/3")
    for q, hint in [
        ("Wer wäre Ihr Hauptansprechpartner für die Iterationen?",
         "(stimmt Feedbackrunden ab, schult später intern)"),
        ("Wie viel Zeit kann diese Person pro Woche realistisch einbringen?",
         "(Richtwert: wenige Stunden für Demos & Freigaben)"),
        ("Wie viele Mitarbeiter würden mit Odoo arbeiten?",
         "(Innendienst, Prüfer, Labor, Verwaltung)"),
        ("Gibt es einen Wunschtermin für den Go-live – und was treibt ihn?", None),
        ("In welchem Budgetrahmen bewegen wir uns – und wer entscheidet?",
         "(Basis für Scoping & Phasierung, keine Festlegung heute)"),
    ]:
        question(doc, q, hint)

    # 8 Nächste Schritte
    heading(doc, "8 · Nächste Schritte & Aufgaben", kicker="Deck-Folie „Nächste Schritte“")
    table(doc,
          ["Nr.", "Aufgabe", "Wer", "Termin", "Status"], [1.2, 8.0, 3.0, 2.4, 2.4],
          [["1", "Zusammenfassung / Protokoll des Discovery Calls versenden", "CertoClav", "", "☐ offen"],
           ["2", "Beispielhafte Rohdaten & Vorlagen teilen (keine Aufbereitung nötig)", "biotec", "", "☐ offen"],
           ["3", "Scoping & Angebot: Phasierung, Aufwandsschätzung, Budgetbasis", "CertoClav", "", "☐ offen"],
           ["4", "Entscheidung & Kick-Off: Hauptansprechpartner benennen, Termin", "Gemeinsam", "", "☐ offen"],
           ["5", "", "", "", "☐ offen"],
           ["6", "", "", "", "☐ offen"],
           ["7", "", "", "", "☐ offen"]])

    # 9 Offene Punkte
    heading(doc, "9 · Offene Punkte & Risiken")
    note(doc, "Was im Termin nicht geklärt werden konnte – inkl. wer es klärt.")
    table(doc,
          ["Offener Punkt", "Klärt", "Bis"], [11.0, 3.0, 3.0],
          [["", "", ""] for _ in range(6)])

    # 10 Interne Notizen
    heading(doc, "10 · Interne Notizen", kicker="Nicht Teil des Kundenprotokolls")
    note(doc, "Einschätzung Machbarkeit, Aufwandstreiber, Stakeholder-Dynamik, Preisindikation. "
              "Vor dem Versand an den Kunden entfernen.")
    answer_lines(doc, 6)

    doc.save(path)
    print(f"geschrieben: {path}")


if __name__ == "__main__":
    build(sys.argv[1] if len(sys.argv) > 1 else "Protokoll_Discovery_Call.docx")

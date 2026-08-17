# Arbeitshinweise für Claude

Dieses Repository ist die **Projektablage** für das Odoo-Einführungsprojekt bei der biotec GmbH
(Certania-Gruppe), durchgeführt von CertoClav Consulting. Es enthält **keinen Anwendungscode** –
die Skripte unter `06_Arbeitsdateien/skripte/` sind Werkzeuge (Dokumentgenerierung,
Datenaufbereitung, Odoo-Zugriff).

## Sprache

Alles auf **Deutsch**: Dokumente, Commit-Messages, Kommentare. Deutsche Anführungszeichen
(„…"), korrekte Umlaute – auch in generierten Word-Dokumenten, die zum Kunden gehen.

## Ablage – wohin gehört was

| Inhalt | Ziel |
|---|---|
| Projektstand, Rollen, Entscheidungen, offene Fragen | `01_Projektsteuerung/` |
| Meetingprotokoll | `02_Meetings/JJJJ-MM-TT_thema.docx` |
| Kundenpräsentation | `03_Praesentationen/JJJJ-MM-TT_Termin/` (Termindatum!) |
| Ausgehendes Kundendokument | `04_Kundendokumente/` |
| Vom Kunden geliefertes | `05_Rohdaten_Kunde/00_eingang/<Block A–L>/JJJJ-MM-TT_Position_name.ext` |
| Interne Arbeitsdatei, Skript, Import-Vorlage | `06_Arbeitsdateien/` |
| Fachkonzept, Architektur | `07_Fachkonzepte/` |

Jeder Ordner hat ein `README.md` mit seinen Regeln – vor dem Ablegen dort nachsehen.

## Regeln

1. **Originale nicht umschreiben.** Quelldokumente in `_quellen/` und Rohdaten in
   `00_eingang/` bleiben unverändert. Konsolidierte Stände entstehen als eigene Datei
   (`01_Projektsteuerung/projektstatus.md`).
2. **Word-Vorlagen per Skript.** Dokumentvorlagen werden mit `python-docx` generiert, nicht
   von Hand gepflegt. Änderungswunsch → Skript in `06_Arbeitsdateien/skripte/` anpassen → neu
   generieren. Benötigt: `pip install python-docx pypdf`.
3. **Intern vs. kundenfähig trennen.** `04_Kundendokumente/` ist kundenfähig – keine
   Aufwandsschätzungen, keine Preisindikationen, keine Stakeholder-Bewertungen. Interne
   Aufwandsrichtwerte stehen in `07_Fachkonzepte/wissensstand-odoo-certania-biotec.md`
   (Abschnitt 6) und bleiben dort.
4. **Keine personenbezogenen Daten und keine Zugangsdaten committen.** Die Git-Historie ist
   dauerhaft. Bei Unsicherheit fragen, nicht committen.
5. **Ergebnisse zurückschreiben.** Nach jedem Termin: neue Erkenntnisse in `projektstatus.md`,
   beantwortete Fragen in `offene-fragen.md` abhaken, Festlegungen in `entscheidungslog.md`
   ergänzen (Zeilen anhängen, nicht überschreiben).

## Faktenlage

Fakten nur aus den Dokumenten im Repo, nicht aus Annahmen. Unbekanntes bleibt als **offen**
markiert – insbesondere: das Altsystem bei biotec, der Scope der POC/WIP-Anforderung, das
Budget und der Hauptansprechpartner. Siehe `01_Projektsteuerung/offene-fragen.md`.

## Branch

Entwicklung auf `claude/odoo-biotec-projekt-1ercyw`.

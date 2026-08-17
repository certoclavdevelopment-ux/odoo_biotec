# Odoo-Einrichtungsprojekt biotec GmbH (Certania-Gruppe)

Projektablage für das Odoo-Einführungsprojekt bei der **biotec GmbH**, Gütersloh –
durchgeführt von **CertoClav Consulting** (Michael Simon, Consultant & SPOC).

> **Interne Ablage.** Dieses Repository enthält interne Arbeitsstände, Aufwandsschätzungen
> und Kundenrohdaten. Nicht als Ganzes mit dem Kunden teilen. Kundenfähige Dokumente
> liegen ausschließlich in `04_Kundendokumente/`.

## Struktur

| Ordner | Inhalt |
|---|---|
| `01_Projektsteuerung/` | Projektstatus, Beteiligte & Rollen, Entscheidungslog, offene Fragen. Originalquellen unter `_quellen/`. |
| `02_Meetings/` | Meetingprotokolle, chronologisch. Vorlage: `_VORLAGE_Protokoll_Discovery_Call.docx`. |
| `03_Praesentationen/` | Kundenpräsentationen als PDF, **ein Ordner je Termin** (`JJJJ-MM-TT_Termin/`). |
| `04_Kundendokumente/` | Kundenfähige Dokumente: Konzepte, Fragebögen, Angebote. |
| `05_Rohdaten_Kunde/` | Vom Kunden gelieferte Rohdaten. `00_eingang/` unverändert, `01_aufbereitet/` importfertig. |
| `06_Arbeitsdateien/` | Interne Arbeitsdateien: Import-Vorlagen, Analysen, Skripte. |
| `07_Fachkonzepte/` | Fachlicher Wissensstand, Architektur- und Lösungskonzepte. |

## Einstieg

1. [`01_Projektsteuerung/projektstatus.md`](01_Projektsteuerung/projektstatus.md) – aktueller Stand, Scope, Zeitplan
2. [`01_Projektsteuerung/offene-fragen.md`](01_Projektsteuerung/offene-fragen.md) – was noch geklärt werden muss
3. [`07_Fachkonzepte/wissensstand-odoo-certania-biotec.md`](07_Fachkonzepte/wissensstand-odoo-certania-biotec.md) – fachliche Basis (P2P/O2C, POC/WIP)

## Konventionen

- **Dateinamen:** Protokolle und datierte Dokumente mit ISO-Datum voran: `JJJJ-MM-TT_thema.md`.
- **Präsentationen nach Datum:** je Termin ein Ordner `JJJJ-MM-TT_Terminbezeichnung/` unter
  `03_Praesentationen/`. Das Datum ist das **Termindatum**, nicht das Erstellungsdatum. Ein
  überarbeitetes Deck bekommt einen neuen Datumsordner – so bleibt belegbar, was wann gezeigt
  wurde. Details in `03_Praesentationen/README.md`.
- **Sprache:** Deutsch, auch in Commit-Messages und Dokumenten.
- **Originale nicht überschreiben:** Vom Kunden gelieferte Dateien bleiben in
  `05_Rohdaten_Kunde/00_eingang/` unverändert. Bearbeitete Stände kommen nach `01_aufbereitet/`.
- **Ein Thema, ein Dokument:** Der konsolidierte Stand steht in `projektstatus.md`;
  Ursprungsdokumente bleiben als Quelle erhalten und werden nicht nachträglich umgeschrieben.

## Datenschutz

Kundenrohdaten können personenbezogene Daten enthalten (Kundenkontakte, Teilnehmerlisten
der VDI-Schulungen, Prüfberichte). Vor dem Commit prüfen:

- Nur Daten ablegen, die für die Migration tatsächlich gebraucht werden.
- Keine Zugangsdaten, API-Keys oder Passwörter – auch nicht in Import-Vorlagen.
- **Git-Historie ist dauerhaft.** Ein `git rm` entfernt eine Datei nicht aus der Historie.
  Im Zweifel vorher fragen statt committen.

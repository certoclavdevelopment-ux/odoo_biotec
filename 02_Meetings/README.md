# Meetings & Protokolle

Ablage chronologisch, ein Protokoll je Termin: `JJJJ-MM-TT_thema.docx` bzw. `.md`.

## Vorlagen

| Vorlage | Zweck |
|---|---|
| `_VORLAGE_Protokoll_Discovery_Call.docx` | Discovery Call. Struktur folgt 1:1 der Discovery-Präsentation: Firmenprofil-Check, Schmerzpunkte & Ziele, Prozesse/Systeme/Daten, App-Hypothese, Finance/Certania, Team/Zeit/Budget, nächste Schritte, offene Punkte. |

Erzeugt durch `06_Arbeitsdateien/skripte/protokoll_vorlage_discovery.py` – Änderungen an der
Vorlage dort machen und neu generieren, damit die Struktur reproduzierbar bleibt.

## Ablauf je Termin

1. Vorlage kopieren, mit Termindatum benennen: `2026-08-17_discovery-call.docx`.
2. Im Termin direkt mitschreiben (die Fragen stehen in der Reihenfolge des Decks).
3. Nach dem Termin: Abschnitt „Kernaussagen" ausfüllen, Aufgaben mit Verantwortlichen und
   Terminen vervollständigen.
4. **Abschnitt „Interne Notizen" löschen**, bevor das Protokoll an den Kunden geht.
5. Ergebnisse übertragen: neue Erkenntnisse → `01_Projektsteuerung/projektstatus.md`,
   beantwortete Fragen → `offene-fragen.md`, Festlegungen → `entscheidungslog.md`.

## Bestand

| Datum | Termin | Protokoll | Präsentation |
|---|---|---|---|
| 04.–05.08.2026 | E-Mail-Abstimmung Projektstart | `01_Projektsteuerung/_quellen/2026-08-17_biotec-erp-projekt-emailstand.md` | – |
| 17.08.2026 | Discovery Call biotec × CertoClav, 12:30–13:30, Teams | `2026-08-17_discovery-call.docx` (ausgefüllt) + `..._rohnotizen.md` (Mitschrift im Original) | `03_Praesentationen/2026-08-17_Discovery_Call/` |

Das Protokoll für den 17.08. wurde aus dem Generator erzeugt:
`python3 06_Arbeitsdateien/skripte/protokoll_vorlage_discovery.py <ziel.docx> 2026-08-17`.
Termindaten (Metadaten, Teilnehmerliste) stehen im Dict `TERMINE` im Skript – für weitere
Termine dort einen Eintrag ergänzen.

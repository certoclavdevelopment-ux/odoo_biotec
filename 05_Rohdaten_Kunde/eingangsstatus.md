# Eingangsstatus der Datenanforderung

Interne Nachverfolgung zu `04_Kundendokumente/Datenanforderung_biotec.docx` (Dok.-Nr.
DATA-2026-001). Beim Eingang: Datum eintragen, Ablageort ergänzen, Status setzen.
Gelieferte Dateien kommen unverändert nach `00_eingang/JJJJ-MM-TT_quelle/`.

Status: `offen` · `angefragt` · `eingegangen` · `geprüft` · `entfällt`

## Paket 1 – für Scoping und Aufwandsschätzung

| Nr. | Inhalt | Wer | Status | Eingang | Ablage / Bemerkung |
|---|---|---|---|---|---|
| A1 | Kundenliste | N. Krupa | offen | | |
| A3 | Lieferantenliste inkl. Fremdlabore | A. Krupa | offen | | |
| B1 | Anlagen-/Objektstamm | M. Brand | offen | | |
| B2 | Beispiel-Anlagenlisten (Datei + Ausdruck) | M. Brand | offen | | |
| D1 | Gutachten je Berichtstyp (PDF) | M. Brand | offen | | |
| D2 | Vorlagendateien des Gutachtenprogramms | Westbomke | offen | | |
| D3 | Belegmuster (Angebot, AB, LS, Rechnung, Mahnung) | N. Krupa | offen | | |
| D4 | Briefpapier, Logo als Vektor, CI | N. Krupa | offen | | |
| E1 | Angebote & Auftragsbestätigungen | N. Krupa | offen | | |
| E2 | Ausgangsrechnungen | N. Krupa | offen | | |
| E4 | Verträge (Rahmen, Wartung, Prüfung) | M. Brand | offen | | |
| F1 | Artikelliste mit Bestand | A. Krupa | offen | | |
| G1 | Kurskatalog | N. Krupa | offen | | |
| H1 | Vollständiger Kontenrahmen | A. Krupa | offen | | |
| I1 | Datenbanksystem, Version, Schema | Westbomke | offen | | |
| I2 | Datenbank-Sicherung / Vollexport | Westbomke | offen | | |
| I4 | Schnittstellenliste | Westbomke | offen | | |
| I5 | Screenshots der Hauptmasken | M. Brand | offen | | |
| J3 | Endgeräte & Netzabdeckung vor Ort | Westbomke | offen | | |
| K1 | Handelsregisterauszüge, Gesellschaftsstruktur | Wilke / Bermpohl | offen | | |

## Paket 2 und 3

Die restlichen 40 Positionen (A2, B3–B4, C1–C4, D5, E3, E5–E6, F2–F3, G2–G7, H2–H8,
I3, I6–I7, J1–J2, J4–J5, K2–K5, L1–L3) laufen nach dem Scoping nach. Vollständige Liste
im Kundendokument.

## Hinweise zur Ablage

- **Datenbanksicherungen und Quellcode gehören nicht in dieses Repository.** Sie sind zu
  groß und enthalten Kundendaten; `.gitignore` blockt `*.sql`, `*.dump` und `*.zip` bereits.
  Getrennt ablegen und hier nur den Ablageort notieren.
- Teilnehmerlisten und andere personenbezogene Daten: anonymisierte Fassung anfordern.
  Wenn nur Klardaten kommen, nicht committen – siehe `README.md` in diesem Ordner.
- Je Lieferung eine kurze `LIEFERUNG.md` im Eingangsordner: wer, wann, welches Quellsystem,
  Auffälligkeiten.

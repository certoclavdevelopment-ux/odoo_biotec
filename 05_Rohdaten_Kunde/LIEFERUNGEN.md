# Lieferungen

Protokoll aller vom Kunden gelieferten Daten. Ersetzt die Ablage nach Lieferdatum: die
Dateien liegen nach Block sortiert, die Herkunft steht hier.

**Je Lieferung eine Zeile anhängen, nichts überschreiben.**

| Eingang | Von | Positionen | Dateien | Quellsystem | Auffälligkeiten |
|---|---|---|---|---|---|
| | | | | | |

## Felder

- **Eingang** – Datum, an dem die Datei bei uns angekommen ist (ISO: JJJJ-MM-TT).
- **Von** – Person, die geliefert hat. Läuft über Michael Brand oder Nicole Krupa.
- **Positionen** – Kennungen aus der Datenanforderung, z. B. `B1, B2`.
- **Dateien** – Anzahl und Ablageort, z. B. `3 Dateien → 00_eingang/B_Anlagen_Objekte/`.
- **Quellsystem** – woraus exportiert wurde: Delphi-Anwendung, Gutachtenprogramm, Excel,
  Buchhaltung, manuell erstellt.
- **Auffälligkeiten** – leere Felder, Umlautprobleme, Dubletten, abgeschnittene Spalten,
  fehlende Kopfzeile, unklare Bedeutung einzelner Spalten. Kurz notieren, nicht ausformulieren –
  das ist die Grundlage für die Rückfragen an biotec.

## Beispielzeile

| Eingang | Von | Positionen | Dateien | Quellsystem | Auffälligkeiten |
|---|---|---|---|---|---|
| 2026-08-20 | M. Brand | B1, B2 | 3 → `00_eingang/B_Anlagen_Objekte/` | Delphi-Anwendung | Anlagentyp als Freitext, keine Codeliste; Prüfintervall teilweise leer |

## 2026-08-31 · Sichtung des Upload-Ordners (biotec meldet Upload abgeschlossen)

Gesichtet über den Microsoft-365-Zugriff auf `Certania/Odoo Biotec Rohdaten`, keine
Dateien ins Repo übernommen. Gesamtvolumen rund 193 MB in 10 der 11 Ordner.

**Eingegangen (Paket 1):** A1 (mit Einschränkung), B1, B2, D1, D2, D3, D4, E1, E2, E4,
G1, K1. **Offen:** A3, F1, H1, I4, J3. **Ungeklärt:** I1 und I2 – stecken vermutlich in
`Current-2026-08-22.zip` (27,5 MB), das über den M365-Zugriff nicht lesbar ist.
**Entfällt:** I5, ersetzt durch die Fernwartungssitzung.

**Leer:** `03 Labor (C)`, `06 Artikel und Lager (F)`, `11 Sonstiges und Fragen`.
`08 Buchhaltung (H)` enthält nur die Notiz „SKR04 mit Sachkontenlänge 4".

Details je Position in `eingangsstatus.md`.

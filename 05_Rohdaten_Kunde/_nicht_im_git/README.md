# Dateien außerhalb des Repositories

Dieser Ordner enthält **keine Daten**, nur die Notiz, wo große oder heikle Lieferungen
liegen. Grund: Die Git-Historie ist dauerhaft, und Datenbanksicherungen wie Quellcode haben
darin nichts zu suchen.

## Verweisliste

| Position | Inhalt | Ablageort | Eingang | Zugriff über |
|---|---|---|---|---|
| I2 | Datenbanksicherung Delphi-Anwendung | | | |
| I3 | Quellcode hauseigene Software | | | |
| | | | | |

## Was hier hin gehört

- **I2 – Datenbanksicherung**: Größe im GB-Bereich, enthält den vollständigen Kundendatenstamm.
- **I3 – Quellcode**: fremdes geistiges Eigentum, ggf. unter Vertraulichkeitsvereinbarung
  übergeben. Nicht in ein Repository kopieren, auf das mehrere Personen Zugriff haben.
- Große Bild- und Fotobestände aus Prüfberichten.

## Regeln

- Ablage auf dem CertoClav-Projektlaufwerk bzw. im geteilten Projektordner, nicht lokal auf
  einem Notebook.
- Zugriff nur für die Personen, die an der Migration arbeiten.
- Nach Projektende gemäß Vereinbarung löschen und den Ablageort hier als `gelöscht`
  markieren.
- Falls eine Vertraulichkeitsvereinbarung existiert: Ablageort und Aufbewahrungsfrist hier
  vermerken.

`.gitignore` blockt `*.sql`, `*.dump`, `*.zip` und `*credentials*` bereits – trotzdem vor
jedem Commit prüfen, was tatsächlich eingecheckt wird.

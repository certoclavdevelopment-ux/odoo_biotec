# Kundendaten – Verwaltung

**Die Rohdaten selbst liegen nicht hier, sondern in OneDrive.** Dieser Ordner enthält nur
die Nachverfolgung: was wurde angefordert, was ist eingegangen, wie wird es auf Odoo
abgebildet.

Grund: Die Daten enthalten personenbezogene und teils sicherheitsrelevante
Kundeninformationen (Ansprechpartner in Kliniken, Schulungsteilnehmer, Prüfberichte). Die
Git-Historie ist dauerhaft – was einmal eingecheckt ist, bleibt drin. In OneDrive lässt sich
der Zugriff steuern und am Projektende löschen.

## Was liegt wo

| Inhalt | Ort |
|---|---|
| Rohdaten von biotec, unverändert | OneDrive: `Certania\Odoo Biotec Upload biotec\` (für biotec freigegeben) |
| Sortierte Rohdaten, Arbeitsstände | OneDrive: `Certania\Odoo Biotec Rohdaten\` (nur CertoClav) |
| Importfertige Dateien | OneDrive: `Certania\Odoo Biotec Rohdaten\01_aufbereitet\` |
| Datenbanksicherung, Quellcode Altsystem | OneDrive: `…\99_nicht_im_repository\` – nie ins Repo |
| Statusliste, Lieferprotokoll, Feldzuordnungen | **hier im Repo** |

## Dateien in diesem Ordner

| Datei | Zweck |
|---|---|
| `eingangsstatus.md` | Statusliste je Position der Datenanforderung |
| `LIEFERUNGEN.md` | Protokoll: wer hat wann was geliefert, mit Auffälligkeiten |
| `_mapping/` | Feldzuordnung Quelle → Odoo je Modell, Transformationsnotizen |

Das Mapping gehört ins Repo, weil es **Dokumentation** ist und keine Kundendaten enthält –
nur Feldnamen und Umformungsregeln. Es ist der Nachweis, wenn später Zahlen nicht stimmen.

## OneDrive-Struktur

### Freigegeben an biotec – `Odoo Biotec Upload biotec\`

Bewusst in Alltagssprache, ohne interne Kürzel. Die Buchstaben in Klammern verweisen auf die
Blöcke der Datenanforderung.

```
00_BITTE_ZUERST_LESEN.txt
01 Kunden und Lieferanten (A)
02 Anlagen und Objekte (B)
03 Labor (C)
04 Gutachten und Vorlagen (D)
05 Angebote, Rechnungen, Vertraege (E)
06 Artikel und Lager (F)
07 Schulungen (G)
08 Buchhaltung (H)
09 IT und Altsystem (I+J)
10 Firma und Organisation (K)
11 Sonstiges und Fragen
```

Die Anleitung für die Ordnerwurzel liegt als `04_Kundendokumente/00_BITTE_ZUERST_LESEN.txt`
im Repo und wird von dort nach OneDrive kopiert. Anlegen der Ordner:
`06_Arbeitsdateien/skripte/onedrive_ordner_anlegen.cmd`.

### Nur CertoClav – `Odoo Biotec Rohdaten\`

```
00_eingang\            aus dem Upload-Ordner übernommen, nach Blöcken A–L
01_aufbereitet\        importfertig, nach Importreihenfolge
99_nicht_im_repository\  Datenbanksicherung, Quellcode
```

Beim Übernehmen aus dem Upload-Ordner umbenennen nach
`JJJJ-MM-TT_Position_kurzbeschreibung.ext`, z. B.
`2026-08-20_B1_anlagenstamm_export.csv`. Das Datum ist das Eingangsdatum, die Position die
Kennung aus der Datenanforderung. Damit ist jede Datei eindeutig einer Anforderung zugeordnet.

## Ablauf bei einer Lieferung

1. biotec lädt in den freigegebenen Ordner.
2. Dateien in den CertoClav-Ordner übernehmen und nach Schema umbenennen – das Original im
   Upload-Ordner liegen lassen.
3. Zeile in `LIEFERUNGEN.md` ergänzen (hier im Repo).
4. Status in `eingangsstatus.md` auf `eingegangen`, nach Sichtung auf `geprüft`.
5. Aufbereitung in OneDrive unter `01_aufbereitet\`; Feldzuordnung nach `_mapping/` hier im Repo.

## Regel

**Keine Kundendaten ins Repository.** Wenn für ein Fachkonzept ein Beispiel gebraucht wird:
anonymisierter Auszug mit Testnamen, wenige Zeilen. `.gitignore` blockt `*.sql`, `*.dump`,
`*.zip` und `*credentials*` – das ist ein Netz, kein Ersatz für Nachdenken vor dem Commit.

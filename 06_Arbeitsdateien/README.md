# Arbeitsdateien

Interne Arbeitsstände. Nichts hier ist kundenfähig.

```
import-vorlagen/   Odoo-Importvorlagen (CSV/XLSX) zum Befüllen durch biotec
analysen/          Auswertungen, Mappings, Prozessvergleiche, Notizen
skripte/           Python-Skripte: Datenaufbereitung, Dokumentgenerierung, Odoo-Zugriff
```

## Bestand

| Datei | Zweck |
|---|---|
| `skripte/docx_bausteine.py` | Gemeinsame Word-Bausteine: Layout, Farben, Kopf-/Fußzeile, Tabellen, Aufzählungen. Von allen Dokumentgeneratoren importiert. |
| `skripte/protokoll_vorlage_discovery.py` | Protokolle zum Discovery Call – leere Vorlage oder mit Termindaten gefüllt (`… <ziel.docx> 2026-08-17`). |
| `skripte/datenanforderung.py` | `04_Kundendokumente/Datenanforderung_biotec.docx` – Liste der vom Kunden benötigten Unterlagen. |
| `skripte/onedrive_ordner_anlegen.cmd` | Legt die beiden OneDrive-Ordner an: den für biotec freigegebenen Upload-Ordner und den internen Arbeitsordner. Auf dem Windows-Rechner ausführen. |

## Konventionen

- **Dokumentvorlagen werden per Skript generiert**, nicht von Hand in Word gepflegt. So
  bleiben Struktur und Layout reproduzierbar und der Diff nachvollziehbar. Änderungswunsch →
  Skript anpassen → neu generieren.
- Skripte mit Odoo-Zugriff: Zugangsdaten **nur** über Umgebungsvariablen, niemals im Code.
- Benötigte Pakete: `python-docx` (Word), `pypdf` (PDF-Textextraktion).

## Import-Vorlagen

Vorlagen entstehen erst, wenn nach dem Discovery Call klar ist, welche Objekte migriert
werden. Regel: eine Datei je Odoo-Modell, erste Zeile mit den technischen Feldnamen, zweite
Zeile mit einer Beispielzeile als Ausfüllhilfe.

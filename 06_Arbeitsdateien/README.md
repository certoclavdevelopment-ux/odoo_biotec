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
| `skripte/protokoll_vorlage_discovery.py` | Generiert `02_Meetings/_VORLAGE_Protokoll_Discovery_Call.docx`. Struktur folgt der Discovery-Präsentation. |

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

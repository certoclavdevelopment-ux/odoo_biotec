# Rohdaten Kunde

Vom Kunden gelieferte Daten. Grundlage für den Datenimport nach Odoo.

```
00_eingang/      Original wie geliefert – niemals bearbeiten
01_aufbereitet/  bereinigte, importfertige Stände
```

## Ablage

- **`00_eingang/`**: Unterordner je Lieferung, `JJJJ-MM-TT_quelle/`
  (z. B. `2026-08-20_export-altsystem/`). Dateien unverändert lassen, auch wenn sie
  chaotisch sind – sie sind der Beleg für den Ausgangszustand.
- **`01_aufbereitet/`**: Ergebnis der Bereinigung, benannt nach Odoo-Zielobjekt
  (`res.partner.csv`, `product.template.csv`, …). Das Skript oder die Schritte, die von
  `00_eingang` nach `01_aufbereitet` führen, gehören nach `06_Arbeitsdateien/skripte/`.
- Je Lieferung eine kurze `LIEFERUNG.md`: Wer hat wann was geliefert, welches Quellsystem,
  welche Auffälligkeiten.

## Erwartete Datenarten (Hypothese – im Discovery Call bestätigen)

| Datenart | Odoo-Ziel |
|---|---|
| Kunden & Kontakte | Kontakte (`res.partner`) |
| Anlagen / Objekte (RLT-Anlagen, Kühlanlagen je Standort) | Ausrüstung / Anlagen, ggf. eigenes Modell |
| Leistungen & Preise (Inspektion, Beratung, Analysen, Schulungen) | Produkte |
| Prüfberichte & Vorlagen | Dokumente / Berichtsvorlagen |
| Kurskatalog & Termine, Teilnehmerlisten | Veranstaltungen |
| Offene Aufträge, laufende Projekte | Verkauf / Projekte |
| Lieferanten (u. a. Fremdlabore) | Kontakte / Einkauf |
| Kontenrahmen, offene Posten | Buchhaltung |

## Datenschutz – vor jedem Commit prüfen

Diese Daten enthalten mit hoher Wahrscheinlichkeit **personenbezogene Daten**
(Ansprechpartner bei Kliniken, Schulungsteilnehmer, Prüferzuordnungen) und teils
sicherheitsrelevante Kundeninformationen aus Hygieneprüfungen.

- Nur ablegen, was für die Migration wirklich gebraucht wird.
- Keine Zugangsdaten, Tokens, Passwörter – auch nicht in Vorlagen oder Skripten.
- **Die Git-Historie ist dauerhaft.** Eine gelöschte Datei bleibt in der Historie.
  Bei Unsicherheit vor dem Commit abstimmen.
- Für Demos und Tests bevorzugt anonymisierte Auszüge verwenden.

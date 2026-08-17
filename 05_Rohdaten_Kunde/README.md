# Rohdaten Kunde

Vom Kunden gelieferte Daten und deren Aufbereitung für den Import nach Odoo.

```
05_Rohdaten_Kunde/
├── LIEFERUNGEN.md              Protokoll: wer hat wann was geliefert
├── eingangsstatus.md           Statusliste je Position der Datenanforderung
├── 00_eingang/                 Original wie geliefert – NIEMALS bearbeiten
│   ├── A_Kunden_Lieferanten/
│   ├── B_Anlagen_Objekte/
│   ├── C_Labor/
│   ├── D_Gutachten_Belege_Layout/
│   ├── E_Verkauf_Einkauf/
│   ├── F_Artikel_Lager/
│   ├── G_Schulungen/
│   ├── H_Buchhaltung_Finanzen/
│   ├── I_Altsystem_Delphi/
│   ├── J_IT_Infrastruktur/
│   ├── K_Organisation_Struktur/
│   ├── L_Certania_Gruppe/
│   └── ZZ_unsortiert/          Eingang, der noch nicht zugeordnet ist
├── 01_aufbereitet/             Bereinigt und importfertig
│   ├── 10_stammdaten/          Kontakte, Produkte, Konten, Anlagen
│   ├── 20_bestaende_offene_posten/   Lagerbestände, offene Posten, Salden
│   ├── 30_historie/            Altbelege, falls überhaupt migriert wird
│   └── _mapping/               Feldzuordnung Quelle → Odoo, Transformationsnotizen
└── _nicht_im_git/              Verweise auf große Dateien außerhalb des Repos
```

## Warum nach Blöcken und nicht nach Lieferdatum

Die Ordner **A bis L** entsprechen genau den Blöcken der Datenanforderung
(`04_Kundendokumente/Datenanforderung_biotec.docx`). Der Kunde wurde gebeten, in dieser
Struktur zu liefern – so landet alles am selben Ort, egal wie oft nachgeliefert wird.

Die **Herkunft** steckt stattdessen im Dateinamen und in `LIEFERUNGEN.md`. Das ist der
Kompromiss: Nach Datum sortiert findet man „alle Rechnungen" nie wieder, weil sie über fünf
Lieferungen verteilt sind. Nach Blöcken sortiert ist die Herkunft eine Zeile im Protokoll.

## Dateinamen im Eingang

```
JJJJ-MM-TT_Position_kurzbeschreibung.ext
```

Beispiele:

```
00_eingang/B_Anlagen_Objekte/2026-08-20_B1_anlagenstamm_export.csv
00_eingang/B_Anlagen_Objekte/2026-08-20_B2_anlagenliste_beispiel_ausdruck.pdf
00_eingang/D_Gutachten_Belege_Layout/2026-08-22_D1_gutachten_rlt_klinikum.pdf
00_eingang/H_Buchhaltung_Finanzen/2026-09-01_H1_kontenrahmen_skr04.xlsx
```

- **Datum** = Eingangsdatum, nicht das Erstellungsdatum der Datei.
- **Position** = Kennung aus der Datenanforderung (A1, B2, D1 …). Damit ist jede Datei
  eindeutig einer Anforderung zugeordnet und `eingangsstatus.md` bleibt pflegbar.
- Kommt eine Position mehrfach oder korrigiert, bleibt die alte Datei liegen; die neue
  bekommt das neue Datum. Nichts überschreiben.
- Passt eine Datei zu mehreren Positionen, in den Block der Hauptposition legen und in
  `LIEFERUNGEN.md` vermerken.

## Ablauf bei einer Lieferung

1. Dateien **unverändert** in den passenden Blockordner legen, nach obigem Schema umbenennen.
2. Nicht zuzuordnendes nach `ZZ_unsortiert/` – dieser Ordner soll leer laufen, nicht wachsen.
3. Zeile in `LIEFERUNGEN.md` ergänzen.
4. Status in `eingangsstatus.md` auf `eingegangen` setzen, nach der Sichtung auf `geprüft`.
5. Aufbereitung in `01_aufbereitet/` – als **neue** Datei, das Original bleibt unberührt.
   Das Skript oder die Schritte dazu gehören nach `06_Arbeitsdateien/skripte/`.

## 01_aufbereitet – nach Importreihenfolge

Die Nummerierung folgt der Reihenfolge, in der importiert werden muss: Stammdaten zuerst,
dann Bestände und offene Posten, Historie zuletzt. Eine Datei je Odoo-Modell, benannt nach
dem technischen Modellnamen:

```
01_aufbereitet/10_stammdaten/res.partner.csv
01_aufbereitet/10_stammdaten/product.template.csv
01_aufbereitet/10_stammdaten/account.account.csv
01_aufbereitet/_mapping/res.partner_mapping.md
```

In `_mapping/` steht je Modell, welches Quellfeld auf welches Odoo-Feld geht und welche
Umformungen nötig waren – das ist der Nachweis, wenn später Zahlen nicht stimmen.

## Was nicht ins Repository gehört

`_nicht_im_git/` enthält **keine** Daten, nur einen Verweis darauf, wo sie liegen:

- **Datenbanksicherungen** der Delphi-Anwendung (Position I2) – zu groß, voller Kundendaten.
- **Quellcode** der hauseigenen Software (Position I3) – fremdes geistiges Eigentum.
- Große Bilddatenbestände, Fotosammlungen aus Prüfberichten.

`.gitignore` blockt `*.sql`, `*.dump` und `*.zip` bereits. Bei Bedarf gezielt freigeben –
aber vorher überlegen, ob es wirklich in die dauerhafte Historie gehört.

## Datenschutz – vor jedem Commit prüfen

Die Daten enthalten mit hoher Wahrscheinlichkeit **personenbezogene Daten**: Ansprechpartner
bei Kliniken, Schulungsteilnehmer, Prüferzuordnungen. Teils auch sicherheitsrelevante
Kundeninformationen aus Hygieneprüfungen.

- Nur ablegen, was für die Migration wirklich gebraucht wird.
- Keine Zugangsdaten, Tokens oder Passwörter – auch nicht in Import-Vorlagen.
- **Die Git-Historie ist dauerhaft.** Ein `git rm` entfernt eine Datei nicht aus der Historie.
  Bei Unsicherheit vor dem Commit abstimmen.
- Für Demos und Tests anonymisierte Auszüge verwenden.

## Erwartete Datenarten je Block

| Block | Inhalt | Odoo-Ziel |
|---|---|---|
| A | Kunden, Lieferanten, Fremdlabore | Kontakte (`res.partner`) |
| B | Anlagen/Objekte, Anlagenlisten, Prüfpläne, Turnusregeln | Ausrüstung, ggf. eigenes Modell |
| C | Probenbegleitscheine, Analysemethoden, Grenzwerte | Qualität, Dokumente |
| D | Gutachten, Belegmuster, Vorlagendateien, CI-Material | Berichtsvorlagen |
| E | Angebote, Rechnungen, Verträge, Bestellungen, Reklamationen | Verkauf, Einkauf |
| F | Artikel mit Bestand, Rezepturen | Produkte, Lager |
| G | Kurskatalog, Seminarkalender, Zertifikate, Dozenten | Veranstaltungen |
| H | Kontenrahmen, Steuerschlüssel, offene Posten, Salden | Buchhaltung |
| I | Datenbankschema und -export, Schnittstellen, Screenshots | Migrationsquelle |
| J | Systemübersicht, M365, Endgeräte, Nutzerliste | Nutzer & Rechte |
| K | Handelsregister, Organigramm, Zeiterfassung | Unternehmensstruktur |
| L | Reporting Package, Konzernkontenplan, Intercompany | Gruppenanforderungen |

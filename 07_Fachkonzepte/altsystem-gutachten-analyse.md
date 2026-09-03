# Altsystem „Gutachten" – Analyse des Quellcodes und der Datenbank

*Stand: 01.09.2026. Grundlage: `Current-2026-08-22.zip`, geliefert von Westbomke EDV über den
OneDrive-Ordner. Ausgewertet wurde eine lokale Kopie außerhalb des Repos.*

**Dieses Dokument enthält keine Zugangsdaten, keinen Quellcode und keine Kundendaten.** Das
Archiv selbst bleibt in OneDrive – siehe `05_Rohdaten_Kunde/README.md`.

## 1. Das System in Zahlen

| Merkmal | Befund |
|---|---|
| Anwendung | Delphi-VCL-Anwendung `Gutachten.exe`, 11,7 MB |
| Delphi-Generation | ProjectVersion 18.2 (Delphi-10.3-Generation), VCL, Win32 |
| Umfang Quellcode | 255 Units mit zugehörigen Formularen, dazu rund 3.700 Delphi-Sicherungsdateien (`~1~`, `~2~` …) |
| Datenzugriff | UniDAC (`TUniConnection`) auf **MariaDB 10.4.32**, Schema `gutachten`, Port 3306 |
| Datenbank-Dump | `gutachten.sql`, 72 MB, erzeugt am 22.08.2026 mit Navicat |
| Tabellen | **430**, davon 393 mit Inhalt |
| Datensätze gesamt | **35.622** |

Das Verhältnis ist der wichtigste Einzelbefund: **ein sehr großes Schema über einer sehr
kleinen Datenmenge.** 430 Tabellen für 35.622 Sätze bedeuten im Schnitt 83 Zeilen je Tabelle.

## 2. Datenbestand

| Tabelle | Zeilen | Bedeutung |
|---|---|---|
| `interessenten` | 10.387 | CRM-Bestand, 45 Spalten – Adresse, Branche, Größe, Umsatz, Wiedervorlage, Kennzeichen `ISTKUNDE` |
| `bt_latex_files_backup` | 9.292 | abgelegte LaTeX-Quellen erzeugter Gutachten, 60 MB – das faktische Gutachtenarchiv |
| `bt_kunden_anlagen` | 938 | Anlagenstamm |
| `bt_kunden_anlagen_copy1/2/3` | 479 / 762 / 913 | drei parallele Kopien desselben Stamms |
| `bt_kunden` | 243 | Kundenstamm |
| `bt_kunden_gebaeude` | 238 | Gebäude je Kunde |
| `massnahmen` + 6 Varianten | je 95–137 | Maßnahmenkatalog, mehrfach dupliziert |
| `bt_pruefliste` und `bt_kd172pruefl_anl_*_v_*` | je 108 | Prüflisten – **eine Tabelle je Kunde, Anlage und Version** |

Drei Muster prägen das Schema und treiben den Migrationsaufwand:

1. **Kopien als Versionierung.** 23 Tabellen enden auf `_copy…`, 10 weitere auf `_backup`,
   `_alt` oder `_orig`. Welche davon der gültige Stand ist, steht nicht im Schema.
2. **Tabellen als Datensätze.** Prüflisten werden nicht als Zeilen mit Fremdschlüssel
   abgelegt, sondern als eigene Tabelle je Kunde, Anlage und Version. Bisher betrifft das nur
   Kundennummer 172 – der Mechanismus ist aber angelegt und würde mit jedem Kunden wachsen.
3. **Keine erkennbare Normalisierung.** `bt_kunden_copy` hat 54 Spalten, `interessenten` 45.
   Adressbestandteile liegen in `Name1` bis `Name5`, `PLZ`/`PLZ2`, `Ort`/`Ort2`.

## 3. Wie ein Gutachten entsteht

Die Software erzeugt Gutachten über **LaTeX**, nicht über Word:

1. Erfassung in den Labor-Eingabemasken (Raumluft, Wasserproben, Luftmessungen, Abstriche)
   und den Prüflisten.
2. Zuordnung der Bilder; Umwandlung über **IrfanView** und `jpeg2ps`.
3. Die Anwendung schreibt eine `.tex`-Datei nach `C:\temp` und ruft **`pdflatex`** auf.
4. Das Ergebnis wird als PDF ausgegeben; die LaTeX-Quelle wandert in
   `bt_latex_files_backup`.

Zwischen den Schritten wird über feste Pfade in `C:\temp`, Vorlagenverzeichnisse und
**Semaphordateien** koordiniert.

## 4. Schnittstellenliste (Position I4)

Aus dem Quellcode abgeleitet. Diese Liste ersetzt die offene Anforderung I4; offen bleibt
nur die Bestätigung durch Westbomke EDV.

| Gegensystem | Richtung | Format | Frequenz |
|---|---|---|---|
| MariaDB 10.4 (lokal) | beide | SQL über UniDAC | permanent |
| `pdflatex` (MiKTeX oder TeX Live) | Software → LaTeX | `.tex`-Datei in `C:\temp` | je Gutachten |
| `jpeg2ps` | Software → Werkzeug | Bilddateien | je Bild |
| IrfanView | Software → Werkzeug | Aufruf über die Kommandozeile | je Bild |
| SMTP-Versand (Indy) | Software → Mailserver | SMTP | selten, an einer Stelle im Code |
| Dateisystem | beide | `C:\temp`, Vorlagen, Semaphordateien | permanent |

**Was es ausdrücklich nicht gibt:** keine Anbindung an DATEV oder eine Buchhaltung, keine
Web- oder REST-Schnittstelle, keinen Import aus Laborgeräten, keine Office-Automation, keine
Anbindung der Pixel-8-Geräte. Die Suche nach `DATEV`, `CSV`, `Excel.Application`, `TIdHTTP`
und seriellen Ports bleibt ergebnislos.

**Die Software ist eine Insel.** Alles Kaufmännische – Rechnungen, Buchhaltung,
Bankverkehr, Kundenportale – läuft heute außerhalb und von Hand.

## 5. Funktionsumfang und Überschneidung mit Odoo

Die Anwendung ist deutlich mehr als ein Gutachtengenerator. Nach den Units gegliedert:

| Bereich | Units | Odoo-Einordnung |
|---|---|---|
| Interessenten und Akquise | 5 | **ersetzbar** – Odoo CRM |
| Kunden und Gebäude | 23 | **ersetzbar** – Odoo Kontakte |
| Angebote | 4 | **ersetzbar** – Odoo Verkauf |
| Anlagen und Objekte | 27 | **ersetzbar** – Odoo Wartung oder eigenes Modell |
| Prüflisten | 5 | Grenzfall – Odoo Qualität oder Eigenentwicklung |
| Labor-Eingabemasken | 13 | **Fachkern** – bleibt oder wird neu gebaut |
| Maßnahmenkatalog | 6 | **Fachkern** |
| Bilder und Zuordnung | 5 | **Fachkern** |
| Gutachten und LaTeX | 15 | **Fachkern** |

Grob die Hälfte der Anwendung deckt Standardfunktionen ab, die Odoo mitbringt. Die andere
Hälfte ist Fachlogik ohne Odoo-Entsprechung.

## 5a. Wofür die Software im Unternehmen tatsächlich verwendet wird

Abgeleitet aus den 255 Units, den Formularbeschriftungen und der Rechtetabelle
`bt_benutzer_menue_allowed` (771 Einträge – Rechte je Benutzer und Menüpunkt).

**Kundengewinnung**
- Interessentenbestand pflegen: 10.387 Adressen mit Branche, Größe, Umsatz, Bundesland
- Akquise mit Wiedervorlage-Termin je Interessent
- Interessent zum Kunden umwidmen (Kennzeichen `ISTKUNDE`)
- Interessentensätze und -übersichten drucken
- Referenzliste der Firmen pflegen – Anlage zum Angebot

**Angebote**
- Angebote erstellen und in einer Übersicht verwalten
- Referenzliste dem Angebot beilegen

**Kunden, Standorte und Anlagen**
- Kundenstamm (243), Ansprechpartner, Niederlassungen, Werke
- Gebäude je Kunde (238)
- Anlagenstamm: 938 RLT-Anlagen mit Werk-ID, Gebäude, Raum-Nr., Hersteller,
  versorgten Gebäuden, RLT-Kundenbezeichnung und biotec-Nummer
- Anlagentechnik im Detail beschreiben: Komponenten, Werte, Variablenfelder
- Anlagen duplizieren; Anlagendokumentation von einer anderen Anlage übernehmen
- gelöschte Datensätze und Kunden wiederherstellen

**Auftrag und Personal**
- Aufträge anzeigen, Ansprechpartner und Notizen je Auftrag
- Projektleiter zuordnen
- Mitarbeiter erfassen, ändern, auflisten

**Prüfung vor Ort**
- Stammprüflisten und kundenspezifische Prüflisten pflegen
- Prüflisten ausfüllen, Bemerkungen erfassen
- Messstellen je Anlage festlegen und drucken
- Formblätter für die Probennahme erzeugen
- Fotodokumentation: Bilder laden, Anlagen zuordnen, Bildtexte vergeben
- Sicherheitsprüfung erfassen

**Labor**
- Laborgrunddaten erfassen
- Eingabemasken je Untersuchungsart: Hygieneinspektion Raumluft, Luftmessungen,
  Abstriche, Gesamtkeimzahl Wasserproben
- Oberflächenbeprobung und Luftkeimzahlbestimmung
- mikrobiologische Ergebnisse
- Messergebnisse erfassen, in Absätze gliedern, fürs Gutachten aufbereiten
- Labordaten-Notizen

**Gutachten erstellen – der Kern**
- Gutachten aus Vorlage oder Mustergutachten anlegen
- kapitelweise erstellen, bearbeiten und drucken: Deckblatt, Inhaltsverzeichnis,
  Anlagentechnik, Messstellen, Messergebnisse, Luftkeimzahlbestimmung,
  Oberflächenbeprobung, Sekundärluftgeräte, Formblätter Probennahme,
  Fotodokumentation, gutachterliche Stellungnahme, Maßnahmenkatalog, Referenzliste
- gutachterliche Stellungnahme mit Textbausteinen, Tabellen, Variablenersetzung und
  kundenspezifischen Abschnitten
- Maßnahmenkatalog mit Soll- und Ist-Zustand je Kunde
- Zusammenfassung mit Bewertung
- Zwischenberichte aus Textblöcken
- Druckreihenfolge der Kapitel in neun Stufen festlegen
- „Gutachten in Arbeit" und „Fertigstellen": alle LaTeX-Dokumente erzeugen und drucken
- Löschen eines Gutachtens nur nach Passwortabfrage
- fertige LaTeX-Quellen archivieren – 9.292 Stück

**Verwaltung und Technik**
- Benutzeranmeldung mit Rechten je Menüpunkt und Benutzer
- Konfiguration, Setup, Farbzuordnung, Debug-Stufen
- Fehlerbehandlung und Log (626 Einträge mit Formular, Funktion, Zeilennummer, Rechner)
- Programmfehler erfassen (112 Einträge)
- Datenbankverwaltung: die Anwendung erzeugt und aktualisiert Tabellen selbst
- E-Mail-Empfänger konfigurieren, Archiveinträge

**Wofür die Software nicht verwendet wird**

Es gibt keine Units für Rechnungen, Buchhaltung, Artikel und Lager, Schulungen und
Seminare oder Zeiterfassung. Diese Bereiche laufen vollständig außerhalb – das
Schulungsgeschäft mit VDI 6022 und VDI 2047 kommt in der Software überhaupt nicht vor.

## 6. Konsequenzen für Angebot und Einrichtungsplan

1. **Die Migration ist mengenmäßig klein, strukturell aufwendig.** 35.622 Datensätze
   überträgt man an einem Tag – wenn klar ist, welche der 430 Tabellen gelten. Der Aufwand
   steckt in der Analyse, nicht im Transport.
2. **Es gibt keine Integration zu erhalten.** Das senkt das Risiko deutlich: kein
   Schnittstellenprojekt, keine Abhängigkeit von Fremdsystemen.
3. **Der Zuschnitt ist eine Entscheidung, keine Zwangslage.** CRM, Kunden, Angebote und
   Anlagen können nach Odoo; der Gutachtenteil kann bleiben und über die gemeinsame
   Datenbank oder eine schmale Schnittstelle angebunden werden.
4. **Der LaTeX-Weg ist ein Aktivposten.** Die Gutachtenerzeugung ist vollständig
   automatisiert und liefert reproduzierbare Dokumente. Sie durch Odoo-Berichte zu ersetzen,
   wäre ein Rückschritt.
5. **Die Pixel-8-Geräte sind nicht angebunden.** Die Vor-Ort-Aufnahmen kommen heute anders
   ins System. Das ist im Discovery Call anders dargestellt worden und gehört geklärt –
   siehe offene Frage 63.

## 7. Sicherheitsbefund

`Gutachten.ini` enthält die **Datenbank-Zugangsdaten im Klartext**, samt Passwort des
Benutzers `root`. Die Datei liegt im ausgelieferten Archiv. Zwei Konsequenzen:

- Das Archiv bleibt in OneDrive und kommt **nicht** ins Repo – die Git-Historie ist dauerhaft.
- biotec und Westbomke EDV sollten das Passwort nach Projektende wechseln. Bei der
  Einrichtung von Odoo bekommt die Anwendung einen eigenen Datenbankbenutzer mit
  eingeschränkten Rechten, nicht `root`.

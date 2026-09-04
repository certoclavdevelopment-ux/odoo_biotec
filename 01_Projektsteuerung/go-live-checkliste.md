# Go-live-Checkliste – Odoo bei biotec

*Internes Arbeitsdokument. Wird über die Projektlaufzeit gepflegt und vor dem Go-live
gemeinsam mit Michael Brand und Nicole Krupa durchgegangen. Punkte, die zum Zeitpunkt der
Erstellung noch nicht erhoben sind, stehen als **offen** markiert.*

Legende: `[ ]` offen · `[x]` erledigt · `[–]` entfällt

---

## 0 · Systemzuschnitt – Festlegung vom 01.09.2026

Zwei Systeme im Parallelbetrieb, keine Vollablösung. Grundlage der Entscheidung ist die
Analyse in `07_Fachkonzepte/altsystem-gutachten-analyse.md`.

**Odoo übernimmt**

| Bereich | Heute |
|---|---|
| Akquise und Interessenten | biotec-Tool (10.387 Datensätze) |
| Kunden, Ansprechpartner, Gebäude | biotec-Tool (243 Kunden, 238 Gebäude) |
| Angebote | biotec-Tool |
| Rechnungen | außerhalb, von Hand |
| Buchhaltung | außerhalb (SKR04) |
| Artikel und Lager | außerhalb, mehrere Dokumente |
| Zeiterfassung | außerhalb |
| Schulungen (VDI 6022, VDI 2047) | außerhalb – im Tool nicht vorhanden |

**Im biotec-Tool bleiben**

- Prüflisten – Stammprüfliste nach VDI 6022 Blatt 1 und die kundenspezifischen Fassungen
- Neues Gutachten erstellen
- Bestehendes Gutachten bearbeiten und fertigstellen

Damit bleiben auch die daran hängenden Schritte im Tool: Labor-Eingabemasken,
Messergebnisse, Maßnahmenkatalog, Messstellen, Fotodokumentation, gutachterliche
Stellungnahme und die LaTeX-Ausgabe.

**Die Kopplung**

Das biotec-Tool wird so angepasst, dass es die Kundendaten beim Erstellen eines Gutachtens
**aus Odoo holt** statt aus seinem eigenen Kundenstamm.

- [ ] Richtung und Umfang festgelegt: welche Felder Odoo liefert (Kunde, Ansprechpartner, Gebäude) und welcher Schlüssel beide Systeme verbindet
- [x] **Technischer Weg entschieden (01.09.2026):** Das biotec-Tool holt die benötigten Daten **per API aus Odoo** – JSON-RPC über HTTP. Indy ist im Projekt bereits vorhanden (bisher nur für SMTP), `TIdHTTP` kommt aus demselben Paket
- [ ] Odoo-API-Zugang eingerichtet: eigener technischer Benutzer, nur Leserecht auf Kontakte und Anlagen, API-Schlüssel statt Passwort
- [ ] Zwischenspeicher im Tool vorgesehen, damit ein Gutachten auch bei nicht erreichbarem Odoo weiterbearbeitet werden kann
- [ ] Odoo ist der führende Stand für Kunden. Die Erfassungsmasken im Tool für **neue Kunden, Interessenten und Angebote werden abgeschaltet**, sonst laufen die Bestände auseinander
- [ ] Kundennummer geklärt: Odoo vergibt sie, das Tool verwendet sie als Schlüssel. Abbildung auf die heutigen Felder `KdNr.` und `biotec-Nr.` dokumentiert
- [ ] Referenzliste der Firmen nach Odoo überführt – sie hing bisher am Angebot im Tool
- [ ] Verhalten bei Ausfall von Odoo festgelegt: kann ein Gutachten weiter erstellt werden, wenn Odoo nicht erreichbar ist
**Der Anlagenstamm geht nach Odoo (Festlegung 01.09.2026)**

Die 938 RLT-Anlagen werden in Odoo geführt; das Tool holt sich die benötigten Felder per API.

- [x] **Odoo-Modell festgelegt (01.09.2026):** App **Wartung**, Modell `maintenance.equipment`, mit einer Gerätekategorie „RLT-Anlage". Keine eigene Datenbank, kein eigenes Modul von Null – der Anlagenstamm wird **nicht** im Kontakt abgebildet
- [ ] Zusatzfelder an der Anlage angelegt: die drei Kennungen, Gebäude / Gebäudeteil / Etage / Raum, Betriebszeiten, Wartungsfirma als Kontaktverweis, die sieben VDI-Luftwerte
- [ ] Gerätekategorie und Standardwerte je Anlagentyp eingerichtet
- [ ] Vorbeugende Wartungsfrequenz je Anlage gesetzt – das Feld, das die heute fehlende Turnussteuerung trägt
- [ ] Standorthierarchie abgebildet: **Werk als untergeordneter Kontakt** des Kunden (hat eine eigene Adresse), **Gebäude, Gebäudeteil, Etage und Raum als Felder an der Anlage** (nur Ortsangaben innerhalb des Werks)
- [ ] Drei parallele Kennungen je Anlage übernommen und ihre Rolle dokumentiert: `ANLAGENR` (Nummer beim Kunden), `BIOTECNR` (eigene Nummer), `RLTKUNDENBEZEICHNUNG` (Bezeichnung des Kunden, z. B. „C6 Vorstand")
- [ ] Wartungsfirma als Kontakt angelegt statt als Freitext – heute 27 Schreibweisen für weniger Firmen
- [ ] Technische VDI-Felder übernommen: Außenluft-Höhe, -Anteil von/bis, Luftleistung, Fortluft-Auslass seitlich und vertikal über/unter Außenluft
- [ ] Zahlenfelder umgesetzt: im Altsystem Text mit deutschem Komma und Tausenderpunkt (`0,5`, `11.500`), `BAUJAHR` enthält auch `n.e.`
- [ ] Herstellerliste bereinigt: 68 Schreibweisen mit Dubletten (`ALKO`/`Alko`, `robatherm`/`Robatherm`, `Siegle & Epple`/`Siegle + Epple`)
- [ ] Testdatensätze erkannt und ausgeschlossen – der Bestand enthält Übungsdaten (`Hersteller`, `Oklahoma`, `Baukiste`, fortlaufende Zahlen 1 bis 8 in den Luftwerten)
- [ ] Felder ohne Inhalt nicht mitgenommen: `PROBENAHMEDATUMVON`/`BIS` sind in allen 938 Sätzen leer; `TABAUSW1` und `AUSWAHL` sind Bedienkennzeichen, keine Daten
- [ ] **Prüfintervall und nächste Fälligkeit in Odoo neu aufgebaut.** Im Altsystem gibt es dafür **kein einziges Feld** – kein Turnus, kein Fälligkeitsdatum, keine Terminplanung. Die Wiederholungsprüfungen werden heute außerhalb gesteuert (Ordner `K2_Terminplanung Außendienst`). Das ist der größte fachliche Zugewinn des Projekts und gehört ins Angebot

**Was der Zuschnitt für die Migration bedeutet**

Zu migrieren sind nur die Bereiche, die nach Odoo wandern: Interessenten, Kunden, Gebäude,
Angebote. Prüflisten und Gutachten bleiben, wo sie sind – ihre Tabellen werden nicht
angefasst. Von den 430 Tabellen des Altsystems ist damit nur ein kleiner Teil im Spiel, und
die Frage nach dem gültigen Stand unter den `_copy`-Tabellen stellt sich nur für den
Kundenstamm.

---

## 1 · Datenmigration

- [ ] Migrationsstichtag festgelegt und mit der Buchhaltung abgestimmt
- [ ] Interessenten aus dem biotec-Tool nach Odoo CRM importiert (10.387 Datensätze)
- [ ] Kunden und Kontakte importiert, Dubletten geprüft – Kundenstamm wird neu aufgebaut, nicht 1:1 übernommen
- [ ] Gültigen Stand unter `bt_kunden` und `bt_kunden_copy` bestimmt und dokumentiert
- [ ] Lieferanten inklusive Fremdlabore importiert
- [ ] Artikel und Verbrauchsmaterial importiert, Einheiten geprüft
- [ ] Anlagen- und Objektstamm nach Odoo importiert (938 Anlagen bei 23 Kunden), Zuordnung Kunde → Werk → Gebäude → Anlage stichprobenartig geprüft
- [ ] Prüfintervalle je Anlage hinterlegt, nächste Fälligkeiten plausibel
- [ ] Kurskatalog und Seminartermine übernommen
- [ ] Kontenrahmen angelegt, Standard bestätigt (SKR03 / SKR04)
- [ ] Steuerschlüssel und Steuersätze eingerichtet, Sonderfälle geprüft (Reverse Charge, Ausland, steuerfreie Leistungen)
- [ ] Eröffnungsbilanz bzw. Saldenvortrag gebucht und gegen die Saldenliste abgestimmt
- [ ] Offene Posten Debitoren und Kreditoren übernommen, Summen stimmen mit dem Altsystem überein
- [ ] Lagerbestände eingebucht und gegen die letzte Inventur abgeglichen
- [ ] Nummernkreise festgelegt – Fortsetzung der Altsystem-Nummern geklärt (Rechnungen, Angebote, Anlagen, Proben)
- [ ] Laufende Aufträge und Projekte übernommen, inklusive bereits fakturierter Anteile

## 2 · Prozesse durchgespielt

Jeder Prozess einmal komplett in der Produktivumgebung, mit echten Daten, von der ersten
Erfassung bis zur Zahlung.

- [ ] **Order-to-Cash:** Anfrage → Angebot → Auftrag → Leistung → Rechnung → Zahlungseingang
- [ ] **Purchase-to-Pay:** Bestellung → Wareneingang bzw. Leistungserfassung → Rechnung → Zahlung
- [ ] **Laborprozess:** Auftrag → Anlagenliste → Probenahme → Bebrütung → Auszählung → Gutachten → Rechnung
- [ ] **Außendienst:** Einsatz planen, vor Ort erfassen, Foto per Pixel 8 am Datensatz hinterlegen
- [ ] **Schulungen:** Kurs anlegen, Anmeldung, Mindestteilnehmerzahl (mehr als 10), Durchführung, Teilnahmebescheinigung, Rechnung
- [ ] **Wiederkehrende Prüfungen:** Folgeauftrag aus dem Prüfintervall wird ausgelöst
- [ ] Fremdlabor: Beauftragung, Ergebniseingang, Kostenzuordnung zum Projekt
- [ ] Reklamation erfassen und nachverfolgen

## 3 · Dokumente und Layout

Der kritische Punkt aus dem Discovery Call: Die Dokumente müssen für die Kunden von biotec
unverändert aussehen.

- [ ] Gutachten je Berichtstyp 1:1 gegen das Muster aus dem Altsystem verglichen
- [ ] Angebot, Auftragsbestätigung, Lieferschein, Rechnung, Mahnung geprüft
- [ ] Teilnahmebescheinigung und Zertifikat geprüft
- [ ] Briefpapier, Logo, Schriftarten korrekt eingebunden
- [ ] Layouts von Michael Brand und Nicole Krupa **schriftlich freigegeben**
- [ ] Fotos und Anlagen erscheinen im Bericht an der richtigen Stelle
- [ ] PDF-Ausgabe auf dem Drucker geprüft, nicht nur am Bildschirm

## 4 · Buchhaltung und Gruppenreporting (IFRS)

**biotec berichtet an die Certania-Gruppe, die nach IFRS konsolidiert.** Die lokalen Bücher
laufen nach HGB. Odoo muss beides bedienen: HGB als führende Buchhaltung und die für IFRS
zusätzlich benötigten Angaben.

Odoo hat **kein natives Multi-GAAP-Ledger**. Der praktikable Weg ist ein eigenes Journal für
IFRS-Anpassungsbuchungen: HGB bleibt unangetastet, die Überleitung ist als Delta jederzeit
nachvollziehbar und prüfbar.

### Einrichtung
- [ ] Bilanzierungsrichtlinie der Certania-Gruppe angefordert und ausgewertet (Konzernhandbuch, Materialitätsgrenzen)
- [ ] Eigenes Journal **„IFRS-Überleitung"** angelegt, getrennt von den HGB-Journalen
- [ ] Konzernkontenplan hinterlegt und Mapping lokales Konto → Gruppenkonto je Konto gepflegt
- [ ] Auswertungen so gefiltert, dass HGB, IFRS-Delta und IFRS-Summe getrennt darstellbar sind
- [ ] Meldetermine und Format des Reporting Package hinterlegt (Fast-Close-Fristen)
- [ ] Gruppengesellschaften an den Kontakten als Intercompany gekennzeichnet
- [ ] Sperrdaten (Lock Dates) gesetzt, damit gemeldete Perioden nicht nachträglich verändert werden

### Zusätzlich zu erfassende Daten
Diese Angaben fallen im HGB-Alltag nicht an, werden für IFRS aber gebraucht. Sie müssen von
Anfang an mitlaufen – nachträglich sind sie kaum zu rekonstruieren.

- [ ] **Projektbezug durchgängig** über analytische Konten: ein Vertrag = ein Projekt = ein analytisches Konto. Grundlage für die Umsatzrealisierung nach Fertigstellungsgrad (IFRS 15)
- [ ] **Auftragswert, geplante Gesamtkosten und Restkostenschätzung** je Projekt als Feld – ohne Cost-to-Complete kein Fertigstellungsgrad
- [ ] **Leasing- und Mietverträge** (IFRS 16) in einem Vertragsregister: Laufzeit, Rate, Zinssatz, Verlängerungs- und Kündigungsoptionen. Betrifft Büro München, Räume im Technologiepark Mittweida, Fahrzeuge und geleaste Laborgeräte. Unter HGB oft nur Aufwand, unter IFRS Nutzungsrecht und Leasingverbindlichkeit
- [ ] **Entwicklungsprojekte** getrennt erfasst mit zurechenbaren Stunden und Kosten (IAS 38). biotec entwickelt neue Analyseverfahren – unter HGB Wahlrecht, unter IFRS Aktivierungspflicht bei erfüllten Kriterien
- [ ] **Nutzungsdauern** des Anlagevermögens: steuerliche und wirtschaftliche Nutzungsdauer getrennt hinterlegt
- [ ] **Rückstellungen** mit Angabe von Grund, Bewertungsbasis und Eintrittswahrscheinlichkeit – IFRS-Ansatzkriterien sind enger als HGB
- [ ] **Drohende Verluste** aus Aufträgen erkennbar (Verlusttest je Projekt)
- [ ] **Fremdwährungspositionen** mit Kursquelle und Stichtagsbewertung (IAS 21), falls vorhanden
- [ ] **Segmentangaben** (IFRS 8): Geschäftsbereiche Inspektion, Labor und Schulung als Dimension trennbar
- [ ] **Personalabgrenzungen** wie Urlaubs- und Überstundenrückstellungen aus der Zeiterfassung ableitbar

### Datenlieferung an LucaNet

Die Konsolidierung der Gruppe läuft über **LucaNet**. Odoo muss dort einliefern – entweder
direkt oder über ein Python-Werkzeug mit Odoo-Anbindung, das die Daten liest, aufbereitet und
im geforderten Format übergibt. Gleiche Architektur wie beim POC/WIP-Rechenkern: lesen,
rechnen, Ergebnis erzeugen, ein Mensch gibt frei.

- [ ] **Bestehendes Lieferformat der Gruppe angefordert** – andere Certania-Gesellschaften liefern schon; das Format zu übernehmen ist billiger als ein neues zu entwerfen
- [ ] LucaNet-Umgebung geklärt: Version, Cloud oder On-Premise, wer administriert
- [ ] Übergabeweg festgelegt: Datei-Import, Datenbankverbindung oder Schnittstelle
- [ ] Lieferumfang je Periode definiert – mindestens Saldenliste, dazu je nach Vorgabe Anlagenspiegel, Intercompany-Salden, Segmentangaben, Leasingdaten (IFRS 16)
- [ ] Kontenmapping lokales Konto → LucaNet-Position gepflegt und versioniert
- [ ] Melderhythmus und Fristen hinterlegt (Fast Close)
- [ ] **Abstimmungsprüfung eingebaut:** Summen der Lieferung gegen die Odoo-Salden, Bilanzgleichung geprüft, Abweichung null oder erklärt
- [ ] Idempotenz: erneute Lieferung derselben Periode überschreibt sauber, keine Doppelbuchung
- [ ] Sperrdaten respektiert – gemeldete Perioden werden in Odoo nicht mehr verändert
- [ ] Lieferprotokoll je Periode: wer, wann, welche Werte, mit Nachvollziehbarkeit für den Wirtschaftsprüfer
- [ ] Freigabe vor Übergabe: Buchhaltung prüft, das Werkzeug liefert nicht unbeaufsichtigt
- [ ] Testlieferung einer abgeschlossenen Periode von der Gruppe abgenommen – **vor** dem Go-live
- [ ] Ablösung des bisherigen Wegs (voraussichtlich Excel) dokumentiert

### Abstimmung
- [ ] Umfang der IFRS-Überleitung mit Jeannette Bühler (Head of Group Accounting) festgelegt
- [ ] Buchungslogik und Konten mit Steuerberater und Wirtschaftsprüfer abgestimmt
- [ ] Erste Probemeldung erstellt und von der Gruppe abgenommen – **vor** dem Go-live
- [ ] Zuständigkeit geklärt: Wer erstellt die Überleitung monatlich, wer prüft, wer bucht final

> Hängt der POC/WIP-Strang mit drin, gilt die im Umsetzungskonzept beschriebene Architektur:
> extern rechnen, Entwürfe in Odoo erzeugen, ein Mensch bucht final.
> Siehe `07_Fachkonzepte/wissensstand-odoo-certania-biotec.md`.

## 5 · Nutzer, Rechte, Schulung

- [ ] Nutzerliste vollständig, Rollen und Rechte je Person gesetzt
- [ ] Rechteprobe: Kann jede Rolle genau das, was sie soll – und nicht mehr
- [ ] Service-Benutzer für Automatisierung ohne Recht zur Finalbuchung
- [ ] **Vor-Ort-Schulung** durchgeführt für die benannten Personen (Stefan, Michael Brand, Markus, vierte Person offen)
- [ ] Schulungsunterlagen übergeben, an den echten Prozessen von biotec orientiert
- [ ] Ansprechpartner für Rückfragen nach dem Go-live benannt und kommuniziert

## 6 · Technik und Betrieb

- [ ] Odoo-Edition, Version und Hosting festgelegt, Lizenzen bestellt
- [ ] Nutzerzahl der Lizenz entspricht der tatsächlichen Zahl
- [ ] E-Mail-Versand aus Odoo getestet: Angebot, Rechnung, Kursbestätigung kommen an und landen nicht im Spam
- [ ] Zugriff mobil vor Ort geprüft, inklusive schlechter Netzabdeckung in Technikzentralen
- [ ] Dokumentenablage geklärt: bleibt OneDrive oder übernimmt Odoo
- [ ] Datensicherung eingerichtet und eine Rücksicherung einmal getestet
- [ ] Schnittstellen der Altanwendung entweder abgelöst oder angebunden – Liste vollständig abgearbeitet
- [ ] **Kopplung Odoo → biotec-Tool im Betrieb getestet:** Gutachten für einen in Odoo neu angelegten Kunden vollständig durchlaufen
- [ ] Zugriffsrechte des Kopplungswegs eingeschränkt – eigener Odoo-Benutzer mit Leserecht, eigener Datenbankbenutzer, nicht `root`
- [ ] DATEV-Export geprüft, Steuerberater hat eine Testdatei erhalten und bestätigt
- [ ] Auftragsverarbeitungsvertrag nach Art. 28 DSGVO geschlossen (AVV-2026-001)
- [ ] **AVV Ziffer 4.5 eingehalten:** KI-Nutzung ausschließlich über Claude for Work (Team/Enterprise) oder API – **nicht** über Free- oder Pro-Konten, für die das Anthropic-DPA nicht gilt
- [ ] Datenminimierung dokumentiert: bei Strukturarbeiten ohne Personenbezug, bei Datenprüfungen auf den geprüften Ausschnitt begrenzt
- [ ] Unterauftragsverarbeiter aus Anlage 2 des AVV stimmen mit der tatsächlichen Systemlandschaft überein

## 6a · Mitwirkung von biotec – terminkritische Zulieferungen

Aus dem Angebot ANG-2026-001 übernommen. Ohne diese Punkte verschiebt sich der Plan;
sie sind nicht delegierbar.

- [ ] **Stichtagsinventur des Verbrauchsmaterials** unmittelbar vor der Umstellung: Gelatinefilter, Nährmedien, Greiner-Röhrchen. Eine vollständige Lagerliste besteht heute nicht – der Bestand wird gezählt, nicht migriert
- [ ] **Finale Unterlagen zum Stichtag:** offene Posten Debitoren und Kreditoren, Saldenvortrag, letzter Kontostand
- [ ] Summen- und Saldenliste als Excel oder CSV (die vorliegende Fassung besteht aus Bildschirmfotos)
- [ ] Fehlende Quelldateien des Altsystems, vor allem Briefköpfe und Vorlagen der Gutachten-Software
- [ ] Prüfintervalle je Anlagentyp: nach welcher Regel wird heute terminiert (offene Frage 65)
- [ ] Bestätigung des gültigen Kundenstands – im Altsystem liegen mehrere Fassungen nebeneinander
- [ ] Freigabe der Belegformulare durch die Geschäftsführung, bevor sie gebaut werden
- [ ] Benennung der vier Personen für die Vor-Ort-Schulung
- [ ] Verfügbarkeit der Fachbereiche für Abstimmung, Test und Betriebssimulation – etwa ein halber Tag je Woche und Bereich
- [ ] Zugang zum produktiven Bestand des Altsystems und eine Sicherung zum Testen

## 7 · Cut-over am Go-live-Tag

- [ ] Termin und Reihenfolge schriftlich, mit Zeitfenstern und Verantwortlichen
- [ ] Altsystem für Neuerfassungen gesperrt, nur noch lesend verfügbar
- [ ] Deltamigration der Belege zwischen Testimport und Stichtag
- [ ] Abstimmung nach dem Import: Summen Debitoren, Kreditoren, Lagerwert, Bank
- [ ] Rückfallebene definiert: Wann wird abgebrochen, und wie sieht der Rückweg aus
- [ ] Erreichbarkeit von CertoClav am Go-live-Tag und den beiden Folgetagen zugesagt

## 8 · Nach dem Go-live

- [ ] Erster Monatsabschluss in Odoo begleitet
- [ ] Erste vollständige IFRS-Meldung an die Gruppe begleitet
- [ ] Offene Punkte aus dem Betrieb gesammelt und priorisiert
- [ ] Altsystem: Aufbewahrung geklärt (GoBD). **Kein Abschaltdatum** – das Tool bleibt für Prüflisten und Gutachten produktiv. Abzuschalten sind nur die Bereiche Akquise, Kunden und Angebote
- [ ] Wartung und Weiterentwicklung des biotec-Tools geregelt: wer pflegt es künftig, mit welchem Aufwand
- [ ] Datenbanksicherung und Quellcode des Altsystems gemäß NDA gelöscht oder archiviert
- [ ] Rückblick mit Brand und Krupa: Was fehlt noch, was kommt in die nächste Phase

---

## Was daraus für die Datenanforderung folgt

Der IFRS-Block braucht Unterlagen, die in der Datenanforderung (DATA-2026-001) noch nicht
enthalten sind. Beim nächsten Stand des Dokuments ergänzen:

| Neu | Inhalt | Wer |
|---|---|---|
| L4 | Bilanzierungsrichtlinie bzw. Konzernhandbuch der Certania-Gruppe, inklusive Materialitätsgrenzen | Certania |
| L5 | Übersicht der bisher gemeldeten IFRS-Überleitungen – wie wird das heute gerechnet, wahrscheinlich in Excel | Certania / A. Krupa |
| L6 | Leasing- und Mietverträge: Büro München, Räume Mittweida, Fahrzeuge, Laborgeräte | A. Krupa |
| L7 | Laufende Entwicklungsprojekte mit zurechenbaren Kosten und Stunden | M. Frank |
| L8 | Anlagenverzeichnis mit steuerlichen und wirtschaftlichen Nutzungsdauern | A. Krupa |
| L9 | **LucaNet:** bestehendes Lieferformat einer anderen Gruppengesellschaft als Muster, Kontenplan bzw. Positionsstruktur, Importvorgaben, Melderhythmus und Fristen | Certania / LucaNet-Administration |

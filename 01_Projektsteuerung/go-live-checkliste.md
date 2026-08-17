# Go-live-Checkliste – Odoo bei biotec

*Internes Arbeitsdokument. Wird über die Projektlaufzeit gepflegt und vor dem Go-live
gemeinsam mit Michael Brand und Nicole Krupa durchgegangen. Punkte, die zum Zeitpunkt der
Erstellung noch nicht erhoben sind, stehen als **offen** markiert.*

Legende: `[ ]` offen · `[x]` erledigt · `[–]` entfällt

---

## 1 · Datenmigration

- [ ] Migrationsstichtag festgelegt und mit der Buchhaltung abgestimmt
- [ ] Kunden und Kontakte importiert, Dubletten geprüft
- [ ] Lieferanten inklusive Fremdlabore importiert
- [ ] Artikel und Verbrauchsmaterial importiert, Einheiten geprüft
- [ ] Anlagen- und Objektstamm importiert, Zuordnung Kunde → Gebäude → Anlage stichprobenartig geprüft
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
- [ ] DATEV-Export geprüft, Steuerberater hat eine Testdatei erhalten und bestätigt
- [ ] Auftragsverarbeitungsvertrag nach Art. 28 DSGVO geschlossen, falls erforderlich

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
- [ ] Altsystem: Aufbewahrung geklärt (GoBD), Abschaltdatum festgelegt
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

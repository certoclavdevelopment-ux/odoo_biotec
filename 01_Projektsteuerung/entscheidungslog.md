# Entscheidungslog

Getroffene Entscheidungen mit Datum, Begründung und Konsequenz. Jede Zeile bleibt stehen –
Änderungen werden als neue Zeile ergänzt, nicht überschrieben.

| Datum | Entscheidung | Begründung | Von | Konsequenz |
|---|---|---|---|---|
| 04.08.2026 | Michael Simon wird Projektleiter für die ERP-Umstellung bei biotec | CertoClav hat die eigene Umstellung Büroware → Odoo mit KI-Unterstützung sehr schnell geschafft; klassische Implementierungsberater haben laut Moritz Gruber einen Anreiz zu großen, langen Projekten | Moritz Gruber | Discovery Call wird aufgesetzt |
| 05.08.2026 | biotec ist mit dem Vorgehen einverstanden, Start ab Mitte August möglich | Dr. Bermpohl informiert die relevanten Ansprechpartner intern | Dr. Bermpohl / biotec | Terminfindung per Calendly |
| ~08.2026 | Arbeitsmodell: SPOC auf Beraterseite, CertoClav richtet ein, biotec validiert; Train-the-Trainer | Minimaler Aufwand beim Kunden, früh sichtbare Ergebnisse, schnellerer Go-live | CertoClav | Grundlage der Discovery- und Kick-Off-Decks |
| ~08.2026 | POC/WIP wird **nicht** über ein Odoo-Zusatzmodul gelöst, sondern über externe Python-App, die Entwurfsbuchungen erzeugt | Kein natives Odoo-Modul vorhanden; Rechenflexibilität außerhalb, Kontrolle & Prüfbarkeit bleiben in Odoo; kostengünstigster Weg | CertoClav | Architektur im Umsetzungskonzept dokumentiert |
| ~08.2026 | Idee verworfen: 100-%-Anzahlungsrechnung als Ersatz für Obligo/POC | Buchhalterisch falsch – reale Verbindlichkeit statt statistischem Obligo, Cut-off-Verzerrung, sofortige Umsatzrealisierung | CertoClav | Nur für echte Anzahlungen zulässig |
| ~08.2026 | Finale Buchung macht der Mensch; Service-User ohne Posting-Recht | Prüfungssicherheit, Audit-Trail | CertoClav | App erzeugt nur Entwürfe |
| ~08.2026 | Produktion und Website vorerst **nicht** im Scope | Bedarf unklar, Go-live-Geschwindigkeit hat Priorität | CertoClav | Im Discovery Call zu bestätigen |
| 17.08.2026 | Präsentationsunterlagen werden nach Termindatum abgelegt (`JJJJ-MM-TT_Termin/`) | Nachvollziehbarkeit, welcher Stand in welchem Termin gezeigt wurde | Michael Simon | Konvention in `03_Praesentationen/README.md` |
| 17.08.2026 | **Kein Train-the-Trainer.** Stattdessen gründliche Vor-Ort-Schulung am Projektende für 3–4 benannte Personen | Wunsch von biotec im Discovery Call; interne Weitergabe der Schulung nicht gewollt | biotec | Schulungsaufwand wandert zu CertoClav. Kick-Off-Deck (Folien „Arbeitsmodell", „Verantwortlichkeiten", „Schulung") und Angebot anpassen |
| 17.08.2026 | Dokumentenlayout ist gesetzt: Gutachten und Berichte müssen exakt so aussehen wie bisher | Kundenerwartung gegenüber den Auftraggebern von biotec | biotec | Berichtsentwicklung in Odoo statt Standardvorlagen – eigener Aufwandsposten im Angebot |
| 17.08.2026 | Fotoerfassung vor Ort per Smartphone (Google Pixel 8) ist Anforderung, nicht Option | Prüfer dokumentieren am Objekt; Fotos gehören an den Datensatz | biotec | Mobile Erfassung muss im Scope der Außendienst-Phase berücksichtigt werden |

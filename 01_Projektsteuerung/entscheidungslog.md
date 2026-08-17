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

# Begleitdokument zum Angebot – Einsparcase und Soll-Organisation

*Internes Planungsdokument. Beschreibt, was neben dem Angebot „Odoo Implementing" entstehen
soll, und wie es gerechnet wird. Erstellung erst nach Auswertung der hochgeladenen Daten –
vorher wäre jede Zahl geraten.*

## Zweck

Moritz Gruber soll den Einsparcase im **IT-Spend-Meeting** darstellen können. Das Angebot allein
zeigt Kosten; das Begleitdokument zeigt, was dagegen steht. Zwei Bausteine:

1. **Einsparpotenzial** vor und nach der Odoo-Einführung, nachvollziehbar gerechnet.
2. **Soll-Organigramm mit Rollenbeschreibungen und Kapazitätsrechnung** – wo Kapazität frei
   wird und wofür sie eingesetzt werden kann.

Adressat ist die Gesellschafter- und Konzernebene, nicht das operative Team bei biotec.

## Todo

- [ ] Einsparpotenzial vor/nach Odoo rechnen – Bandbreite, nicht Punktwert
- [ ] Soll-Organigramm erstellen (KI-gestützt, auf Basis der Ist-Rollen aus dem Discovery Call)
- [ ] Rollenbeschreibungen je Stelle mit den zugehörigen Odoo-Rechten
- [ ] Kapazitätsrechnung je Rolle: heutige Belastung, erwartete Belastung nach Odoo
- [ ] Umsatzhebel getrennt vom Kostenhebel ausweisen
- [ ] Annahmenverzeichnis anlegen – jede Zahl mit Quelle und Rechenweg
- [ ] Mit Michael Brand und Nicole Krupa gegenlesen, bevor es an die Gruppe geht
- [ ] Kurzfassung für das IT-Spend-Meeting: eine Seite, drei Zahlen, ein Diagramm

## Einsparcase – Methode

Je Prozessschritt: **Häufigkeit × Zeitaufwand heute − Zeitaufwand nachher × Vollkostensatz**.
Konservativ rechnen und die Annahmen offenlegen. Eine Zahl, die im Meeting zerpflückt wird,
schadet mehr als eine kleinere, die hält.

Nur Effekte ansetzen, die einer konkreten Tätigkeit zurechenbar sind. Pauschales
„Effizienzgewinn 20 %" ist im IT-Spend-Meeting wertlos.

### Kostenhebel

| Hebel | Heute | Datenquelle für die Rechnung |
|---|---|---|
| Anlagenliste doppelt erfasst | In Zusatzsoftware erstellt, ausgedruckt, im Labor nach Papier gearbeitet, Ergebnisse manuell zurückgeführt | Anlagen pro Woche (Position B1), Zeitaufnahme je Liste |
| Auszählung und Fotozuordnung | Fotos manuell dem Datensatz zuordnen | Platten pro Woche (offene Frage 28), Minuten je Vorgang |
| Gutachtenerstellung | Separates Programm, Übertragung, Ablage in OneDrive per Hand | Gutachten pro Monat, Zeit je Gutachten |
| Rechnungsstellung | Startet manuell nach Fertigstellung des Gutachtens | Rechnungen pro Monat (Position E2) |
| Kursorganisation | Anmeldungen, Bestätigungen, Teilnehmerlisten, Zertifikate – Weg noch unklar | Kurse und Teilnehmer pro Jahr (Position G1, G2) |
| Mehrfachpflege Stammdaten | Delphi, Excel, Buchhaltung getrennt | Anzahl Neukunden pro Monat |
| Monatsabschluss und IFRS-Überleitung | Voraussichtlich Excel | Aufwand je Abschluss (offene Frage 45) |
| Fremdlabor | Beauftragung und Kostenzuordnung manuell | Aufträge pro Monat (Position C4) |

### Umsatzhebel – gehört getrennt ausgewiesen

Diese Punkte sind für die Gruppe oft interessanter als die Zeitersparnis, weil sie oben in der
Gewinn- und Verlustrechnung wirken:

| Hebel | Wirkung |
|---|---|
| Prüfintervalle systematisch nachverfolgt | Folgeaufträge gehen nicht verloren. Wiederkehrendes Geschäft aus dem Anlagenbestand ist der stärkste Hebel – Anzahl Anlagen × Intervall × Auftragswert |
| Gutachten schneller fertig | Frühere Rechnung, kürzere Außenstandsdauer, besserer Cashflow |
| Freie Kapazität für das zweite Dozententeam | Wachstum im Schulungsgeschäft ohne Neueinstellung |
| Auslastungstransparenz im Labor | Engpässe früher erkennbar, weniger Terminverschiebungen |

### Nicht monetär, aber im Meeting relevant

Nachweisführung und Auditsicherheit bei VDI-Prüfungen, Vertretbarkeit bei Personalausfall,
Abhängigkeit von einer selbst entwickelten Delphi-Anwendung reduziert.

## Soll-Organigramm, Rollen, Kapazität

### Ist-Stand als Ausgangspunkt
Aus dem Discovery Call bekannt: Melanie Frank (Laborkoordination, übergeordnete Prozesse),
Michael Brand (Projektleitung Hygieneinspektion, Kundenorganisation, Gutachtenübergabe),
Nicole Krupa (Rechnungen, Schulungen, Werbung), Annette Krupa (Buchhaltung), 5 Dozenten
(3 intern, 2 extern), Prüferteam München (2–3), Analytik Mittweida (2–3), Labor Gütersloh.
Gesamtzahl der Mitarbeitenden ist noch offen (Frage 11).

### Was das Dokument enthalten soll
- Organigramm der Soll-Organisation, Stellen statt Namen
- Je Stelle: Aufgaben, Verantwortung, Schnittstellen, **zugehörige Odoo-Rechte**
- Kapazitätsrechnung: verfügbare Stunden, gebundene Stunden heute, erwartet nach Odoo
- Ausweis, wo Kapazität frei wird – und der Vorschlag, wohin sie fließt

Die Rollenbeschreibungen erledigen zwei Dinge auf einmal: Sie sind die Grundlage für das
**Rechtekonzept in Odoo** und für die **Lizenzzahl**. Was hier steht, wird später beim Go-live
in Abschnitt 5 der Checkliste geprüft.

### Ein Punkt, der über die Wirkung entscheidet
Freiwerdende Kapazität sollte **nicht als Personaleinsparung** dargestellt werden. biotec baut
gerade ein zweites Dozententeam auf – die eingesparte Zeit fließt in Wachstum, nicht in
Stellenabbau. Diese Darstellung ist ehrlicher und im Meeting stärker: Mehr Geschäft mit
demselben Team ist ein besseres Argument als eine halbe eingesparte Stelle.

Das ist auch praktisch wichtig: Brand, Krupa und Frank müssen beim Projekt mitarbeiten. Ein
Dokument, das nach Rationalisierung klingt und intern die Runde macht, kostet Kooperation.

## Datengrundlage

Rechenbar wird der Case erst mit den Mengen aus dem Upload. Gebraucht werden vor allem:

- **B1** Anlagenstamm – Anzahl, Typen, Prüfintervalle → Basis für den stärksten Umsatzhebel
- **E2** Rechnungen der letzten Wochen – Volumen und Frequenz
- **G1, G2** Kurskatalog und Seminarkalender – Kurse und Teilnehmer pro Jahr
- **F1** Artikelliste mit Bestand – Kapitalbindung
- Offene Frage 28: Plattenmenge pro Woche
- Offene Frage 11: Mitarbeiterzahl je Rolle
- Interne Stunden- und Kostensätze (Position K3) – ohne Vollkostensatz keine Eurobeträge

Zeitaufnahmen je Prozessschritt gibt es nicht. Die schätzen wir gemeinsam mit Brand und Krupa
in einem kurzen Termin – lieber grob und abgestimmt als exakt und erfunden.

## Reihenfolge

1. Upload abwarten und auswerten
2. Mengengerüst aufstellen
3. Kurzer Termin mit Brand und Krupa für die Zeitschätzungen
4. Einsparcase rechnen, Annahmen dokumentieren
5. Soll-Organigramm und Rollen erstellen
6. Von biotec gegenlesen lassen
7. Angebot und Begleitdokument gemeinsam an die Gruppe

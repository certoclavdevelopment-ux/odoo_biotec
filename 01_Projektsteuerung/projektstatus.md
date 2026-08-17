# Projektstatus – Odoo-Einführung biotec GmbH

*Konsolidierter Stand: 17.08.2026, nach dem Discovery Call. Quellen: E-Mail-Verlauf
„Biotec ERP" (04.–05.08.2026), Wissensstand Certania/biotec (10.08.2026), Discovery- und
Kick-Off-Präsentation, Protokoll Discovery Call vom 17.08.2026.*

## Kurzfassung

CertoClav Consulting (Michael Simon als Consultant & SPOC) soll bei der **biotec GmbH**,
Gütersloh – Tochter der **CERTANIA Holding GmbH** – Odoo einführen. Vorbild ist die eigene
Umstellung bei CertoClav (Büroware → Odoo, Referenzwert ca. eine Woche), durchgeführt mit
KI-Unterstützung (Claude). Das Arbeitsmodell dreht die klassische ERP-Einführung um:
**CertoClav richtet ein und importiert Daten, biotec validiert** – der SPOC sitzt auf
Beraterseite, geschult wird per Train-the-Trainer.

Der Discovery Call fand am **17.08.2026** statt. Das Scoping und damit die Budgetbasis steht
noch aus.

## Erkenntnisse aus dem Discovery Call (17.08.2026)

### Struktur
Zwei Standorte: **Gütersloh** (Hauptstandort – Labor, Auszählung, Gutachten, Verwaltung) und
**München** („biotec Süd", 3er-Team Hygienekontrollen, Büro in einem Privatgebäude). Dazu
notiert: „Walda Technologiepark", Analytik von Boden und Wasser mit 2–3 Personen – Zuordnung
noch unklar. Selbstbeschreibung: **ERP für eine kleine Gesellschaft**. Damit ist
**Multi-Company** ein Thema, das im Deck nicht vorkam.

### Altsystem – Frage 1 ist beantwortet
- **Delphi-Applikation mit vielen Schnittstellen** als führendes Altsystem.
- Separates **Gutachtenprogramm** erzeugt die Berichte.
- Kleine Zusatzsoftware für die **Anlagenliste**, die auf Papier ausgedruckt wird.
- Dokumentenablage über **OneDrive**.

### Kernprozess Labor
Auftrag → Anlagenliste (Software, Papierausdruck) → Arbeiten im Labor nach Papierdokument →
Proben nach Gütersloh → Bebrütung, Auszählung nach 3 oder 5 Tagen → Fotos am Datensatz
hinterlegen → Gutachtenprogramm erzeugt Bericht → OneDrive → Autoklavieren und Entsorgen →
Info und Rechnung.

Analytik: Keimzahl auf zwei Medien (Gesamtkeimzahl, Pilze), wenige Analysetechniken.
Mengen: 100 Anlagen pro Woche bei Volllast, 8–9 Platten je Anlage.

### Schulungsgeschäft
Bundesweit beworben, Durchführung ab mehr als 10 Teilnehmern, Zielgruppe Großkonzerne und
Industrieparks (Pflichtschulung). Lange Vorplanung, Seminarfläche 6 Monate im Voraus gebucht.
Inhouse-Schulungen ebenfalls im Angebot. 5 Dozenten (3 intern, 2 extern), zweites Team im
Aufbau.

### Produktion, Handelsware, Lager
Minimale Eigenproduktion (einige Chemikalien), 5–6 Händlerprodukte, Lager mit
Greiner-Röhrchen und Verbrauchsmaterial – Gelatinefilter allein rund 15.000 €.

### Zwei harte Randbedingungen
1. **Kein Train-the-Trainer.** Stattdessen gründliche Vor-Ort-Schulung am Projektende für
   3–4 namentlich benannte Personen (Stefan, Michael Brand, Markus + eine weitere).
   Damit wandert Schulungsaufwand von biotec zu CertoClav – das Arbeitsmodell aus dem Deck
   muss angepasst werden.
2. **Layouttreue.** Gutachten und Berichte müssen exakt so aussehen wie bisher. Das macht
   Berichtsentwicklung nötig statt Odoo-Standardvorlagen.

### Vor Ort
Fotos müssen direkt vor Ort per Smartphone möglich sein (Google Pixel 8) und am Datensatz
bzw. an der Anlage hinterlegt werden.

### Rollen und Entscheiderlage geklärt
- **Dr. Thomas Wilke** ist **CEO biotec** und gleichzeitig Direktor Food bei Certania – über
  ihn läuft die Freigabe. Dr. Bermpohl hat **Prokura** und ist der Zugang, nicht der
  Entscheider.
- **Ansprechpartner für CertoClav sind Michael Brand und Nicole Krupa** – Brand (Projektleiter
  Hygieneinspektion seit 2020, Begleiter des ERP-Projekts) für fachlich/technisch, Krupa
  (Rechnungen, Schulungen, Werbung) für kaufmännisch/organisatorisch. Beide bündeln die
  Rückmeldungen auf biotec-Seite.
- **Melanie Frank** (promovierte Biologin) koordiniert Labortätigkeiten und übergeordnete
  Prozesse, **Annette Krupa** die Buchhaltung – zusammen mit Brand und Krupa die fachliche
  Validierungsbreite für die Iterationen. Annette Krupa war nicht eingeladen und sollte
  einbezogen werden.
- **Westbomke** stellt die **IT-Administration** – technische Gegenstelle für die Ablösung der
  Delphi-Applikation und deren Schnittstellen. Früh einbinden.
- Auf CertoClav-Seite begleiten Jonas Leitenmeier (AI-Ops-Lead) sowie Balázs Szaradics und
  Patrick Gottfried (AI-Operator) das Projekt.

### Im Termin nicht behandelt
Schmerzpunkte und Auslöser, Erfolgskriterien, Go-live-Wunschtermin, Budget, Nutzerzahl,
Hauptansprechpartner – und der gesamte Finance-/Certania-Block (P2P/O2C, POC/WIP).

## Zwei Projektstränge

Es laufen zwei Anforderungsstränge, deren Verhältnis noch nicht geklärt ist. **Das ist die
wichtigste offene Scoping-Frage.**

### Strang A – ERP-Einführung biotec (operativ)
- Einstieg über **Moritz Gruber** (CEO Certania Holding) → **Dr. Andreas Bermpohl** (Richtung biotec).
- Ziel: operative Prozesse von biotec in Odoo – CRM/Verkauf, Rechnungsstellung, Einkauf/Lager,
  Außendienst (VDI-6022-/2047-Inspektionen), Projekte & Zeiterfassung, VDI-Schulungen.
- Artefakte: Discovery-Deck, Kick-Off-Deck.
- Status: Discovery Call terminiert; Ist-System bei biotec **noch unbekannt**.

### Strang B – Group-Accounting-Anforderungen (Certania)
- Einstieg über **Jeannette Bühler** (Head of Group Accounting, Certania).
- Zwei Kernanforderungen: (1) vollintegriertes **P2P/O2C** ohne manuelle Schnittstellen,
  (2) saubere **POC-/WIP-Bewertung** mit Cost-to-Complete und Verlustantizipation.
- Artefakte: Umsetzungskonzept POC/WIP (Word), Workshop-Fragebogen A–N.
- Status: Erstkontakt-Phase, Go von Certania steht aus.

### Warum das zusammen gehört
biotec ist ein klassischer POC/WIP-Fall: mehrmonatige Festpreisprojekte, Inspektorenstunden,
Fremdlabor-Analysen, Meilensteinabrechnung. Wenn Strang B in den biotec-Scope kommt, ändert
das Aufwand und Zeitplan deutlich (siehe Konflikte unten).

## Bekannte Konflikte & Klärungsbedarf

| Thema | Konflikt | Klärung |
|---|---|---|
| **Scope** | Ist POC/WIP Teil des biotec-Rollouts oder separates Gruppenthema? Im Discovery Call **nicht** behandelt | Certania |
| **Arbeitsmodell** | Deck verkauft Train-the-Trainer; biotec lehnt das ab und will Vor-Ort-Schulung. Kick-Off-Deck und Angebot müssen angepasst werden | CertoClav |
| **Freigabe** | Deck sieht **einen** Hauptansprechpartner vor, biotec benennt **zwei** (Brand, Krupa). Wer final freigibt, ist offen | biotec / CertoClav |
| **Layouttreue** | Gutachten müssen unverändert aussehen → Berichtsentwicklung statt Standardvorlagen; Aufwandstreiber | CertoClav |
| **Multi-Company** | Zwei Standorte, „biotec Süd" – eigene Gesellschaft oder nur Standort? Beeinflusst Odoo-Setup und Lizenzen | biotec |
| **Grundannahme** | Fragebogen und POC-Konzept setzen ein **laufendes Odoo** voraus (Fragen M1–M3: Edition, aktive Module, WIP-Übernahme). Bei biotec ist es ein Greenfield-Projekt mit unbekanntem Altsystem. | Fragebogen für Greenfield anpassen |
| **Aufwandserwartung** | Erzählung „Umstellung in einer Woche" (CertoClav-Referenz) vs. interne Schätzung von ca. 25–57 PT allein für POC/WIP | vor Budgeterstellung |
| **Odoo-Lücke** | Es gibt **kein natives Odoo-Modul** für bilanzielle POC-/WIP-Umsatzrealisierung. Deferred Revenue ist zeitbasiert, nicht fortschrittsbasiert. | Konzept liegt vor: externe Python-App erzeugt Entwurfsbuchungen |
| **Interessenskonflikt** | CertoClav gehört Michael Simon und Moritz Gruber gemeinsam; Moritz beauftragt eine teilweise eigene Firma | Gesellschafter-Klärung durch Moritz |

## Arbeitsmodell (aus den Decks)

**CertoClav:** Businessanalyse, Projektmanagement & SPOC, Konfiguration + Datenimport mit
Claude, Befähigung des Hauptansprechpartners.
**biotec:** Daten & Unterlagen bereitstellen, Prozesse erklären, Iterationen abstimmen,
validieren & freigeben, am Ende alle Mitarbeiter intern schulen.

Projektzyklus je Phase: Kick-Off → Einrichtung → Demo & Feedback → Validierung → Schulung → Go-live.
Schritte 2–4 wiederholen sich pro Phase bis zur Freigabe. Priorisierung nach Mehrwert/Einfachheit
(Quick Win zuerst, Game Changer später, Feinabstimmung nach Go-live).

## Phasenstand

| Phase | Status |
|---|---|
| 1. Discovery | **durchgeführt** 17.08.2026 – Protokoll in `02_Meetings/` |
| 2. Scoping & Angebot | **nächster Schritt** |
| 3. Kick-Off | Deck vorbereitet, unterminiert |
| 4. Iterative Phasen | offen |
| 5. Schulung (Train-the-Trainer) | offen |
| 6. Go-live & Support | offen |

## Zeitplan

- Projektstart **ab Mitte August 2026** möglich (von Bermpohl bestätigt).
- Discovery Call: 17.08.2026.
- Wunschtermin Go-live: **offen** – im Discovery Call zu erheben.

## Nächste Schritte

1. **Protokoll & Zusammenfassung** an biotec versenden – CertoClav.
   (Abschnitt 10 „Interne Notizen" vorher entfernen.)
2. **Rohdaten anfordern** → `05_Rohdaten_Kunde/00_eingang/`: Anlagenlisten, Kunden- und
   Artikelstamm aus der Delphi-Applikation, Kurskatalog.
3. **Gutachten- und Berichtsvorlagen als Muster** anfordern – Grundlage für die Bewertung
   des Layoutaufwands.
4. **Delphi-Applikation**: Exportmöglichkeiten und Schnittstellen dokumentieren lassen.
5. **Vor-Ort-Schulung klären**: 3 oder 4 Personen, vierter Name, Termin und Ort.
6. **Hauptansprechpartner** benennen lassen.
7. **Scoping & Phasierung** erstellen – mit Vor-Ort-Schulung statt Train-the-Trainer,
   Multi-Company und Berichtsentwicklung als eigene Posten.
8. **Scope-Frage POC/WIP** mit Certania klären; Fragebogen auf Greenfield anpassen.
9. **Gesellschafter-Klärung** durch Moritz Gruber abwarten.

## Erste Einordnung für die Phasierung

Aus dem Discovery Call lässt sich die Reihenfolge grob ableiten – zu bestätigen im Scoping:

| Kandidat | Einordnung |
|---|---|
| Veranstaltungen (VDI-Schulungen) | **Quick Win** – klar umrissen, Odoo-Standard trägt viel, früh sichtbarer Nutzen |
| CRM, Verkauf, Rechnungsstellung | **Quick Win** – Standardprozess, Basis für alles Weitere |
| Einkauf & Lager | **Quick Win** – kleiner Artikelstamm, überschaubarer Lagerwert |
| Außendienst mit Fotodokumentation | **Game Changer** – ersetzt Papierlauf, braucht mobile Erfassung |
| Laborprozess & Gutachten mit Layouttreue | **Game Changer** – der eigentliche Kern, höchster Aufwand |
| Multi-Company für zwei Standorte | abhängig von der Gesellschaftsstruktur |

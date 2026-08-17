# Projektstatus – Odoo-Einführung biotec GmbH

*Konsolidierter Stand: 17.08.2026. Quellen: E-Mail-Verlauf „Biotec ERP" (04.–05.08.2026),
Wissensstand Certania/biotec (10.08.2026), Discovery- und Kick-Off-Präsentation.*

## Kurzfassung

CertoClav Consulting (Michael Simon als Consultant & SPOC) soll bei der **biotec GmbH**,
Gütersloh – Tochter der **CERTANIA Holding GmbH** – Odoo einführen. Vorbild ist die eigene
Umstellung bei CertoClav (Büroware → Odoo, Referenzwert ca. eine Woche), durchgeführt mit
KI-Unterstützung (Claude). Das Arbeitsmodell dreht die klassische ERP-Einführung um:
**CertoClav richtet ein und importiert Daten, biotec validiert** – der SPOC sitzt auf
Beraterseite, geschult wird per Train-the-Trainer.

Der Projektstand ist **vor dem Discovery Call**. Discovery- und Kick-Off-Deck sind fertig,
das Scoping und damit die Budgetbasis steht noch aus.

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
| **Scope** | Ist POC/WIP Teil des biotec-Rollouts oder separates Gruppenthema? | Discovery Call / Certania |
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
| 1. Discovery | **läuft** – Termin 17.08.2026 |
| 2. Scoping & Angebot | offen – nach Discovery |
| 3. Kick-Off | Deck vorbereitet, unterminiert |
| 4. Iterative Phasen | offen |
| 5. Schulung (Train-the-Trainer) | offen |
| 6. Go-live & Support | offen |

## Zeitplan

- Projektstart **ab Mitte August 2026** möglich (von Bermpohl bestätigt).
- Discovery Call: 17.08.2026.
- Wunschtermin Go-live: **offen** – im Discovery Call zu erheben.

## Nächste Schritte

1. **Discovery Call durchführen** und protokollieren
   (Vorlage: `02_Meetings/_VORLAGE_Protokoll_Discovery_Call.docx`).
2. **Protokoll & Zusammenfassung** an biotec versenden – CertoClav.
3. **Rohdaten anfordern**: Beispieldaten & Vorlagen, ohne Aufbereitung → `05_Rohdaten_Kunde/00_eingang/`.
4. **Scoping & Phasierung** erstellen: Reihenfolge der Apps, Aufwandsschätzung, Budgetbasis.
5. **Scope-Frage POC/WIP** mit Certania klären; Fragebogen auf Greenfield anpassen.
6. **Gesellschafter-Klärung** durch Moritz Gruber abwarten.

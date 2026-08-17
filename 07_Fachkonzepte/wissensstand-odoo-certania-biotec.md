# Odoo bei Certania / biotec – Wissensstand

*Konsolidierte Zusammenfassung aller bisher erarbeiteten Informationen (Stand: 2026-08-10). Erstellt für den Export/Weiterverwendung.*

---

## 1. Unternehmen & Kontext

### Certania (Holding)
- **CERTANIA Holding GmbH**, Löwengrube 18, 80333 München.
- Diversifizierter **TIC-Konzern**: Testing, Inspection, Certification & Compliance – Netzwerk spezialisierter Tochtergesellschaften.
- **5 Servicesegmente:**
  1. **Life Sciences** – pharmazeutische/medizinische Tests, klinische Studien, Stabilitätstests, QS für Healthcare.
  2. **Food & Consumer Goods** – Mikrobiologie, Lebensmittelsicherheit, Wassertests, Inspektionen.
  3. **Industrials** – Materialprüfung, Schadensanalyse, Zertifizierung erneuerbarer Energien, chem. Analysen.
  4. **Buildings & Infrastructure** – Gebäudeinspektionen, Umweltanalytik, Brandschutz, Materialprüfung.
  5. **Certification & Compliance** – ISO-Zertifizierungen, ESG, Chemikalienregulierung, Nachhaltigkeitsberatung.
- **Geschäftsmodell:** B2B-Dienstleistungen (Laboranalysen, technische Inspektionen, Zertifizierungen, Beratung, Compliance) für Pharma-, Lebensmittel-, Industrie- und Bausektor.
- **Ansprechpartnerin (ERP-Thema):** Jeannette Bühler, **Head of Group Accounting**, jbuehler@certania.com, +49 176 7200 2586.

### biotec GmbH (Tochter der Certania-Gruppe)
- Standort **Gütersloh**, +49 5241 307200. Web: biotec-gmbh.com.
- **Hygiene-, Gesundheits- und Sicherheits-Dienstleister.** Konkrete Leistungen:
  - **Hygieneinspektion nach VDI 6022** (raumlufttechnische/RLT-Anlagen).
  - Prüfung/Zertifizierung von Luftdesinfektionssystemen (VDI 4300, DIN TS 67506).
  - Raumluft-Hygiene, **Trinkwasser-Hygiene**, **Krankenhaushygiene**.
  - **Gefährdungsbeurteilungen**, Arbeits-/Gesundheitsschutz-Beratung.
  - **Laboranalysen & Forschung**, Entwicklung neuer Analyseverfahren; u. a. BMWi-gefördertes Forschungsprojekt „forensische DNA-Spuren aus Raumluft".
  - Schulungen nach VDI 6022 / VDI 2047.
- **Projekttypischer Charakter:** mehrmonatige, projektbasierte Dienstleistungen mit Inspektorenstunden, Probenahmen, mikrobiologischen Analysen (teils **Fremdlabor**), Abschlussdokumentation, Meilenstein-Abrechnung → **klassische POC/WIP-Fälle**.

### Verbindung / Anlass
- Kontakt kam über **Moritz** zustande (Mitgesellschafter). **Michael Simon** ist Geschäftsführer (alleinvertretungsberechtigt) der **CertoClav Sterilizer GmbH** (Laborgeräte-Hersteller + Softwaredienstleister, Österreich; Sparte **Certos** entwickelt Software für Laborgerätehersteller; eigene IT-Abteilung; KI-erfahren inkl. Forschungsprojekten).
- CertoClav hat Odoo **mithilfe von KI (Claude)** eingeführt – deutlich schneller als der klassische ERP-Berater-Weg (Erfahrungswert grob Faktor 20). Daraus die mögliche Zusammenarbeit/Inspiration für Certania/biotec.

---

## 2. Die zwei ERP-Kernanforderungen (von Jeannette)

### Anforderung 1 – Vollintegrierte End-to-End-Prozesse
- **Purchase-to-Pay** vollständig: Bestellung → Wareneingang/Leistungserfassung → Rechnung → Zahlung.
- **Order-to-Cash** vollständig: Auftrag → Leistung/Lieferung → Rechnung → Zahlung.
- **Keine manuellen Schnittstellen** zwischen operativen Systemen und Finance.
- **Verpflichtungen bereits vor Rechnungseingang sichtbar** – wichtig für Accruals, Cut-off und POC/WIP.
- Kernkritik von Jeannette: „Große" ERP-Systeme (gemeint v. a. **SAP**) leiten die Daten automatisch in **Vorratsbuchungen** über; in Odoo müsse das teils manuell gemacht werden.

### Anforderung 2 – Saubere POC-/WIP-Bewertung
- Integrierte Projektlogik: **Auftrag/Vertrag → Projekt → Budget → Bestellung → Ist-Kosten → geleistete Stunden → Fremdleistungen → Billing → Revenue Recognition**.
- Ziel: Projektfortschritt, Cost-to-Complete, WIP und Margen **direkt aus dem System** ableiten – keine Excel-Sammelaktion am Monatsende.

---

## 3. Odoo-Fähigkeiten – ehrliche Einordnung

### Zu Anforderung 1
| Punkt | Odoo-Status |
|---|---|
| P2P & O2C in einem System, keine manuellen Schnittstellen | ✅ funktioniert (Stärke von Odoo) |
| Automatische **WE/RE-Buchung** beim Wareneingang (Waren) | ✅ mit automatischer Bestandsbewertung + „Anglo-Saxon Accounting" → Wareneingang bucht auf Verrechnungskonto (**Stock Interim / GR/IR**), Rechnung löst auf |
| **Obligo** vor Rechnungseingang (PO angelegt, nichts erhalten) | ⚠️ nur **statistisch** über offene Bestellungen + **Budget-Modul** (Obligo gegen Budget) + „received-not-billed"-Reports; **keine** FI-Buchung (in SAP i. d. R. ebenfalls CO-statistisch) |
| **Dienstleistungen/Fremdleistungen ohne Lager** | ⬜ **Todo** – kein automatischer Abgrenzungs-Trigger; braucht definierten **Accrual-Prozess** (manuell oder „Deferred"-Funktion) |

### Zu Anforderung 2
| Punkt | Odoo-Status |
|---|---|
| Integrierte Projekt-/Kostenlogik (Auftrag→Projekt→Budget→Kosten→Billing), Echtzeit-Projektmarge | ✅ vorhanden |
| **Bilanzielle POC-Automatik** (Umsatzrealisierung nach Fertigstellungsgrad, automatische WIP-Aktivierung, Cost-to-Complete) | ⬜ **kein Odoo-Standard** – wird über Zusatzlösung ergänzt |

### Wichtige Klarstellungen
- **„Deferred Revenue/Expense"** in Odoo ist **zeitbasiert** (z. B. 1/12 pro Monat) – **nicht** fortschrittsbasiert → **kein** cost-to-cost-POC.
- **Fakturieren ≠ Umsatzrealisierung**: Odoo kann meilenstein-/anteilig fakturieren, deckt damit aber nicht die bilanzielle POC-Logik ab.
- **Es gibt kein natives Odoo-Enterprise-Modul für POC/WIP-Umsatzrealisierung.**
- Verworfene Idee: eine **100%-Anzahlungs-/Vorkasse-Rechnung** als Ersatz für Obligo/POC → buchhalterisch falsch (reale Verbindlichkeit/Forderung statt statistisches Obligo, Cut-off-Verzerrung, Doppelbuchungsrisiko; bei POC würde 100 % Umsatz sofort realisiert). Nur für **echte Anzahlungen** geeignet.

### Wege, die Lücke (POC/WIP) zu schließen
1. **Drittanbieter-App** aus dem Odoo App Store (Revenue Recognition / POC / Construction) – Eignung/Reife/Odoo-19-Tauglichkeit im Einzelfall prüfen.
2. **OCA-Module** (Community) – rund um Projekt/Analytik vorhanden, aber **kein vollständiger POC-Buchungs-Automatismus** out of the box.
3. **Gezielte Entwicklung** durch Odoo-Partner – belastbarste, aber aufwändigste Variante.

---

## 4. POC/WIP – Konzept in einfachen Worten

### Kernbegriffe
- **Fertigstellungsgrad (cost-to-cost):** angefallene Kosten ÷ voraussichtliche Gesamtkosten.
- **WIP-Aktivierung:** bereits erbrachte, noch nicht fakturierte Leistung wird als **Vermögenswert** aktiviert (bei Überfakturierung umgekehrt als **passive Abgrenzung**).
- **Cost-to-Complete:** laufende Schätzung der Restkosten → Basis für Fortschritt **und** frühzeitige Erkennung drohender Verluste (Verlustantizipation → sofort Rückstellung).

### Rechenbeispiel (biotec – VDI-6022-Hygieneinspektion Klinikum)
- Auftragswert **120.000 €**, geplante Gesamtkosten **90.000 €** (Marge 30.000 € / 25 %).
- Laufzeit ~8 Monate; Kosten: Inspektorenstunden, Probenahme/Reise, **Fremdlabor**-Analysen; Meilenstein-Abrechnung.

| Zeitpunkt | Ist-Kosten kum. | Fertigstellung | Umsatz kum. (POC) | Fakturiert kum. | WIP (Bilanz) |
|---|---|---|---|---|---|
| nach Monat 2 | 22.500 € | 25 % | 30.000 € | 30.000 € | 0 € |
| nach Monat 4 | 45.000 € | 50 % | 60.000 € | 30.000 € | **+30.000 €** |
| nach Monat 6 | 67.500 € | 75 % | 90.000 € | 60.000 € | **+30.000 €** |
| nach Monat 8 (Abschluss) | 90.000 € | 100 % | 120.000 € | 120.000 € | 0 € |

- **Verlustfall:** Steigen die erwarteten Gesamtkosten z. B. auf 130.000 € (> 120.000 € Auftragswert), wird der drohende Verlust von 10.000 € **sofort** als Rückstellung gebucht.

### Beispiel-Buchungen (Periode)
- **WIP aktivieren:** Soll *Nicht abgerechnete Leistungen (Aktiv)* / Haben *Umsatzerlöse POC* (bei Unterfakturierung; bei Überfakturierung umgekehrt gegen passive Abgrenzung).
- **Verlustrückstellung:** Soll *Aufwand drohende Verluste* / Haben *Rückstellung*.
- **Folgemonat:** Reversal der WIP-Buchung, dann Neubuchung mit aktuellem Stand.

---

## 5. Empfohlene Architektur (Umsetzungskonzept)

**Prinzip:** Odoo = führendes System (Daten, Konfiguration, finale Buchung). Externe **Python-App** = monatliche Berechnung + Erzeugung von **Entwurfs-Buchungen**. Buchhaltung prüft und bucht final in Odoo. → Rechen-Flexibilität + Kontrolle/Prüfbarkeit in Odoo. Bewusst **kostengünstigster** Weg: vorhandene Odoo-Datenbasis maximal nutzen, nur den fehlenden Rechen-/Buchungsteil ergänzen (statt schweres Zusatzmodul oder Komplett-Neuentwicklung).

### Datenfluss
1. Odoo → (lesen) Vertrags-/Projektdaten, Restkosten, Ist-Kosten aus der Kostenrechnung.
2. Python-App → rechnet Fertigstellungsgrad, Umsatz, WIP, Verlustrückstellung.
3. Python-App → (schreiben) POC-Periodensatz je Projekt/Monat + Buchungen als **Entwurf** in Odoo.
4. Odoo → Buchhaltung prüft und bucht final; Folgemonat: automatisches Reversal + neuer Stand.

### Odoo-Seite (Datenschicht)
- **Projekt / analytisches Konto** als Kern (1 Vertrag = 1 Projekt = 1 analytisches Konto).
- Custom-Felder/Modelle (kleines Modul, besser als Studio wegen Versionierung):
  - `x_poc_contract`: `contract_revenue`, `planned_cost`, `cost_to_complete`, `poc_method`, Kontenzuordnung.
  - `x_poc_period` (je Projekt+Monat, Audit-Datensatz): `period`, `actual_cost_cum`, `percent_complete`, `revenue_recognized_cum`, `revenue_this_period`, `billed_cum`, `wip_amount`, `loss_provision`, `status`, `move_id`; **Unique-Key (Projekt, Periode)**.
- **Kostenquelle:** `account.analytic.line` (Einkauf/Fremdleistungen, Stunden, Verbrauch, Reise) + fakturiert aus Ausgangsrechnungen.
- **Konten + eigenes Journal „POC/Abgrenzung":** WIP/unfertige Leistungen (Aktiv), passive Abgrenzung/erhaltene Anzahlungen, Umsatzerlöse POC, Aufwand drohende Verluste + Rückstellung.
- **Freigabe/Buchung:** Entwürfe (`account.move` draft) verknüpft mit `x_poc_period`; Mensch prüft & bucht.

### Externe Python-App (Monatslauf)
1. Verbinden (JSON-RPC) mit eingeschränktem Service-User.
2. Aktive POC-Projekte + `cost_to_complete` lesen.
3. Ist-Kosten kumuliert + `billed_cum` je Projekt lesen.
4. Rechnen (cost-to-cost, s. Formeln unten).
5. `x_poc_period` upserten (Unique-Key → kein Doppeldatensatz).
6. Entwurfsbuchung(en) mit fester Referenz `POC/<Projekt>/<JJJJ-MM>` erzeugen (Idempotenz).
7. Protokoll/Report schreiben.

### Rechenlogik
```
Fertigstellungsgrad = Ist-Kosten / (Ist-Kosten + Restkosten)   # forecast-basiert, robuster als /planned_cost
Umsatz kumuliert     = Fertigstellungsgrad × Auftragswert
Umsatz diese Periode = Umsatz kumuliert − Umsatz Vormonat       # Delta-Methode
WIP                  = Umsatz kumuliert − fakturiert kumuliert  # + = aktivieren, − = passive Abgrenzung
Verlusttest          = (Ist + Restkosten) > Auftragswert → Rückstellung = erwarteter Gesamtverlust − bereits erfasst
```

### Kritische Kontrollen der App
- **Idempotenz:** feste Referenz je Projekt+Periode; gebuchte Belege nie verändern.
- **Storno/Reversal** der WIP-Bilanzposten im Folgemonat; **Delta-Buchung** beim Umsatz.
- **Sperrdaten (Lock Dates)** respektieren; Fremdwährung/Rundung korrekt.
- **Service-User ohne Posting-Recht** – finale Buchung macht der Mensch (bevorzugte, prüfungssichere Variante: „extern rechnen → Entwürfe → im Odoo buchen").

### Wer macht was
| Aufgabe | Odoo | Python-App |
|---|---|---|
| Vertrags-/Projektdaten, Cost-to-Complete pflegen | ✔ | – |
| Ist-Kosten sammeln (Stunden/Fremdlabor/Reise) | ✔ (Quelle) | liest |
| Fertigstellungsgrad, Umsatz, WIP, Verlust rechnen | – | ✔ |
| POC-Periodensätze füllen / Buchungen (Entwurf) | Speicherort | schreibt/erzeugt |
| Prüfen & final buchen | ✔ (Mensch) | – |
| Reporting/Nachweis (WIP, Marge) | ✔ | Vorbereitung |

---

## 6. Aufwand (grobe Richtwerte – NICHT nach außen kommuniziert)
> Offizielle Schätzung erst nach vollständiger Ist-Erhebung.
- Odoo-Teil (Modul: Felder/Modelle, Konten, Journal, Report): ~5–12 PT.
- Python-App (Rechenkern, Entwurfsbuchungen, Idempotenz/Storno, Report): ~15–35 PT.
- Buchhaltungs-Spezifikation mit StB/WP: ~5–10 PT.
- Treiber nach oben: Fremdwährung, IFRS/HGB-Feinheiten, Sonderfälle.

---

## 7. Nächste Schritte
1. **Buchhaltungs-Spezifikation** mit Steuerberater/Wirtschaftsprüfer festzurren (Methode cost-to-cost, Konten, Verlustantizipation, Cut-off-Regeln, HGB/IFRS).
2. Odoo-Datenmodell + Konten in Testumgebung anlegen.
3. Python-App zunächst als **„Rechnen-only"** (füllt Felder + Report, bucht noch nicht) → Zahlen validieren.
4. Erst danach Entwurfsbuchungen aktivieren → Buchhaltung bucht → Reversal-Mechanik testen → Rollout.
5. Parallel: **Requirements-Workshop** zu (a) Abgrenzungen/Cut-off inkl. Service-Accruals und (b) POC/WIP inkl. Revenue Recognition.

---

## 8. Bereits erstellte Artefakte
- **Umsetzungskonzept (Word):** `POC_WIP_Certania_biotec.docx` – Prozess, biotec-Beispiel (VDI-6022), Architektur; Header (Dok.-Nr. POC-WIP-2026-001, Datum, „Umsetzungskonzept POC/WIP"), Footer mit CertoClav-Firmendaten + support@certoclav.com. Aufwandstabelle bewusst entfernt.
- **Workshop-Fragebogen (Word):** `Workshop_Fragebogen_POC_WIP.docx` – 14 Blöcke (A–N): Rahmen/Rechnungslegung, Projekte/Verträge, Kostenarten/Datenquellen, POC-Methode, WIP & Über-/Unterfakturierung, drohende Verluste, Cost-to-Complete-Prozess, Billing, Beschaffung/Accruals, Periodenabschluss/Kontrolle, Währung/Mehrgesellschaft, Reporting, Systemumfeld/Technik, Sonstiges. Ausfüllbar (Checkboxen + Antwortlinien).
- **E-Mail-Entwürfe:** (a) fachliche Antwort auf die zwei Anforderungen mit ✅/⬜-Markierung (was funktioniert / Todo) und Verweis auf das Konzept (kostengünstigster Ansatz); (b) kurze, bewusst zurückhaltende Vorstellungs-Mail an Jeannette (Kontakt über Moritz; unverbindlich Inspiration/Input; bei Interesse auch Implementierung).

---

## 9. Offene Punkte / Entscheidungen
- **Datenbasis für POC-Buchungen** (HGB vs. IFRS, Konten, Verlustantizipation) – mit StB/WP zu klären.
- **Umfang der Umsetzung** (nur POC/WIP oder auch Service-Accruals/Cut-off gleich mit).
- **Buchungsmodus:** nur Entwürfe (empfohlen) vs. automatisches Buchen.
- **App vs. Custom-Dev:** prüfen, ob eine bestehende Odoo-App 70–80 % abdeckt (halbiert ggf. den Aufwand).
- Interesse/Go von Certania steht noch aus (Erstkontakt-Phase).

---

*Hinweis: Certania/biotec ist ein separates Projekt und hat nichts mit der CertoClav-Odoo-Produktivumgebung zu tun. Diese Datei fasst ausschließlich den Analyse-/Konzeptstand zusammen.*

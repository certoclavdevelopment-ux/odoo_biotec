# Eingangsstatus der Datenanforderung

Interne Nachverfolgung zu `04_Kundendokumente/Datenanforderung_biotec.docx` (Dok.-Nr.
DATA-2026-001). Beim Eingang: Datum eintragen, Ablageort ergänzen, Status setzen.
Gelieferte Dateien kommen unverändert nach `00_eingang/JJJJ-MM-TT_quelle/`.

**Koordination auf biotec-Seite:** Michael Brand (fachlich/technisch) und Nicole Krupa
(kaufmännisch/organisatorisch). Nachfassen läuft über die beiden – nicht direkt bei den in
der Spalte „Wer" genannten Personen.

Status: `offen` · `angefragt` · `eingegangen` · `geprüft` · `entfällt`

**Stand 31.08.2026** – Sichtung des freigegebenen OneDrive-Ordners `Certania/Odoo Biotec Rohdaten`. biotec meldet den Upload als abgeschlossen.

**Wiederkehrendes Muster:** Zwei der wichtigsten Lieferungen sind nicht maschinell auswertbar – die Kundenliste ist eine gedruckte Kontaktliste, die Summen-Salden-Liste besteht aus Bildschirmfotos. Bei künftigen Anforderungen ausdrücklich nach „Export aus dem System“ fragen, nicht nach „Liste“.

## Paket 1 – für Scoping und Aufwandsschätzung

| Nr. | Inhalt | Wer | Status | Eingang | Ablage / Bemerkung |
|---|---|---|---|---|---|
| A1 | Kundenliste | N. Krupa | **eingegangen, unzureichend** | 31.08. | `01 Kunden und Lieferanten (A)/Kundenliste (alt - nicht aktualisiert).xlsx` – 166 Zeilen × 7 Spalten. Ist eine **Kontaktliste**, kein Kundenstamm: keine Kundennummer, keine USt-IdNr., keine Zahlungsbedingung, keine Preisgruppe. Kopfzeile mitten im Blatt wiederholt, Ansprechpartner ohne Firmenzuordnung in der Zeile, Spaltenversatz und Dubletten. Für die Schätzung brauchbar, für die Migration nicht |
| A3 | Lieferantenliste inkl. Fremdlabore | A. Krupa | **abhängig von H1** | | Die Kreditoren stecken in derselben Summen-Salden-Liste wie H1 und teilen deren Problem – Bilder statt Text. Mit einem Excel- oder CSV-Export sind A3 und H1 zugleich erledigt |
| B1 | Anlagen-/Objektstamm | M. Brand | **eingegangen** | 31.08. | `02 Anlagen und Objekte (B)/B1 Anlagen und Objektstamm (beispielhaft bei Kunden)` |
| B2 | Beispiel-Anlagenlisten (Datei + Ausdruck) | M. Brand | **eingegangen** | 31.08. | `02 Anlagen und Objekte (B)/B2 Anlagenlisten` |
| D1 | Gutachten je Berichtstyp (PDF) | M. Brand | **eingegangen** | 31.08. | `04 Gutachten und Vorlagen (D)/D1_fertige Gutachten (altes Branding)` – 16,6 MB |
| D2 | Vorlagendateien des Gutachtenprogramms | Westbomke | **eingegangen** | 31.08. | `04 Gutachten und Vorlagen (D)/D2_Vorlagen Gutachtensoftware` – 1,7 MB |
| D3 | Belegmuster (Angebot, AB, LS, Rechnung, Mahnung) | N. Krupa | **eingegangen** | 31.08. | Verteilt: Lieferscheine und Mahnungen unter D3, Angebote in E1, Rechnungen in E2 (Verweise als .txt hinterlegt) |
| D4 | Briefpapier, Logo als Vektor, CI | N. Krupa | **eingegangen** | 31.08. | `D4_Briefvorlage` und `D4_Logo - Schriftart - Farben` – 47,5 MB |
| E1 | Angebote & Auftragsbestätigungen | N. Krupa | **eingegangen** | 31.08. | `05 .../E1_Angebote Auftragsbestätigungen` – 44 MB |
| E2 | Ausgangsrechnungen | N. Krupa | **eingegangen** | 31.08. | `05 .../E2_Ausgangsrechnungen Mai bis Mitte August` – 33 MB |
| E4 | Verträge (Rahmen, Wartung, Prüfung) | M. Brand | **eingegangen** | 31.08. | `05 .../E4_Rahmenverträge (Beispiele)` – 13,5 MB |
| F1 | Artikelliste mit Bestand | A. Krupa | **offen** | | Ordner `06 Artikel und Lager (F)` ist leer. Bestände werden zum Go-live per Stichtagsinventur erfasst, das Artikelspektrum kommt aus den Eingangsrechnungen |
| G1 | Kurskatalog | N. Krupa | **eingegangen** | 31.08. | `07 Schulungen (G)/G1_Kurskatalog` |
| H1 | Vollständiger Kontenrahmen | A. Krupa | **eingegangen, nicht auswertbar** | 31.08. | `08 Buchhaltung (H)/H1_Konten Summe-Saldenliste Januar bis Juli.pdf` – 7 Seiten, 1,3 MB. Enthält laut biotec alle Buchungskonten inkl. Kreditoren. **Die Seiten sind Bilder**: extrahierbarer Text sind nur die sieben Monatsnamen. Nachgefordert am 31.08. als XLSX/CSV oder als gedrucktes PDF mit Textebene |
| I1 | Datenbanksystem, Version, Schema | Westbomke | **eingegangen** | 31.08. | Aus Quellcode und Datenbankinhalten ableitbar. Datenbanksystem und Version in der Fernwartungssitzung bestätigen lassen – eine Zeile |
| I2 | Datenbank-Sicherung / Vollexport | Westbomke | **eingegangen** | 31.08. | In `Current-2026-08-22.zip` enthalten (Prüfung Michael Simon). Damit liegen auch die Datenmengen je Tabelle vor – der Multiplikator für die Migrationsschätzung |
| I4 | Schnittstellenliste | Westbomke | **offen** | | Nichts im Ordner |
| I5 | Screenshots der Hauptmasken | M. Brand | **entfällt** | | Ersetzt durch die Fernwartungssitzung mit Westbomke EDV (Jonas Leitenmeier) |
| J3 | Endgeräte & Netzabdeckung vor Ort | Westbomke | **offen** | | Nichts im Ordner |
| K1 | Handelsregisterauszüge, Gesellschaftsstruktur | Wilke / Bermpohl | **eingegangen** | 31.08. | `10 Firma und Organisation (K)/K1_Handesregisterauszug` |

## Leere Ordner in der Lieferung

| Ordner | Betroffene Positionen | Paket |
|---|---|---|
| `03 Labor (C)` | C1 bis C4 (Probenbegleitschein, Analysemethoden, Kennzeichnung, Fremdlabor) | 2 |
| `06 Artikel und Lager (F)` | F1 (Paket 1), F2, F3 | 1 / 2 |
| `08 Buchhaltung (H)` | H2 bis H8 – H1 liegt vor, ist aber als Bild nicht auswertbar | 2 |
| `11 Sonstiges und Fragen` | – | – |

In `10 Firma und Organisation (K)` liegt neben K1 nur `K2_Terminplanung Außendienst`; das
Organigramm nach K2 fehlt. Zu Block L (Certania-Reporting) liegt nichts vor.

## Paket 2 und 3

Die restlichen 40 Positionen (A2, B3–B4, C1–C4, D5, E3, E5–E6, F2–F3, G2–G7, H2–H8,
I3, I6–I7, J1–J2, J4–J5, K2–K5, L1–L3) laufen nach dem Scoping nach. Vollständige Liste
im Kundendokument.

## Hinweise zur Ablage

- **Die Daten liegen in OneDrive, nicht im Repo.** biotec lädt direkt in den freigegebenen
  Ordner `Certania\Odoo Biotec Rohdaten\` in die Ordner 01 bis 11.
- Die Position im Dateinamen verbindet Datei und Tabellenzeile oben. Details in `README.md`.
- Je Lieferung eine Zeile in `LIEFERUNGEN.md` – die liegt im Repo, damit der Verlauf
  versioniert ist.
- Personenbezogene Daten werden **nicht** anonymisiert angefordert – NDA-2026-001 und
  AVV-2026-001 sind seit 22.08.2026 beidseitig unterschrieben.
- **ZIP-Archive sind über den Microsoft-365-Zugriff nicht lesbar** (`application/zip` wird
  abgelehnt). `Current-2026-08-22.zip` wurde daher lokal geprüft.
- **Quellcode und Datenbankinhalte: eingegangen** (Prüfung Michael Simon, 31.08.2026). Es fehlen
  nur einzelne kleine Dateien, etwa Briefköpfe und Vorlagen aus der Software. Nachreichen zu
  einem späteren Zeitpunkt genügt; für Angebot und Einrichtungsplan reicht der jetzige Stand.
  Vor dem Produktivstart der Dokumentausgabe nachfassen, sonst fehlt das Briefpapier im
  fertigen Gutachten.

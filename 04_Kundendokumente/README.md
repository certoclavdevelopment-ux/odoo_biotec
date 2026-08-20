# Kundendokumente

Dokumente, die an biotec bzw. Certania gehen oder gegangen sind. Alles hier ist kundenfähig –
keine internen Aufwandsschätzungen, keine Preisindikationen, keine interne Bewertung von
Stakeholdern.

| Dokument | Inhalt | Adressat | Status |
|---|---|---|---|
| `POC_WIP_Certania_biotec.docx` | Umsetzungskonzept POC/WIP: Erklärung, Rechenbeispiel VDI-6022-Hygieneinspektion Klinikum (120.000 € / 8 Monate), monatlicher Prozess, Architektur, Odoo-Einordnung. Dok.-Nr. POC-WIP-2026-001. Aufwandstabelle bewusst entfernt. | Certania (Jeannette Bühler) | erstellt |
| `Workshop_Fragebogen_POC_WIP.docx` | Erhebungsfragebogen, 14 Blöcke A–N: Rechnungslegung, Projekte/Verträge, Kostenarten, POC-Methode, WIP, drohende Verluste, Cost-to-Complete, Billing, Beschaffung/Accruals, Periodenabschluss, Währung, Reporting, Systemumfeld, Sonstiges | Certania / biotec Finance | erstellt, **noch nicht versendet** |
| `Datenanforderung_biotec.docx` | 60 Positionen in 12 Blöcken (A–L) mit Format, Verantwortlichem und Paket-Priorität; Paket 1 gelb hinterlegt (20 Positionen). Fordert ausdrücklich **keine** Anonymisierung – Exporte unverändert. Dok.-Nr. DATA-2026-001. Generiert aus `06_Arbeitsdateien/skripte/datenanforderung.py` | biotec | erstellt, **noch nicht versendet** |
| `NDA_CertoClav_biotec.docx` | Gegenseitige Vertraulichkeitsvereinbarung, 9 Abschnitte: Zweck, vertrauliche Informationen (inkl. Quellcode und Datenbank), Ausnahmen, Pflichten, personenbezogene Daten mit Abgrenzung zum AV-Vertrag, keine Rechteübertragung, Rückgabe/Löschung, Laufzeit 3 Jahre, Schlussbestimmungen. Dok.-Nr. NDA-2026-001. **Version 2 vom 19.08.2026** mit Ziffer 4.6 (nachvertragliche Wirkung), Dr. Bermpohl als Unterzeichner und den Registerdaten (Amtsgericht Gütersloh HRB 3829). **Vorlage, keine Rechtsberatung – vor Verwendung prüfen lassen.** Vorbelegt: deutsches Recht, Gerichtsstand Gütersloh | biotec | erstellt, wird auf Wunsch versendet |
| `AVV_CertoClav_biotec.docx` | Vertrag über die Auftragsverarbeitung nach Art. 28 DSGVO, 10 Abschnitte plus zwei Anlagen: technische und organisatorische Maßnahmen (Art. 32) und Unterauftragsverarbeiter. Dok.-Nr. AVV-2026-001. Ergänzt Ziffer 5.2 der NDA. **Unterschriftsfertig** – Anlage 2 nennt abschließend Microsoft Ireland und Odoo S.A., Verarbeitung nur in EU/EWR. Ziffer 2.4 grenzt nicht personenbezogene Daten ausdrücklich aus (dafür gilt die NDA). Ziffer 4.4 sagt zu, dass keine personenbezogenen Daten durch KI-Dienste verarbeitet werden – **diese Zusage bindet die Umsetzung**, betrifft aber nur den personenbezogenen Anteil. Vorlage, keine Rechtsberatung | biotec | erstellt |
| `2026-08-20_email-antwort-avv.md` | Antwort an Melanie Frank: AVV anbei, Standard von Certania bevorzugt angeboten, Hinweis auf Anlage 2 und die KI-Frage | biotec | Entwurf |
| `2026-08-19_email-antwort-nda-version2.md` | Versandfassung: NDA Version 2, keine Anonymisierung nötig, alles direkt hochladen. Mit optionalem Zusatz zum AV-Vertrag | biotec | Entwurf |
| `2026-08-18_email-antwort-nda-und-datenschutz.md` | Antwort auf die NDA-Prüfung von Nicole Krupa: Ziffer 4.6, Wechsel des Unterzeichners, Klarstellung zur Anonymisierung, Angebot eines AV-Vertrags | biotec | Entwurf |
| `00_BITTE_ZUERST_LESEN.txt` | Kurzanleitung für die Wurzel des freigegebenen OneDrive-Upload-Ordners: was gehört in welchen Ordner, zwei Bitten (nichts vorher aufbereiten, unvollständig ist besser als nichts), Ansprechpartner. UTF-8 mit BOM und CRLF, damit Notepad die Umlaute korrekt zeigt. | biotec | erstellt |

Eingangsnachverfolgung zur Datenanforderung: `05_Rohdaten_Kunde/eingangsstatus.md`.
Die Rohdaten selbst liegen in OneDrive – siehe `05_Rohdaten_Kunde/README.md`.

## Offener Punkt zum Fragebogen

Block M (Systemumfeld) fragt nach vorhandener Odoo-Edition, aktiven Modulen und der Übernahme
laufender Projekte mit bereits realisiertem WIP. Das setzt ein produktives Odoo voraus. Bei
biotec ist es eine Neueinführung mit noch unbekanntem Altsystem – Block M sollte vor dem
Versand entsprechend umformuliert werden (Ist-System statt Odoo-Bestand).

## Ausgefüllte Rückläufer

Ausgefüllte Fragebögen kommen nach `05_Rohdaten_Kunde/00_eingang/` mit Lieferdatum – nicht
hierher. Dieser Ordner enthält nur die ausgehenden Fassungen.

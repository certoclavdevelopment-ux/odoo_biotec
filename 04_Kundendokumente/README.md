# Kundendokumente

Dokumente, die an biotec bzw. Certania gehen oder gegangen sind. Alles hier ist kundenfähig –
keine internen Aufwandsschätzungen, keine Preisindikationen, keine interne Bewertung von
Stakeholdern.

| Dokument | Inhalt | Adressat | Status |
|---|---|---|---|
| `POC_WIP_Certania_biotec.docx` | Umsetzungskonzept POC/WIP: Erklärung, Rechenbeispiel VDI-6022-Hygieneinspektion Klinikum (120.000 € / 8 Monate), monatlicher Prozess, Architektur, Odoo-Einordnung. Dok.-Nr. POC-WIP-2026-001. Aufwandstabelle bewusst entfernt. | Certania (Jeannette Bühler) | erstellt |
| `Workshop_Fragebogen_POC_WIP.docx` | Erhebungsfragebogen, 14 Blöcke A–N: Rechnungslegung, Projekte/Verträge, Kostenarten, POC-Methode, WIP, drohende Verluste, Cost-to-Complete, Billing, Beschaffung/Accruals, Periodenabschluss, Währung, Reporting, Systemumfeld, Sonstiges | Certania / biotec Finance | erstellt, **noch nicht versendet** |
| `Datenanforderung_biotec.docx` | 60 Positionen in 12 Blöcken (A–L) mit Format, Verantwortlichem und Paket-Priorität; Paket 1 gelb hinterlegt (20 Positionen). Fordert ausdrücklich **keine** Anonymisierung – Exporte unverändert. Dok.-Nr. DATA-2026-001. Generiert aus `06_Arbeitsdateien/skripte/datenanforderung.py` | biotec | erstellt, **noch nicht versendet** |
| `NDA_CertoClav_biotec.docx` | Gegenseitige Vertraulichkeitsvereinbarung, 9 Abschnitte: Zweck, vertrauliche Informationen (inkl. Quellcode und Datenbank), Ausnahmen, Pflichten, personenbezogene Daten mit Abgrenzung zum AV-Vertrag, keine Rechteübertragung, Rückgabe/Löschung, Laufzeit 3 Jahre, Schlussbestimmungen. Dok.-Nr. NDA-2026-001. **Version 2 vom 19.08.2026** mit Ziffer 4.6 (nachvertragliche Wirkung), Dr. Bermpohl als Unterzeichner und den Registerdaten (Amtsgericht Gütersloh HRB 3829). **Vorlage, keine Rechtsberatung – vor Verwendung prüfen lassen.** Vorbelegt: deutsches Recht, Gerichtsstand Gütersloh | biotec | **unterzeichnet 22.08.2026** |
| `AVV_CertoClav_biotec.docx` | Vertrag über die Auftragsverarbeitung nach Art. 28 DSGVO, 10 Abschnitte plus zwei Anlagen: technische und organisatorische Maßnahmen (Art. 32) und Unterauftragsverarbeiter. Dok.-Nr. AVV-2026-001. Ergänzt Ziffer 5.2 der NDA. **Unterschriftsfertig** – Anlage 2 nennt abschließend Microsoft Ireland und Odoo S.A., Verarbeitung nur in EU/EWR. Ziffer 2.4 grenzt nicht personenbezogene Daten ausdrücklich aus (dafür gilt die NDA). Ziffer 4.4 erlaubt den Einsatz von KI-Diensten, die in Anlage 2 benannt sind; Ziffer 4.5 fordert Trainingsausschluss, geschäftliche Nutzungsbedingungen und Datenminimierung. Ziffer 1.5 benennt die weisungsberechtigten Personen (Art. 28 Abs. 3 lit. a). Im Dokument stehen keine Platzhalter – auszufüllen sind nur Ort, Datum und die beiden Unterschriften. Der Generator kann über `KI_ERLAUBT` auf die enge Variante ohne KI-Verarbeitung umschalten – diese wird biotec **nicht** angeboten (Entscheidung vom 20.08.2026). Vorlage, keine Rechtsberatung | biotec | **unterzeichnet 22.08.2026** |
| `2026-09-01_email-antwort-frank-datenlieferung-abgeschlossen.md` | Schließt die Datenphase ab: Lieferung reicht für die Aufwandsschätzung, kein Nachreichen nötig, Excel-Export der Saldenliste erst bei einem GO. Meldet die Auswertung von Quellcode und Datenbank, stellt die Rückfrage zur fehlenden Pixel-8-Anbindung und weist auf die Zugangsdaten im Klartext hin | biotec / Westbomke EDV | Entwurf |
| `2026-08-31_email-antwort-frank-saldenliste.md` | **überholt, nicht versendet.** Antwort an Melanie Frank: die Summen-Salden-Liste deckt H1 und A3 inhaltlich ab, das PDF enthält aber nur Bilder (lesbarer Text sind allein die sieben Monatsnamen). Bitte um XLSX/CSV-Export oder ein gedrucktes PDF mit Textebene, dazu die Kontenstammliste | biotec | Entwurf |
| `2026-08-23_email-antwort-frank-eingangsrechnungen.md` | Antwort an Melanie Frank: Maßstab der Phase ist Angebot und Einrichtungsplan, nicht Migration. Für die Eingangsrechnungen genügt daher eine Stichprobe (ein Monat oder 20 bis 30 Belege); noch besser ein Export von Kreditorenstamm oder Buchungsjournal. Lagerbestände sind daraus nicht ableitbar und werden per Inventur zum Go-live erfasst. Fragt nach eigenen Dateien in München und Mittweida | biotec | Entwurf |
| `2026-08-22_email-antwort-westbomke-software.md` | Antwort an Markus Westbomke: Fernwartung angenommen, Terminfindung über Jonas Leitenmeier (Di bis Do 10 bis 15 Uhr, zwei Vorschläge von Westbomke), eine Stunde reservieren. Kernauftrag: alles durchklicken. Benennt den Quellcode ausdrücklich als wertvollste Lieferung – für die KI-Auswertung mehr wert als jede Aufnahme | biotec / Westbomke EDV | Entwurf |
| `2026-08-22_email-antwort-brand-datenupload.md` | Antwort an Michael Brand: alles unbearbeitet hochladen – die Auswertung läuft KI-gestützt, niemand liest die Rohdateien durch, Vollständigkeit und Erläuterungen sind nicht nötig. Einzige Ausnahme ist die Gutachten-Software (Zugang oder Bildschirmaufnahme, Datenbank, Quellcode, Vorlagen). Reine Textfassung zum Kopieren | biotec | Entwurf |
| `2026-08-20_email-antwort-avv.md` | Antwort an Melanie Frank, Kurzfassung: AVV unterschriftsfertig anbei, Abgrenzung zur NDA und Ausschluss der Art.-9-Daten, geregelter KI-Einsatz, Anlage 2 mit Anthropic (USA, EU-Standardvertragsklauseln). Die enge Variante wird bewusst nicht angeboten | biotec | Entwurf |
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

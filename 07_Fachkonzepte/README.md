# Fachkonzepte

Fachlicher Wissensstand und Lösungskonzepte.

| Datei | Inhalt | Vertraulichkeit |
|---|---|---|
| `wissensstand-odoo-certania-biotec.md` | Konsolidierter Wissensstand (10.08.2026): Certania & biotec, die zwei Kernanforderungen von Jeannette Bühler, ehrliche Odoo-Einordnung (was geht / was nicht), POC/WIP-Konzept mit Rechenbeispiel, empfohlene Architektur, Rechenlogik | **intern** – Abschnitt 6 enthält Aufwandsrichtwerte, die ausdrücklich nicht nach außen kommuniziert werden |

Die kundenfähige Fassung des POC/WIP-Konzepts (ohne Aufwandstabelle) liegt in
`04_Kundendokumente/POC_WIP_Certania_biotec.docx`.

## Kernaussagen in einem Satz

Odoo deckt P2P/O2C integriert ab und liefert Projektmargen in Echtzeit; eine **bilanzielle
POC-/WIP-Umsatzrealisierung nach Fertigstellungsgrad ist kein Odoo-Standard** und wird über
eine externe Python-App ergänzt, die monatlich rechnet und Entwurfsbuchungen in Odoo anlegt –
gebucht wird final von einem Menschen.

## Zu beachten

Der Wissensstand wurde geschrieben, als noch offen war, ob bei biotec schon ein Odoo läuft.
Für biotec gilt: **Greenfield-Einführung**, Altsystem noch unbekannt. Das ist für POC/WIP
günstig – Kontenrahmen, Analytikstruktur und Projektlogik können von Anfang an passend
aufgesetzt werden, statt sie nachträglich umzubauen.

@echo off
REM ===================================================================
REM  OneDrive-Ordner fuer das Odoo-Projekt biotec.
REM
REM  Stand: "Odoo Biotec Rohdaten" ist bereits an biotec FREIGEGEBEN und
REM  enthaelt die Kundenordner 01 bis 11. Dieses Skript
REM    - ergaenzt fehlende Kundenordner dort (idempotent)
REM    - legt daneben "Odoo Biotec Intern" fuer unsere Arbeit an
REM    - listet auf, was im freigegebenen Ordner NICHTS zu suchen hat
REM
REM  Auf dem Rechner von Michael Simon ausfuehren.
REM ===================================================================

set BASIS=%USERPROFILE%\OneDrive - CertoClav Sterilizer GmbH\Certania
set KUNDE=%BASIS%\Odoo Biotec Rohdaten
set INTERN=%BASIS%\Odoo Biotec Intern

echo Basispfad: %BASIS%
if not exist "%BASIS%" (
    echo FEHLER: Basispfad nicht gefunden. Bitte BASIS im Skript anpassen.
    pause
    exit /b 1
)

REM ---------- Kundenordner (freigegeben) ergaenzen ----------
md "%KUNDE%" 2>nul
pushd "%KUNDE%"
md "01 Kunden und Lieferanten (A)" 2>nul
md "02 Anlagen und Objekte (B)" 2>nul
md "03 Labor (C)" 2>nul
md "04 Gutachten und Vorlagen (D)" 2>nul
md "05 Angebote, Rechnungen, Vertraege (E)" 2>nul
md "06 Artikel und Lager (F)" 2>nul
md "07 Schulungen (G)" 2>nul
md "08 Buchhaltung (H)" 2>nul
md "09 IT und Altsystem (I+J)" 2>nul
md "10 Firma und Organisation (K)" 2>nul
md "11 Sonstiges und Fragen" 2>nul
popd
echo Kundenordner geprueft und ergaenzt.

REM ---------- Interner Arbeitsordner (NICHT freigeben) ----------
md "%INTERN%" 2>nul
pushd "%INTERN%"
md "00_eingang\A_Kunden_Lieferanten" 2>nul
md "00_eingang\B_Anlagen_Objekte" 2>nul
md "00_eingang\C_Labor" 2>nul
md "00_eingang\D_Gutachten_Belege_Layout" 2>nul
md "00_eingang\E_Verkauf_Einkauf" 2>nul
md "00_eingang\F_Artikel_Lager" 2>nul
md "00_eingang\G_Schulungen" 2>nul
md "00_eingang\H_Buchhaltung_Finanzen" 2>nul
md "00_eingang\I_Altsystem_Delphi" 2>nul
md "00_eingang\J_IT_Infrastruktur" 2>nul
md "00_eingang\K_Organisation_Struktur" 2>nul
md "00_eingang\ZZ_unsortiert" 2>nul
md "01_aufbereitet\10_stammdaten" 2>nul
md "01_aufbereitet\20_bestaende_offene_posten" 2>nul
md "01_aufbereitet\30_historie" 2>nul
md "99_gross_und_vertraulich" 2>nul
popd
echo Interner Arbeitsordner angelegt.

REM ---------- Kontrolle: was liegt im freigegebenen Ordner? ----------
echo.
echo ============================================================
echo Inhalt des FREIGEGEBENEN Ordners - biotec sieht das alles:
echo ============================================================
dir /b /ad "%KUNDE%"
echo.
echo Dort duerfen NUR die Ordner 01 bis 11 und die Datei
echo 00_BITTE_ZUERST_LESEN.txt liegen.
echo Falls 00_eingang, 01_aufbereitet oder 99_... auftauchen:
echo bitte nach "Odoo Biotec Intern" verschieben.
echo.

echo Noch zu tun:
echo   1. 00_BITTE_ZUERST_LESEN.txt in die Wurzel des Kundenordners kopieren
echo   2. Freigabe pruefen: nur Michael Brand und Nicole Krupa, mit Schreibrecht
echo   3. "Odoo Biotec Intern" NICHT freigeben
echo.
pause

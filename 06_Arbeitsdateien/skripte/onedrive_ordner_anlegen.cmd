@echo off
REM ===================================================================
REM  Legt die OneDrive-Ordner fuer das Odoo-Projekt biotec an.
REM
REM  Zwei getrennte Ordner:
REM    "Odoo Biotec Upload biotec"  -> wird an biotec freigegeben
REM    "Odoo Biotec Rohdaten"       -> nur CertoClav, nicht freigeben
REM
REM  Auf dem Rechner von Michael Simon ausfuehren. Basispfad ggf. anpassen.
REM ===================================================================

set BASIS=%USERPROFILE%\OneDrive - CertoClav Sterilizer GmbH\Certania

echo Basispfad: %BASIS%
if not exist "%BASIS%" (
    echo FEHLER: Basispfad nicht gefunden. Bitte BASIS im Skript anpassen.
    pause
    exit /b 1
)

REM ---------- Freigegeben an biotec ----------
set UPLOAD=%BASIS%\Odoo Biotec Upload biotec
md "%UPLOAD%" 2>nul
pushd "%UPLOAD%"
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
echo Upload-Ordner angelegt.

REM ---------- Nur CertoClav ----------
set ARBEIT=%BASIS%\Odoo Biotec Rohdaten
md "%ARBEIT%" 2>nul
pushd "%ARBEIT%"
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
md "99_nicht_im_repository" 2>nul
popd
echo Arbeitsordner angelegt.

echo.
echo Fertig. Noch zu tun:
echo   1. 00_BITTE_ZUERST_LESEN.txt aus 04_Kundendokumente in den Upload-Ordner kopieren
echo   2. Upload-Ordner an Michael Brand und Nicole Krupa freigeben
echo   3. NUR den Upload-Ordner freigeben, nicht "Odoo Biotec Rohdaten"
echo.
pause

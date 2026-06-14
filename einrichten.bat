@echo off
chcp 65001 >nul
echo.
echo  =============================================
echo   WordPress MCP – heidifrank.de
echo   Automatische Einrichtung
echo  =============================================
echo.

:: ── 1. Zielordner anlegen ──────────────────────────────────────────────────
set ZIEL=C:\HeidiFrank-WordPress
if not exist "%ZIEL%" (
    mkdir "%ZIEL%"
    echo [OK] Ordner erstellt: %ZIEL%
) else (
    echo [OK] Ordner vorhanden: %ZIEL%
)

:: ── 2. MCP-Server-Skript dorthin kopieren ──────────────────────────────────
copy /Y "%~dp0wordpress-mcp-server.py" "%ZIEL%\wordpress-mcp-server.py" >nul
echo [OK] wordpress-mcp-server.py kopiert nach %ZIEL%

:: ── 3. Claude-Konfig-Ordner sicherstellen ──────────────────────────────────
set CLAUDE=%USERPROFILE%\.claude
if not exist "%CLAUDE%" (
    mkdir "%CLAUDE%"
    echo [OK] Claude-Ordner erstellt: %CLAUDE%
)

:: ── 4. settings.json schreiben ─────────────────────────────────────────────
set SETTINGS=%CLAUDE%\settings.json

if exist "%SETTINGS%" (
    echo.
    echo [HINWEIS] Du hast bereits eine settings.json.
    echo          Der neue Eintrag wird als separate Datei gespeichert.
    echo          Bitte manuell in deine bestehende settings.json einfuegen.
    echo.

    (
        echo {
        echo   "mcpServers": {
        echo     "heidifrank-wordpress": {
        echo       "command": "python",
        echo       "args": ["%ZIEL%\\wordpress-mcp-server.py"],
        echo       "env": {
        echo         "WP_URL": "https://heidifrank.de",
        echo         "WP_USER": "HIER-BENUTZERNAME-EINTRAGEN",
        echo         "WP_PASSWORD": "HIER-ANWENDUNGSPASSWORT-EINTRAGEN",
        echo         "PEXELS_API_KEY": "",
        echo         "OPENAI_API_KEY": "",
        echo         "HIGGSFIELD_API_KEY": ""
        echo       }
        echo     }
        echo   }
        echo }
    ) > "%CLAUDE%\settings-heidifrank-ergaenzung.json"

    echo [OK] Gespeichert als: %CLAUDE%\settings-heidifrank-ergaenzung.json

) else (
    (
        echo {
        echo   "mcpServers": {
        echo     "heidifrank-wordpress": {
        echo       "command": "python",
        echo       "args": ["%ZIEL%\\wordpress-mcp-server.py"],
        echo       "env": {
        echo         "WP_URL": "https://heidifrank.de",
        echo         "WP_USER": "HIER-BENUTZERNAME-EINTRAGEN",
        echo         "WP_PASSWORD": "HIER-ANWENDUNGSPASSWORT-EINTRAGEN",
        echo         "PEXELS_API_KEY": "",
        echo         "OPENAI_API_KEY": "",
        echo         "HIGGSFIELD_API_KEY": ""
        echo       }
        echo     }
        echo   }
        echo }
    ) > "%SETTINGS%"

    echo [OK] settings.json erstellt: %SETTINGS%
)

:: ── 5. Python-Pakete installieren ──────────────────────────────────────────
echo.
echo [..] Installiere Python-Pakete (mcp + requests)...
pip install mcp requests >nul 2>&1
echo [OK] Pakete installiert

:: ── 6. Anleitung anzeigen ──────────────────────────────────────────────────
echo.
echo  =============================================
echo   FERTIG – was du jetzt noch tun musst:
echo  =============================================
echo.
echo  1. Oeffne diese Datei:
echo     %SETTINGS%
echo     (oder: %CLAUDE%\settings-heidifrank-ergaenzung.json)
echo.
echo  2. Ersetze die zwei Platzhalter:
echo     WP_USER     ^> dein WordPress-Benutzername
echo     WP_PASSWORD ^> das Anwendungspasswort aus WordPress
echo              (WordPress Admin ^> Benutzer ^> Profil ^> nach unten scrollen)
echo.
echo  3. Claude Code neu starten
echo.
echo  4. In Claude Code eingeben:
echo     "Teste die WordPress-Verbindung zu heidifrank.de"
echo.
echo  =============================================
echo.
pause

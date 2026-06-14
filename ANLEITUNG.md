# WordPress MCP – heidifrank.de
## Schritt-für-Schritt Einrichtung

---

## SCHRITT 1: Anwendungspasswort in WordPress erstellen

1. Öffne: **https://heidifrank.de/wp-admin**
2. Links im Menü: **Benutzer → Profil**
3. Ganz nach unten scrollen zu **"Anwendungspasswörter"**
4. Im Textfeld Namen eingeben: `Claude-Code`
5. Klick auf **"Anwendungspasswort hinzufügen"**
6. Das Passwort das erscheint **sofort kopieren und aufschreiben**
   (sieht aus wie: `xxxx xxxx xxxx xxxx xxxx xxxx`)
   → Es wird NUR einmal angezeigt!

---

## SCHRITT 2: Pexels API-Key holen (kostenlos, für Bilder)

1. Gehe zu: https://www.pexels.com/api/
2. Konto erstellen (kostenlos)
3. API-Key kopieren (langer Text)

---

## SCHRITT 3: Zugangsdaten eintragen

Öffne die Datei `.claude/settings.json` in diesem Ordner.

Ersetze diese Werte:
```
"WP_USER":      "DEIN-BENUTZERNAME"     → dein WordPress-Admin-Benutzername
"WP_PASSWORD":  "xxxx xxxx xxxx..."     → das Anwendungspasswort aus Schritt 1
"PEXELS_API_KEY": "DEIN-PEXELS-KEY"    → der Pexels API-Key aus Schritt 2
```

---

## SCHRITT 4: Python-Pakete installieren

Einmal im Terminal ausführen (oder Doppelklick auf `einrichten.bat`):
```
pip install mcp requests
```

---

## SCHRITT 5: Verbindung testen

In Claude Code eingeben:
```
Teste die WordPress-Verbindung zu heidifrank.de
```

Claude antwortet dann mit: Verbindung OK! oder erklärt was nicht stimmt.

---

## SCHRITT 6: Ersten Blogbeitrag erstellen

Einfach in Claude Code eingeben, zum Beispiel:
```
Schreib einen Blogbeitrag für heidifrank.de über das Thema
"Stressabbau in 5 Minuten" – mit Tabelle, Checkliste und Bild.
Als Entwurf speichern.
```

Claude erstellt dann:
- Professionellen Block-Aufbau in den Farben von heidifrank.de
- Passende Bilder von Pexels automatisch
- Tabellen und Checklisten wo sinnvoll
- CTA-Block mit Kontakt-Button
- Speichert als Entwurf → du siehst es zuerst in WordPress

---

## Was Claude automatisch macht

| Claude-Befehl | Was passiert |
|---|---|
| "Blogbeitrag über [Thema]" | Erstellt vollständigen Beitrag als Entwurf |
| "Veröffentliche Beitrag ID 123" | Schaltet Entwurf live |
| "Zeig mir alle Beiträge" | Listet alle Posts mit Status |
| "Welche Kategorien gibt es?" | Zeigt WordPress-Kategorien |

---

## Block-Elemente die Claude einbaut

- **Einleitungs-Block** (orangener Rand, kursiv, fesselnd)
- **Inhalts-Blöcke** (abwechselnd weiß / hellgrau, mit Bild)
- **Tipp-Box** (Orange-Gold Gradient, hervorgehoben)
- **Tabelle** (mit orangenen Kopfzeilen)
- **Checkliste** (mit orangen Haken)
- **Fazit-Block** (goldener Balken oben)
- **CTA-Block** (dunkel mit orangem Button)
- **Autorinnen-Zeile** (Heidi Frank, Gesundheitspädagogin)

---

## Farben der Vorlage

| Element | Farbe | Hex |
|---|---|---|
| Überschriften, Akzente | Orange-Rot | `#D94A15` |
| Goldakzent (Logo-Stil) | Gold | `#D4A020` |
| Hintergrund Blöcke | Warmweiß | `#FFF8F5` |
| Grauer Block | Hellgrau | `#F5F5F0` |
| Fließtext | Dunkelgrau | `#333333` |

---

## Dateien in diesem Ordner

| Datei | Was sie macht |
|---|---|
| `wordpress-mcp-server.py` | Der MCP-Server (läuft im Hintergrund) |
| `.claude/settings.json` | Konfiguration (URL, Passwort, API-Key) |
| `blog-vorlage-vorschau.html` | Vorschau wie Beiträge aussehen |
| `einrichten.bat` | Windows-Einrichtung per Doppelklick |
| `ANLEITUNG.md` | Diese Datei |

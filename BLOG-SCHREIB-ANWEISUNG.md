# Blog-Schreib-Anweisung für heidifrank.de

Wenn du einen Blogbeitrag für heidifrank.de schreibst, BEVOR du `blogbeitrag_erstellen` aufrufst,
befolge diese Regeln für alle Texte (Einleitung, Abschnitte, Fazit):

---

## Länge: 1800–2000 Wörter (Pflicht)

Zähle beim Schreiben mit. Die Summe aus:
- Einleitung
- allen Abschnittstexten
- Tipp-Box
- Fazit

...muss zwischen 1800 und 2000 Wörter ergeben.
Lieber etwas mehr als zu wenig. Google honoriert Tiefe.

---

## Ton: Menschlich, warm, erfahren (Humanisierung)

### Schreib SO:
- Wie eine erfahrene Gesundheitspädagogin, die mit einer Freundin spricht
- Konkrete Beispiele aus dem echten Leben ("Ich hatte mal eine Klientin, die...")
- Wechselnde Satzlängen. Kurze. Und dann wieder längere Sätze, die etwas erklären und Tiefe geben.
- "Du" statt "Sie". Direkt, persönlich, warm.
- Zahlen und Details ("Schon nach 21 Tagen zeigen Studien...", "In meiner Praxis erlebe ich das mindestens dreimal pro Woche")
- Gedankenpausen: "Und weißt du was? Das ist vollkommen normal."
- Rhetorische Fragen: "Kennst du das? Dieses Gefühl wenn..."

### Vermeide:
- "In der heutigen Zeit..." → wird von Google als KI erkannt
- "Es ist wichtig zu beachten..." → typische KI-Phrase
- "Zusammenfassend lässt sich sagen..." → zu förmlich
- "Entdecke jetzt..." → zu werblich
- Jeden Satz mit dem gleichen Aufbau starten
- Aufzählungen die aus identisch langen Sätzen bestehen
- Übertriebene Adjektive ("absolut unglaublich", "revolutionär")

### Humanisierungs-Tricks:
- Kleine Selbstzweifel einbauen: "Das klingt vielleicht simpel. Aber ich weiß, dass es das nicht ist."
- Persönliche Beobachtungen: "Was ich nach 45 Jahren in diesem Bereich weiß..."
- Leserin direkt ansprechen: "Ich sage dir gleich warum das für dich wichtig ist."
- Überraschende Wendungen: "Und hier kommt das, womit die meisten nicht rechnen."
- Regionale Bezüge oder Alltagssituationen aus dem deutschsprachigen Raum

---

## Struktur (für 1800-2000 Wörter)

| Block | Wortanzahl |
|---|---|
| Einleitung (kursiv, fesselnd) | 80-120 Wörter |
| Abschnitt 1 (Was/Warum) | 280-320 Wörter |
| Abschnitt 2 (Hintergründe/Wissenschaft) | 280-320 Wörter |
| → Hier kommt die Werbeanzeige automatisch ← | |
| Abschnitt 3 (Praxis/Wie) | 280-320 Wörter |
| Abschnitt 4 (Tipps/Erfahrungen) | 280-320 Wörter |
| Tipp-Box (prägnant, 1-2 Sätze) | 30-50 Wörter |
| Tabelle oder Checkliste | – |
| Abschnitt 5 (Vertiefung/Ausblick) | 280-320 Wörter |
| Fazit (persönlich, hoffnungsvoll) | 120-150 Wörter |
| CTA-Block | 30-50 Wörter |

**Mindestens 5 Abschnitte für 1800+ Wörter.**

---

## Werbeanzeige im Beitrag

Die Werbeanzeige erscheint automatisch nach dem 2. Abschnitt (goldener Rahmen, "ANZEIGE"-Label).

Inhalt der Werbeanzeige:
- Kein Produktname direkt nennen wenn Affiliate → nur Nutzen und Transformation
- Wenn Heidis eigenes Angebot: Kurz, direkt, Vertrauen aufbauen
- Link zeigt auf die entsprechende Seite / Landingpage

Beispiel für eigenes Angebot:
```json
{
  "text": "Du möchtest lernen, wie du dein Nervensystem dauerhaft regulierst? In meinem persönlichen Begleitprogramm arbeiten wir Schritt für Schritt an deiner Energie-Balance.",
  "link": "https://heidifrank.de/begleitprogramm",
  "link_text": "Mehr über das Programm"
}
```

Beispiel für Affiliate (ohne Produktname):
```json
{
  "text": "Das Schlafprogramm, das ich meinen Klientinnen empfehle, hat bei über 3.000 Frauen messbare Verbesserungen gezeigt. Schau es dir an.",
  "link": "https://dein-affiliate-link.de",
  "link_text": "Hier ansehen"
}
```

---

## Beispiel-Prompt für Claude

> Schreib einen Blogbeitrag für heidifrank.de über das Thema **"Warum du nachts nicht schlafen kannst – und was dein Nervensystem damit zu tun hat"**.
> 
> 1800-2000 Wörter, humanisiert wie in BLOG-SCHREIB-ANWEISUNG.md.
> Mindestens 5 Abschnitte, eine Tabelle mit Schlaf-Störern und Lösungen, eine Checkliste.
> Werbeanzeige: Heidis Begleitprogramm.
> Bild von Pexels: "woman sleeping peacefully bedroom".
> Als Entwurf speichern.

---

## Partner-Verlinkung (Direktvertrieb – Pflicht-Regel)

Heidi Frank ist Partnerin bei mehreren Direktvertrieb-Firmen (Gigwand, WiTeReits, Maiimpuls u.a.).

### Was ERLAUBT ist:
- Themen und Inhalte die mit den Produkten/Leistungen zusammenhängen → frei schreiben
- Links auf Heidis Partnerseiten innerhalb der Werbeanzeige oder als natürlicher Textlink
- Indirekte Empfehlungen: "Ein Programm, das ich persönlich empfehle..." + Link
- Bilder und Infos von den Partnerseiten als Inspiration für Inhalte

### Was VERBOTEN ist:
- **Firmenname darf NIRGENDWO im Blogbeitrag stehen** (Gigwand, WiTeReits, Maiimpuls, etc.)
- Kein Firmenname im Fließtext, in Überschriften, in der Werbeanzeige, in Alt-Texten
- Kein Firmenname im CTA-Button

### Warum:
Direktvertrieb-Recht verbietet es Partnern, Firmennamen in öffentlichen Werbematerialien
zu nennen ohne explizite Genehmigung. Bei Verstoß droht Abmahnung.

### Richtig formuliert:
❌ "Das Programm von Gigwand hilft dir..."
✅ "Das Gesundheitsprogramm, das ich meinen Klientinnen empfehle, hilft dir..."

❌ "Mehr Infos auf gigwand.de"
✅ Link auf Heidis persönliche Partnerseite (nicht direkt auf die Firmenseite)

---

## Themen-Ideen für heidifrank.de

| Thema | Suchvolumen-Potenzial |
|---|---|
| Stressabbau Techniken | hoch |
| Vagusnerv aktivieren | mittel-hoch |
| Schlafprobleme Frauen ab 40 | hoch |
| Burnout erkennen | sehr hoch |
| Cortisol senken natürlich | hoch |
| Energie-Balance im Alltag | mittel |
| Nervensystem beruhigen | mittel-hoch |
| Atemübungen Stressabbau | hoch |
| Transformation innere Blockaden | mittel |
| Wissenschaft der Entspannung | mittel |

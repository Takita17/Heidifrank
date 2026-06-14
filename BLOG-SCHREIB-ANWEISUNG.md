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

Heidi Frank ist Partnerin bei diesen Direktvertrieb-Firmen:

| Interne Bezeichnung | Was sie anbieten | Blog-Themen die passen |
|---|---|---|
| **Partner A** (Qi-Quant) | Quantenfeld-Technologie: Wasservitalisierung, Raumklima, Arbeitsplatz-Energie | Wasserqualität, Raumenergie, Elektrosmog, Vitalität |
| **Partner B** (Vitarights) | Frequenztechnologie, Vitalizer, Biophotonen, ViSponder | Frequenzmedizin, Zellerneuerung, Energie-Balance |
| **Partner C** (MyImpulse) | Nahrungsergänzung, Frequenz-Tropfen, B6+B12 | Vitaminmangel, Burnout, Energie, Immunsystem |
| **Partner D** (Wenura) | Neu – Details noch zu klären | – |

### Was ERLAUBT ist:
- Themen und Inhalte die mit den Produkten zusammenhängen → frei und ausführlich schreiben
- Links auf Heidis persönliche Partnerseiten (in der Werbeanzeige oder als Textlink)
- Indirekte Empfehlung: "Ein Gerät, das ich meinen Klientinnen zeige..." + Link
- Formulierungen wie "ein Frequenzgerät", "ein Nahrungsergänzungsprodukt", "eine Technologie..."

### Was VERBOTEN ist:
- **Kein Firmenname irgendwo im Beitrag** (Qi-Quant, Vitarights, MyImpulse, Wenura)
- Nicht in Überschriften, Fließtext, Werbeanzeige, Bildtexten, Alt-Tags, CTA
- Nicht mal andeutungsweise: "Qi..." oder "Vita..." als Abkürzung

### Warum:
Direktvertrieb-Gesetz: Ohne ausdrückliche Genehmigung des Unternehmens darf der Name
nicht in öffentlicher Werbung erscheinen. Verstoß = Abmahnung möglich.

### Richtig formuliert:
❌ "Das Qi-Quant Gerät hilft dir..."
✅ "Das Quantenfeld-Gerät, das ich selbst nutze, hat mein Raumklima verändert..." + Link

❌ "Mehr auf vitarights.de"
✅ Link auf Heidis eigene Partnerseite bei Vitarights

---

## Themen-Ideen für heidifrank.de

Themen die zu Heidis Arbeit passen UND natürlich zu einem oder mehreren Partnern führen:

| Thema | Suchvolumen | Passender Partner |
|---|---|---|
| Leitungswasser vs. vitales Wasser – was ist wirklich gesund? | hoch | Partner A (Wasservitalisierung) |
| Elektrosmog im Alltag – wie schützt du dein Nervensystem? | mittel-hoch | Partner A (Raumklima) |
| Frequenzmedizin: Was steckt wirklich dahinter? | mittel | Partner B |
| Biophotonen und Zellenergie – die Wissenschaft dahinter | mittel | Partner B |
| Vitaminmangel erkennen: Warum B6 und B12 so wichtig sind | sehr hoch | Partner C |
| Burnout oder Vitaminmangel? Wie du den Unterschied erkennst | hoch | Partner C |
| Stressabbau Techniken – was Wissenschaft und Erfahrung zeigen | hoch | Heidis Programm |
| Vagusnerv aktivieren: 5 Wege in 5 Minuten | mittel-hoch | Heidis Programm |
| Schlafprobleme Frauen ab 40 – die wahren Ursachen | hoch | Alle Partner |
| Cortisol senken natürlich – ohne Medikamente | hoch | Alle Partner |
| Energie-Balance im Alltag | mittel | Heidis Programm + Partner C |
| Nervensystem beruhigen – mein persönlicher Weg | mittel-hoch | Heidis Programm |
| Transformation: Warum innere Blockaden körperlich sind | mittel | Heidis Programm |
| Raumklima und Gesundheit – unterschätzt und unterschätzt | mittel | Partner A |

#!/usr/bin/env python3
"""
WordPress MCP Server – heidifrank.de
Gesundheit · Stressregulation · Transformation
"""

import os
import json
import base64
import requests
from mcp.server.fastmcp import FastMCP

WP_URL           = os.environ.get("WP_URL", "https://heidifrank.de")
WP_USER          = os.environ.get("WP_USER", "")
WP_PASSWORD      = os.environ.get("WP_PASSWORD", "")
PEXELS_KEY       = os.environ.get("PEXELS_API_KEY", "")
OPENAI_KEY       = os.environ.get("OPENAI_API_KEY", "")
HIGGSFIELD_KEY   = os.environ.get("HIGGSFIELD_API_KEY", "")

mcp = FastMCP("heidifrank-wordpress")

# ── Hilfsfunktionen ──────────────────────────────────────────────────────────

def wp_headers():
    token = base64.b64encode(f"{WP_USER}:{WP_PASSWORD}".encode()).decode()
    return {"Authorization": f"Basic {token}", "Content-Type": "application/json"}

def wp_media_headers():
    token = base64.b64encode(f"{WP_USER}:{WP_PASSWORD}".encode()).decode()
    return {"Authorization": f"Basic {token}"}

def pexels_bild_url(suchbegriff: str) -> str:
    if not PEXELS_KEY:
        return ""
    try:
        r = requests.get(
            "https://api.pexels.com/v1/search",
            headers={"Authorization": PEXELS_KEY},
            params={"query": suchbegriff, "per_page": 3, "orientation": "landscape"},
            timeout=10
        )
        if r.status_code == 200:
            fotos = r.json().get("photos", [])
            if fotos:
                return fotos[0]["src"]["large2x"]
    except Exception:
        pass
    return ""

def dalle_bild_url(prompt: str) -> str:
    """Generiert ein KI-Bild via DALL-E 3 (OpenAI). Prompt auf Englisch für beste Qualität."""
    if not OPENAI_KEY:
        return ""
    try:
        r = requests.post(
            "https://api.openai.com/v1/images/generations",
            headers={"Authorization": f"Bearer {OPENAI_KEY}", "Content-Type": "application/json"},
            json={
                "model": "dall-e-3",
                "prompt": f"Professional health and wellness photography. {prompt}. Clean, warm, optimistic, natural light. No text, no logos. Magazine quality.",
                "size": "1792x1024",
                "quality": "standard",
                "n": 1
            },
            timeout=60
        )
        if r.status_code == 200:
            return r.json()["data"][0]["url"]
    except Exception:
        pass
    return ""

def higgsfield_bild_url(prompt: str) -> str:
    """Generiert ein KI-Bild via Higgsfield AI."""
    if not HIGGSFIELD_KEY:
        return ""
    try:
        r = requests.post(
            "https://api.higgsfield.ai/v1/image/generate",
            headers={"Authorization": f"Bearer {HIGGSFIELD_KEY}", "Content-Type": "application/json"},
            json={"prompt": prompt, "aspect_ratio": "16:9"},
            timeout=90
        )
        if r.status_code == 200:
            data = r.json()
            return data.get("url") or data.get("image_url", "")
    except Exception:
        pass
    return ""

def bild_holen(suchbegriff: str, quelle: str = "pexels") -> str:
    """Holt Bild von der gewählten Quelle. Fällt auf nächste verfügbare zurück."""
    quelle = quelle.lower().strip()
    if quelle == "dalle" or quelle == "dall-e":
        url = dalle_bild_url(suchbegriff)
        if url:
            return url
    if quelle == "higgsfield":
        url = higgsfield_bild_url(suchbegriff)
        if url:
            return url
    # Standard: Pexels
    return pexels_bild_url(suchbegriff)

def bild_nach_wordpress_hochladen(bild_url: str, dateiname: str) -> int:
    """Lädt ein Bild von URL in die WordPress-Mediathek hoch. Gibt Media-ID zurück."""
    try:
        r = requests.get(bild_url, timeout=15)
        if r.status_code != 200:
            return 0
        headers = wp_media_headers()
        headers["Content-Disposition"] = f"attachment; filename={dateiname}.jpg"
        headers["Content-Type"] = "image/jpeg"
        resp = requests.post(
            f"{WP_URL}/wp-json/wp/v2/media",
            headers=headers,
            data=r.content,
            timeout=30
        )
        if resp.status_code in (200, 201):
            return resp.json().get("id", 0)
    except Exception:
        pass
    return 0

# ── HTML-Vorlage für Blogbeiträge ────────────────────────────────────────────

def erstelle_blog_html(
    einleitung: str,
    abschnitte: list,
    tipp_box: str = "",
    tabelle: dict = None,
    checkliste: list = None,
    fazit: str = "",
    cta_text: str = "",
    werbeanzeige: dict = None
) -> str:
    """
    Baut professionelles Block-HTML für den Beitrag.
    abschnitte   = [{"titel": str, "text": str, "bild_url": str (optional)}]
    tabelle      = {"kopfzeile": [...], "zeilen": [[...]]}
    checkliste   = ["Punkt 1", "Punkt 2", ...]
    werbeanzeige = {"text": str, "link": str, "link_text": str, "bild_url": str (optional)}
    """

    ORANGE  = "#D94A15"
    GOLD    = "#D4A020"
    HELL    = "#FFF8F5"
    TEXT    = "#333333"
    GRAU    = "#F5F5F0"

    html = f"""
<div style="font-family:'Segoe UI',Arial,sans-serif;max-width:860px;margin:0 auto;color:{TEXT};line-height:1.75;">

<!-- EINLEITUNG -->
<div style="border-left:5px solid {ORANGE};background:{HELL};padding:22px 28px;border-radius:0 10px 10px 0;margin-bottom:35px;font-size:1.12em;font-style:italic;">
{einleitung}
</div>
"""

    # Abschnitte – nach dem 2. Abschnitt kommt ggf. die Werbeanzeige
    for i, a in enumerate(abschnitte):
        bild = a.get("bild_url", "")
        bild_html = f'<img src="{bild}" alt="{a["titel"]}" style="width:100%;height:auto;border-radius:10px;margin-bottom:20px;display:block;">' if bild else ""

        if i % 2 == 0:
            html += f"""
<!-- ABSCHNITT {i+1} -->
<div style="background:#fff;border:1px solid #EEE;border-radius:12px;padding:28px;margin-bottom:28px;box-shadow:0 2px 8px rgba(0,0,0,0.06);">
  {bild_html}
  <h2 style="color:{ORANGE};font-size:1.45em;margin-top:0;margin-bottom:14px;border-bottom:2px solid {GOLD};padding-bottom:8px;">{a['titel']}</h2>
  <p style="margin:0;font-size:1.02em;">{a['text']}</p>
</div>
"""
        else:
            html += f"""
<!-- ABSCHNITT {i+1} (Akzent) -->
<div style="background:{GRAU};border-radius:12px;padding:28px;margin-bottom:28px;">
  {bild_html}
  <h2 style="color:{ORANGE};font-size:1.45em;margin-top:0;margin-bottom:14px;">{a['titel']}</h2>
  <p style="margin:0;font-size:1.02em;">{a['text']}</p>
</div>
"""

        # Werbeanzeige nach dem 2. Abschnitt einfügen
        if i == 1 and werbeanzeige:
            w_bild  = werbeanzeige.get("bild_url", "")
            w_text  = werbeanzeige.get("text", "")
            w_link  = werbeanzeige.get("link", "#")
            w_btn   = werbeanzeige.get("link_text", "Jetzt ansehen")
            w_bild_html = f'<img src="{w_bild}" alt="Anzeige" style="width:110px;border-radius:8px;flex-shrink:0;">' if w_bild else ""
            html += f"""
<!-- WERBEANZEIGE -->
<div style="border:2px solid {GOLD};border-radius:12px;padding:24px 28px;margin-bottom:28px;background:#FFFDF5;position:relative;">
  <div style="position:absolute;top:-13px;left:20px;background:{GOLD};color:#fff;padding:3px 14px;border-radius:20px;font-size:0.78em;font-weight:700;letter-spacing:1px;">ANZEIGE</div>
  <div style="display:flex;gap:20px;align-items:center;flex-wrap:wrap;">
    {w_bild_html}
    <div style="flex:1;min-width:200px;">
      <p style="color:{TEXT};margin:0 0 10px;font-size:1em;line-height:1.6;">{w_text}</p>
      <a href="{w_link}" style="background:{ORANGE};color:#fff;padding:9px 22px;border-radius:25px;text-decoration:none;font-weight:700;font-size:0.92em;display:inline-block;">{w_btn} →</a>
    </div>
  </div>
</div>
"""

    # Tipp-Box
    if tipp_box:
        html += f"""
<!-- TIPP-BOX -->
<div style="background:linear-gradient(135deg,{ORANGE},{GOLD});color:#fff;border-radius:12px;padding:28px;margin-bottom:28px;text-align:center;">
  <div style="font-size:2em;margin-bottom:8px;">💡</div>
  <p style="margin:0;font-size:1.1em;font-weight:600;">{tipp_box}</p>
</div>
"""

    # Tabelle
    if tabelle and tabelle.get("kopfzeile") and tabelle.get("zeilen"):
        kopf_html = "".join(f'<th style="background:{ORANGE};color:#fff;padding:12px 16px;text-align:left;">{k}</th>' for k in tabelle["kopfzeile"])
        zeilen_html = ""
        for idx, zeile in enumerate(tabelle["zeilen"]):
            bg = "#fff" if idx % 2 == 0 else HELL
            zellen = "".join(f'<td style="padding:11px 16px;border-bottom:1px solid #eee;">{z}</td>' for z in zeile)
            zeilen_html += f'<tr style="background:{bg};">{zellen}</tr>'

        html += f"""
<!-- TABELLE -->
<div style="overflow-x:auto;margin-bottom:28px;">
<table style="width:100%;border-collapse:collapse;border-radius:12px;overflow:hidden;box-shadow:0 2px 8px rgba(0,0,0,0.08);">
  <thead><tr>{kopf_html}</tr></thead>
  <tbody>{zeilen_html}</tbody>
</table>
</div>
"""

    # Checkliste
    if checkliste:
        punkte_html = "".join(
            f'<li style="padding:10px 0;border-bottom:1px solid #eee;display:flex;align-items:flex-start;gap:12px;"><span style="color:{ORANGE};font-size:1.3em;flex-shrink:0;">✓</span><span>{p}</span></li>'
            for p in checkliste
        )
        html += f"""
<!-- CHECKLISTE -->
<div style="background:#fff;border:2px solid {ORANGE};border-radius:12px;padding:28px;margin-bottom:28px;">
  <h3 style="color:{ORANGE};margin-top:0;margin-bottom:16px;font-size:1.2em;">Das nimmst du mit:</h3>
  <ul style="list-style:none;padding:0;margin:0;">{punkte_html}</ul>
</div>
"""

    # Fazit
    if fazit:
        html += f"""
<!-- FAZIT -->
<div style="background:{HELL};border-radius:12px;padding:28px;margin-bottom:28px;border-top:4px solid {GOLD};">
  <h3 style="color:{ORANGE};margin-top:0;">Fazit</h3>
  <p style="margin:0;font-size:1.05em;">{fazit}</p>
</div>
"""

    # CTA-Block
    cta_inhalt = cta_text or "Möchtest du mehr über Stressregulation und Energie-Balance erfahren? Ich begleite dich persönlich auf deinem Weg zur Transformation."
    html += f"""
<!-- CTA-BLOCK -->
<div style="background:linear-gradient(135deg,#1a1a1a,#2d2d2d);color:#fff;border-radius:14px;padding:38px;margin-bottom:28px;text-align:center;">
  <p style="color:{GOLD};font-size:1.3em;font-weight:700;margin-bottom:12px;">Bereit für deine persönliche Transformation?</p>
  <p style="color:#ddd;margin-bottom:24px;font-size:1.05em;">{cta_inhalt}</p>
  <a href="{WP_URL}/kontakt"
     style="background:{ORANGE};color:#fff;padding:14px 36px;border-radius:30px;text-decoration:none;font-weight:700;font-size:1.05em;display:inline-block;letter-spacing:0.5px;">
    ✉ Jetzt Kontakt aufnehmen
  </a>
</div>

<!-- AUTORIN -->
<div style="display:flex;align-items:center;gap:20px;padding:24px;background:{GRAU};border-radius:12px;margin-bottom:10px;">
  <div>
    <strong style="color:{ORANGE};font-size:1.05em;">Heidi Frank</strong><br>
    <span style="color:#666;font-size:0.92em;">Gesundheitspädagogin · Stressregulation & Energie-Balance · seit 1979</span>
  </div>
</div>

</div>
"""
    return html


# ── MCP Tools ────────────────────────────────────────────────────────────────

@mcp.tool()
def blogbeitrag_erstellen(
    titel: str,
    einleitung: str,
    abschnitte_json: str,
    bild_suchbegriff: str = "",
    bild_quelle: str = "pexels",
    tipp_box: str = "",
    tabelle_json: str = "",
    checkliste_json: str = "",
    werbeanzeige_json: str = "",
    fazit: str = "",
    cta_text: str = "",
    status: str = "draft"
) -> str:
    """
    Erstellt einen professionellen Blogbeitrag für heidifrank.de.

    abschnitte_json:    JSON-Array z.B. [{"titel":"Abschnitt 1","text":"langer Text..."}]
                        WICHTIG: Gesamt-Wortanzahl aller Texte zusammen = 1800-2000 Wörter.
    bild_suchbegriff:  Suchbegriff / Prompt für das Bild (Englisch empfohlen)
    bild_quelle:       "pexels" (Stockfoto), "dalle" (KI via ChatGPT/OpenAI), "higgsfield" (KI)
    tipp_box:          Kurzer hervorgehobener Tipp (optional)
    tabelle_json:      JSON z.B. {"kopfzeile":["Was","Wie"],"zeilen":[["...","..."]]}
    checkliste_json:   JSON-Array z.B. ["Punkt 1","Punkt 2"]
    werbeanzeige_json: JSON z.B. {"text":"Empfehlung...","link":"https://...","link_text":"Mehr erfahren","bild_url":"https://..."}
    fazit:             Abschlusstext (optional)
    cta_text:          Text im CTA-Block am Ende (optional)
    status:            "draft" (Entwurf) oder "publish" (sofort live)
    """
    try:
        abschnitte = json.loads(abschnitte_json) if abschnitte_json else []
    except Exception:
        return "Fehler: abschnitte_json ist kein gültiges JSON."

    try:
        tabelle = json.loads(tabelle_json) if tabelle_json else None
    except Exception:
        tabelle = None

    try:
        checkliste = json.loads(checkliste_json) if checkliste_json else None
    except Exception:
        checkliste = None

    try:
        werbeanzeige = json.loads(werbeanzeige_json) if werbeanzeige_json else None
    except Exception:
        werbeanzeige = None

    # Bild holen (Pexels / DALL-E / Higgsfield)
    bild_url = ""
    media_id = 0
    if bild_suchbegriff:
        bild_url = bild_holen(bild_suchbegriff, bild_quelle)
        if bild_url:
            sicherer_name = bild_suchbegriff.replace(" ", "-")[:40]
            media_id = bild_nach_wordpress_hochladen(bild_url, sicherer_name)

    # Bild in erstes Abschnitt einfügen wenn vorhanden
    if bild_url and abschnitte:
        abschnitte[0]["bild_url"] = bild_url

    # HTML bauen
    inhalt = erstelle_blog_html(
        einleitung=einleitung,
        abschnitte=abschnitte,
        tipp_box=tipp_box,
        tabelle=tabelle,
        checkliste=checkliste,
        fazit=fazit,
        cta_text=cta_text,
        werbeanzeige=werbeanzeige
    )

    # An WordPress senden
    daten = {
        "title": titel,
        "content": inhalt,
        "status": status
    }
    if media_id:
        daten["featured_media"] = media_id

    try:
        r = requests.post(
            f"{WP_URL}/wp-json/wp/v2/posts",
            headers=wp_headers(),
            json=daten,
            timeout=30
        )
        if r.status_code in (200, 201):
            post = r.json()
            return f"Beitrag erstellt!\nID: {post['id']}\nStatus: {post['status']}\nURL: {post.get('link','–')}"
        else:
            return f"WordPress-Fehler {r.status_code}: {r.text[:300]}"
    except Exception as e:
        return f"Verbindungsfehler: {e}"


@mcp.tool()
def beitraege_anzeigen(anzahl: int = 10, status: str = "any") -> str:
    """Listet vorhandene Blogbeiträge auf. status: draft, publish oder any"""
    try:
        r = requests.get(
            f"{WP_URL}/wp-json/wp/v2/posts",
            headers=wp_headers(),
            params={"per_page": anzahl, "status": status},
            timeout=15
        )
        if r.status_code == 200:
            beitraege = r.json()
            if not beitraege:
                return "Keine Beiträge gefunden."
            zeilen = [f"ID {b['id']:5} | {b['status']:9} | {b['title']['rendered'][:60]}" for b in beitraege]
            return "Blogbeiträge auf heidifrank.de:\n" + "\n".join(zeilen)
        return f"Fehler {r.status_code}"
    except Exception as e:
        return f"Verbindungsfehler: {e}"


@mcp.tool()
def kategorien_anzeigen() -> str:
    """Zeigt alle WordPress-Kategorien mit ID."""
    try:
        r = requests.get(
            f"{WP_URL}/wp-json/wp/v2/categories",
            headers=wp_headers(),
            timeout=15
        )
        if r.status_code == 200:
            cats = r.json()
            zeilen = [f"ID {c['id']:4} | {c['name']} ({c['count']} Beiträge)" for c in cats]
            return "\n".join(zeilen) if zeilen else "Keine Kategorien vorhanden."
        return f"Fehler {r.status_code}"
    except Exception as e:
        return f"Verbindungsfehler: {e}"


@mcp.tool()
def beitrag_aktualisieren(
    post_id: int,
    titel: str = "",
    status: str = ""
) -> str:
    """Aktualisiert Titel oder Status eines vorhandenen Beitrags."""
    daten = {}
    if titel:
        daten["title"] = titel
    if status:
        daten["status"] = status
    if not daten:
        return "Nichts zu aktualisieren angegeben."
    try:
        r = requests.post(
            f"{WP_URL}/wp-json/wp/v2/posts/{post_id}",
            headers=wp_headers(),
            json=daten,
            timeout=15
        )
        if r.status_code == 200:
            return f"Beitrag {post_id} aktualisiert. Status: {r.json().get('status')}"
        return f"Fehler {r.status_code}: {r.text[:200]}"
    except Exception as e:
        return f"Verbindungsfehler: {e}"


@mcp.tool()
def beitrag_inhalt_holen(post_id: int) -> str:
    """
    Liest Titel und Inhalt eines bestehenden Beitrags aus.
    Nutze das um alte Beiträge umzuformatieren:
    1. beitrag_inhalt_holen(id) aufrufen
    2. Inhalt mit blogbeitrag_html_ersetzen() im neuen Block-Layout speichern
    """
    try:
        r = requests.get(
            f"{WP_URL}/wp-json/wp/v2/posts/{post_id}",
            headers=wp_headers(),
            timeout=15
        )
        if r.status_code == 200:
            p = r.json()
            titel    = p["title"]["rendered"]
            inhalt   = p["content"]["rendered"]
            status   = p["status"]
            link     = p.get("link", "")
            return f"TITEL: {titel}\nSTATUS: {status}\nURL: {link}\n\nINHALT (HTML):\n{inhalt}"
        return f"Beitrag {post_id} nicht gefunden. Fehler {r.status_code}"
    except Exception as e:
        return f"Verbindungsfehler: {e}"


@mcp.tool()
def blogbeitrag_html_ersetzen(
    post_id: int,
    neuer_inhalt_html: str,
    status: str = ""
) -> str:
    """
    Ersetzt den HTML-Inhalt eines bestehenden Beitrags komplett.
    Zum Umformatieren alter Beiträge ins neue Block-Layout.
    status leer lassen = Status bleibt wie er ist.
    """
    daten: dict = {"content": neuer_inhalt_html}
    if status:
        daten["status"] = status
    try:
        r = requests.post(
            f"{WP_URL}/wp-json/wp/v2/posts/{post_id}",
            headers=wp_headers(),
            json=daten,
            timeout=30
        )
        if r.status_code == 200:
            p = r.json()
            return f"Beitrag {post_id} aktualisiert.\nStatus: {p['status']}\nURL: {p.get('link','–')}"
        return f"Fehler {r.status_code}: {r.text[:300]}"
    except Exception as e:
        return f"Verbindungsfehler: {e}"


@mcp.tool()
def alle_beitraege_umformatieren_vorbereiten(anzahl: int = 50) -> str:
    """
    Listet alle Beiträge mit ID und Titel auf, damit du sie nacheinander
    umformatieren kannst. Ruf dann für jeden: beitrag_inhalt_holen(id),
    dann blogbeitrag_html_ersetzen(id, neues_html) auf.
    """
    try:
        r = requests.get(
            f"{WP_URL}/wp-json/wp/v2/posts",
            headers=wp_headers(),
            params={"per_page": anzahl, "status": "any"},
            timeout=20
        )
        if r.status_code == 200:
            beitraege = r.json()
            if not beitraege:
                return "Keine Beiträge vorhanden."
            zeilen = [
                f"ID {b['id']:5} | {b['status']:9} | {b['title']['rendered'][:55]}"
                for b in beitraege
            ]
            total = len(zeilen)
            return (
                f"{total} Beiträge gefunden. Starte Umformatierung mit:\n"
                "→ beitrag_inhalt_holen(ID) → Inhalt analysieren → blogbeitrag_html_ersetzen(ID, neues_html)\n\n"
                + "\n".join(zeilen)
            )
        return f"Fehler {r.status_code}"
    except Exception as e:
        return f"Verbindungsfehler: {e}"


@mcp.tool()
def seite_lesen(slug_oder_id: str) -> str:
    """
    Liest eine WordPress-Seite (Page) aus – z.B. die Partner-Seite.
    slug_oder_id: Seiten-Slug (z.B. "partner") oder numerische ID.
    Nutze das um Partner-Links, Seiteninhalt etc. zu lesen.
    """
    try:
        # Erst per Slug versuchen
        params = {"slug": slug_oder_id} if not slug_oder_id.isdigit() else {}
        if slug_oder_id.isdigit():
            url = f"{WP_URL}/wp-json/wp/v2/pages/{slug_oder_id}"
            r = requests.get(url, headers=wp_headers(), timeout=15)
        else:
            r = requests.get(
                f"{WP_URL}/wp-json/wp/v2/pages",
                headers=wp_headers(),
                params={"slug": slug_oder_id, "per_page": 1},
                timeout=15
            )
            if r.status_code == 200 and r.json():
                seite = r.json()[0]
                return (
                    f"TITEL: {seite['title']['rendered']}\n"
                    f"SLUG: {seite['slug']}\n"
                    f"URL: {seite.get('link','')}\n\n"
                    f"INHALT:\n{seite['content']['rendered']}"
                )
            return f"Seite '{slug_oder_id}' nicht gefunden."

        if r.status_code == 200:
            seite = r.json()
            if isinstance(seite, list):
                seite = seite[0] if seite else None
            if not seite:
                return "Seite nicht gefunden."
            return (
                f"TITEL: {seite['title']['rendered']}\n"
                f"SLUG: {seite['slug']}\n"
                f"URL: {seite.get('link','')}\n\n"
                f"INHALT:\n{seite['content']['rendered']}"
            )
        return f"Fehler {r.status_code}"
    except Exception as e:
        return f"Verbindungsfehler: {e}"


@mcp.tool()
def alle_seiten_auflisten() -> str:
    """Listet alle WordPress-Seiten (Pages) mit ID, Slug und Titel auf."""
    try:
        r = requests.get(
            f"{WP_URL}/wp-json/wp/v2/pages",
            headers=wp_headers(),
            params={"per_page": 100},
            timeout=15
        )
        if r.status_code == 200:
            seiten = r.json()
            if not seiten:
                return "Keine Seiten gefunden."
            zeilen = [f"ID {s['id']:5} | /{s['slug']:<30} | {s['title']['rendered'][:50]}" for s in seiten]
            return "WordPress-Seiten:\n" + "\n".join(zeilen)
        return f"Fehler {r.status_code}"
    except Exception as e:
        return f"Verbindungsfehler: {e}"


@mcp.tool()
def verbindung_testen() -> str:
    """Testet ob WordPress und Zugangsdaten korrekt sind."""
    try:
        r = requests.get(
            f"{WP_URL}/wp-json/wp/v2/users/me",
            headers=wp_headers(),
            timeout=10
        )
        if r.status_code == 200:
            u = r.json()
            return f"Verbindung OK!\nBenutzer: {u.get('name')} ({u.get('slug')})\nRolle: {', '.join(u.get('roles', []))}\nSeite: {WP_URL}"
        return f"Fehler {r.status_code}: Bitte Zugangsdaten in .claude/settings.json prüfen."
    except Exception as e:
        return f"Verbindungsfehler zu {WP_URL}: {e}"


if __name__ == "__main__":
    mcp.run()

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

WP_URL      = os.environ.get("WP_URL", "https://heidifrank.de")
WP_USER     = os.environ.get("WP_USER", "")
WP_PASSWORD = os.environ.get("WP_PASSWORD", "")
PEXELS_KEY  = os.environ.get("PEXELS_API_KEY", "")

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
    cta_text: str = ""
) -> str:
    """
    Baut professionelles Block-HTML für den Beitrag.
    abschnitte = [{"titel": str, "text": str, "bild_url": str (optional)}]
    tabelle = {"kopfzeile": [...], "zeilen": [[...]]}
    checkliste = ["Punkt 1", "Punkt 2", ...]
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

    # Abschnitte
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
    pexels_suchbegriff: str = "",
    tipp_box: str = "",
    tabelle_json: str = "",
    checkliste_json: str = "",
    fazit: str = "",
    cta_text: str = "",
    status: str = "draft"
) -> str:
    """
    Erstellt einen professionellen Blogbeitrag für heidifrank.de.

    abschnitte_json: JSON-Array z.B. [{"titel":"Abschnitt 1","text":"..."},{"titel":"...","text":"..."}]
    pexels_suchbegriff: Englischer Suchbegriff für Pexels-Bild (z.B. "meditation stress relief")
    tipp_box: Kurzer fettgedruckter Tipp (optional)
    tabelle_json: JSON z.B. {"kopfzeile":["Was","Wie"],"zeilen":[["Punkt","Beschreibung"]]}
    checkliste_json: JSON-Array z.B. ["Punkt 1","Punkt 2","Punkt 3"]
    fazit: Abschlusstext (optional)
    cta_text: Text im CTA-Block (optional)
    status: "draft" (Entwurf) oder "publish" (sofort veröffentlichen)
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

    # Pexels-Bild holen
    bild_url = ""
    media_id = 0
    if pexels_suchbegriff:
        bild_url = pexels_bild_url(pexels_suchbegriff)
        if bild_url:
            sicherer_name = pexels_suchbegriff.replace(" ", "-")[:40]
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
        cta_text=cta_text
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

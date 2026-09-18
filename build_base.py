# -*- coding: utf-8 -*-
import os

ROOT = "/home/claude/kinbound-site"

SITE_NAME = "Kinbound Home Care"
DOMAIN = "https://www.kinboundhomecare.com"   # PLACEHOLDER — replace with live domain before launch
PHONE_DISPLAY = "(402) 555-0142"              # PLACEHOLDER — replace with real business line
PHONE_TEL = "+14025550142"                    # PLACEHOLDER
EMAIL = "hello@kinboundhomecare.com"          # PLACEHOLDER
REQUEST_CARE_URL = "#axiscare-intake"         # PLACEHOLDER — point to AxisCare intake workflow
REFER_CLIENT_URL = "#axiscare-referral"       # PLACEHOLDER — point to AxisCare referral workflow
JOIN_TEAM_URL = "#axiscare-careers"           # PLACEHOLDER — point to AxisCare / ATS application flow
OFFICE_CITY = "Omaha, Nebraska"

NAV_ITEMS = [
    ("Home", "/"),
    ("About", "/about-kinbound/"),
    ("SERVICES_DROPDOWN", None),
    ("Service Areas", "/service-areas/"),
    ("For Professionals", "/healthcare-professionals/"),
    ("Resources", "/resources/"),
    ("Careers", "/careers/"),
]

SERVICES_DROPDOWN = [
    ("Personal Care", "/personal-care-omaha-ne/"),
    ("Companion Care", "/companion-care-omaha-ne/"),
    ("Homemaker Services", "/homemaker-services-omaha-ne/"),
    ("Dementia & Memory Support", "/dementia-memory-care-omaha-ne/"),
    ("Respite Care", "/respite-care-omaha-ne/"),
]

FONTS = '<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin><link href="https://fonts.googleapis.com/css2?family=Newsreader:opsz,wght@6..72,400;6..72,500;6..72,600&family=Public+Sans:wght@400;500;600;700;800&display=swap" rel="stylesheet">'

BRAND_MARK_SVG = """<svg class="brand-mark" viewBox="0 0 40 40" fill="none" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">
<circle cx="20" cy="20" r="18.5" stroke="#A97A34" stroke-width="1.4"/>
<path d="M20 6 L23 18 L35 20 L23 22 L20 34 L17 22 L5 20 L17 18 Z" fill="#3E5541"/>
<circle cx="20" cy="20" r="2.4" fill="#F2ECDE" stroke="#1C2A2A" stroke-width="1"/>
</svg>"""


def head(title, description, path, extra_schema=""):
    canonical = DOMAIN.rstrip("/") + path
    return f"""<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title>
<meta name="description" content="{description}">
<link rel="canonical" href="{canonical}">
<meta property="og:type" content="website">
<meta property="og:site_name" content="{SITE_NAME}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{description}">
<meta property="og:url" content="{canonical}">
<meta property="og:image" content="{DOMAIN}/assets/img/og-default.jpg">
<meta name="twitter:card" content="summary_large_image">
<meta name="theme-color" content="#1C2A2A">
<link rel="icon" href="/assets/img/favicon.svg" type="image/svg+xml">
{FONTS}
<link rel="stylesheet" href="/assets/css/style.css">
{extra_schema}"""


def nav_html(current_path):
    def is_current(href):
        return " current" if href == current_path else ""

    parts = ['<nav class="primary-nav" aria-label="Primary">', "<ul>"]
    for label, href in NAV_ITEMS:
        if label == "SERVICES_DROPDOWN":
            svc_current = current_path in [h for _, h in SERVICES_DROPDOWN]
            parts.append(
                f'<li class="has-dropdown"><a href="/personal-care-omaha-ne/" class="{"current" if svc_current else ""}" aria-haspopup="true">Services</a>'
            )
            parts.append('<div class="dropdown">')
            for slabel, shref in SERVICES_DROPDOWN:
                parts.append(f'<a href="{shref}"{is_current(shref)}>{slabel}</a>')
            parts.append("</div></li>")
        else:
            parts.append(f'<li><a href="{href}"{is_current(href)}>{label}</a></li>')
    parts.append("</ul></nav>")
    return "\n".join(parts)


def header_html(current_path):
    return f"""<div class="topbar">
  <div class="container">
    <span>Serving Omaha and the surrounding communities &mdash; non-medical home care</span>
    <a class="phone" href="tel:{PHONE_TEL}">Call {PHONE_DISPLAY}</a>
  </div>
</div>
<header class="site-header">
  <div class="container">
    <a class="brand" href="/">
      {BRAND_MARK_SVG}
      <span class="brand-word">Kin<b>bound</b></span>
    </a>
    {nav_html(current_path)}
    <div class="nav-cta">
      <a class="btn btn-outline btn-sm" href="{REFER_CLIENT_URL}"><span class="long">Refer a </span>Client</a>
      <a class="btn btn-brass btn-sm" href="/request-care/">Request Care</a>
      <button class="menu-toggle" aria-label="Open menu" aria-expanded="false">&#9776;</button>
    </div>
  </div>
</header>"""


def footer_html():
    return f"""<footer class="site-footer">
  <div class="container">
    <div class="footer-grid">
      <div class="footer-brand">
        <a class="brand" href="/" style="margin-bottom:14px;">
          {BRAND_MARK_SVG}
          <span class="brand-word">Kin<b>bound</b></span>
        </a>
        <p class="text-sm" style="max-width:34ch;">Non-medical home care for Omaha-area seniors, built on intentional caregiver matching rather than shift-filling.</p>
        <p class="text-sm">{OFFICE_CITY}<br>
        <a href="tel:{PHONE_TEL}">{PHONE_DISPLAY}</a><br>
        <a href="mailto:{EMAIL}">{EMAIL}</a></p>
      </div>
      <div>
        <h4>Services</h4>
        <ul>
          <li><a href="/personal-care-omaha-ne/">Personal Care</a></li>
          <li><a href="/companion-care-omaha-ne/">Companion Care</a></li>
          <li><a href="/homemaker-services-omaha-ne/">Homemaker Services</a></li>
          <li><a href="/dementia-memory-care-omaha-ne/">Dementia &amp; Memory Support</a></li>
          <li><a href="/respite-care-omaha-ne/">Respite Care</a></li>
        </ul>
      </div>
      <div>
        <h4>Kinbound</h4>
        <ul>
          <li><a href="/about-kinbound/">About Kinbound</a></li>
          <li><a href="/service-areas/">Service Areas</a></li>
          <li><a href="/healthcare-professionals/">For Healthcare Professionals</a></li>
          <li><a href="/careers/">Careers</a></li>
          <li><a href="/resources/">Resources</a></li>
        </ul>
      </div>
      <div>
        <h4>Get Started</h4>
        <ul>
          <li><a href="/request-care/">Request Care</a></li>
          <li><a href="{REFER_CLIENT_URL}">Refer a Client</a></li>
          <li><a href="{JOIN_TEAM_URL}">Join Kinbound</a></li>
          <li><a href="tel:{PHONE_TEL}">Call {PHONE_DISPLAY}</a></li>
        </ul>
      </div>
    </div>
    <div class="footer-bottom">
      <span>&copy; 2026 Kinbound Home Care. Locally owned &amp; operated in Omaha, Nebraska.</span>
      <span>Non-medical home care &mdash; not a licensed home health or skilled nursing agency.</span>
    </div>
  </div>
</footer>
<div class="mobile-call-bar">
  <a class="call" href="tel:{PHONE_TEL}">Call {PHONE_DISPLAY}</a>
  <a href="/request-care/">Request Care</a>
</div>"""


def page(title, description, path, body, current_path=None, schema=""):
    cp = current_path if current_path is not None else path
    html = f"""<!DOCTYPE html>
<html lang="en-US">
<head>
{head(title, description, path, schema)}
</head>
<body>
<a class="skip-link" href="#main">Skip to main content</a>
{header_html(cp)}
<main id="main">
{body}
</main>
{footer_html()}
<script src="/assets/js/main.js"></script>
</body>
</html>
"""
    return html


def write(rel_path, content):
    full = os.path.join(ROOT, rel_path)
    os.makedirs(os.path.dirname(full), exist_ok=True)
    with open(full, "w", encoding="utf-8") as f:
        f.write(content)
    print("wrote", rel_path)

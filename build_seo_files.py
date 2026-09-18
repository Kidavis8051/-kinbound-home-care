# -*- coding: utf-8 -*-
from build_base import write, DOMAIN

URLS = [
    "/",
    "/about-kinbound/",
    "/personal-care-omaha-ne/",
    "/companion-care-omaha-ne/",
    "/homemaker-services-omaha-ne/",
    "/dementia-memory-care-omaha-ne/",
    "/respite-care-omaha-ne/",
    "/service-areas/",
    "/healthcare-professionals/",
    "/request-care/",
    "/careers/",
    "/resources/",
    "/resources/signs-parent-needs-help-at-home/",
    "/resources/home-care-vs-home-health/",
    "/resources/what-is-non-medical-home-care/",
    "/resources/preparing-home-for-dementia-loved-one/",
    "/resources/hospital-discharge-still-needs-help-at-home/",
]

def build_sitemap():
    entries = "\n".join(
        f"  <url>\n    <loc>{DOMAIN.rstrip('/')}{u}</loc>\n  </url>"
        for u in URLS
    )
    xml = f"""<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
{entries}
</urlset>
"""
    write("sitemap.xml", xml)


def build_robots():
    txt = f"""User-agent: *
Allow: /

Sitemap: {DOMAIN.rstrip('/')}/sitemap.xml
"""
    write("robots.txt", txt)


if __name__ == "__main__":
    build_sitemap()
    build_robots()

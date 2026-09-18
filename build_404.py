# -*- coding: utf-8 -*-
from build_base import write, page, PHONE_TEL, PHONE_DISPLAY

BODY = f"""
<section class="page-hero">
  <div class="container">
    <div class="bearing"><div class="tick"></div><span>404</span></div>
    <h1>This page took a wrong turn.</h1>
    <p class="lede">The page you're looking for doesn't exist, may have moved, or the address may have been typed incorrectly. Here are a few places to head instead.</p>
  </div>
</section>

<section>
  <div class="container">
    <div class="area-list">
      <a class="area-chip" href="/">Home</a>
      <a class="area-chip" href="/personal-care-omaha-ne/">Personal Care</a>
      <a class="area-chip" href="/companion-care-omaha-ne/">Companion Care</a>
      <a class="area-chip" href="/homemaker-services-omaha-ne/">Homemaker Services</a>
      <a class="area-chip" href="/dementia-memory-care-omaha-ne/">Dementia &amp; Memory Support</a>
      <a class="area-chip" href="/respite-care-omaha-ne/">Respite Care</a>
      <a class="area-chip" href="/service-areas/">Service Areas</a>
      <a class="area-chip" href="/healthcare-professionals/">For Healthcare Professionals</a>
      <a class="area-chip" href="/resources/">Resources</a>
      <a class="area-chip" href="/careers/">Careers</a>
      <a class="area-chip" href="/request-care/">Request Care</a>
    </div>
    <p style="margin-top:30px;">Or call us directly at <a href="tel:{PHONE_TEL}">{PHONE_DISPLAY}</a>.</p>
  </div>
</section>
"""

write("404.html", page(
    title="Page Not Found | Kinbound Home Care",
    description="The page you're looking for could not be found. Explore Kinbound Home Care's services, service areas and resources instead.",
    path="/404.html",
    body=BODY,
    current_path="__none__",
))
